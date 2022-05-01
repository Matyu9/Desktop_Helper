import ipinfo
import requests
import asyncio
import aiohttp

access_token_ipinfo = "89129f7ee2f780"


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.status()


async def main():
    res = await get("https://matbe.tk/")
    print(res.status)
    down = False
    if res == 521 & down == False:
        print("Serveur Web éteint!")
        down = True
    elif res == 200 & down:
        print("Serveur Web rallumer!")
        down = False
loop = asyncio.get_event_loop()

print(""" _______  _______ _________ ______   _______  _  _______    _________ _______  _______  _                                 
(       )(  ___  )\__   __/(  ___ \ (  ____ \( )(  ____ \   \__   __/(  ___  )(  ___  )( \                                
| () () || (   ) |   ) (   | (   ) )| (    \/|/ | (    \/      ) (   | (   ) || (   ) || (                                
| || || || (___) |   | |   | (__/ / | (__       | (_____       | |   | |   | || |   | || |                                
| |(_)| ||  ___  |   | |   |  __ (  |  __)      (_____  )      | |   | |   | || |   | || |                                
| |   | || (   ) |   | |   | (  \ \ | (               ) |      | |   | |   | || |   | || |                                
| )   ( || )   ( |   | |   | )___) )| (____/\   /\____) |      | |   | (___) || (___) || (____/\                          
|/     \||/     \|   )_(   |/ \___/ (_______/   \_______)      )_(   (_______)(_______)(_______/                          
                                                                                                                         
 ______   _______  _______  _       _________ _______  _______               _______  _        _______  _______  _______ 
(  __  \ (  ____ \(  ____ \| \    /\\__   __/(  ___  )(  ____ )    |\     /|(  ____ \( \      (  ____ )(  ____ \(  ____ )
| (  \  )| (    \/| (    \/|  \  / /   ) (   | (   ) || (    )|    | )   ( || (    \/| (      | (    )|| (    \/| (    )|
| |   ) || (__    | (_____ |  (_/ /    | |   | |   | || (____)|    | (___) || (__    | |      | (____)|| (__    | (____)|
| |   | ||  __)   (_____  )|   _ (     | |   | |   | ||  _____)    |  ___  ||  __)   | |      |  _____)|  __)   |     __)
| |   ) || (            ) ||  ( \ \    | |   | |   | || (          | (   ) || (      | |      | (      | (      | (\ (   
| (__/  )| (____/\/\____) ||  /  \ \   | |   | (___) || )          | )   ( || (____/\| (____/\| )      | (____/\| ) \ \__
(______/ (_______/\_______)|_/    \/   )_(   (_______)|/           |/     \|(_______/(_______/|/       (_______/|/   \__/
                                                                                                                         """)


print("Bienvenue dans Desktop Helper CLI!")
print("""1: Ip Info, donne des info sur un ip donné.
2: Down?, Vérifie si une ip/un site web est éteint""")

do_run = True
while do_run:

    first = input("Quelle fonction voullez vous Utilisez? ")

    if first == "1":
        do_run_IP = True
        while do_run_IP:
            choice1 = input("""    Pour demander des informations sur un IP, marquer 1.
    Pour quitter ce module marquer 2: """)
            if choice1 == "2":
                print("Merci d'avoir utiliser ce module!")
                do_run_IP = False

            elif choice1 == "1":
                choice2 = input("Quelle est l'ip ciblé? ")
                if choice2 == "":
                    print("Merci de mettre une valeur qui n'est pas vide")
                    do_run_IP = False
                else:
                    handler = ipinfo.getHandler(access_token_ipinfo)
                    details = handler.getDetails(choice2)
                    print(f"""IP: {choice2};
Ville: {details.city};
Position: {details.loc};
Pays: {details.country}, {details.country_name};
Region: {details.region};
""")
                    sms_IP = 'input("Voullez vous recevoir les informations par SMS? 1 = oui; 2 = non")'
                    if sms_IP == "1":
                        # faire connection avec l'api d'OVH
                        print("Cette fonction nest pas disponible pour le moment")

                    go_out_IP = input("Voullez vous revenir à la paged'accueil? 1 = Oui; 2 = Non ")
                    if go_out_IP == "1":
                        do_run_IP = False

                    else:
                        pass

    elif first == "2":
        do_run_Check = True
        while do_run_Check:
            check = input("Quelle domaine est ciblé? marquer 99 pour revenir au menu principale; ")
            if check == "99":
                print("Merci d'avoir utiliser ce module!")
                do_run_Check = False

            elif check == "":
                print("Merci de rentrer une valeurs non nul!")
            else:
                try:
                    try:
                        r = requests.get(check)
                        status = r.status_code
                        if status == 200:
                            print("Le domaine cible est actif!")
                        elif status == 521:
                            print("Le domaine cible est inactif! Le serveur peut être éteint.")
                        elif status == 404:
                            print("Le site marche, mais la ressource demandé n'existe pas!")
                    except requests.exceptions.MissingSchema:
                        r = requests.get("http://"+check)
                        status = r.status_code
                        if status == 200:
                            print("Le domaine cible est actif!")
                        elif status == 521:
                            print("Le domaine cible est inactif! Le serveur peut être éteint.")
                        elif status == 404:
                            print("Le site marche, mais la ressource demandé n'existe pas!")
                except requests.exceptions.ConnectionError:
                    print("Votre requêtes n'as pas été faites car vous n'êtes pas connecté à Internet, "
                          "merci de vérifier votre connexion ou réessayer ultérieurment!")
                    do_run_Check = False

    elif first == "99":
        print("Merci d'avoir utilisé Desktop Helper")
        loop.close()
        exit()
