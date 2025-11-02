---
id: 58d5180c-fe67-4c17-b796-e2e2bc51f555
name: Nmap LDAP Enumeration with Scripts
type: command
executor: bash
data: nmap -p $_TARGET_PORT -script ldap-search $_TARGET_IP
output: "root@kali:~# nmap -p389 -script ldap-search 10.10.10.10\nStarting Nmap 7.70\
  \ ( https://nmap.org ) at 2019-09-13 18:06 EDT\nNmap scan report for 10.10.10.107\n\
  Host is up (0.069s latency).\n\nPORT    STATE SERVICE\n389/tcp open  ldap\n| ldap-search:\
  \ \n|   Context: dc=host,dc=local\n|     dn: dc=host,dc=local\n|         dc: host\n\
  |         objectClass: top\n|         objectClass: domain\n|     dn: ou=passwd,dc=host,dc=local\n\
  |         ou: passwd\n|         objectClass: top\n|         objectClass: organizationalUnit\n\
  \nNmap done: 1 IP address (1 host up) scanned in 0.90 seconds"
created_at: '2019-09-13T22:29:10.938901+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap LDAP Enumeration with Scripts

```bash
nmap -p $_TARGET_PORT -script ldap-search $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -p389 -script ldap-search 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:06 EDT
Nmap scan report for 10.10.10.107
Host is up (0.069s latency).

PORT    STATE SERVICE
389/tcp open  ldap
| ldap-search: 
|   Context: dc=host,dc=local
|     dn: dc=host,dc=local
|         dc: host
|         objectClass: top
|         objectClass: domain
|     dn: ou=passwd,dc=host,dc=local
|         ou: passwd
|         objectClass: top
|         objectClass: organizationalUnit

Nmap done: 1 IP address (1 host up) scanned in 0.90 seconds
```


