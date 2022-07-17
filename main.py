import os
from tkinter import *
import time
import keyboard
from termcolor import colored
import cryptocode



infos = {}


def afficher():
    if os.path.exists(infos['path']):
        for file in os.listdir(infos['path']):
            print(file)
            time.sleep(0.05)
    time.sleep(0.75)
    print("\n>>Press Enter to continue\n")
    rec = keyboard.record(until='Enter')
    options(infos['path'])

def gestionnaire(path_1, extensions):
    if os.path.exists(path_1):
        for file in os.listdir(path_1):
            for ext in extensions:
                if file.endswith(ext):
                    if os.path.exists(path_1 + "\{}".format(ext + "Files")):
                        ext_folders = path_1 + "\{}".format(ext+ "Files")
                        os.rename(path_1 + "\{}".format(file), ext_folders + "\{}".format(file))
                        print(f"{file} ---> {ext}")
                        time.sleep(0.025)
                    else:
                        os.mkdir(path_1 + "\{}".format(ext+ "Files"))
                        ext_folders = path_1 + "\{}".format(ext+ "Files")
                        os.rename(path_1 + "\{}".format(file), ext_folders + "\{}".format(file))
                        print(f"{file} ---> {ext}")
                        time.sleep(0.025)
    time.sleep(0.75)
    print("\n>>Press Enter to continue\n")
    rec = keyboard.record(until='Enter')
    time.sleep(0.5)
    options(infos['path'])

def delete(extensions):
    path_1 = infos['path']
    if os.path.exists(path_1):
        for file in os.listdir(path_1):
            for ext in extensions:
                if file.endswith(ext):
                    os.remove(path_1 + "\{}".format(file))
                    print(file + " supprimé")
                    time.sleep(0.025)
    time.sleep(0.75)
    print("\n>>Press Enter to continue\n")
    rec = keyboard.record(until='Enter')
    time.sleep(0.5)
    options(infos['path'])

def files():
    print(' ')
    time.sleep(0.25)
    print("\n\33[90m        Copyright © 2022 Formu-Git")
    time.sleep(0.25)
    print("________________________________________________\n\33[0m")
    print("\33[35m ███████  ████████  ██        ████████   ██████   \33[0m")
    time.sleep(0.25)
    print("\33[35m ██          ██     ██        ██        ██        \33[0m")
    time.sleep(0.25)
    print("\33[35m ███████     ██     ██        ████████   ██████   \33[0m")
    time.sleep(0.25)
    print("\33[35m ██          ██     ██        ██              ██  \33[0m")
    time.sleep(0.25)
    print("\33[35m ██       ████████  ████████  ████████   ██████ \n\33[0m")
    time.sleep(0.25)

def main():
    os.system('cls')
    files()
    time.sleep(0.2)
    print("\33[90mDiscord: .formu#1578")
    print("\33[90mhttps://github.com/Formu-Git")
    time.sleep(0.5)
    print("\n\33[90m>>\33[35mPress Enter to continue\n")
    rec = keyboard.record(until='Enter')
    time.sleep(0.5)
    get_repertoire()

def get_repertoire():
    os.system('cls')
    files()
    repertoire = input("\n\33[90m>>\33[35mPlease indicate any directory\n\33[90m>>\33[35m")
    verif_repertoire(repertoire)

def verif_repertoire(repertoire):
    if os.path.exists(repertoire):
        infos['path'] = repertoire
        options(repertoire)
    else:
        get_repertoire()

def options(repertoire):
    os.system('cls')
    files()
    print(f"\n \33[90m>>\33[35m{repertoire} \n")
    options = input("\33[35m[ 1 ] \33[90mClassify  files with their extension   \n\33[35m[ 2 ] \33[90mDisplay all the files of the folder  \n\33[35m[ 3 ] \33[90mDelete files that has a certain extension \n\33[35m[ 4 ] \33[90mCrypt or Decrypt a file  \n\33[35m[ 5 ] \33[90mChoose another directory   \n\33[35m[ exit ] \33[90mQuit \n\n\33[90m>> \33[35mChoose an option\n\33[90m>>\33[35m")
    verif_option(options)

def verif_option(option):
    if option in ['1', '2', '3', '4']:
        if option == '1':
            time.sleep(0.5)
            extensions = input(
                "\n\33[90m>>\33[35mChoose extensions \n>>Exemple: .txt .docx .pdf \n\33[90m>>\33[35m")
            extensions = extensions.split(" ")
            time.sleep(1)
            gestionnaire(infos['path'], extensions)
        elif option == '2':
            time.sleep(0.5)
            afficher()
        elif option == '5':
            time.sleep(0.5)
            get_repertoire()
        elif option == '3':
            extensions = input(
                "\n\33[90m>>\33[35mChoose extensions \n>>Exemple: .txt .docx .pdf \n\33[90m>>\33[35m")
            extensions = extensions.split(" ")
            time.sleep(1)
            delete(extensions)
        elif option == '4':
            os.system('cls')
            time.sleep(0.1)
            print("Soon !")
            options(infos['path'])
    elif option == 'exit':
        time.sleep(0.5)
        print("\n\33[90m>>...")
        time.sleep(1)
        os.system('cls')
        exit()
    else:
        options(infos['path'])

main()
