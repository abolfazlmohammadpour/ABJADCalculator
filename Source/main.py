import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from References.Constants.abjad import ABJADListArabic
from References.Constants.abjad import ABJADListPersian
from References.Constants.abjad import UnSupportedCharacters
from References.Constants.abjad import UnSupportedAlphabetics

while True:
    Status = str()
    Language = str()
    Sentence = str()
    Summarize = int()
    
    while True:
        print("1) Start")
        print("2) Exit")
        Status = input("Please Select Your Operation : ")

        try:
            Status = int(Status)
            if Status < 1 or Status > 2:
                print("Error : Select A Valid Operation, Please Try Again.")
                continue
            match Status:
                case int(1):
                    break
                case int(2):
                    exit()
        except:
            print("Error : Just Enter A Number, Please Try Again.")
            continue

    while True:
        print("1) Arabic")
        print("2) Persian")
        Language = str(input("Please Select Your Language : "))

        try:
            Language = int(Language)
            if Language < 1 or Language > 2:
                print("Error : Select A Valid Language, Please Try Again.")
                continue
            break    
        except:
            print("Error : Just Enter A Number, Please Try Again.")
            continue

    Sentence = str(input("Please Enter Your Sentence : "))
    for Character in UnSupportedCharacters:
        Sentence = Sentence.replace(Character, '')

    for Alphabet in UnSupportedAlphabetics:
        Sentence = Sentence.replace(Alphabet, '')

    match Language:
        case int(1):
            for Character in Sentence:
                Character = str(Character)
                if Character in ABJADListArabic.keys():
                    Summarize += ABJADListArabic[Character]
                else:
                    print(f"Error : The <{Character}> Is Not Supported, Please Try Again.")
                    continue
        case int(2):
            for Character in Sentence:
                Character = str(Character)
                if Character in ABJADListPersian.keys():
                    Summarize += ABJADListPersian[Character]
                else:
                    print(f"Error : The <{Character}> Is Not Supported, Please Try Again.")

    
    print(f"\n\nABJAD Value Of Your Sentence Is : {Summarize}\n\n")