def main():
    with open("flags/wrongflag.txt", "r", encoding="utf-8") as file:
        unreadableFlag = file.read()

        #get rid of new lines

        unreadableFlag = unreadableFlag.replace("\n", "").replace("\n", "")
        #makeItByte = unreadableFlag.encode()
        #print(makeItByte)

        #unshift

        n = None #figure it OUT!
        almostReadable = everyNthChar(makeItByte,n)
        #print(almostReadable)

        #decrease letters

        gettingCloser = shift(almostReadable,-14)
        #print(gettingCloser)

        #pull out flag

        flag = gettingCloser
        print(extractFlag(flag))

def shift(data, amount):
    result = bytearray(data)
    for i in len(result):
        result[i] = (result[i] + amount) % 128
    return result

def everyNthChar(flag, n):
    if len(flag) % n != 1:
        return None
    else:
        newByte = bytearray()
        i = 0 
        while i < len(flag):
            newByte.append(flag[i])
            i += n
        return newByte

def extractFlag(flag):
    IDX = flag.find("CTF{")
    finalFlag = ""
    while flag[IDX] != "}":
        finalFlag += flag[IDX]
        IDX -= 1
    return finalFlag + "}"


if __name__ == "__main__":
    main()