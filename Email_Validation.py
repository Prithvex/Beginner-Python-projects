email = input("Enter Your Email: ")   # a@g.in

k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                
                for l in email:
                    if l.isspace():
                        k = 1
                    elif l.isalpha():
                        if l == l.upper():
                            j = 1
                    elif l.isdigit():
                        continue
                    elif l == "_" or l == "." or l == "@":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")

            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
