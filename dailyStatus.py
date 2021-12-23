import sys
import datetime
import calendar
import shutil
import os

todays_date = datetime.datetime.now()
curr_dir = os.getcwd() 
log_dir = curr_dir + '\\TimeSheet\\LogFiles\\'
export_dir = curr_dir + '\\TimeSheet\\'
log_file = log_dir + todays_date.strftime("%B")+'.txt'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

try:
    process = sys.argv[1].lower()

    if process not in ['a', 'v', 'add', 'view', 'e', 'export']:
        print('Argument must be "add" or "view" or "export"')

    if process in ['a', 'add']:
        message = str(todays_date.date()) + ','
        for i in range(2, len(sys.argv)):
            message += sys.argv[i]
            message += ' ' 
        
        with open(log_file,'a') as fo:
            fo.write(message + '\n')
            print('Updated >> ' + message)

    elif process in ['v', 'view']:
        month_number = int(sys.argv[2])
        request_file = log_dir + calendar.month_name[month_number]+'.txt'
        if month_number not in list(range(1,13)):
            print('Month ranges from 1 to 12')
        else:
            with open(request_file,'r') as fo:
                content = fo.read()
                print(content)
    
    elif process in ['e', 'export']:
        month_number = int(sys.argv[2])
        request_file = log_dir + calendar.month_name[month_number]+'.txt'
        if month_number not in list(range(1,13)):
            print('Month ranges from 1 to 12')
        else:
            dest_file = export_dir + "E" + calendar.month_name[month_number]+'.csv'
            shutil.copy(request_file,dest_file)
            print('Exported File >> ', dest_file)

except:
    print('''
To Add status 
>> python dailyStatus.py a <message>
>>>> python dailyStatus.py a TaskID 1234 completed
>>>> python dailyStatus.py add TaskID 1234 completed

To View status 
>> python dailyStatus.py v <month number>
>>>> python dailyStatus.py v 12
>>>> python dailyStatus.py view 12
               
To Export it to CSV
>> python dailyStatus.py e <month number>
>>>> python dailyStatus.py e 12
>>>> python dailyStatus.py export 12
''')


