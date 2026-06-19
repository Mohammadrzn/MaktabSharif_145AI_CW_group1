with open("name.txt","r") as file:
    txt = file.readlines()
    for i,text in enumerate(txt):
        txt[i] =text.replace("\n","")
    print(txt)
    print(len(txt))