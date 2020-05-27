import pyautogui
import time
import datetime

def clickit():
    time.sleep(1.0)
    print("\n\nClick Time's Now !!!!!")
    print("\n\nAttempting opening [Class- XII] Server")
    try:
        loc = pyautogui.locateCenterOnScreen("bin/server2.png")
    except:
        loc = pyautogui.locateCenterOnScreen(r'C:/Users/Dunking/Documents/Python33/AutoJoin/bin/server2.png')
    print('\n\nServer found. Coordinates - ',loc)
    pyautogui.moveTo(loc)
    pyautogui.click()
    print("\n\nServer succesfully opened")
    pyautogui.click(classes[dclass])
    print("\nSuccesfully joined ",dclass," class.")
 
print("                ------------AutoJoiner------------\n    Ik the name's lame,couldn't come up with anything better\n\n\n")

weekday = datetime.datetime.today().weekday()
print('Today is - ',datetime.datetime.today().strftime('%A'),'\n\n')

classes = {'english' : (144,403),
           'chemistry' :(144,475),
           'cs' : (144,545),
           'physics' : (144,437),
           'maths' : (144, 512) }

schedule = {0:'english',
            1:'english',
            2:'chemistry',
            3:'chemistry',
            4:'cs',
            5:'physics',
            6:'nuffin'}

dclass = schedule[weekday]
print("\n\nSubject Selected as per the schedule : ",dclass)

otm = ""
timern = []
dday = input("\n\nEnter Time or Press enter")
if dday == "" : 
    dday = "10:00:00"

print("\n\nWaiting For Clock to show - ",dday)

while timern != dday:
    timern = str(datetime.datetime.now()).split()[1].split(".")[0]
    if otm == timern:
        continue
    else:
        otm = timern
        print(timern)




print("\n\n\n--------Initiating Join Process--------")    
pyautogui.moveTo(715,1035)
pyautogui.click()
print("\n\n\nSuccesfully Switched to Discord")

    
clickit()
print("\n\n\n\n----------------Have fun studying (Ik you won't)----------------")
