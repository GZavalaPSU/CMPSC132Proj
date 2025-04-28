running = True
while True:
    print("Hello")
    gg = int(input("ENTER 1 OR I EJECT"))
    if gg == 1:

        while True:
            gg = int(input("ENTER 1 OR I EJECT AGIN ROUND 2"))
            if gg == 1:
                print("GOTTEM")
            else:
                break
    else:
        break

print("NAH ID BREAK")