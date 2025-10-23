---
id: b0693974-eaa0-4945-8fa3-589593a56ec6
name: External Discovery without creds
type: cheatsheet
verified: false
created_at: '2023-01-11T19:19:55.085168+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# External Discovery without creds

# Description

Look for: 

- Open ports with vulnerable hosts.

- Active DIrectory IP

- DNS Zone transfer

- SMB Shares with guest access

- Enum LDAP to find users

- Find users

- Relay / Poisoning on the local network



## Instructions

1. Scan the network to find vulnerable hosts



Enumerate SMB hosts with CME





**Command** ([[crackmapexec scan smb ip range]]):

```bash
crackmapexec smb $IPRANGE
```





Run an aggressive full network scan





**Command** ([[More aggressive Full TCP Scan]]):

```bash
nmap -sA -PN -sN $ip
nmap -sS -sV -T4 -F -A -O $ip

```







Scan the top 50 ports



**Command** ([[nmap top 50 ports]]):

```bash
nmap -PN -sV --top-ports 50 --open $IPRANGE
```









Search SMB ports for vulns on port 139,445



**Command** ([[NSE SMB unsafe]]):

```bash
nmap --script=smb-* -p139,445 --script-args=unsafe=1 $ip

```





Scan for UDP ports



**Command** ([[Nmap Service Scan of UDP ports]]):

```bash
nmap -sU -sV $_TARGET_IP
```





2. Find Active Directory





**Command** ([[Get list of DCs]]):

```bash
nslookup -type=srv _ldap._tcp.dc._msdcs.corp.test.com

```





3. DNS one transfer





**Command** ([[Dig zone transfer]]):

```bash
dig axfr $DOMAIN@$NAMESERVER
```





4. Enumerate for anonymous or guest access





**Command** ([[enum4linux anonymous]]):

```bash
enu4linux -a -u"" -p "" $AD_IP
```









**Command** ([[enum4linux guest]]):

```bash
enum4linux -a -u "guest" -p "" $AD_IP
```





5. Identify SMB shares with guest access







**Command** ([[SMBMap list guest access on smb share]]):

```bash
smbmap -u "" -p "" -P 445 -H $DC_IP
```









**Command** ([[SMBMap list guest access tricks]]):

```bash
smbmap -U '%' -L //$DC_IP
smbmap -U 'guest%' -L //$DC_IP
```









**Command** ([[CrackMapExec enumerate null sessions]]):

```bash
crackmapexec $IP -u "" -p ""
```









**Command** ([[CrackMapExec enumerate anonymous access]]):

```bash
crackmapexec smb $IP -u 'a' -p ''
```



6. Enumerate LDAP to find users







**Command** ([[Nmap Query LDAP for Root DSE Object Information]]):

```bash
nmap -script ldap-rootdse -p 389 $_TARGET_IP
```







**Command** ([[Query LDAP Root DSE with Anonymous Bind]]):

```bash
ldapsearch -x -h $_TARGET_IP -s base
```





7.Enumerate to find users





**Command** ([[enum4linux find users]]):

```bash
enum4linux -U $DC_IP | grep 'user:'
```









**Command** ([[CrackMapExec Brute Force SMB Usernames and Passwords]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```









**Command** ([[nmap nse krb5-enum-users ]]):

```bash
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='$DOMAIN',userdb=$USER_LIST_FILE" $IP
```










