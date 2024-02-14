import os
if __name__ == '__main__':
    print("Welcome to Robospeaker ver. 1.1,created by rahul.")
    while True:
        x = input("Ener what you want to say?:")
        if x == "q":
            os.system("Say 'bye to user'")
            break
        command = f"say {x}" ;
        os.system(command)