---
id: 6fed1213-9fa8-471a-ab29-6166fe79a155
name: Enum RPC, Kerberos TGT Brute Force w/ hashcat & Sharphound + DCSync (no kerberos
  preauth)
type: attack_chain
description: windows, rpc, kerberos, tgt, hashcat, , sharphound, bloodhound, active
  directory, domain controller, dcsync, WinRM, remote, UF_DONT_REQUIRE_PREAUTH
verified: false
submitted: false
step_count: 12
created_at: '2020-03-13T23:58:22.902373+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Analyze BloodHound Data for Relationships]]'
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Dump Secrets from a Remote System]]'
- '[[Identify a Password Hash (Hashcat)]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
- '[[Connect to WinRM from a Linux System (Pass-the-Hash)]]'
- '[[List Domain Users and Groups with MS-RPC/SMB Service]]'
- '[[Add DCSync Rights with WriteDACL Active Directory Permissions]]'
- '[[Map an Active Directory Environment (SharpHound)]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[Add User to Active Directory Domain Group]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
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

# Enum RPC, Kerberos TGT Brute Force w/ hashcat & Sharphound + DCSync (no kerberos preauth)

**Description**: windows, rpc, kerberos, tgt, hashcat, , sharphound, bloodhound, active directory, domain controller, dcsync, WinRM, remote, UF_DONT_REQUIRE_PREAUTH

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0007** Discovery → **TA0006** Credential Access → **TA0008** Lateral Movement

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Network Service Scanning|T1046 - Network Service Scanning]]

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: List Domain Users and Groups with MS-RPC/SMB Service

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Account Discovery|T1087 - Account Discovery]]

**Procedure**: [[List Domain Users and Groups with MS-RPC/SMB Service]]

> Connect to a Microsoft SMB server using rpcclient, and enumerate domain users and groups. 

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

### Step 9: Add User to Active Directory Domain Group

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Account Manipulation|T1098 - Account Manipulation]]

**Procedure**: [[Add User to Active Directory Domain Group]]

> Use PowerView's "Add-DomainGroupMember" cmdlet to add a user  to a domain group, assuming the current user has sufficient domain privileges (eg: GenericAll). 

---

### Step 10: Add DCSync Rights with WriteDACL Active Directory Permissions

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Account Manipulation|T1098 - Account Manipulation]]

**Procedure**: [[Add DCSync Rights with WriteDACL Active Directory Permissions]]

> Users with WriteDACL permissions to a domain can add the appropriate ACE in order to perform a DCSync attack. DCSync involves the simulation of a domain controller, which is used to connect to a legitimate domain controller and dump password hashes. 

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
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Remote Services|T1021 - Remote Services]], [[Account Manipulation|T1098 - Account Manipulation]], [[Credential Dumping|T1003 - Credential Dumping]], [[Network Service Scanning|T1046 - Network Service Scanning]], [[Pass the Hash|T1075 - Pass the Hash]], [[Account Discovery|T1087 - Account Discovery]], [[Kerberoasting|T1208 - Kerberoasting]]
- **Key Procedures**: 12 procedures
