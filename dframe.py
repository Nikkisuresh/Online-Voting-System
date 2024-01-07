import pandas as pd
from pathlib import Path
import socket
import csv

# path = Path("C:/Users/Desktop/Sem-5/CS301 CN/Project/Voting/database")
path = Path("C:/Users/Nidhi/Desktop/PES UNIVERSITY/CS SEM 4/COMPUTER NETWORKS/Online Voting System")

def count_reset():
    df=pd.read_csv(path/'Voterlist.csv')
    df=df[['VOTER_ID','FIRST NAME','LAST NAME','DATE OF BIRTH','GENDER','ZONE','CITY','PASSWORD','Voted']]
    for index, row in df.iterrows():
        df['Voted'].iloc[index]=0
    df.to_csv(path/'Voterlist.csv')

    df=pd.read_csv(path/'Candidatelist.csv')
    df=df[['PARTY SIGN','CANDIDATE NAME','VOTES RECEIVED']]
    for index, row in df.iterrows():
        df['VOTES RECEIVED'].iloc[index]=0
    df.to_csv (path/'Candidatelist.csv')

def verify(vid,passw):
    df=pd.read_csv(path/'Voterlist.csv')
    df=df[['VOTER_ID','FIRST NAME','LAST NAME','DATE OF BIRTH','GENDER','ZONE','CITY','PASSWORD','Voted']]
    for index, row in df.iterrows():
        if df['VOTER_ID'].iloc[index]==vid and df['PASSWORD'].iloc[index]==passw:
            return True
    return False


def isEligible(vid):
    df=pd.read_csv(path/'Voterlist.csv')
    df=df[['VOTER_ID','FIRST NAME','LAST NAME','DATE OF BIRTH','GENDER','ZONE','CITY','PASSWORD','Voted']]
    for index, row in df.iterrows():
        if df['VOTER_ID'].iloc[index]==vid and df['Voted'].iloc[index]==0:
            return True
    return False


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'Candidatelist.csv')
        df=df[['PARTY SIGN','CANDIDATE NAME','VOTES RECEIVED']]
        for index, row in df.iterrows():
             if df.at[index,'PARTY SIGN'] == st:
                df.at[index,'VOTES RECEIVED']+=1

        df.to_csv (path/'Candidatelist.csv')

        df=pd.read_csv(path/'Voterlist.csv')
        df=df[['VOTER_ID','FIRST NAME','LAST NAME','DATE OF BIRTH','GENDER','ZONE','CITY','PASSWORD','Voted']]
        for index, row in df.iterrows():
            if df['VOTER_ID'].iloc[index]==vid:
                df['Voted'].iloc[index]=1
        df.to_csv(path/'Voterlist.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'Candidatelist.csv')
    df=df[['PARTY SIGN','CANDIDATE NAME','VOTES RECEIVED']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['PARTY SIGN'].iloc[index]] = df['VOTES RECEIVED'].iloc[index]
    # print(v_cnt)
    return v_cnt


def taking_data_voter(firstname,lastname,dob,gender,zone,city,passw):

    df=pd.read_csv(path/'Voterlist.csv')
    df=df[['VOTER_ID','FIRST NAME','LAST NAME','DATE OF BIRTH','GENDER','ZONE','CITY','PASSWORD','Voted']]
    row,col=df.shape
    if row==0:
        vid =100001
        df = pd.DataFrame({"VOTER_ID":[vid],
                    "FIRST NAME":[firstname],
                    "LAST NAME":[lastname],
                    "DATE OF BIRTH":[dob],
                    "GENDER":[gender],
                    "ZONE":[zone],
                    "CITY":[city],
                    "PASSWORD":[passw],
                    "Voted":[0]},)
        
    else:
        vid=df['VOTER_ID'].iloc[-1]+1
        df1 = pd.DataFrame({"VOTER_ID":[vid],
                    "FIRST NAME":[firstname],
                    "LAST NAME":[lastname],
                    "DATE OF BIRTH":[dob],
                    "GENDER":[gender],
                    "ZONE":[zone],
                    "CITY":[city],
                    "PASSWORD":[passw],
                    "Voted":[0]},)

        df=df.append(df1,ignore_index=True)

    df.to_csv(path/'Voterlist.csv')
    with open('Voterlist.csv','r') as file:
         reader=csv.reader(file)
         data=list(reader)
    data_str='\n'.join([','.join(row) for row in data])
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('10.30.203.247',6000))
    client_socket.send(data_str.encode())
    client_socket.close()


    return vid
