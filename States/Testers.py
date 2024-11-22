def getGameStateTester(Gamestatename:str, className: str):
    TestFile = f"""
#include "{Gamestatename}.h"
#include <iostream>
#include <signal.h>
#include <cstring>

void handler(int nSignum, siginfo_t* si, void* vcontext) {{
  std::cout << "❌ Segmentation fault" << std::endl;

  ucontext_t* context = (ucontext_t*)vcontext;
  context->uc_mcontext.gregs[REG_RIP]++;
}}

int main(){{
    struct sigaction action;
    memset(&action, 0, sizeof(struct sigaction));
    action.sa_flags = SA_SIGINFO;
    action.sa_sigaction = handler;
    sigaction(SIGSEGV, &action, NULL);
    {className}* gameStarter = new {className}(sf::Vector2i(25,16));
    delete gameStarter;
    gameStarter = new {className}(sf::Vector2i(25,16), 50);
    delete gameStarter;
    gameStarter = new {className}();
    int flags = gameStarter->getFlagCount();
    int mines = gameStarter->getMineCount();
    {className}::PlayStatus first = gameStarter->getPlayStatus();
    Tile* tile;
    for (int i = 0; i < 25; i++){{
        for (int j = 0; j < 16; j++){{
            tile = gameStarter->getTile(j,i);
        }}
    }}
    gameStarter->setPlayStatus(first);
    {className}::PlayStatus second = gameStarter->getPlayStatus();
    if (second != first){{
        std::cout << "❌ Differing Play Status" << std::endl;
        return 1;
    }}
    if (flags != 0){{
        std::cout << "❌ Incorrect Flags" << std::endl;
        return 1;
    }}
    if (mines != 50){{
        std::cout << "❌ Incorrect Mines" << std::endl;
        return 1;
    }}
    tile->draw();
    delete gameStarter;
    
    //testboard1.brd
    {className}* gameStarters = new {className}("/MineSweeper/boards/testboard1.brd", sf::Vector2i(21, 18));
    Tile* Sectile = gameStarters->getTile(0,0);
    
    delete gameStarters;
    return 0;
}}
    
    """
    return TestFile

def getTileStateTester():
    TestFile = f"""
#include "GameState.h"
#include <iostream>
#include <signal.h>
#include <cstring>
#include <time.h>

void handler(int nSignum, siginfo_t* si, void* vcontext) {{
  std::cout << "❌ Segmentation fault" << std::endl;
  
  ucontext_t* context = (ucontext_t*)vcontext;
  context->uc_mcontext.gregs[REG_RIP]++;
}}

int main(){{
    struct sigaction action;
    memset(&action, 0, sizeof(struct sigaction));
    action.sa_flags = SA_SIGINFO;
    action.sa_sigaction = handler;
    sigaction(SIGSEGV, &action, NULL);
    
    
    Toolbox &toolbox = Toolbox::getInstance();
    clock_t time_req;
    time_req = clock();
    // (float)time_req / CLOCKS_PER_SEC;
    GameState* Starter = new GameState();
    Starter->getTile(5,5)->onClickLeft();
    
    Tile::State temp = Starter->getTile(5,5)->getState();
    int i = 6;
    while(temp != Tile::State::HIDDEN){{
        temp = Starter->getTile(i,5)->getState();
        i++;
        std::cout << i << std::endl;
    }}
    std::cout << i << std::endl;
    Starter->getTile(5,6)->getState();

    
    GameState* Start = new GameState();
    Start->getTile(5,5)->onClickLeft();
    
    Tile::State tempe = Start->getTile(5,5)->getState();
    int j = 6;
    while(tempe != Tile::State::HIDDEN){{
        tempe = Start->getTile(j,5)->getState();
        j++;
    }}
    std::cout << j << std::endl;
    std::cout << Start->getTile(5,6)->getState() << std::endl;
    
    if (i == j)
        {{
            std::cout << "❌ not random" << std::endl;
        }}
    for (int checker = 0; checker < 5; checker++){{
    std::cout << ((float)time_req / CLOCKS_PER_SEC) << std::endl;
        while(  ((int)time_req / CLOCKS_PER_SEC) < 2*checker){{
            //std::cout << (int)time_req / CLOCKS_PER_SEC << std::endl;
            time_req = clock();
            toolbox.window->clear();
            int flag = 0;

            Start->getTile((checker*25)%10, (checker*35)%20)->onClickLeft();
            for (int i = 0; i < 10; i++)
            {{
                for (int j = 0; j < 10; j++){{
                    Start->getTile(i+(checker*25)%10,j+(checker*35)%20)->draw();
                    if (Start->getTile(i+(checker*25)%10,j+(checker*35)%15)->getState() != Tile::State::HIDDEN)
                        flag = 1;
                }}
            }}
            if (flag == 0)
                std::cout << "❌ Left Click Didn't work" << std::endl;
            toolbox.window->display();
        }}
    }}
    delete Start;
    Start = new GameState();
    while(  ((int)time_req / CLOCKS_PER_SEC) < 11){{
        //std::cout << (int)time_req / CLOCKS_PER_SEC << std::endl;
        time_req = clock();
        toolbox.window->clear();
        for (int i = 0; i < 5; i++)
        {{
            for (int j = 0; j < 5; j++){{
                Start->getTile(i+3,j+3)->draw();
            }}
        }}
        toolbox.window->display();
    }}


    
  return 0;
}}
    
    """
    return TestFile

def getStateFromFileTester():
    TestFile = f"""
#include "GameState.h"
#include <iostream>
#include <signal.h>
#include <cstring>
#include <time.h>

void handler(int nSignum, siginfo_t* si, void* vcontext) {{
  std::cout << "❌ Segmentation fault" << std::endl;
  
  ucontext_t* context = (ucontext_t*)vcontext;
  context->uc_mcontext.gregs[REG_RIP]++;
}}

int main(){{
    struct sigaction action;
    memset(&action, 0, sizeof(struct sigaction));
    action.sa_flags = SA_SIGINFO;
    action.sa_sigaction = handler;
    sigaction(SIGSEGV, &action, NULL);
    
    GameState* gameStarters = new GameState("./MineSweeper/boards/testboard1.brd", sf::Vector2i(21, 16));
    Tile* Sectile = gameStarters->getTile(0,0);
    Tile::State first = Sectile->getState();
    Sectile->onClickLeft();
    Tile::State second = Sectile->getState();
    if (second != Tile::State::EXPLODED)
        std::cout << "❌ never Exploded" << std::endl;

    gameStarters = new GameState("./MineSweeper/boards/testboard2.brd", sf::Vector2i(25, 16));
    Sectile = gameStarters->getTile(12,3);
    first = Sectile->getState();
    Sectile->onClickLeft();
    Tile* Second;
    for (int i = 0; i < 4; i++){{
        Second = gameStarters->getTile(8, 2+i);
        std::cout << Second->getState()<< std::endl;
        if (Second->getState() == Tile::State::HIDDEN)
            std::cout << "❌ never Revealed" << std::endl;
    }}
    Toolbox &toolbox = Toolbox::getInstance();
    clock_t time_req;
    time_req = clock();
    while(  ((int)time_req / CLOCKS_PER_SEC) < 4){{
        //std::cout << (int)time_req / CLOCKS_PER_SEC << std::endl;
        time_req = clock();
        toolbox.window->clear();
        for (int i = 0; i < 5; i++)
        {{
            for (int j = 0; j < 5; j++){{
                gameStarters->getTile(i+3,j+3)->draw();
            }}
        }}
        toolbox.window->display();
    }}
    std::cout << "Before Free" << std::endl;
    return 0;
}}
    
    """
    return TestFile

