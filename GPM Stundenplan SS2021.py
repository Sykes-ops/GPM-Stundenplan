from tkinter import *
import webbrowser
import datetime

USER_NAME = "" # Wenn der Name gespeichert werden soll, hier einfach eingeben
# USER_GROUP_2 = 0 # Wenn die Gruppe für PM + Vorgehensmodelle von der eigentlichen Aufteilung abweicht, hier einfach eingeben
# USER_GROUP_4 = 0 # Wenn die Gruppe für Englisch von der eigentlichen Aufteilung abweicht, hier einfach eingeben

LINKS = {
    "PM + Vorgehensmodelle, Gruppe 1":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/93853095952?pwd=Yy9VWWhESzJ5ZjIwSUZ6U3gvU3Rudz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16870"
    },
    "PM + Vorgehensmodelle, Gruppe 2":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/93853095952?pwd=Yy9VWWhESzJ5ZjIwSUZ6U3gvU3Rudz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16870"
    },
    "PM + Vorgehensmodelle, Zimmermann":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/98834178306?pwd=eXRua1R0elkxTkZhT3NRczhLSFNzQT09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16849"
    },
    "PM + Vorgehensmodelle, Zimmermann 13":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/94599788454?pwd=bEFoTDI0bUZPTDNLdXJPTXBHUGdPdz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16849"
    },
    "PM + Vorgehensmodelle, Zimmermann 16":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/99057389432?pwd=VjY5N3JNMXR1dEdpTVlTc2xjaFlhZz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16849"
    },
    "Englisch 1, Gruppe 1":{
        "Zoom":"https://hs-neu-ulm.zoom.us/j/92641935671?pwd=ek0rRDVsV2w3TFI0eE9VTnFua1pNUT09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16950"
    },
    "Englisch 1, Gruppe 2":{
        "Zoom":"",
        "Elearning":"https://google.com"
    },
    "Englisch 1, Gruppe 3":{
        "Zoom":"",
        "Elearning":"https://google.com"
    },
    "Englisch 1, Gruppe 4":{
        "Zoom":"",
        "Elearning":"https://google.com"
    },
    "Wirtsch.Mathe + Statistik, Gerlach":{ # Mittwoch 14:00 - 15:30
        "Zoom":"https://hs-neu-ulm.zoom.us/j/95149959870?pwd=UDFXMWs5bko1aUJId2NWSUZTQVFpUT09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16904"
    },
    "Wirtsch.Mathe + Statistik, Faußer 1. Hälfte":{ # Mittwoch 15:45 - 17:15 1. Hälfte
        "Zoom":"https://hs-neu-ulm.zoom.us/j/93494273950?pwd=R1FyQUtRd3hKVFZUME52S0pBNFRWdz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16888"
    },
    "Wirtsch.Mathe + Statistik, Faußer 2. Hälfte":{ # Freitag 09:00 - 10:50 2. Hälfte
        "Zoom":"https://hs-neu-ulm.zoom.us/j/93494273950?pwd=R1FyQUtRd3hKVFZUME52S0pBNFRWdz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16886"
    },
    "Wirtsch.Mathe + Statistik, Übungen":{ # Mittwoch 08:15 - 09:45
        "Zoom":"https://hs-neu-ulm.zoom.us/j/96932033370?pwd=R1g4czZHVUNGV2hydlpTM3JNdlBwZz09",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16885"
    },
    "Wirtsch.Mathe + Statistik, Tormählen":{ # Montag 14:00 - 15:30
        "Zoom":"https://hs-neu-ulm.zoom.us/j/99692490323?pwd=QmU4QmlWa1R3cld5dU9wT0RLakZwUT09",
        "Elearning":"https://elearning.hs-neu-ulm.de/enrol/index.php?id=16891"
    },
    "Info- und KommDes":{
        "Zoom":"",
        "Elearning":"https://elearning.hs-neu-ulm.de/course/view.php?id=16869"
    }
}

TIMES = [
    "",
    "08:00 bis 09:00",
    "09:00 bis 10:00",
    "10:00 bis 11:00",
    "11:00 bis 12:00",
    "12:00 bis 13:00",
    "13:00 bis 14:00",
    "14:00 bis 15:00",
    "15:00 bis 16:00",
    "16:00 bis 17:00",
    "17:00 bis 18:00"
]
DAYS = [
    "",
    "MONTAG",
    "DIENSTAG",
    "MITTWOCH",
    "DONNERSTAG",
    "FREITAG"
]

MODULES = {
    1:{
        "Name":"PM + Vorgehensmodelle",
        "Groups":2,
        "Times":[
            {
                "Group":[1],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":1,
                "Starttime":900,
                "Duration":155,
                "Clockstring":"09:00 - 11:35",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Gruppe 1"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Gruppe 1"]["Elearning"]
            },
            {
                "Group":[1],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":1,
                "Starttime":1145,
                "Duration":90,
                "Clockstring":"11:45 - 13:15",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Gruppe 1"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Gruppe 1"]["Elearning"]
            },
            {
                "Group":[2],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":2,
                "Starttime":900,
                "Duration":155,
                "Clockstring":"09:00 - 11:35",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Gruppe 2"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Gruppe 2"]["Elearning"]
            },
            {
                "Group":[2],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":2,
                "Starttime":1145,
                "Duration":90,
                "Clockstring":"11:45 - 13:15",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Gruppe 2"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Gruppe 2"]["Elearning"]
            },
            {
                "Group":[1,2],
                "Weeks":[16],
                "Day":2,
                "Starttime":1400,
                "Duration":195,
                "Clockstring":"14:00 - 17:15",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Zimmermann 16"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Zimmermann 16"]["Elearning"]
            },
            {
                "Group":[1,2],
                "Weeks":[13],
                "Day":3,
                "Starttime":1005,
                "Duration":190,
                "Clockstring":"10:05 - 13:15",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Zimmermann 13"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Zimmermann 13"]["Elearning"]
            },
            {
                "Group":[1,2],
                "Weeks":[12,14,15,17,18],
                "Day":5,
                "Starttime":1400,
                "Duration":195,
                "Clockstring":"14:00 - 17:15",
                "Zoom-Link":LINKS["PM + Vorgehensmodelle, Zimmermann"]["Zoom"],
                "Elearning":LINKS["PM + Vorgehensmodelle, Zimmermann"]["Elearning"]
            }
        ],
    },
    2:{
        "Name":"Wirtsch.Mathe + Statistik",
        "Groups":0,
        "Times":[
            {
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":1,
                "Starttime":1400,
                "Duration":90,
                "Clockstring":"14:00 - 15:30",
                "Zoom-Link":LINKS["Wirtsch.Mathe + Statistik, Tormählen"]["Zoom"],
                "Elearning":LINKS["Wirtsch.Mathe + Statistik, Tormählen"]["Elearning"]
                
            },
            {
                "Weeks":[12,13,14,15,16,17,18,19,23,24,25,26,27],
                "Day":3,
                "Starttime":815,
                "Duration":90,
                "Clockstring":"08:15 - 09:45",
                "Zoom-Link":LINKS["Wirtsch.Mathe + Statistik, Übungen"]["Zoom"],
                "Elearning":LINKS["Wirtsch.Mathe + Statistik, Übungen"]["Elearning"]
            },
            {
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":3,
                "Starttime":1400,
                "Duration":90,
                "Clockstring":"14:00 - 15:30",
                "Zoom-Link":LINKS["Wirtsch.Mathe + Statistik, Gerlach"]["Zoom"],
                "Elearning":LINKS["Wirtsch.Mathe + Statistik, Gerlach"]["Elearning"]
            },
            {
                "Weeks":[12,13,14,15,16,17,18],
                "Day":3,
                "Starttime":1545,
                "Duration":90,
                "Clockstring":"15:45 - 17:15",
                "Zoom-Link":LINKS["Wirtsch.Mathe + Statistik, Faußer 1. Hälfte"]["Zoom"],
                "Elearning":LINKS["Wirtsch.Mathe + Statistik, Faußer 1. Hälfte"]["Elearning"]
            },
            {
                "Weeks":[19,23,24,25,26,27],
                "Day":5,
                "Starttime":900,
                "Duration":110,
                "Clockstring":"09:00 - 10:50",
                "Zoom-Link":LINKS["Wirtsch.Mathe + Statistik, Faußer 2. Hälfte"]["Zoom"],
                "Elearning":LINKS["Wirtsch.Mathe + Statistik, Faußer 2. Hälfte"]["Elearning"]
            }
        ],
    },
    3:{
        "Name":"Englisch 1",
        "Groups":4,
        "Times":[
            {
                "Group":[2],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":2,
                "Starttime":1145,
                "Duration":180,
                "Clockstring":"11:45 - 14:45",
                "Zoom-Link":LINKS["Englisch 1, Gruppe 2"]["Zoom"],
                "Elearning":LINKS["Englisch 1, Gruppe 2"]["Elearning"]
            },
            {
                "Group":[1],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":2,
                "Starttime":915,
                "Duration":140,
                "Clockstring":"09:15 - 11:35",
                "Zoom-Link":LINKS["Englisch 1, Gruppe 1"]["Zoom"],
                "Elearning":LINKS["Englisch 1, Gruppe 1"]["Elearning"]
            },
            {
                "Group":[3],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":4,
                "Starttime":1400,
                "Duration":150,
                "Clockstring":"14:00 - 16:30",
                "Zoom-Link":LINKS["Englisch 1, Gruppe 3"]["Zoom"],
                "Elearning":LINKS["Englisch 1, Gruppe 3"]["Elearning"]
            },
            {
                "Group":[4],
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":4,
                "Starttime":1400,
                "Duration":150,
                "Clockstring":"14:00 - 16:30",
                "Zoom-Link":LINKS["Englisch 1, Gruppe 4"]["Zoom"],
                "Elearning":LINKS["Englisch 1, Gruppe 4"]["Elearning"]
            }
        ]
    },
    4:{
        "Name":"Info- und KommDes",
        "Groups":0,
        "Times":[
            {
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":4,
                "Starttime":815,
                "Duration":155,
                "Clockstring":"08:15 - 10:50",
                "Zoom-Link":LINKS["Info- und KommDes"]["Zoom"],
                "Elearning":LINKS["Info- und KommDes"]["Elearning"]
            },
            {
                "Weeks":[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                "Day":4,
                "Starttime":1050,
                "Duration":100,
                "Clockstring":"10:50 - 12:30",
                "Zoom-Link":LINKS["Info- und KommDes"]["Zoom"],
                "Elearning":LINKS["Info- und KommDes"]["Elearning"]
            }
        ]
    }
}

LABEL_RGB= "#0099ff"
LABEL_MODULE_RGB = "#33ccff"
LABEL_WIDTH = 100
LABEL_HEIGHT = 30
LABEL_SPACING_X = LABEL_WIDTH + 5
LABEL_SPACING_Y = LABEL_HEIGHT + 5

TTP = LABEL_HEIGHT / 60

FIRST_WEEK = 12
LAST_WEEK = 27

if datetime.date.today().isocalendar()[1] < FIRST_WEEK:
    CURRENT_WEEK = FIRST_WEEK
elif datetime.date.today().isocalendar()[1] > LAST_WEEK:
    CURRENT_WEEK = LAST_WEEK
else:
    CURRENT_WEEK = datetime.date.today().isocalendar()[1]

CURRENT_WEEK_DISPLAYED = CURRENT_WEEK

WINDOW_WIDTH = (len(DAYS) * LABEL_SPACING_X - 5) + 2 * LABEL_SPACING_X
WINDOW_HEIGHT = len(TIMES) * LABEL_SPACING_Y - 5

window = Tk()
window.title("GPM2 Stundenplan - SS2021")
window.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

def ModulePosX(moduleNumber):
    rList = []
    for times in MODULES[moduleNumber]["Times"]:
        rList.append(times["Day"] * LABEL_SPACING_X)
    return rList

def ModulePosY(moduleNumber):
    rList = []
    for times in MODULES[moduleNumber]["Times"]:
        if len(str(times["Starttime"])) == 3:
            rList.append(
                ((int(str(times["Starttime"])[0]) - 7) * LABEL_SPACING_Y)
                + (times["Starttime"] - int(str(times["Starttime"])[0] + "00")) * TTP
                )
        elif len(str(times["Starttime"])) == 4:
            rList.append(
                ((int(str(times["Starttime"])[0] + str(times["Starttime"])[1]) - 7) * LABEL_SPACING_Y)
                + (times["Starttime"] - int(str(times["Starttime"])[0] + str(times["Starttime"])[1] + "00")) * TTP
                )
    return rList

def ModuleHeight(moduleNumber):
    rList = []
    for times in MODULES[moduleNumber]["Times"]:
        rList.append(times["Duration"] * TTP + (((int(str(times["Starttime"])[-2:]) + times["Duration"]) // 60 * 5)))
    return rList

def OpenURL(times, zoomlink):
    if zoomlink:
        if times["Zoom-Link"] == "":
            return lambda e: webbrowser.open_new(times["Elearning"])
        else:
            return lambda e: webbrowser.open_new(times["Zoom-Link"])
    else:
        return lambda e: webbrowser.open_new(times["Elearning"])

def ChangeWeek(n):
    global CURRENT_WEEK_DISPLAYED
    global USER_GROUP_2
    global USER_GROUP_4

    if n == 0:
        CURRENT_WEEK_DISPLAYED = CURRENT_WEEK
    else:
        CURRENT_WEEK_DISPLAYED += n
    displayedWeekLabel["text"] = "Angezeigte KW: " + str(CURRENT_WEEK_DISPLAYED)
    DisplayModules(CURRENT_WEEK_DISPLAYED, USER_GROUP_2, USER_GROUP_4)
    SetButtons()

if USER_NAME == "":
    enterNameLabel = Label(window, text="Nachname: " + USER_NAME, anchor="w", wraplengt=120)
    enterNameLabel.pack()
    enterNameLabel.place(x=680, y=65, width=120, height=60)
    enterNameEntry = Entry(window)
    enterNameEntry.place(x=680, y=130, width=120, height=30)
    enterNameButton = Button(window, text="Stundenplan anzeigen", command=lambda: SetUser())
    enterNameButton.place(x=680, y=165, width=120, height=30)

forwardButton = Button(window, text=">", command=lambda: ChangeWeek(1))
forwardButton.place(x=800, y=200, width=30, height=30)
currentButton = Button(window, text="Momentane Woche", command=lambda: ChangeWeek(0))
currentButton.place(x=680, y=200, width=120, height=30)
backwardButton = Button(window, text="<", command=lambda: ChangeWeek(-1))
backwardButton.place(x=650, y=200, width=30, height=30)

currentWeekLabel = Label(window, text="Momentane KW: " + str(CURRENT_WEEK))
currentWeekLabel.place(x=680, y=235, width=120, height=30)
displayedWeekLabel = Label(window, text="Angezeigte KW: " + str(CURRENT_WEEK_DISPLAYED))
displayedWeekLabel.place(x=680, y=260, width=120, height=30)

def SetButtons():
    if CURRENT_WEEK_DISPLAYED <= FIRST_WEEK:
        backwardButton["state"] = "disabled"
        backwardButton["text"] = ""
    else:
        backwardButton["state"] = "normal"
        backwardButton["text"] = "<"

    if CURRENT_WEEK_DISPLAYED >= LAST_WEEK:
        forwardButton["state"] = "disabled"
        forwardButton["text"] = ""
    else:
        forwardButton["state"] = "normal"
        forwardButton["text"] = ">"

def SetTable():
    for time in TIMES:
        newLabel = Label(
            window, 
            text=TIMES[TIMES.index(time)],
            bg=LABEL_RGB,
            )
        newLabel.place(x=0,y=TIMES.index(time)*LABEL_SPACING_Y,width=LABEL_WIDTH,height=LABEL_HEIGHT)

    for day in DAYS:
        newLabel = Label(
            window, 
            text=DAYS[DAYS.index(day)],
            bg=LABEL_RGB,
            )
        newLabel.place(x=DAYS.index(day)*LABEL_SPACING_X,y=0,width=LABEL_WIDTH,height=LABEL_HEIGHT)

def SetUser():
    global USER_NAME
    global USER_GROUP_2
    global USER_GROUP_4

    USER_NAME = enterNameEntry.get()
    enterNameLabel["text"] = "Nachname: " + USER_NAME

    if USER_NAME[:2] <= "Kr":
        USER_GROUP_2 = 1
    else:
        USER_GROUP_2 = 2
    
    if USER_NAME[:1] <= "E":
        USER_GROUP_4 = 1
    elif USER_NAME[:2] <= "Kr":
        USER_GROUP_4 = 2
    elif USER_NAME[:1] <= "R":
        USER_GROUP_4 = 3
    else:
        USER_GROUP_4 = 4
    
    DisplayModules(CURRENT_WEEK_DISPLAYED, USER_GROUP_2, USER_GROUP_4)

currentlyDisplayedLabels = []
def DisplayModules(currentWeek, group2, group4):
    global currentlyDisplayedLabels
    for label in currentlyDisplayedLabels:
        label.destroy()
    currentlyDisplayedLabels = []
    if not USER_NAME == "":
        for module in MODULES:
            for times in MODULES[module]["Times"]:
                if currentWeek in times["Weeks"]:
                    if MODULES[module]["Groups"] == 0 or (MODULES[module]["Groups"] == 2 and group2 in times["Group"]) or (MODULES[module]["Groups"] == 4 and group4 in times["Group"]):
                        newLabel = Label(window, text=MODULES[module]["Name"] + "\n" + times["Clockstring"], bg=LABEL_MODULE_RGB, cursor="hand2", wraplengt=100)
                        newLabel.place(x=ModulePosX(module)[MODULES[module]["Times"].index(times)], y=ModulePosY(module)[MODULES[module]["Times"].index(times)], width=LABEL_WIDTH, height=ModuleHeight(module)[MODULES[module]["Times"].index(times)])
                        newLabel.bind("<Button-1>", OpenURL(times, True))
                        newLabel.bind("<Button-3>", OpenURL(times, False))
                        currentlyDisplayedLabels.append(newLabel)

SetButtons()
SetTable()
window.mainloop()