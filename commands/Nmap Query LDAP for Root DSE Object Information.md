---
id: def6d704-288a-4be0-bd5c-53e24d9db06a
name: Nmap Query LDAP for Root DSE Object Information
type: command
executor: bash
data: nmap -script ldap-rootdse -p 389 $_TARGET_IP
output: "root@kali:~# nmap -script ldap-rootdse -p 389 10.10.10.10\nStarting Nmap\
  \ 7.80 ( https://nmap.org ) at 2019-12-15 17:23 EST\nNmap scan report for 10.10.10.10\n\
  Host is up (0.078s latency).\n\nPORT    STATE SERVICE\n389/tcp open  ldap\n| ldap-rootdse:\
  \ \n| LDAP Results\n|   <ROOT>\n|       supportedLDAPVersion: 3\n|       namingContexts:\
  \ dc=corporatehq,dc=com\n|       supportedExtension: 1.3.6.1.4.1.1466.20037\n|_\
  \      subschemaSubentry: cn=schema\n\nNmap done: 1 IP address (1 host up) scanned\
  \ in 1.08 seconds"
created_at: '2019-12-15T22:33:38.234029+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Query LDAP for Root DSE Object Information

```bash
nmap -script ldap-rootdse -p 389 $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -script ldap-rootdse -p 389 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-15 17:23 EST
Nmap scan report for 10.10.10.10
Host is up (0.078s latency).

PORT    STATE SERVICE
389/tcp open  ldap
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       supportedLDAPVersion: 3
|       namingContexts: dc=corporatehq,dc=com
|       supportedExtension: 1.3.6.1.4.1.1466.20037
|_      subschemaSubentry: cn=schema

Nmap done: 1 IP address (1 host up) scanned in 1.08 seconds
```
