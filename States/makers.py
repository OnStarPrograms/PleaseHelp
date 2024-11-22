def MakeMake(files: list[str], test: str, testerfile: str, directory: str):
    f = open("CMakeLists.txt", "x")
    f.write(f""" 
cmake_minimum_required(VERSION 3.5.0)
project({test} VERSION 0.1.0 LANGUAGES C CXX)

# set(SFML_DIR "C:/SFML-2.5.1/lib/cmake/SFML")
find_package(SFML 2.5 COMPONENTS graphics audio REQUIRED)

add_executable({test} {directory}/{testerfile})
target_link_libraries({test} sfml-graphics sfml-audio)

set(CPACK_PROJECT_NAME ${{PROJECT_NAME}})
set(CPACK_PROJECT_VERSION ${{PROJECT_VERSION}})
include(CPack)
            
            """)
    f.write("\n")
    f.close()

def addMake(files: list[str], test: str, testerfile: str, directory: str):
    f = open("Makefile", "a")
    f.write(f"{test}:\n")
    f.write(f"\t g++ -o {test} {directory}/{testerfile}")
    for i in files:
        f.write(f" {directory}/{i}")
    f.write("\n")
    f.close()
         