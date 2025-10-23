---
id: 9d862c4b-ecdb-4bd9-8506-df7bd525c730
name: NTLM Hash Cracking with Hashcat
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.102377+00:00'
updated_at: '2023-04-10T20:26:22.215668+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
sub_techniques:
- '[[Password Cracking|T1110.002 - Password Cracking]]'
- '[[Password Guessing|T1110.001 - Password Guessing]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Crack NTLM hashes with hashcat]]'
- '[[Dumping AD Domain Credentials]]'
commands:
- '[[Generate custom mask for hashcat]]'
- '[[Optimize wordlist for hashcat]]'
---

# NTLM Hash Cracking with Hashcat

## Summary

NTLM hashes are commonly used in Windows environments to store user passwords. If an attacker gains access to these hashes, they can use tools like hashcat to crack them and gain access to user accounts. This procedure details how to use hashcat to crack NTLM hashes. 

To crack NTLM hashes, an atta

## Description

# Description

NTLM hashes are commonly used in Windows environments to store user passwords. If an attacker gains access to these hashes, they can use tools like hashcat to crack them and gain access to user accounts. This procedure details how to use hashcat to crack NTLM hashes. 

To crack NTLM hashes, an attacker first needs to obtain them. This can be done by dumping the credentials from the domain controller using tools like Mimikatz. Once the hashes are obtained, the attacker can use hashcat to generate custom masks and crack the passwords. 

This procedure can be used by attackers to gain access to user accounts and escalate privileges within a Windows environment.

 

## Requirements

1. Access to a Windows domain controller

1. NTLM hashes to crack

1. Hashcat installed

 

## Defense

1. Implement strong password policies to prevent easy cracking of passwords

1. Monitor network traffic for suspicious activity, such as large amounts of failed logins

1. Use multi-factor authentication to prevent unauthorized access to user accounts

 

## Objectives

1. Obtain NTLM hashes from a Windows domain controller

1. Use hashcat to generate custom masks and crack the passwords

1. Gain access to user accounts and escalate privileges within a Windows environment

 

# Instructions

1. To generate a custom mask based on a wordlist:
1. Clone the git repository using the command: $ git clone https://github.com/iphelix/pack/blob/master/README
2. Run the command: $ python2 statsgen.py ../hashcat.potfile -o hashcat.mask
3. Run the command: $ python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask

To crack passwords using hashcat:
1. Run the command: $ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico -r myrules.rule --opencl-device-types 1,2

 



**Code**: [[# Basic wordlist
# (-O) will Optimize for 32 chara]]



> The above command is useful when you want to crack passwords using hashcat. The command takes multiple arguments, which are explained below:
1. -m: Hash type. In this case, it is set to 1000, which corresponds to NTLM.
2. -w: Workload profile. In this case, it is set to 4, which corresponds to Insane.
3. -O: Optimize for 32 characters or less passwords.
4. -a: Attack mode. In this case, it is set to 0, which corresponds to straight.
5. -o: Output file.
6. -r: Rule file.
7. --opencl-device-types: Comma-separated list of OpenCL device types to use.

The custom mask generated using the above command can be used to crack passwords that are similar to the words in the wordlist. The targettime argument specifies the time in seconds that the mask generation algorithm should run for. The optindex argument specifies the optimization index to use. The -q flag suppresses the output, and the -o flag specifies the output file.



**Command** ([[Optimize wordlist for hashcat]]):

```bash
$ hashcat64.exe -m 1000 -w 4 -O -a 0 -o pathtopotfile pathtohashes pathtodico -r myrules.rule --opencl-device-types 1,2
```





**Command** ([[Generate custom mask for hashcat]]):

```bash
$ python2 statsgen.py ../hashcat.potfile -o hashcat.mask
$ python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

### Sub-Techniques

- [[Password Cracking|T1110.002 - Password Cracking]]
- [[Password Guessing|T1110.001 - Password Guessing]]

## Commands Used

- [[Generate custom mask for hashcat]]
- [[Optimize wordlist for hashcat]]

## Tags

- [[Active Directory Attacks]]
- [[Crack NTLM hashes with hashcat]]
- [[Dumping AD Domain Credentials]]


