---
id: 5339fab7-f0dd-4dbe-b1dc-1a5d455f9156
name: ecat821's Mr. Robot clone
type: attack_chain
description: Mr. Robot 2019 Completed
verified: false
submitted: false
step_count: 8
created_at: '2020-06-18T22:51:40.613250+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Nmap Interactive Mode Shell Escape]]'
- '[[Add and Execute Code on a WordPress Site (Authenticated)]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Brute Force a Web Login Form]]'
- '[[Find Linux Files with Elevated Privileges]]'
- '[[Brute Force Valid Users from a Forgotten Password Form]]'
- '[[Directory Brute Force a Web App (Wfuzz)]]'
- '[[Upgrade from a Website RCE to Reverse Shell (Linux)]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
tags:
- Mr. Robot 2019 Completed
---

# ecat821's Mr. Robot clone

**Description**: Mr. Robot 2019 Completed

## Overview

This attack chain progresses through the following MITRE ATT&CK tactics:

**TA0007** Discovery → **TA0006** Credential Access → **TA0002** Execution → **TA0004** Privilege Escalation

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[Network Service Scanning|T1046 - Network Service Scanning]]

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Directory Brute Force a Web App (Wfuzz)

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Directory Brute Force a Web App (Wfuzz)]]

> Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

---

### Step 3: Brute Force Valid Users from a Forgotten Password Form

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force Valid Users from a Forgotten Password Form]]

> Website login forms often include a 'Forgot Your Password' feature to help users retrieve their passwords. Many of these forms display a different message depending on whether a valid username was entered, allowing attackers to enumerate valid usernames. 

---

### Step 4: Brute Force a Web Login Form

**MITRE ATT&CK**: [[Credential Access|TA0006 - Credential Access]] → [[Brute Force|T1110 - Brute Force]]

**Procedure**: [[Brute Force a Web Login Form]]

> In order to brute force a web login, required fields such as Cookies, HTTP methods, and additional parameters must be verified. This can be done using an HTTP proxy such as Burp Suite's proxy. 

---

### Step 5: Add and Execute Code on a WordPress Site (Authenticated)

**MITRE ATT&CK**: [[Execution|TA0002 - Execution]] → [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

**Procedure**: [[Add and Execute Code on a WordPress Site (Authenticated)]]

> Authenticated users with the ability to edit themes can easily add PHP code to a WordPress site, which will be executed as the web application's user. 

---

### Step 6: Upgrade from a Website RCE to Reverse Shell (Linux)

**MITRE ATT&CK**: [[Execution|TA0002 - Execution]] → [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

**Procedure**: [[Upgrade from a Website RCE to Reverse Shell (Linux)]]

> In cases where Remote Code Execution (RCE) is achieved on a web application, the next step is usually to launch a reverse shell for terminal access. This procedure will outline a few common approaches. 

---

### Step 7: Find Linux Files with Elevated Privileges

**MITRE ATT&CK**: [[Discovery|TA0007 - Discovery]] → [[File and Directory Discovery|T1083 - File and Directory Discovery]]

**Procedure**: [[Find Linux Files with Elevated Privileges]]

> Linux and *nix systems include features which allow certain programs to run with elevated privileges. This is a requirement for many system services, but occasionally these programs may allow attackers to execute arbitrary commands. Setuid - Programs with this permission set can run commands as the

---

### Step 8: Nmap Interactive Mode Shell Escape

**MITRE ATT&CK**: [[Privilege Escalation|TA0004 - Privilege Escalation]] → [[Setuid and Setgid|T1166 - Setuid and Setgid]]

**Procedure**: [[Nmap Interactive Mode Shell Escape]]

> Older versions of Nmap (2.02 to 5.21) include an interactive mode which can allow attackers to escape to a shell. This vulnerability can lead to privilege escalation, as Nmap is occasionally configured with SUID access rights in order for low privilege users access to features requiring root privil

---

## Chain Summary

- **Total Steps**: 8
- **Tactics Used**: [[Execution|TA0002 - Execution]], [[Privilege Escalation|TA0004 - Privilege Escalation]], [[Credential Access|TA0006 - Credential Access]], [[Discovery|TA0007 - Discovery]]
- **Techniques Used**: [[Brute Force|T1110 - Brute Force]], [[Setuid and Setgid|T1166 - Setuid and Setgid]], [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]], [[Network Service Scanning|T1046 - Network Service Scanning]], [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- **Key Procedures**: 8 procedures
