---
id: 3c400801-8323-4409-a048-7daf04d2da24
name: Enum RPC, Kerberos TGT Brute Force w/ hashcat & Sharphound + Auto Logon Registry
  + Dump Secrets (no kerberos preauth)
type: attack_chain
description: ' windows, rpc, kerberos, tgt, hashcat, , sharphound, bloodhound, active
  directory, domain controller, dcsync, WinRM, remote, UF_DONT_REQUIRE_PREAUTH'
verified: false
submitted: false
step_count: 12
created_at: '2020-03-17T22:51:45.314442+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Analyze BloodHound Data for Relationships]]'
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Dump Secrets from a Remote System]]'
- '[[Identify a Password Hash (Hashcat)]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
- '[[Query LDAP and Enumerate the Base DN (Nmap)]]'
- '[[Connect to WinRM from a Linux System (Pass-the-Hash)]]'
- '[[List Windows Autologon Logon Credentials]]'
- '[[Map an Active Directory Environment (SharpHound)]]'
- '[[List Local Users on Windows]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
tags:
- windows
- rpc
- kerberos
- tgt
- hashcat
- sharphound
- bloodhound
- active directory
- domain controller
- dcsync
- WinRM
- remote
- UF_DONT_REQUIRE_PREAUTH
---

# Enum RPC, Kerberos TGT Brute Force w/ hashcat & Sharphound + Auto Logon Registry + Dump Secrets (no kerberos preauth)

**Description**:  windows, rpc, kerberos, tgt, hashcat, , sharphound, bloodhound, active directory, domain controller, dcsync, WinRM, remote, UF_DONT_REQUIRE_PREAUTH

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0007** Discovery → **TA0006** Credential Access → **TA0008** Lateral Movement

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Network Service Scanning|T1046 - Network Service Scanning]]

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Query LDAP and Enumerate the Base DN (Nmap)

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

**Procedure**: [[Query LDAP and Enumerate the Base DN (Nmap)]]

> Connect to LDAP with anonymous bind and enumerate the base DN. 

---

### Step 3: Brute Force Users with "Do Not Require Kerberos Preauth." Set

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Kerberoasting|T1208 - Kerberoasting]]

**Procedure**: [[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]

> Users with "Do not require Kerberos preauthentication" will disclose their TGT without authenticating with a valid password, as long as the username is correct. This allows attackers to build a wordlist and brute force valid users with GetNPUsers.py, also retreiving their TGT. 

---

### Step 4: Identify a Password Hash (Hashcat)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]]

**Procedure**: [[Identify a Password Hash (Hashcat)]]

> Analyze a password hash to identify the type and Hashcat mode. 

---

### Step 5: Brute Force Password Hashes (Hashcat)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force Password Hashes (Hashcat)]]

> Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode. 

---

### Step 6: Spawn an Interactive Shell with WinRM (Linux)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Remote Services|T1021 - Remote Services]]

**Procedure**: [[Spawn an Interactive Shell with WinRM (Linux)]]

> Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions. 

---

### Step 7: Map an Active Directory Environment (SharpHound)

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[Map an Active Directory Environment (SharpHound)]]

> Use SharpHound to connect to an Active Directory environment and enumerate objects such as users, groups, ACLs, trusts, etc. This data then can be imported into BloodHound for analysis of objects, their relationships, and potential vulnerabilities. 

---

### Step 8: Analyze BloodHound Data for Relationships

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[Analyze BloodHound Data for Relationships]]

> Prepare BloodHound data to query relationships and view suggested attacks. 

---

### Step 9: List Windows Autologon Logon Credentials

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Credential Dumping|T1003 - Credential Dumping]]

**Procedure**: [[List Windows Autologon Logon Credentials]]

> Query the Windows registry for credentials configured with the automatic logon feature. Windows allows users to specify credentials to skip logon prompts, but since these credentials are stored openly in the registry, other users can view them. 

---

### Step 10: List Local Users on Windows

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[List Local Users on Windows]]

> List local users on a Windows system using command prompt or PowerShell. 

---

### Step 11: Dump Secrets from a Remote System

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Credential Dumping|T1003 - Credential Dumping]]

**Procedure**: [[Dump Secrets from a Remote System]]

> Use Impacket's secretsdump.py to dump password hashes on a remote system, using a variety of methods, including SAM/SYSTEM hive dumps, NTDS, LSA, etc. This typically requires authentication with Administrator rights. 

---

### Step 12: Connect to WinRM from a Linux System (Pass-the-Hash)

**MITRE ATT&CK**: [[Lateral Movement|TA0008 - Lateral Movement]] → [[Pass the Hash|T1075 - Pass the Hash]]

**Procedure**: [[Connect to WinRM from a Linux System (Pass-the-Hash)]]

> Spawn a PowerShell instance on a remote system using the WinRM service (usuallyport 5985) using an NTLM password hash instead of a password. 

---

## Chain Summary

- **Total Steps**: 12
- **Tactics Used**: [[Lateral Movement|TA0008 - Lateral Movement]], [[Credential Access|TA0006 - Credential Access]], [[Discovery|TA0007 - Discovery]]
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Remote Services|T1021 - Remote Services]], [[Credential Dumping|T1003 - Credential Dumping]], [[Network Service Scanning|T1046 - Network Service Scanning]], [[Pass the Hash|T1075 - Pass the Hash]], [[Account Discovery|T1087 - Account Discovery]], [[Kerberoasting|T1208 - Kerberoasting]], [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]
- **Key Procedures**: 12 procedures
