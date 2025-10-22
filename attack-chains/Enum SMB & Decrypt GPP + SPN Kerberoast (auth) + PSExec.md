---
id: eaa41e18-3fc0-4a6b-a66d-313968ebafae
name: Enum SMB & Decrypt GPP + SPN Kerberoast (auth) + PSExec
type: attack_chain
description: Windows, SMB, Group Password Policy, SYSVOL, SPN, Kerberoast, psexec
verified: false
submitted: false
step_count: 10
created_at: '2020-03-26T01:58:07.907746+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Identify a Password Hash (Hashcat)]]'
- '[[Connect to Windows using PsExec (Authenticated)]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Decrypt a Group Policy Preferences (GPP) Password]]'
- '[[Search SMB by Filename and Download Matches]]'
- '[[List All Active Directory Users]]'
- '[[Browse an SMB Share]]'
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[List SMB Shares]]'
tags:
- Windows
- SMB
- Group Password Policy
- SYSVOL
- SPN
- Kerberoast
- psexec
---

# Enum SMB & Decrypt GPP + SPN Kerberoast (auth) + PSExec

**Description**: Windows, SMB, Group Password Policy, SYSVOL, SPN, Kerberoast, psexec

## Overview

This attack chain consists of 10 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: List SMB Shares

**Procedure**: [[List SMB Shares]]

> Query an SMB server and attempt to list available shares using a null session (no login). 

---

### Step 3: Browse an SMB Share

**Procedure**: [[Browse an SMB Share]]

> Use smbclient to connect to an SMB share and browse with an interactive shell. 

---

### Step 4: Search SMB by Filename and Download Matches

**Procedure**: [[Search SMB by Filename and Download Matches]]

> SMB shares often contain sensitive information, which can be easily enumerated. Tools such as smbmap can crawl a SMB share, looking for and downloading files which match certain name criteria. 

---

### Step 5: Decrypt a Group Policy Preferences (GPP) Password

**Procedure**: [[Decrypt a Group Policy Preferences (GPP) Password]]

> Decrypt a Group Policy Preference Password using gpp-decrypt. While passwords contained in these GPP files are encrypted, Microsoft published the AES key, making decryption trivial. GPP files are often found on SYSVOL shares, as administrators use them to apply the same settings across multiple mac

---

### Step 6: List All Active Directory Users

**Procedure**: [[List All Active Directory Users]]

> Attackers with valid credentials to an Active Directory domain user can authenticate with a domain controller and list other users in the domain. 

---

### Step 7: Query Domain for SPN and Attempt to Kerberoast (Authenticated)

**Procedure**: [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]

> Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts. 

---

### Step 8: Identify a Password Hash (Hashcat)

**Procedure**: [[Identify a Password Hash (Hashcat)]]

> Analyze a password hash to identify the type and Hashcat mode. 

---

### Step 9: Brute Force Password Hashes (Hashcat)

**Procedure**: [[Brute Force Password Hashes (Hashcat)]]

> Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode. 

---

### Step 10: Connect to Windows using PsExec (Authenticated)

**Procedure**: [[Connect to Windows using PsExec (Authenticated)]]

> Use PSExec to connect to a remote Windows system and spawn a Command shell  (cmd.exe). In order to use PSExec, the user must have full permissions to the "$ADMIN" share, which generally requires administrator credentials. 

---

## Chain Summary

- **Total Steps**: 10
- **Key Procedures**: 10 procedures
