---
id: 3019ae17-0b33-41df-b58d-089c41c0dfb5
name: Big Generic Windows
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:28.733700+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Big Generic Windows

# Description

The "Big Generic Windows" Cheatsheet. Just filled with a lot of useful commands when working on Windows.





**Command** ([[View your current user:]]):

```bash
whoami

```







**Command** ([[View information about the current user:]]):

```bash
net user myuser(for a local user)

```







**Command** ([[View information about domain user:]]):

```bash
net user myuser /domain (for a domain user)

```







**Command** ([[View the local groups:]]):

```bash
net localgroup

```







**Command** ([[View the local administrators:]]):

```bash
net localgroup Administrators

```







**Command** ([[Add a new user:]]):

```bash
net user myuser mypass /add

```







**Command** ([[Add a user in the local Administrators group:]]):

```bash
net localgroup Administrators myuser /add

```







**Command** ([[View the domain name of current machine:]]):

```bash
net config workstation
net config server

```







**Command** ([[View the name of the domain controller:]]):

```bash
reg query "HKEY_LOCAL_MACHINE\ SOFTWARE\Microsoft\Windows\ CurrentVersion\Group Policy\ History" /v DCName

```







**Command** ([[View the name of the domain controller:]]):

```bash
Import-Module ActiveDirectory; (Get-ADDomainController -DomainName corp.test.com -Discover -NextClosestSite).HostName

```







**Command** ([[View the name of the domain controller:]]):

```bash
set l

```







**Command** ([[Get list of DCs]]):

```bash
nltest /dclist:domainname

```







**Command** ([[Get list of DCs]]):

```bash
netdom query /D:domin DC

```







**Command** ([[Get list of DCs]]):

```bash
dsquery server

```







**Command** ([[Get list of DCs]]):

```bash
nslookup -type=srv _ldap._tcp.dc._msdcs.corp.test.com

```







**Command** ([[Get list of DCs]]):

```bash
Get DC Info

```







**Command** ([[Get list od CD's]]):

```bash
nltest /dsgetdc:domain

```







**Command** ([[ Get DC site mapping]]):

```bash
nltest /dsaddresstosite:dcname.corp.test.com

```







**Command** ([[Get PDC]]):

```bash
netdom query /D:domain PDC

```







**Command** ([[Get PDC]]):

```bash
nslookup -type=srv _ldap._tcp.pdc._msdcs.corp.test.com

```





# Get AD roles



**Command** ([[Get Roles]]):

```bash
netdom query /D:domain FSMO

```







**Command** ([[View the list of domain users:]]):

```bash
C:\> wmic useraccount where (domain='%USERDOMAIN%') get Name > userlist.txt PS C:\> ([adsisearcher]"objectCategory=User").Findall() | ForEach
{$_.properties.samaccountname} | Sort | Out-File -Encoding ASCII users.txt

```







**Command** ([[List domain users]]):

```bash
net user /domain

```







**Command** ([[Get domain info (including DC)]]):

```bash
gpresult /z

```







**Command** ([[View the list of domain admins:]]):

```bash
net group "Domain Admins" /domain

```







**Command** ([[View domain groups]]):

```powershell
net group /domain
powershell (new-object system.directoryservices.directorysearcher("(&(objectcategory=user)(samaccountname=$($env:username)))")).FindOne().GetDirectoryEntry().memberof

```







**Command** ([[View the list of started services (search for antivirus):]]):

```bash
net start
sc query

```







**Command** ([[Stop a service:]]):

```bash
net stop "Symantec Endpoint Protection"

```







**Command** ([[View the list of started processes and the owner:]]):

```bash
tasklist /v

```







**Command** ([[Kill a process by its name:]]):

```bash
taskkill /F /IM "cmd.exe"

```







**Command** ([[Abort a shutdown/restart countdown:]]):

```bash
shutdown /a

```







**Code**: [[
echo open 10.1.2.3> C:\script.txt
echo user myftp]]







**Code**: [[
echo open 10.1.2.3> C:\script.txt
echo user myftp]]







**Command** ([[WMI call remote system]]):

```bash
wmic /node:remote_computer process call create "netstat.exe -ano > C:\output.txt"

```







**Command** ([[View established connections of current machine:]]):

```bash
netstat -a -n -p tcp | find "ESTAB"

```







**Command** ([[View open TCP ports of current machine:]]):

```bash
netstat -a -n -p tcp | find "LISTEN"

```







**Command** ([[View open UDP ports]]):

```bash
netstat -a -n -p udp

```







**Command** ([[View network configuration:]]):

```bash
netsh interface ip show addresses
netsh interface ip show route
netsh interface ip show neighbors

```







**Command** ([[View current network shares:]]):

```bash
net share

```







**Command** ([[Mount a remote share with the rights of the current user:]]):

```bash
net use K: \\10.1.2.3\C$

```







**Command** ([[Enable Remote Desktop:]]):

```bash
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

```





# Reference: https://gist.github.com/KyleHanslovan/cadf9737401b85422c84091855473eb7



**Command** ([[One-Liner Windows Enumeration]]):

```bash
whoami & hostname & ipconfig /all & net user /domain 2>&1 & net group /domain 2>&1 & net group "domain admins" /domain 2>&1 & net group "Exchange Trusted Subsystem" /domain 2>&1 & net accounts /domain 2>&1 & net user 2>&1 & net localgroup administrators 2>&1 & netstat -an 2>&1 & tasklist 2>&1 & sc query 2>&1 & systeminfo 2>&1 & reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" 2>&1 & net view & net view /domain & net user %USERNAME% /domain & nltest /dclist & gpresult /z

```







**Command** ([[Command to enable proxy usage:]]):

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f 

```







**Command** ([[Command to disable proxy usage:]]):

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f 

```







**Command** ([[Command to change the proxy address:]]):

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d proxyserveraddress:proxyport /f 

```





Also, in this case, it is a per-user setting than a system-wide setting.



**Command** ([[Mount a .win image remotely on target machine]]):

```bash
Dism /get-wiminfo /wimfile:z:\win7\Acme_Win7.wim Boot Dir
Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:1 /MountDir:C:\windows\temp\offline C: Drive
Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:2 /MountDir:C:\windows\temp\offline Dism /UnMount-Wim /MountDir:C:\windows\temp\offline /discard

```







**Command** ([[Check if file is locked]]):

```bash
@echo off; 2>nul ( >>file.txt echo off) && (echo not locked) || (echo locked)

```







**Command** ([[Lock a file for testing]]):

```bash
(>&2 pause) >> file.txt

```






