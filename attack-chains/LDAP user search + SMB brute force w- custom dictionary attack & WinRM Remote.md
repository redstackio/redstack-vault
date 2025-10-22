---
id: 59640cc2-9092-4784-a801-d729d35a8626
name: LDAP user search + SMB brute force w/ custom dictionary attack & WinRM Remote
type: attack_chain
description: ' windows, ldap, smb, dictionary, winrm, remote'
verified: true
submitted: true
step_count: 6
created_at: '2023-02-19T19:13:01.593743+00:00'
updated_at: '2023-05-30T20:16:26.162776+00:00'
procedures:
- '[[List Local Users and Group Membership on Windows]]'
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Browse an SMB Share]]'
- '[[Query LDAP and Enumerate the Base DN (ldapsearch)]]'
- '[[Brute Force SMB Usernames and Passwords]]'
- '[[Build a Password List for Online Dictionary Attack]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
tags:
- windows
- ldap
- smb
- dictionary
- winrm
- remote
---

# LDAP user search + SMB brute force w/ custom dictionary attack & WinRM Remote

**Status**: ✓ Verified

**Description**:  windows, ldap, smb, dictionary, winrm, remote

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0007** Discovery → **TA0006** Credential Access → **TA0009** Collection → **TA0008** Lateral Movement

## Attack Steps

### Step 1: Query LDAP and Enumerate the Base DN (ldapsearch)

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[Query LDAP and Enumerate the Base DN (ldapsearch)]]

> Connect to LDAP with anonymous bind and enumerate the root DSA-specific Entry (DSE), then use the result to enumerate the base DN. 

---

### Step 2: Build a Password List for Online Dictionary Attack

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Build a Password List for Online Dictionary Attack]]

> Build a custom wordlist of potential passwords using contextual information to minimize network traffic. Brute forcing passwords over the network is slow and noisy, making lists like rockyou unfit. 

---

### Step 3: Brute Force SMB Usernames and Passwords

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force SMB Usernames and Passwords]]

> Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement. 

---

### Step 4: Browse an SMB Share

**MITRE ATT&CK**: [[Collection|TA0009 - Collection]] → [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]

**Procedure**: [[Browse an SMB Share]]

> Use smbclient to connect to an SMB share and browse with an interactive shell. 

---

### Step 5: Spawn an Interactive Shell with WinRM (Linux)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Windows Remote Management|T1028 - Windows Remote Management]]

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

### Step 6: List Local Users and Group Membership on Windows

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[List Local Users and Group Membership on Windows]]

> Query a Windows system for a list of users, then request basic account information and group membership of a user. 

---

## Chain Summary

- **Total Steps**: 6
- **Tactics Used**: [[Collection|TA0009 - Collection]], [[Lateral Movement|TA0008 - Lateral Movement]], [[Credential Access|TA0006 - Credential Access]], [[Discovery|TA0007 - Discovery]]
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Account Discovery|T1087 - Account Discovery]], [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]], [[Windows Remote Management|T1028 - Windows Remote Management]]
- **Key Procedures**: 6 procedures
