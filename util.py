import pandas as pd
headers = ['S.No.','Name','Sex','Age','Blood Group','Pincode','Phone No.','Email','DOB',"Father's Name",'Aadhaar No.']
altheaders = ['Name','Sex','Age','Blood Group','Pincode','Phone No.','Email','DOB',"Father's Name",'Aadhaar No.']
def ask():
    n = input('What do you want to do? ')
    while True:    
        try:
            n=int(n)
        except ValueError:
            print('Invalid Choice!')
            n=ask()
        else:
            break
    while n not in (0,1,2,3,4,5,6,7,8):
        print('Invalid Choice!')
        n=ask()
    return n

def tabulate_dict(mydict,headers=headers):
    header = headers
    print(f'{header[0]: <10}{header[1]: <20}{header[2]: <10}{header[3]: <10}{header[4]: <15}{header[5]: <15}{header[6]: <15}{header[7]: <29}{header[8]: <15}{header[9]: <20}{header[10]}')
    for key, value in mydict.items():
        print(f'{key: <10}{value[0]: <20}{value[1]: <10}{value[2]: <10}{value[3]: <15}{value[4]: <15}{value[5]: <15}{value[6]: <29}{value[7]: <15}{value[8]: <20}{value[9]}')
    if mydict=={}:
        print('[NO RECORDS]')

def export_dict(mydict):
    data = mydict
    df = pd.DataFrame.from_dict(data, orient='index', columns=altheaders)
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Serial Number'}, inplace=True)
    df.to_excel('output.xlsx', index=False)

def import_dict(path):
    serial=1
    df = pd.read_excel(path)
    serial_column = 'Serial Number'
    df.set_index(serial_column, inplace=True)
    data_dict = df.to_dict(orient='index')
    for i in list(data_dict.values()):
        j = list(i.values())
        data_dict[serial] = j
        serial+=1
    return data_dict