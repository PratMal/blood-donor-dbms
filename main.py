from util import *
record = []
database = {}
max_serial = 1
print('Hi And Welcome To Blood Donor Management System!')
print('''[(1)Insert Record       ]
[(2)Delete Record       ]
[(3)View Records        ]
[(4)Filter              ]
[(5)Display Instructions]
[(6)Export Database     ]
[(7)Import Database     ]
[(0)Exit                ]''')
n=ask()
while True:
    while n==1:
        name = input('Input Name: ').title()
        while len(name)>20:
            print('Name length under 20 characters!')
            name = input('Input Name: ').title()
        sex = input('Input Sex(Male/Female): ').title()
        while sex not in ['Male','Female']:
            print('Invalid!')
            sex = input('Input Sex(Male/Female): ').title()
        while True:    
            try:
                age=int(input('> '))
            except ValueError:
                print('Error!')
            else:
                if not 18<=age<=65:
                    print('invalid')
                    continue
                else:
                    break
        blood_group = input('Input Blood Group: ').title()
        while blood_group not in ['O+','O-','A+','A-','B+','B-','Ab+','Ab-']:
            print('Invalid Blood Group!')
            blood_group = input('Input Blood Group: ').title()
        pincode = input('Input Pincode: ')
        while (len(pincode)!=6 or pincode[0] == '0') or (not pincode.isdigit()):
            print('Invalid Pincode')
            pincode = input('Input Pincode: ')
        phone = input('Input Phone No.: ')
        while len(phone)!=10 or (not phone.isdigit()):
            print('Invalid Phone Number')
            phone = input('Input Phone No.: ')
        email = input('Input Email: ')
        while email.count('@')!=1 or email.count('.')<1:
            print('Invalid Email Address')
            email = input('Input Email: ')
        dob = input('Input DOB(DD.MM.YYYY): ')
        while (len(dob)!=10 or dob.count('.')!=2) or (not dob.replace('.','').isdigit() or not dob[2]==dob[5]=='.'):
            print('Invalid Date!')
            dob = input('Input DOB(DD.MM.YYYY): ')
        father = input("Input Father's Name: ").title()
        while len(father)>20:
            print('Name length under 20 characters!')
            father = input("Input Father's Name: ").title()
        aadhaar = input('Input Aadhaar No.: ')
        while (aadhaar[0] in ['0','1'] or len(aadhaar)!=12) or (not aadhaar.isdigit()):
            print('Invalid Aadhaar No.!')
            aadhaar = input('Input Aadhaar No.: ')
        record.extend([name,sex,age,blood_group,pincode,phone,email,dob,father,aadhaar])
        database[max_serial] = record
        record = []
        max_serial += 1
        n = ask()
    while n==2:
        x = int(input('Serial Number? '))
        try:    
            del(database[x])
        except KeyError:
            print("Serial Number Doesn't Exist!")
        else:
            print('Record Deleted')
        n=ask()
    while n==3:
        tabulate_dict(database)
        n=ask()
    while n==4:
        x = input('Filter by which field name? ').title()
        while x not in headers+['S.no.','S. No.','Serial','Serial No.','S.No','S. No']:
            print('Invalid Field Name!')
            x = input('Filter by which field name? ').title()
        y = input('Value? ').title()
        if y.isdigit():
            y=int(y)
        if x in ('S.No.','S. No.','Serial','Serial No.','S.no','S. No'):
            try:   
                inter = {y:list(database.values())[y-1]}
            except IndexError:
                tabulate_dict(inter)
            else:
                tabulate_dict(inter)
        elif x=='Age':
            param = input(f'Greater than, less than or equal to {y}?(>/</=)')
            inter = {}
            ind = 1
            if param=='>':
                param = '>'
            elif param=='<':
                param = '<'
            else:
                param = '=='
            for i in list(database.values()):
                age = i[2]
                if eval(f'age {param} y'):
                    inter[ind] = i
                    ind+=1
            tabulate_dict(inter) 
        else:
            inter = {}
            ind = 1
            for i in list(database.values()):
                if y in i:
                    inter[ind] = i
                    ind += 1
            tabulate_dict(inter)
        n=ask()

    while n==5:
        print('''[(1)Insert Record      ]
[(2)Delete Record       ]
[(3)View Records        ]
[(4)Filter              ]
[(5)Display Instructions]
[(6)Export Database     ]
[(7)Import Database     ]
[(0)Exit                ]''')
        n=ask()
    while n==6:
        if database == {}:
            print('Nothing to export')
        else:
            export_dict(database)
            print('Exported to local directory')
        n=ask()
    while n==7:
        path = input('Input path of .xlsx(Or just name if present in local directory): ')
        if database != {}:
            y = input('Overwrite Exixting Database?(Y/N) ').lower()
            if y in ('y','yes'):
                database = import_dict(path)
                print('Database Imported')
            else:
                pass
        else:
            database=import_dict(path)
            print('Database Imported')
        n=ask()
    if n==0:
        conf = input('Are you sure you want to exit?(Y/N): ').lower()
        while conf not in ('y','yes','n','no'):
            print('Invalid Input')
            conf = input('Are you sure you want to exit?(Y/N): ').lower()
        if conf in ['y','yes']:
            if database == {}:
                break
            else:
                conf = input('Export database before exiting?(Y/N): ').lower()
                while conf not in ('y','yes','n','no'):
                    print('Invalid Input')
                    conf = input('Export database before exiting?(Y/N): ').lower()
                if conf in ['y','yes']:
                    export_dict(database)
                    print('Exported to local directory')
                    break
                else:
                    break
        else:
            n=ask()
print('Thank You For Using Blood Donor Management System!')