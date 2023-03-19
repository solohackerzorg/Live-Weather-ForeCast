import requests,random,os
A = '\x1b[0;97m' 
B = '\x1b[0;91m' 
C = '\x1b[0;92m' 
D = '\x1b[0;93m' 
E = '\x1b[0;94m'
F = '\x1b[0;95m' 
G = '\x1b[0;96m' 
H = '\x1b[0m'   
I='\x1b[0;32m'
J='\x1b[0;36m'
K='\x1b[0;31m'
L='\x1b[0;35m'
M='\x1b[0;33m'
N='\033[0;37m'
O='\x1b[00m'
P='\x1b[0;90m'
Q="\x1b[00m"
R='\x1b[1;30;32m'
S='\x1b[0;36m'
T='\x1b[0;31m'
U='\x1b[0;35m'
V='\x1b[0;33m'
W='\x1b[0;34m'
X='\033[0;37m'
Y='\x1b[00m'
Z='\x1b[0;90m'

sziloveyu = random.choice([Z,X,C,V,B,N,M,A,S,D,F,G,H,J,K,L])
linex = ('\033[0;97m═══════════════════════════════════════════════')
def sologo():
	os.system('clear') or os.system('cls')
	print(f'{sziloveyu}   ▄████████    ▄█    █▄     ▄██████▄  \n  ███    ███   ███    ███   ███    ███ \n  ███    █▀    ███    ███   ███    ███\n  ███         ▄███▄▄▄▄███▄▄ ███    ███ [S]\n▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ [O]\n         ███   ███    ███   ███    ███ [L]\n   ▄█    ███   ███    ███   ███    ███ [O]\n ▄████████▀    ███    █▀     ▀██████▀  ')
	print(f'{linex}\n Author    : SOLO HACKER\n Version   : 4.3\n Github    : solohackerzorganization \n{linex}\n\tLive Weather Forecast\n{linex}')
def get_weather_data(city):
    url = f'https://wttr.in/{city}?format=%C,%t'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text.strip().split(',')
        temperature = data[1].strip().split()[0]
        return {'condition': data[0], 'temperature': temperature}
    else:
        return None
sologo()
city = input('Enter a city name: ')
weather_data = get_weather_data(city)
if weather_data:
    print(f'{linex}\nThe current temperature in {city} is {R}{weather_data["temperature"]} {X}and {R}{weather_data["condition"]} {X}in the city.')
else:
    print('Unable to fetch weather data.')
