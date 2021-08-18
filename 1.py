#HEALTHY PROGRAMMER
import time
from pygame import mixer
Run = True
curtime =time.ctime()
def checkif():
    global check
    check = input(f"If you have to do {xtask} now :\t")
    if check != "y":
        print("Thats not good, please don't skip this")
        checkif()
    else:
        print("Have a great day")
        with open ("temp.log", "a") as filelogcheck:
            filelogcheck.write(f"Task [{xtask}]  Done at [{curtime}]\n\n")

    return check

def water():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(100)
    mixer.music.play()
    print("You Need to Drink one glass of water \n\n")
    checkif()
    if check == "y":
        mixer.music.stop()

def eyes():
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    print("You Need to Take a break and close your eyes \n\n")
    checkif()  
    if check == "y":
        mixer.music.stop()  

def exercise():
    mixer.init()
    mixer.music.load("exercise.ogg")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    print("You Need to do exercise Now \n\n")
    checkif()
    if check == "y":
        mixer.music.stop()

# username = input("Who is Going to use this program? ")
# gender = input("Press M for MALE\nPress F for Female")


# if gender == "M" or "m":
#     print(f"Welcome {username} Sir \n")
# elif gender == "F" or "f":
#     print(f"Welcome {username} Mam \n")
# else:
#     print(f"Welcome {username} Sir \n")
start_water = time.time()
start_eyes = time.time()
start_exercise = time.time()
watertime = 2
eyestime = 1
exercisetime = 3

while Run:
    if time.time() - start_water > watertime:
        xtask = "water drank"
        water()
        start_water = time.time()
    if time.time() - start_eyes > eyestime:
        xtask = "eyes relax"
        eyes()
        start_eyes = time.time()
    if time.time() - start_exercise > exercisetime:
        xtask = "Exercise"
        exercise()
        start_exercise = time.time()    