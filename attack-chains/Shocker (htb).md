---
id: 07fb5ba1-6d9f-4035-b1fb-74ad89ac3523
name: Shocker (htb)
type: attack_chain
description: ''
verified: false
submitted: false
step_count: 4
created_at: '2019-10-10T22:31:13.284211+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Directory Brute Force a Web App with Extensions (GoBuster)]]'
- '[[Spawn a Root Shell using Sudo and Perl]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Exploit Shellshock on a Vulnerable Web App]]'
---

# Shocker (htb)

## Overview

This attack chain consists of 4 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Directory Brute Force a Web App with Extensions (GoBuster)

**Procedure**: [[Directory Brute Force a Web App with Extensions (GoBuster)]]

> Perform a directory brute force while specifying extensions. Choose file extensions to brute force based on initial recon of  files on the webserver (.php, .asp, .js, etc), directories (cgi-bin suggests .sh scripts), underlying technology disclosed in headers (Python, PHP, Ruby), etc. For example, 

---

### Step 3: Exploit Shellshock on a Vulnerable Web App

**Procedure**: [[Exploit Shellshock on a Vulnerable Web App]]

> Shellshock is a family of security bugs in the Bash shell (pre 43-027), which allows attackers to remotely execute arbitrary commands on a vulnerable system. Web servers can be exploited by identifying a vulnerable script in the /cgi-bin directory, then using fields in the header to specify command

---

### Step 4: Spawn a Root Shell using Sudo and Perl

**Procedure**: [[Spawn a Root Shell using Sudo and Perl]]

> In some instances, a user may need to run Perl commands as root. This is often implemented by giving the user permission to use sudo to execute Perl, or Perl itself may be configured with SUID rights. Both situations introduce a privilege escalation vulnerability,  as attackers can use it to spawn 

---

## Chain Summary

- **Total Steps**: 4
- **Key Procedures**: 4 procedures
