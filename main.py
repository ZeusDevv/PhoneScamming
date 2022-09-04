import requests
import time
import json
import random
import string

access_key = "34bdc6199c909ef0faf2871d165235a2"

def status():
    url =  'http://apilayer.net/api/validate?access_key=' + access_key
    try:
        request = requests.get(url)
        req = request.json()
        valid = str(req['error']['info'])
        print(valid)
    except Exception:
        print("Your IP is being rate limited")

def checkgenn():
    areacode = input("Enter the area code > ")
    amount = input("How many numbers > ")
    checkgen(areacode, amount)

def check():
    with open ("phones.txt", "r") as file:
        while True:
            next_line = file.readline()

            if not next_line:
                print("\nNo More Phones To Check")
                break
            url =  'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + next_line + "&format=1"
            request = requests.get(url)
            req = request.json()
            valid = str(req['valid'])
            number = str(req['number'])
            location = req['location']
            carrier = req['carrier']
            if valid == "True":
                with open("valid.txt", "a") as f:
                    f.write(f"{number} {location} {carrier}\n")
                    print("Valid Phone > "+ number + " " + location+ " " + carrier)
                    time.sleep(3)
            if valid == "False":
                time.sleep(3)
                print(f"{number} Is Invalid!")

def checkgen(areacode, amount):
    name = "".join(random.choice(string.ascii_lowercase) for i in range(16))

    for numbers in range(int(amount)):
        with open (f"generated/{name}.txt", "a") as f:

            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            randomnum1 = random.choice(numbers)
            randomnum2 = random.choice(numbers)
            randomnum3 = random.choice(numbers)
            randomnum4 = random.choice(numbers)
            randomnum5 = random.choice(numbers)
            randomnum6 = random.choice(numbers)
            randomnum7 = random.choice(numbers)

            phonenumber = str((f"1{areacode}{randomnum1}{randomnum2}{randomnum3}{randomnum4}{randomnum5}{randomnum6}{randomnum7}"))
            f.write(phonenumber+"\n")
    print("Generating Numbers")
            #print(phonenumber + " | Created")

    print(f"File Created in /generated/{name}.txt") 

    with open (f"generated/{name}.txt", "r") as file:
        while True:
            next_line = file.readline()
            if not next_line:
                print("\nNo More Phones To Check")
                break
            try:
                url =  'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + next_line + "&format=1"
                request = requests.get(url)
                req = request.json()
                valid = str(req['valid'])
                number = str(req['number'])
                location = req['location']
                carrier = req['carrier']
                if valid == "True":
                    if carrier == "Cellco Partnership (Verizon Wireless)":
                        with open(f"valid/Verizon/valid-{name}.txt", "a") as f:
                            f.write(f"{number}\n")
                            print("Valid Phone > "+ number + " " + location+ " " + carrier)
                            time.sleep(3)
                    elif carrier == "T-Mobile USA Inc.":
                        with open(f"valid/TMobile/valid-{name}.txt", "a") as f:
                            f.write(f"{number}\n")
                            print("Valid Phone > "+ number + " " + location+ " " + carrier)
                            time.sleep(3)
                    elif carrier == "AT&T Mobility LLC":
                        with open(f"valid/ATT/valid-{name}.txt", "a") as f:
                            f.write(f"{number}\n")
                            print("Valid Phone > "+ number + " " + location+ " " + carrier)
                            time.sleep(3)
                    else:
                        with open(f"valid/Unspecified/valid-{name}.txt", "a") as f:
                            f.write(f"{number} {location} {carrier}\n")
                            print("Valid Phone > "+ number + " " + location+ " " + carrier)
                            time.sleep(3)

                if valid == "False":
                    time.sleep(3)
                    print(f"{number} Is Invalid!")
            except Exception:
                print("Your IP is being rate limited")   


def menu():
    print("""                                                                              
█████ █████ █████ █████ █████ █████ █████ █████ █████                                                                                                                          
                                    
██████  ██   ██  ██████  ███    ██ ███████ ███████ 
██   ██ ██   ██ ██    ██ ████   ██ ██      ██      
██████  ███████ ██    ██ ██ ██  ██ █████   ███████ 
██      ██   ██ ██    ██ ██  ██ ██ ██           ██ 
██      ██   ██  ██████  ██   ████ ███████ ███████ 

█████ █████ █████ █████ █████ █████ █████ █████ █████

""")
    print("Please Choose one of 3 Options")
    men = input("1. Generate & Validate Numbers\n2. Validate Numbers\n3. Check status of API Key\n#> ")
    if men == "2":
        print("\n\nPlease make sure your phones are in the phones.txt file!")
        time.sleep(2)
        check()
    if men == "1":
        checkgenn()
    if men == "3":
        status()
        
menu()