def checker(pwd):
    vuln = []
    spec = ['!', '@', '#', '$', '%', '&', '=']
    cap = 0
    spc = 0
    num = 0
    smll = 0
    while True:
        if len(pwd) >= 16:
            for p in pwd:
                if p.isdigit():
                    num += 1

            for p in pwd:
                if p.islower():
                    smll += 1

            for p in pwd:
                if p.isupper():
                    cap += 1

            for p in pwd:
                if p in spec:
                    spc += 1

            break

        else:
            print("It must be 16 or more chars long ... Try again :/ \n")

    if spc >= 3:
        em4 = "✅"
        vuln.append(True)
    else:
        em4 = "❌"
    if cap >= 3:
        em3 = "✅"
        vuln.append(True)
    else:
        em3 = "❌"
    if smll >= 6:
        em2 = "✅"
        vuln.append(True)
    else:
        em2 = "❌"
    if num >= 4:
        em1 = "✅"
        vuln.append(True)
    else:
        em1 = "❌"

    print(smll, "/6 small letters - ", em2)
    print(cap, "/3 capital letters - ", em3)
    print(num, "/4 numbers - ", em1)
    print(spc, "/3 special characters - ", em4)
    x = 0
    for i in vuln:
        if i:
            x += 1
    if x == 4:
        print("\nStrong password !")
    elif x == 3:
        print("\nMediocre password !")
    else:
        exit("\nWEAK PASSWORD")

    return x
