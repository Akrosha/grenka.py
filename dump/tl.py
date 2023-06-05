with open("tllt.txt", "w") as file:
    file.write("".join([chr(int(oct(ord(i))[2:])) for i in input("to lukrat>")]))
