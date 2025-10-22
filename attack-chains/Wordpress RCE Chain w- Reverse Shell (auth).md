---
id: 55c64832-35f0-4a6d-9d4e-bcf65161fda7
name: Wordpress RCE Chain w/ Reverse Shell (auth)
type: attack_chain
description: webapp, linux, CTF, wordpress, brute force
verified: false
submitted: false
step_count: 8
created_at: '2019-12-05T00:03:49.439343+00:00'
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
tags:
- webapp
- linux
- CTF
- wordpress
- brute force
---

# Wordpress RCE Chain w/ Reverse Shell (auth)

**Description**: webapp, linux, CTF, wordpress, brute force

## Overview

This attack chain consists of 8 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Directory Brute Force a Web App (Wfuzz)

**Procedure**: [[Directory Brute Force a Web App (Wfuzz)]]

> Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

---

### Step 3: Brute Force Valid Users from a Forgotten Password Form

**Procedure**: [[Brute Force Valid Users from a Forgotten Password Form]]

> Website login forms often include a 'Forgot Your Password' feature to help users retrieve their passwords. Many of these forms display a different message depending on whether a valid username was entered, allowing attackers to enumerate valid usernames. 

---

### Step 4: Brute Force a Web Login Form

**Procedure**: [[Brute Force a Web Login Form]]

> In order to brute force a web login, required fields such as Cookies, HTTP methods, and additional parameters must be verified. This can be done using an HTTP proxy such as Burp Suite's proxy. 

---

### Step 5: Add and Execute Code on a WordPress Site (Authenticated)

**Procedure**: [[Add and Execute Code on a WordPress Site (Authenticated)]]

> Authenticated users with the ability to edit themes can easily add PHP code to a WordPress site, which will be executed as the web application's user. 

---

### Step 6: Upgrade from a Website RCE to Reverse Shell (Linux)

**Procedure**: [[Upgrade from a Website RCE to Reverse Shell (Linux)]]

> In cases where Remote Code Execution (RCE) is achieved on a web application, the next step is usually to launch a reverse shell for terminal access. This procedure will outline a few common approaches. 

---

### Step 7: Find Linux Files with Elevated Privileges

**Procedure**: [[Find Linux Files with Elevated Privileges]]

> Linux and *nix systems include features which allow certain programs to run with elevated privileges. This is a requirement for many system services, but occasionally these programs may allow attackers to execute arbitrary commands. Setuid - Programs with this permission set can run commands as the

---

### Step 8: Nmap Interactive Mode Shell Escape

**Procedure**: [[Nmap Interactive Mode Shell Escape]]

> Older versions of Nmap (2.02 to 5.21) include an interactive mode which can allow attackers to escape to a shell. This vulnerability can lead to privilege escalation, as Nmap is occasionally configured with SUID access rights in order for low privilege users access to features requiring root privil

---

## Chain Summary

- **Total Steps**: 8
- **Key Procedures**: 8 procedures
