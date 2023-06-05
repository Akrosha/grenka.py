with open("tllt.txt", "r") as file:
    print("".join([chr(int(str(ord(i)), 8)) for i in file.read()]))