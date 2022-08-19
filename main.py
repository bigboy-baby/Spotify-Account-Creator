#Code by bigboybigboi#0001 skid if ur homosexual (ew)
import requests, random, string, threading, json

with open('config.json') as config_file:
  config = json.load(config_file)

def create(prox):
  proxy = {
    "http":f"http://{prox}",
    "https":f"http://{prox}",
  }
  while True:
    try:
      headers = {'User-agent': 'S4A/2.0.15 (com.spotify.s4a; build:201500080; iOS 13.4.0) Alamofire/4.9.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'Accept': 'application/json, text/plain;q=0.2, */*;q=0.1', 'App-Platform': 'IOS', 'Spotify-App': 'S4A', 'Accept-Language': 'en-TZ;q=1.0', 'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5', 'Spotify-App-Version': '2.0.15'}
      domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
      email1 = ('').join(random.choices(string.ascii_letters + string.digits, k=5))
      email = f"orcus.{email1}@{random.choice(domains)}"
      psw = ('').join(random.choices(string.ascii_letters + string.digits, k=5))
      password = f"{psw}_Biggie_{psw}"
      birth_year = random.randint(1970, 2005)
      birth_month = random.randint(1, 12)
      birth_day = random.randint(1, 28)
      gender = random.choice(['male', 'female'])

      data = 'creation_point=lite_7e7cf598605d47caba394c628e2735a2&password_repeat=%s&platform=Android-ARM&iagree=true&password=%s&gender=%s&key=a2d4b979dc624757b4fb47de483f3505&birth_day=%s&birth_month=%s&email=%s&birth_year=%s' % (password, password, gender, birth_day, birth_month, email, birth_year)
      create = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', data = data, headers = headers, proxies = proxy)
      if create.json()['status'] == 1:
        username = create.json()['username']
        if username != '':
          print(f"Generated | {username}:{password}")
          f = open("accounts.txt", "a")
          f.write(f"{username}:{password}\n")
          f.close()
        else:
          pass
          #username error
          #print("Username Error")
          #print(create.text)
      else:
        pass
        #request error
        #print("Request Error")
        #print(create.text)
    except:
      pass

print("Put Threads High ~500-1000")
am = int(input("Thread Amount: "))

prox = config['proxy']
if prox:
  print(f"Using Proxy: {prox}")
else:
  print("Wtf? You really tryna use this with no proxy? Lol bozo")

for n in range(am):
  x = threading.Thread(target=create, args=(prox,))
  x.start()
