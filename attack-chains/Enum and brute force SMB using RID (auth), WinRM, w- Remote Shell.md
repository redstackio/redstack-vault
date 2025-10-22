---
id: cf2c2de0-46a3-496b-8e59-d11fb9328e8e
name: Enum and brute force SMB using RID (auth), WinRM, w/ Remote Shell
type: attack_chain
description: Windows, smb, rid, winrm, shell, cisco type 7, brute force, CTF
verified: false
submitted: false
step_count: 11
created_at: '2020-03-31T04:28:39.042317+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Brute Force SMB Users Using RID (Authenticated)]]'
- '[[Dump a Process''s Memory (PowerShell)]]'
- '[[Identify a Password Hash (Hashcat)]]'
- '[[Build a User List from a Public Webpage]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Find Interesting Strings in a Raw Memory Dump]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[Brute Force SMB Usernames and Passwords]]'
- '[[Decrypt a Cisco Type 7 Password]]'
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

# Enum and brute force SMB using RID (auth), WinRM, w/ Remote Shell

**Description**: Windows, smb, rid, winrm, shell, cisco type 7, brute force, CTF

## Overview

This attack chain consists of 11 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Decrypt a Cisco Type 7 Password

**Procedure**: [[Decrypt a Cisco Type 7 Password]]

> Cisco router passwords encrypted using Type 7 are trivial to decrypt using open source tools, as the key is public. 

---

### Step 3: Identify a Password Hash (Hashcat)

**Procedure**: [[Identify a Password Hash (Hashcat)]]

> Analyze a password hash to identify the type and Hashcat mode. 

---

### Step 4: Brute Force Password Hashes (Hashcat)

**Procedure**: [[Brute Force Password Hashes (Hashcat)]]

> Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode. 

---

### Step 5: Build a User List from a Public Webpage

**Procedure**: [[Build a User List from a Public Webpage]]

> Administrators will often create user names following predictable patterns, making it possible for attackers to guess at valid names. This procedure will go over popular naming schemes for building potential user lists from a public website, which can be then used to brute force logins. 

---

### Step 6: Brute Force SMB Usernames and Passwords

**Procedure**: [[Brute Force SMB Usernames and Passwords]]

> Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement. 

---

### Step 7: Brute Force SMB Users Using RID (Authenticated)

**Procedure**: [[Brute Force SMB Users Using RID (Authenticated)]]

> Various tools can be used to brute force valid SMB users using their relative identifier (RID). This allows attackers to easily enumerate additional users on a system with which they've already authenticated. 

---

### Step 8: Spawn an Interactive Shell with WinRM (Linux)

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

### Step 9: Dump a Process's Memory (PowerShell)

**Procedure**: [[Dump a Process's Memory (PowerShell)]]

> Dump a process's memory  into a file using PowerSploit's Out-Minidump cmdlet. 

---

### Step 10: Find Interesting Strings in a Raw Memory Dump

**Procedure**: [[Find Interesting Strings in a Raw Memory Dump]]

> Basic enumeration of human readable strings can quickly provide information from a raw memory dump. Depending on the source, a dump may include usernames and passwords, encryption keys, cookies, library calls, etc, all of which can be easily identified without the need for more sophisticated analys

---

### Step 11: Spawn an Interactive Shell with WinRM (Linux)

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

## Chain Summary

- **Total Steps**: 11
- **Key Procedures**: 10 procedures
