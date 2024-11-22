from States.Testers import *
from States.makers import *
import os

def TestTileState():
    f = open("MineSweeper/TestGameState.cpp", "x")
    f.write(getTileStateTester())
    f.close()
    MakeMake([], "GameStater", "TestGameState.cpp", "MineSweeper" )
    os.system("cmake .")
    os.system("make")
    print(os.system("./GameStater | python3 recv.py"))        

def TestGameState():
    f = open("MineSweeper/TestGameState.cpp", "x")
    f.write(getGameStateTester("GameState","GameState"))
    f.close()
    MakeMake([], "GameStater", "TestGameState.cpp", "MineSweeper" )
    os.system("cmake .")
    os.system("make")
    print(os.system("./GameStater | python3 recv.py"))
    
def TestGameStateFile():
    f = open("MineSweeper/TestGameState.cpp", "x")
    f.write(getStateFromFileTester())
    f.close()
    MakeMake([], "GameStater", "TestGameState.cpp", "MineSweeper" )
    os.system("cmake .")
    os.system("make")
    print(os.system("./GameStater | python3 recv.py"))

