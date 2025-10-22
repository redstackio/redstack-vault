---
id: e2bb5ab8-dc52-42cf-8117-be20d11aa9c4
name: Drupal 7.x RCE Chain w/ Reverse Shell (no auth)
type: attack_chain
description: 'Web app, windows, CTF '
verified: false
submitted: false
step_count: 6
created_at: '2019-12-05T20:41:35.722844+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Upgrade from a Website RCE to Netcat Reverse Shell (Windows)]]'
- '[[Exploit the ClientCopyImage Vulnerability (MS15-051)]]'
- '[[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Directory Brute Force a Web App (Wfuzz)]]'
- '[[Drupal 7.x Services Module RCE (CVE-2019-6340)]]'
tags:
- Web app
- windows
- CTF
---

# Drupal 7.x RCE Chain w/ Reverse Shell (no auth)

**Description**: Web app, windows, CTF 

## Overview

This attack chain consists of 6 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Directory Brute Force a Web App (Wfuzz)

**Procedure**: [[Directory Brute Force a Web App (Wfuzz)]]

> Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

---

### Step 3: Drupal 7.x Services Module RCE (CVE-2019-6340)

**Procedure**: [[Drupal 7.x Services Module RCE (CVE-2019-6340)]]

> Improper sanitation of input from non-form sources allows attackers to execute arbitrary code if either: the site uses a RESTful API the site has a module like JSON.API enabled. 

---

### Step 4: Upgrade from a Website RCE to Netcat Reverse Shell (Windows)

**Procedure**: [[Upgrade from a Website RCE to Netcat Reverse Shell (Windows)]]

> Download and execute Netcat to create  a reverse shell on a remote system. While Windows  can spawn reverse shells natively, the key functions are often blocked for security reasons, so a third party program like Netcat is required. 

---

### Step 5: Enumerate Windows for Missing Patches and Hotfixes (Sherlock)

**Procedure**: [[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]

> Use Sherlock to enumerate a Windows system for potential privilege escalation paths, including common vulnerabilities , unquoted service paths, missing patches, permission issues, and more. 

---

### Step 6: Exploit the ClientCopyImage Vulnerability (MS15-051)

**Procedure**: [[Exploit the ClientCopyImage Vulnerability (MS15-051)]]

> Windows 2003, 2008, Vista, 7, and 2012  which have not been patched with KB3065979 may be vulnerable to MS15-051, a kernel exploit which can allow attackers to escalate privileges to SYSTEM. This exploit is architecture specific, so the build (x86 or x64) must match the target system. 

---

## Chain Summary

- **Total Steps**: 6
- **Key Procedures**: 6 procedures
