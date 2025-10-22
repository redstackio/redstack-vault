---
id: b164be96-431f-4160-bead-6fb6eaeaf7ea
name: Enum SMB & Decrypt GPP + SPN Kerberoast (creds) + PSExec
type: attack_chain
description: Windows, SMB, Group Password Policy, SYSVOL, SPN, Kerberoast, psexec
verified: true
submitted: true
step_count: 9
created_at: '2023-02-19T19:12:24.401529+00:00'
updated_at: '2023-05-30T20:16:15.078670+00:00'
procedures:
- '[[Identify a Password Hash (Hashcat)]]'
- '[[Connect to Windows using PsExec (Authenticated)]]'
- '[[Decrypt a Group Policy Preferences (GPP) Password]]'
- '[[Search SMB by Filename and Download Matches]]'
- '[[List All Active Directory Users]]'
- '[[Browse an SMB Share]]'
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[List SMB Shares]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Collection|TA0009 - Collection]]'
tags:
- Windows
- SMB
- Group Password Policy
- SYSVOL
- SPN
- Kerberoast
- psexec
---

# Enum SMB & Decrypt GPP + SPN Kerberoast (creds) + PSExec

**Status**: ✓ Verified

**Description**: Windows, SMB, Group Password Policy, SYSVOL, SPN, Kerberoast, psexec

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0007** Discovery → **TA0009** Collection → **TA0011** Command and Control → **TA0006** Credential Access → **TA0008** Lateral Movement

## Attack Steps

### Step 1: List SMB Shares

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Network Share Discovery|T1135 - Network Share Discovery]]

**Procedure**: [[List SMB Shares]]

> Query an SMB server and attempt to list available shares using a null session (no login). 

---

### Step 2: Browse an SMB Share

**MITRE ATT&CK**: [[Collection|TA0009 - Collection]] → [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]

**Procedure**: [[Browse an SMB Share]]

> Use smbclient to connect to an SMB share and browse with an interactive shell. 

---

### Step 3: Search SMB by Filename and Download Matches

**MITRE ATT&CK**: [[Command and Control|TA0011 - Command and Control]] → [[Remote File Copy|T1105 - Remote File Copy]]

**Procedure**: [[Search SMB by Filename and Download Matches]]

> SMB shares often contain sensitive information, which can be easily enumerated. Tools such as smbmap can crawl a SMB share, looking for and downloading files which match certain name criteria. 

---

### Step 4: Decrypt a Group Policy Preferences (GPP) Password

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Credential Dumping|T1003 - Credential Dumping]]

**Procedure**: [[Decrypt a Group Policy Preferences (GPP) Password]]

> Decrypt a Group Policy Preference Password using gpp-decrypt. While passwords contained in these GPP files are encrypted, Microsoft published the AES key, making decryption trivial. GPP files are often found on SYSVOL shares, as administrators use them to apply the same settings across multiple mac

---

### Step 5: List All Active Directory Users

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[List All Active Directory Users]]

> Attackers with valid credentials to an Active Directory domain user can authenticate with a domain controller and list other users in the domain. 

---

### Step 6: Query Domain for SPN and Attempt to Kerberoast (Authenticated)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Kerberoasting|T1208 - Kerberoasting]]

**Procedure**: [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]

> Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts. 

---

### Step 7: Identify a Password Hash (Hashcat)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]]

**Procedure**: [[Identify a Password Hash (Hashcat)]]

> Analyze a password hash to identify the type and Hashcat mode. 

---

### Step 8: Brute Force Password Hashes (Hashcat)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force Password Hashes (Hashcat)]]

> Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode. 

---

### Step 9: Connect to Windows using PsExec (Authenticated)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Windows Remote Management|T1028 - Windows Remote Management]]

**Procedure**: [[Connect to Windows using PsExec (Authenticated)]]

> Use PSExec to connect to a remote Windows system and spawn a Command shell  (cmd.exe). In order to use PSExec, the user must have full permissions to the "$ADMIN" share, which generally requires administrator credentials. 

---

## Chain Summary

- **Total Steps**: 9
- **Tactics Used**: [[Command and Control|TA0011 - Command and Control]], [[Credential Access|TA0006 - Credential Access]], [[Lateral Movement|TA0008 - Lateral Movement]], [[Discovery|TA0007 - Discovery]], [[Collection|TA0009 - Collection]]
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Credential Dumping|T1003 - Credential Dumping]], [[Remote File Copy|T1105 - Remote File Copy]], [[Account Discovery|T1087 - Account Discovery]], [[Kerberoasting|T1208 - Kerberoasting]], [[Network Share Discovery|T1135 - Network Share Discovery]], [[Windows Remote Management|T1028 - Windows Remote Management]], [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]
- **Key Procedures**: 9 procedures
