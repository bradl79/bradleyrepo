import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Viper Wizard'
EXCLUDES       = [ADDON_ID, 'repository.bradleyrepo']
# Text File with build info in it.
BUILDFILE      = 'http://bradl79.x10.mx/viperwizard/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://wolfpackcrew.co.uk/seeddata/wolfpackrepo/wizard/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'How to guides'
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://wolfpackcrew.co.uk/seeddata/wolfpackrepo/wizard/adooninstaller.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://bradl79.x10.mx/viperwizard/advancedsettings/advanced.txt'
# Text file for roms and emus
ROMPACK        = 'http://wolfpackcrew.co.uk/seeddata/wolfpackrepo/wizard/rom-packs.txt'
EMUAPKS        = 'http://wolfpackcrew.co.uk/seeddata/wolfpackrepo/wizard/emuapks.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = os.path.join(ART, 'builds.png')
ICONMAINT      = os.path.join(ART, 'maintenance.png')
ICONSPEED      = os.path.join(ART, 'speedtest.png')
ICONAPK        = os.path.join(ART, 'apk.png')
ICONRETRO      = os.path.join(ART, 'retro.png')
ICONADDONS     = os.path.join(ART, 'addons.png')
ICONYOUTUBE    = os.path.join(ART, 'youtube.png')
ICONSAVE       = os.path.join(ART, 'save.png')
ICONTRAKT      = os.path.join(ART, 'trakt.png')
ICONREAL       = os.path.join(ART, 'real.png')
ICONLOGIN      = os.path.join(ART, 'login.png')
ICONCONTACT    = os.path.join(ART, 'contact.png')
ICONSETTINGS   = os.path.join(ART, 'settings.png')
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'red'
COLOR2         = 'ghostwhite'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']Viper Wizard[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+'][B]Current Build:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+'][B]Current Theme:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing viper wizard.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'qricon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'repository.bradleyrepo'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/bradl79/bradleyrepo/master/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://github.com/bradl79/bradleyrepo/raw/master/zips'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'no'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Viper Wizard'
# url to image if using Image 500x50(Width can vary but height of image needs to be 50px)
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################