#!/usr/bin/env python
########################################################################
#
# texte des menus pour SET
#
########################################################################
from src.core.setcore import bcolors, get_version, check_os, meta_path

# récupère la version de SET
define_version = get_version()

# vérifie le système d'exploitation
operating_system = check_os()

# récupère le chemin de Metasploit
msf_path = meta_path()

PORT_NOT_ZERO = "Le port ne peut pas être zéro !"
PORT_TOO_HIGH = "Restons sur des ports INFÉRIEURS à 65 535..."

main_text = " Sélectionnez dans le menu :\n"

main_menu = ['Attaques d\'ingénierie sociale',
             'Tests d\'intrusion (Fast-Track)',
             'Modules tiers',
             'Mettre à jour le Social-Engineer Toolkit',
             'Mettre à jour la configuration de SET',
             'Aide, crédits et à propos']

main = ['Vecteurs d\'attaque par spear-phishing',
        'Vecteurs d\'attaque par site web',
        'Générateur de média infecté',
        'Créer un payload et un listener',
        'Attaque par envoi massif d\'emails',
        'Vecteur d\'attaque basé sur Arduino',
        'Vecteur d\'attaque par point d\'accès sans fil',
        'Vecteur d\'attaque par génération de QRCode',
        'Vecteurs d\'attaque PowerShell',
        'Modules tiers']

spearphish_menu = ['Effectuer une attaque par email massif',
                   'Créer un payload de type FileFormat',
                   'Créer un modèle d\'ingénierie sociale',
                   '0D']

spearphish_text = ("""
 Le module """ + bcolors.BOLD + """Spearphishing""" + bcolors.ENDC + """ vous permet de rédiger des emails sur mesure et de les
 envoyer à un grand (ou petit) nombre de personnes avec des payloads malveillants
 en pièce jointe (FileFormat). Si vous voulez usurper votre adresse email, assurez-vous
 que "Sendmail" est installé (apt-get install sendmail) et changez le paramètre
 config/set_config SENDMAIL=OFF en SENDMAIL=ON.

 Il y a deux options : la première consiste à se familiariser et à laisser SET
 tout faire pour vous (option 1), la seconde consiste à créer votre propre
 payload FileFormat et à l'utiliser dans votre propre attaque. Dans tous les cas,
 bonne chance et amusez-vous bien !
""")

webattack_menu = ['Attaque par Applet Java',
                  'Attaque par exploit navigateur Metasploit',
                  'Attaque par récupération d\'identifiants (Credential Harvester)',
                  'Attaque par Tabnabbing',
                  'Attaque par Web Jacking',
                  'Attaque Web multi-méthodes',
                  'Attaque HTA',
                  '0D']

fasttrack_menu = ['Bruteforce Microsoft SQL',
                  'Exploits personnalisés',
                  'Vecteur d\'attaque SCCM',
                  'Vérificateur de mots de passe par défaut Dell DRAC/Chassis',
                  'RID_ENUM - Attaque d\'énumération des utilisateurs',
                  'Injection PowerShell via PSEXEC',
                  '0D']

fasttrack_text = ("""
Bienvenue dans la plateforme de tests d'intrusion """ + bcolors.BOLD + """Fast-Track""" + bcolors.ENDC + """ du Social-Engineer Toolkit. Ces vecteurs
d'attaque regroupent une série d'exploits et des aspects d'automatisation pour vous aider dans l'art
du test d'intrusion. SET intègre désormais les vecteurs d'attaque exploités par Fast-Track. Tous ces
vecteurs d'attaque ont été entièrement réécrits et personnalisés depuis zéro afin d'améliorer les
fonctionnalités et les capacités.
""")

fasttrack_exploits_menu1 = ['MS08-067 (Win2000, Win2k3, WinXP)',
                            'Mozilla Firefox 3.6.16 - Exploit Use After Free sur l\'objet mChannel (Win7)',
                            'Solarwinds Storage Manager 5.1.0 - Injection SQL SYSTEM distante',
                            'RDP | Use after Free - Déni de service',
                            'Contournement d\'authentification MySQL',
                            'Contournement d\'authentification root F5',
                            '0D']

fasttrack_exploits_text1 = ("""
Bienvenue dans la section """ + bcolors.BOLD + """Exploits""" + bcolors.ENDC + """ de la plateforme de tests d'intrusion Fast-Track du Social-Engineer Toolkit.
Ce menu regroupe des exploits plus rares et majoritairement écrits en Python. Il continuera de s'enrichir avec le temps.
""")

fasttrack_mssql_menu1 = ['Scanner et attaquer MSSQL',
                         'Se connecter directement à MSSQL',
                         '0D']

fasttrack_mssql_text1 = ("""
Bienvenue dans le """ + bcolors.BOLD + """Bruteforceur Microsoft SQL""" + bcolors.ENDC + """ de la plateforme de tests d'intrusion Fast-Track du Social-Engineer Toolkit.
Ce vecteur d'attaque va tenter d'identifier les serveurs MSSQL actifs et de forcer les mots de passe faibles
qui pourraient être trouvés. Si cela réussit, SET compromettra alors le système affecté en déployant un
binaire via un vecteur d'attaque binaire vers hexadécimal, qui convertit un binaire brut en hexadécimal et
l'envoie par étapes sur le système cible. À ce stade, un déclencheur reconvertira le payload en binaire.
""")

webattack_text = ("""
Le module d'attaque Web est une méthode unique combinant plusieurs attaques basées sur le web afin de compromettre la victime visée.

L'""" + bcolors.BOLD + """attaque par Applet Java""" + bcolors.ENDC + """ usurpe un certificat Java et délivre un payload Metasploit. Elle utilise un applet Java personnalisé créé par Thomas Werth pour délivrer le payload.

L'""" + bcolors.BOLD + """exploit navigateur Metasploit""" + bcolors.ENDC + """ utilise certains exploits de navigateur Metasploit via une iframe et délivre un payload Metasploit.

Le """ + bcolors.BOLD + """Credential Harvester""" + bcolors.ENDC + """ clone un site web possédant un champ nom d'utilisateur/mot de passe et récupère toutes les informations envoyées au site.

Le """ + bcolors.BOLD + """TabNabbing""" + bcolors.ENDC + """ attend que l'utilisateur change d'onglet, puis rafraîchit la page vers autre chose.

L'""" + bcolors.BOLD + """attaque Web-Jacking""" + bcolors.ENDC + """ a été introduite par white_sheep et emgent. Cette méthode utilise un remplacement par iframe pour faire apparaître le lien d'URL mis en évidence comme légitime ; cependant, un clic ouvre une fenêtre qui est ensuite remplacée par le lien malveillant. Vous pouvez modifier les paramètres de remplacement de lien dans set_config si c'est trop lent/rapide.

Le """ + bcolors.BOLD + """mode multi-attaques""" + bcolors.ENDC + """ combine plusieurs attaques via le menu d'attaque Web. Par exemple, vous pouvez utiliser l'Applet Java, l'exploit navigateur Metasploit, le Credential Harvester/Tabnabbing en même temps pour voir lequel fonctionne.

L'""" + bcolors.BOLD + """attaque HTA""" + bcolors.ENDC + """ vous permet de cloner un site et d'effectuer une injection PowerShell via des fichiers HTA, utilisable pour l'exploitation PowerShell sous Windows via le navigateur.
""")

webattack_vectors_menu = ['Modèles web',
                          'Cloneur de site',
                          'Import personnalisé\n',
                          ]

webattack_vectors_text = ("""
 La première méthode permet à SET d'importer une liste d'applications
 web prédéfinies qu'il peut utiliser dans l'attaque.

 La deuxième méthode clone entièrement un site web de votre choix
 et vous permet d'utiliser les vecteurs d'attaque au sein de
 l'application web identique que vous souhaitiez cloner.

 La troisième méthode vous permet d'importer votre propre site web ; notez
 que vous ne devez avoir qu'un fichier index.html lors de l'utilisation
 de la fonctionnalité d'import de site web.
   """)

teensy_menu = ['Payload MSF PowerShell HTTP GET',
               'Payload MSF WSCRIPT HTTP GET',
               'Payload Reverse Shell basé sur PowerShell',
               'Payload Beef Jack pour Internet Explorer/FireFox',
               'Payload : aller sur un site Java malveillant et accepter l\'applet',
               'Payload Gnome wget Download',
               'Attaque Binaire vers Teensy (déploie des payloads MSF)',
               'Attaque SDCard vers Teensy (déploie n\'importe quel EXE)',
               'Attaque SDCard vers Teensy (déploie sur OSX)',
               'PDE et bibliothèques du Sniffer X10 Arduino',
               'PDE et bibliothèques du Jammer X10 Arduino',
               'Attaque Teensy ShellCode direct via PowerShell',
               'Attaque Peensy multi-attaque Dip Switch + SDCard',
	       'Attaque HID Msbuild compilation en mémoire Shellcode',
               '0D']

teensy_text = ("""
 Le vecteur d'attaque """ + bcolors.BOLD + """basé sur Arduino""" + bcolors.ENDC + """ utilise un appareil basé sur Arduino pour
 programmer le dispositif. Vous pouvez tirer parti des Teensy, qui disposent
 d'un stockage embarqué et permettent l'exécution de code à distance sur
 le système physique. Comme ces appareils sont reconnus comme des claviers
 USB, ils contournent toute protection par désactivation de l'autorun ou
 par protection des terminaux.

 Vous devrez acheter le dispositif USB Teensy, pour environ 22 dollars.
 Ce vecteur d'attaque génère automatiquement le code nécessaire pour
 déployer le payload sur le système.

 Ce vecteur d'attaque créera les fichiers .pde nécessaires à importer
 dans Arduino (l'IDE utilisé pour programmer le Teensy). Les vecteurs
 d'attaque vont des téléchargeurs basés sur PowerShell aux attaques
 wscript, et d'autres méthodes.

 Pour plus d'informations sur les spécifications et de bons tutoriels, visitez :

 http://www.irongeek.com/i.php?page=security/programmable-hid-usb-keystroke-dongle

 Pour acheter un Teensy, visitez : http://www.pjrc.com/store/teensy.html
 Remerciements spéciaux à : IronGeek, WinFang, et Garland

 Ce vecteur d'attaque cible aussi les contrôleurs basés sur X10, assurez-vous
 d'utiliser des dispositifs de communication X10 pour que cela fonctionne.

 Sélectionnez un payload pour créer le fichier pde à importer dans Arduino :
""")

wireless_attack_menu = ['Démarrer le point d\'accès du vecteur d\'attaque sans fil SET',
                        'Arrêter le point d\'accès du vecteur d\'attaque sans fil SET',
                        '0D']


wireless_attack_text = """
 Le module d'""" + bcolors.BOLD + """attaque sans fil""" + bcolors.ENDC + """ crée un point d'accès en utilisant votre
 carte sans fil et redirige toutes les requêtes DNS vers vous. Le concept est
 assez simple : SET crée un point d'accès sans fil, un serveur DHCP, et usurpe
 le DNS pour rediriger le trafic vers la machine attaquante. Il quitte ensuite
 ce menu avec tout s'exécutant en tant que processus enfant.

 Vous pouvez alors lancer n'importe quel vecteur d'attaque SET, par exemple l'attaque
 par Applet Java, et lorsqu'une victime rejoint votre point d'accès et tente d'accéder
 à un site web, elle sera redirigée vers votre machine attaquante.

 Ce vecteur d'attaque nécessite AirBase-NG, AirMon-NG, DNSSpoof, et dhcpd3.

"""

infectious_menu = ['Exploits de type FileFormat',
                   'Exécutable Metasploit standard',
                   '0D']


infectious_text = """
 Le module """ + bcolors.BOLD + bcolors.GREEN + """Infectious""" + bcolors.ENDC + """ USB/CD/DVD crée un fichier autorun.inf et un
 payload Metasploit. Lorsque le DVD/USB/CD est inséré, il s'exécutera
 automatiquement si l'autorun est activé.""" + bcolors.ENDC + """

 Choisissez le vecteur d'attaque que vous souhaitez utiliser : exploits de type fichier ou exécutable direct.
"""

# utilisé dans create_payloads.py
if operating_system != "windows":
    if msf_path != False:
        payload_menu_1 = [
            'Injection mémoire Meterpreter (PAR DÉFAUT)   Dépose un payload Meterpreter via injection PowerShell',
            'Injection mémoire multiple Meterpreter       Dépose plusieurs payloads Metasploit via injection PowerShell',
            'Shell interactif SE Toolkit                  Shell interactif inversé personnalisé conçu pour SET',
            'Shell inversé HTTP SE Toolkit                 Shell HTTP purement natif avec support du chiffrement AES',
            'Payload de tunneling HTTP RATTE               Payload de contournement de sécurité qui tunnelise toute la communication via HTTP',
            'Shellcode Alphanumérique ShellCodeExec        Dépose un payload Meterpreter via shellcodeexec',
            'Importer votre propre exécutable               Indiquez un chemin vers votre propre exécutable',
            'Importer votre propre commands.txt              Spécifiez les payloads à envoyer via la ligne de commande\n']

if operating_system == "windows" or msf_path == False:
    payload_menu_1 = [
        'Shell interactif SE Toolkit    Shell interactif inversé personnalisé conçu pour SET',
        'Shell inversé HTTP SE Toolkit   Shell HTTP purement natif avec support du chiffrement AES',
        'Payload de tunneling HTTP RATTE   Payload de contournement de sécurité qui tunnelise toute la communication via HTTP\n']

payload_menu_1_text = """
Quel payload souhaitez-vous générer :

  Nom :                                       Description :
"""

# utilisé dans gen_payload.py
payload_menu_2 = [
    'Windows Shell Reverse_TCP               Lance un shell de commandes sur la victime et le renvoie à l\'attaquant',
    'Windows Reverse_TCP Meterpreter         Lance un shell Meterpreter sur la victime et le renvoie à l\'attaquant',
    'Windows Reverse_TCP VNC DLL             Lance un serveur VNC sur la victime et le renvoie à l\'attaquant',
    'Windows Shell Reverse_TCP X64           Shell de commandes Windows X64, Reverse TCP Inline',
    'Windows Meterpreter Reverse_TCP X64     Connexion retour vers l\'attaquant (Windows x64), Meterpreter',
    'Windows Meterpreter Egress Buster       Lance un shell Meterpreter et trouve un port de sortie parmi plusieurs ports',
    'Windows Meterpreter Reverse HTTPS       Tunnelise la communication via HTTP avec SSL et utilise Meterpreter',
    'Windows Meterpreter Reverse DNS         Utilise un nom d\'hôte plutôt qu\'une adresse IP et utilise Reverse Meterpreter',
    'Télécharger/Exécuter votre propre exécutable        Télécharge un exécutable et l\'exécute\n'
]


payload_menu_2_text = """\n"""

payload_menu_3_text = ""
payload_menu_3 = [
    'Windows Reverse TCP Shell              Lance un shell de commandes sur la victime et le renvoie à l\'attaquant',
    'Windows Meterpreter Reverse_TCP        Lance un shell Meterpreter sur la victime et le renvoie à l\'attaquant',
    'Windows Reverse VNC DLL                Lance un serveur VNC sur la victime et le renvoie à l\'attaquant',
    'Windows Reverse TCP Shell (x64)        Shell de commandes Windows X64, Reverse TCP Inline',
    'Windows Meterpreter Reverse_TCP (X64)  Connexion retour vers l\'attaquant (Windows x64), Meterpreter',
    'Windows Shell Bind_TCP (X64)           Exécute le payload et crée un port en écoute sur le système distant',
    'Windows Meterpreter Reverse HTTPS      Tunnelise la communication via HTTP avec SSL et utilise Meterpreter\n']

# appelé depuis create_payload.py, dictionnaire associé = ms_attacks
create_payloads_menu = [
    'Vecteur d\'attaque DLL Hijacking personnalisé SET (RAR, ZIP)',
    'Attaque par capture UNC LM SMB sur document personnalisée SET',
    'MS15-100 Vulnérabilité Microsoft Windows Media Center MCL',
    'MS14-017 Confusion d\'objet RTF dans Microsoft Word (2014-04-01)',
    'Dépassement de pile Microsoft Windows CreateSizedDIBSECTION',
    'Dépassement de pile RTF pFragments de Microsoft Word (MS10-087)',
    'Exécution de code à distance Adobe Flash Player "Button"',
    'Dépassement Adobe CoolType SING Table "uniqueName"',
    'Utilisation de pointeur invalide Adobe Flash Player "newfunction"',
    'Dépassement de tampon Adobe Collab.collectEmailInfo',
    'Dépassement de tampon Adobe Collab.getIcon',
    'Exploit de corruption mémoire Adobe JBIG2Decode',
    'Ingénierie sociale par EXE intégré dans un PDF Adobe',
    'Dépassement de tampon Adobe util.printf()',
    'EXE personnalisé vers VBA (envoyé via RAR) (RAR requis)',
    'Dépassement de tableau Adobe U3D CLODProgressiveMeshDeclaration',
    'Ingénierie sociale par EXE intégré dans un PDF Adobe (NOJS)',
    'Dépassement de pile sur le titre de Foxit PDF Reader v4.1.1',
    'Dépassement de tampon Apple QuickTime PICT PnSize',
    'Dépassement de pile au lancement de Nuance PDF Reader v6.0',
    'Vulnérabilité de corruption mémoire Adobe Reader u3D',
    'Dépassement de tampon ActiveX MSCOMCTL (ms12-027)\n']

create_payloads_text = """
 Sélectionnez l'exploit de type fichier que vous voulez.
 Par défaut, il s'agit de l'EXE intégré dans un PDF.\n
           ********** PAYLOADS **********\n"""

browser_exploits_menu = [
    'Adobe Flash Player - Use After Free sur ByteArray (2015-07-06)',
    'Adobe Flash Player - Dépassement de tampon décodage audio Nellymoser (2015-06-23)',
    'Adobe Flash Player - Corruption mémoire Drawing Fill Shader (2015-05-12)',
    'MS14-012 Internet Explorer - Use-After-Free sur TextRange (2014-03-11)',
    'MS14-012 Internet Explorer - Use-After-Free sur CMarkup (2014-02-13)',
    'Internet Explorer - Use-After-Free sur CDisplayPointer (13/10/2013)',
    'Internet Explorer - Use-After-Free sur SetMouseCapture (17/09/2013)',
    'Exécution de code à distance Applet Java JMX (MIS À JOUR 2013-01-19)',
    'Exécution de code à distance Applet Java JMX (2013-01-10)',
    'MS13-009 Internet Explorer - Use-After-Free sur SLayoutRun (2013-02-13)',
    'Internet Explorer - Use-After-Free sur l\'objet CDwnBindInfo (2012-12-27)',
    'Exécution de code à distance Applet Java 7 (2012-08-26)',
    'Vulnérabilité Use-After-Free Internet Explorer execCommand (2012-09-14)',
    'Vulnérabilité de violation de type Java AtomicReferenceArray (2012-02-14)',
    'Exécution de code à distance via le cache du vérificateur de bytecode Applet Java (2012-06-06)',
    'MS12-037 Internet Explorer - Corruption mémoire sur la gestion d\'objet supprimé Same ID Property (2012-06-12)',
    'Corruption mémoire non initialisée Microsoft XML Core Services MSXML (2012-06-12)',
    'Confusion de type Adobe Flash Player Object (2012-05-04)',
    'Dépassement Adobe Flash Player MP4 "cprt" (2012-02-15)',
    'MS12-004 Dépassement de tas midiOutPlayNextPolyEvent (2012-01-10)',
    'Exécution de code à distance Applet Java Rhino Script Engine (2011-10-18)',
    'MS11-050 Internet Explorer - Use After Free sur mshtml!CObjectElement (2011-06-16)',
    'Vulnérabilité de corruption mémoire Adobe Flash Player 10.2.153.1 SWF (2011-04-11)',
    'Téléchargement et exécution via la propriété ActiveX URL du client Cisco AnyConnect VPN (2011-06-01)',
    'Internet Explorer - Use After Free sur l\'import CSS (2010-11-29)',
    'Dépassement de tampon ActiveX des outils d\'administration Microsoft WMI (2010-12-21)',
    'Corruption mémoire des balises CSS dans Internet Explorer (2010-11-03)',
    'Exécution de code à distance Sun Java Applet2ClassLoader (2011-02-15)',
    'Dépassement de tampon docbase du nouveau plugin Sun Java Runtime (2010-10-12)',
    'Détournement de DLL via l\'application Microsoft Windows WebDAV (2010-08-18)',
    'Vulnérabilité de vérification de bytecode AVM Adobe Flash Player (2011-03-15)',
    'Exploit de corruption mémoire Adobe Shockwave rcsL (2010-10-21)',
    'Dépassement de pile Adobe CoolType SING Table "uniqueName" (2010-09-07)',
    'Exécution de code Apple QuickTime 7.6.7 Marshaled_pUnk (2010-08-30)',
    'XSS et exécution de commandes Microsoft Help Center (2010-06-09)',
    'Internet Explorer - Use After Free sur iepeers.dll (2010-03-09)',
    'Corruption mémoire Internet Explorer "Aurora" (2010-01-14)',
    'Exploit Tabular Data Control d\'Internet Explorer (2010-03-0)',
    'Corruption mémoire non initialisée Internet Explorer 7 (2009-02-10)',
    'Corruption du style getElementsbyTagName d\'Internet Explorer (2009-11-20)',
    'Dépassement isComponentInstalled d\'Internet Explorer (2006-02-24)',
    'Corruption de liaison de données Internet Explorer (2008-12-07)',
    'Mauvaise configuration de script non sécurisé dans Internet Explorer (2010-09-20)',
    'Corruption mémoire de la valeur de retour escape dans FireFox 3.5 (2009-07-13)',
    'Vulnérabilité use after free mChannel dans FireFox 3.6.16 (2011-05-10)',
    'Autopwn navigateur Metasploit (À UTILISER À VOS RISQUES !)\n']

browser_exploits_text = """
 Entrez l'exploit navigateur que vous souhaitez utiliser [8] :
"""

# ceci concerne les vecteurs d'attaque powershell
powershell_menu = ['Injecteur de Shellcode alphanumérique PowerShell',
                   'Shell inversé PowerShell',
                   'Shell d\'écoute PowerShell',
                   'Extraction de la base SAM via PowerShell',
                   '0D']

powershell_text = ("""
Le module """ + bcolors.BOLD + """vecteur d'attaque PowerShell""" + bcolors.ENDC + """ vous permet de créer des attaques spécifiques à PowerShell. Ces attaques vous permettent d'utiliser PowerShell, disponible par défaut sur tous les systèmes Windows Vista et ultérieurs. PowerShell offre un terrain fertile pour déployer des payloads et effectuer des opérations qui ne déclenchent pas les technologies de prévention.\n""")


encoder_menu = ['shikata_ga_nai',
                'Pas d\'encodage',
                'Multi-Encoder',
                'Exécutable piégé (backdoor)\n']

encoder_text = """
Sélectionnez l'une des options ci-dessous ; "exécutable piégé" est généralement la meilleure.
Cependant, la plupart sont encore détectés par les antivirus. Il peut être nécessaire d'effectuer
un packing/chiffrement supplémentaire pour contourner la détection antivirus de base.
"""

dll_hijacker_text = """
 La vulnérabilité DLL Hijacker permet à des extensions de fichiers normales
 d'appeler des fichiers .dll locaux (ou distants) qui peuvent ensuite appeler
 votre payload ou exécutable. Dans ce scénario, l'attaque sera compactée dans
 un fichier zip et, lorsque l'utilisateur ouvrira l'extension de fichier,
 déclenchera la DLL puis finalement notre payload. Au moment de cette version,
 toutes ces extensions de fichiers ont été testées et semblent fonctionner et
 ne sont pas corrigées. Cette liste sera mise à jour continuellement avec le temps.
"""

fakeap_dhcp_menu = ['10.0.0.100-254',
                    '192.168.10.100-254\n']

fakeap_dhcp_text = "Veuillez choisir la configuration DHCP que vous souhaitez utiliser : "
