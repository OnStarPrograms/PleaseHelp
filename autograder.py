#!/usr/bin/python3.12
import os
import re
import States.TestStates

points = 150


###### NOTES ################################
#                                           #
# Testing where RenderWindow is             #
# in the ToolBoxclass named **window**      #
# AND IS A POINTER TO A RENDERWINDOW OBJECT #
#                                           #
# THIS IS NOT YOUR FINAL GRADE              #
#                                           #
#############################################


TrueButtons = [['public:'], ['Button(sf::Vector2f', 'std::function<void(void)>'], ['sf::Vector2f', 'getPosition()'], ['sf::Sprite*', 'getSprite()'], ['void', 'setSprite(sf::Sprite*'], ['void', 'onClick()'], ['~Button()']]
TrueGameState = [['public:'], ['enum', 'PlayStatus'], ['GameState(sf::Vector2i'], ['GameState(const'], ['~GameState()'], ['int', 'getFlagCount()'], ['int', 'getMineCount()'], ['Tile*', 'getTile(int'], ['PlayStatus', 'getPlayStatus()'], ['void', 'setPlayStatus(PlayStatus']]
TrueTileState = [['public:'], ['enum', 'State'], ['Tile(sf::Vector2f'], ['~Tile()'], ['void', 'draw()'], ['sf::Vector2f', 'getLocation()'], ['State', 'getState()'], ['void', 'setState(State'], ['void', 'revealNeighbors()'], ['void', 'onClickLeft()'], ['void', 'setNeighbors(std::array<Tile*'], ['void', 'onClickRight()']]


def Check_Private():
    pass

def Lexer(filename):
    os.chdir("./MineSweeper")
    f = open(filename)
    buffer = f.readlines()
    f.close()
    os.chdir("../")
    
    tempbuffer = buffer
    buffer = []
    for i,j in enumerate(tempbuffer):
        temp = j.split(";")
        for k in temp:
            if k != '':
                buffer.append(k)
    
    for i,j in enumerate(buffer):
        temp = j.split("\n")
        buffer[i] = ""
        for k in temp:
            if k != '':
                buffer[i]+=k

    for i,j in enumerate(buffer):
        temp = j.split(",")
        buffer[i] = ""
        for k in temp:
            if k != '':
                buffer[i]+=k

    tempbuffer = buffer
    buffer = [[]]
    for i,j in enumerate(tempbuffer):
        temp = j.split(" ")
        buffer.append([])
        for k in temp:
            if k != '':
                buffer[i].append(k)
    
    tempbuffer = buffer
    buffer = [[]]
    for i in tempbuffer:
        if i != [] and i[0][0] != "/":
            buffer.append(i)
   
    
    publics = False
    private = False
    
    tempbuffer = buffer
    buffer = [[]]
    trig = 0
    classTrig = 0
    for i,j in enumerate(tempbuffer):
        buffer.append([])
        for k in j:
            if trig == 0:
                buffer[i].append(k)
            if ("class" in k):
                classTrig = 1
            if ("{" in k):
                if (classTrig == 0):
                    trig += 1
                else:
                    classTrig = 0
            elif ("}" in k and trig > 0):
                trig -= 1
    
    tempbuffer = buffer
    buffer = []
    for i in tempbuffer:
        if i != [] and i[0][0] != "{" and i[0][0] != "}" and i[0] != "#include" and i[0] != "class":
            buffer.append(i)   
    
    for i,j in enumerate(buffer):
        if ("}" in j[0]):
            j[0] = j[0][1:]
        if ("{" in j[-1]):
            j[-1] = j[-1][0:-1]
     
    return buffer


def get_protecteds(file):
    buffer = Lexer(file)
    myPublic = []
    publics = False
    k = 0
    for i,j in enumerate(buffer):
        if (len(j) > 0 and "protected:" in j[0].lower()):
            publics = True
        
        if ((len(j) > 0 and "public:" in j[0].lower()) or (len(j) > 0 and "private:" in j[0].lower())):
            publics = False
             
        if (publics == True):
            myPublic.append(j)
    return myPublic

def get_privates(file):
    buffer = Lexer(file)
    myPublic = []
    publics = False
    k = 0
    for i,j in enumerate(buffer):
        if (len(j) > 0 and "private:" in j[0].lower()):
            publics = True
        
        if ((len(j) > 0 and "public:" in j[0].lower()) or (len(j) > 0 and "protected:" in j[0].lower())):
            publics = False
             
        if (publics == True):
            myPublic.append(j)
    return myPublic
        
def get_publics(file):
    buffer = Lexer(file)
    myPublic = []
    publics = False
    k = 0
    for i,j in enumerate(buffer):
        if (len(j) > 0 and "public:" in j[0].lower()):
            publics = True
        
        if ((len(j) > 0 and "private:" in j[0].lower()) or (len(j) > 0 and "protected:" in j[0].lower())):
            publics = False
             
        if (publics == True):
            myPublic.append(j)
    return myPublic
         
def cleanup():
    # os.system("rmdir /s")
    for i in os.listdir():
        if (".py" not in i and ".pdf" not in i and "MineSweeper" not in i and "images" not in i and "States" not in i):
            try:
                os.remove(f"{i}")
            except:
                os.system(f"rm {i} -r")
                # os.system("Y")
    
    try:
        os.remove(f"./MineSweeper/TestGameState.cpp")
    except:
         pass
    # try:
    #       os.remove("CMakeLists.txt")
    # except:
    #       pass
    # try:
    #       os.remove("Makefile")
    # except:
    #       pass
    # os.chdir("../")
    # for i in os.listdir():
    #     if (".zip" in i):
    #         os.remove(f"{i}")
    return 0

    
def getFiles():
    os.chdir("./MineSweeper")
    files = [i for i in os.listdir() if '.' in i and '.git' not in i and '.md' not in i]
    os.chdir("../")
    return files
      
def readGrade(points):
    f = open("States/grade.txt", "r")
    points -= int(f.read())
    f.close()
    return points
    

if __name__ == "__main__":
    
    publics  = get_publics("Button.h")
    pass
    print(publics)
    
    for Trueb in TrueButtons:
        flag = False
        for publicButton in publics:
            if (Trueb[0] == publicButton[0]):
                flag = True
        if flag == False:
            print("❌ Button Class doesn't have proper publics")
    
    publics  = get_publics("GameState.h")
    pass
    print(publics)
    
    for Trueb in TrueGameState:
        flag = False
        for publicButton in publics:
            if (Trueb[0] == publicButton[0]):
                flag = True
        if flag == False:
            print("❌ GameState Class doesn't have proper publics")
    
    publics  = get_publics("Tile.h")
    pass
    print(publics)
    
    for Trueb in TrueTileState:
        flag = False
        for publicButton in publics:
            if (Trueb[0] == publicButton[0]):
                flag = True
        if flag == False:
            print("❌ Tile Class doesn't have proper publics")
    

    print("✅ Testing GameState Class ✅")
    States.TestStates.TestGameState()
    cleanup()
    points = readGrade(points)
    print("✅ Testing The Tiles Class ✅")
    States.TestStates.TestTileState()
    cleanup()
    points = readGrade(points)
    print("✅ Testing Test Files ✅")
    States.TestStates.TestGameStateFile()
    cleanup()
    points = readGrade(points)
    print(f"✅ {points}/150 Tested Normal GameState and Tiles ✅\n✅ Check The Command Line Interface for Errors ✅\n ✅ NOT FINISHED GRADE!!! ✅")