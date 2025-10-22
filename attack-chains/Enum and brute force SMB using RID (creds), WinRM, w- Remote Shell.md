---
id: 7a2865c1-f1b8-4d34-9be1-5eb89a6620c5
name: Enum and brute force SMB using RID (creds), WinRM, w/ Remote Shell
type: attack_chain
description: Windows, smb, rid, winrm, shell, cisco type 7, brute force, CTF
verified: true
submitted: true
step_count: 7
created_at: '2023-02-19T19:09:26.795501+00:00'
updated_at: '2023-05-30T20:16:01.720164+00:00'
procedures:
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Brute Force SMB Users Using RID (Authenticated)]]'
- '[[Build a User List from a Public Webpage]]'
- '[[Find Interesting Strings in a Raw Memory Dump]]'
- '[[Brute Force SMB Usernames and Passwords]]'
- '[[Dump a Process''s Memory (PowerShell)]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]'
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]'
- '[[Collection|TA0009 - Collection]]'
tags:
- Windows
- smb
- rid
- winrm
- shell
- cisco type 7
- brute force
- CTF
---

# Enum and brute force SMB using RID (creds), WinRM, w/ Remote Shell

**Status**: ✓ Verified

**Description**: Windows, smb, rid, winrm, shell, cisco type 7, brute force, CTF

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0017** Organizational Information Gathering → **TA0006** Credential Access → **TA0007** Discovery → **TA0008** Lateral Movement → **TA0009** Collection

## Attack Steps

### Step 1: Build a User List from a Public Webpage

**MITRE ATT&CK**: [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]] → [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]

**Procedure**: [[Build a User List from a Public Webpage]]

> Administrators will often create user names following predictable patterns, making it possible for attackers to guess at valid names. This procedure will go over popular naming schemes for building potential user lists from a public website, which can be then used to brute force logins. 

---

### Step 2: Brute Force SMB Usernames and Passwords

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force SMB Usernames and Passwords]]

> Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement. 

---

### Step 3: Brute Force SMB Users Using RID (Authenticated)

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[Brute Force SMB Users Using RID (Authenticated)]]

> Various tools can be used to brute force valid SMB users using their relative identifier (RID). This allows attackers to easily enumerate additional users on a system with which they've already authenticated. 

---

### Step 4: Spawn an Interactive Shell with WinRM (Linux)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Windows Remote Management|T1028 - Windows Remote Management]]

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

### Step 5: Dump a Process's Memory (PowerShell)

**MITRE ATT&CK**: [[Collection|TA0009 - Collection]] → [[Data from Local System|T1005 - Data from Local System]]

**Procedure**: [[Dump a Process's Memory (PowerShell)]]

> Dump a process's memory  into a file using PowerSploit's Out-Minidump cmdlet. 

---

### Step 6: Find Interesting Strings in a Raw Memory Dump

**MITRE ATT&CK**: [[Collection|TA0009 - Collection]] → [[Data from Local System|T1005 - Data from Local System]]

**Procedure**: [[Find Interesting Strings in a Raw Memory Dump]]

> Basic enumeration of human readable strings can quickly provide information from a raw memory dump. Depending on the source, a dump may include usernames and passwords, encryption keys, cookies, library calls, etc, all of which can be easily identified without the need for more sophisticated analys

---

### Step 7: Spawn an Interactive Shell with WinRM (Linux)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Windows Remote Management|T1028 - Windows Remote Management]]

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

## Chain Summary

- **Total Steps**: 7
- **Tactics Used**: [[Credential Access|TA0006 - Credential Access]], [[Lateral Movement|TA0008 - Lateral Movement]], [[Discovery|TA0007 - Discovery]], [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]], [[Collection|TA0009 - Collection]]
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Data from Local System|T1005 - Data from Local System]], [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]], [[Account Discovery|T1087 - Account Discovery]], [[Windows Remote Management|T1028 - Windows Remote Management]]
- **Key Procedures**: 6 procedures
