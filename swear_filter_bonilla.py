string_inp = input("Enter you swear words: ")

listd = string_inp.split()

wordlist = ['bobo', 'tanga', 'kupal',]
hasdetected = True
for word in listd:
    for swear in wordlist:
        if word.find(swear)>-1:
            print("*"*len(swear),end=" ")
            hasdetected = True
            break
        else:
            hasdetected = False
    if not hasdetected:
        print(word,end=" ")
