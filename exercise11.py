text = input("Please write some text :")

if text == "":
    print("you did not write anything :")
    text = input("Please again write some text :")
    if text != "":
        print(len(text))
else:
    print(len(text))


