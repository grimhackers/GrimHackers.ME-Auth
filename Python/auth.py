import requests
import json
import random
import os

authgroup = [3, 5, 6, 7, 8, 12, 13]
set_a = set(authgroup)
n = random.randint(0, 22)
secondarygroup = ""
set_b = ""

def grimauth():
    if os.path.isfile('key.dat'):
        f = open('key.dat', 'r')
        authkey = f.read()
        print("Please wait...")
        print("Connecting to GrimHackers Server #", n, sep="")

        checkauth2 = requests.get('https://grimhackers.me/auth/verify?auth_code=' + authkey)

        checkauth = requests.get('https://grimhackers.me/auth/verify?auth_code=' + authkey).json()

        with checkauth2:
            json2 = json.loads(checkauth2.text)
            if 'No user exists' in checkauth2.text:
                print("Error. Invalid Auth.")
                f.close()
                os.remove('key.dat')
                exit()
            else:
                print("Hello,", checkauth["username"])
                secondarygroup = checkauth["secondarygroup"]
                set_b = set(secondarygroup)
                if (set_a & set_b):
                    f = open('key.dat', 'w')
                    f.write(authkey)
                    print("Success. Logging you in.")
                else:
                    print("You need to be Premium+ to use this tool sir.")
                    exit()
    else:
        authkey = str(input('Insert GrimHackers.ME Auth Key: '))

        print("Please wait...")
        print("Connecting to GrimHackers Server #", n, sep="")

        checkauth2 = requests.get('https://grimhackers.me/auth/verify?auth_code=' + authkey)

        checkauth = requests.get('https://grimhackers.me/auth/verify?auth_code=' + authkey).json()

        with checkauth2:
            json2 = json.loads(checkauth2.text)
            if 'No user exists' in checkauth2.text:
                print("Error. Invalid Auth.")
                exit()
            else:
                print("Hello,", checkauth["username"])
                secondarygroup = checkauth["secondarygroup"]
                set_b = set(secondarygroup)
                if (set_a & set_b):
                    f = open('key.dat', 'w')
                    f.write(authkey)
                    print("Success. Logging you in.")
                else:
                    print("You need to be Premium+ to use this tool sir.")
                    exit()
