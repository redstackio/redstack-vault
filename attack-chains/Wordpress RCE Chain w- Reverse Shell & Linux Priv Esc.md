---
id: a3ee0b5a-99cc-457d-ad2a-c2406c88a470
name: Wordpress RCE Chain w/ Reverse Shell & Linux Priv Esc
type: attack_chain
description: Web app, linux, steganography, wordpress, enumerate, privilege escalation,
  CTF
verified: false
submitted: false
step_count: 8
created_at: '2019-10-28T17:27:41.084478+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Add and Execute Code on a WordPress Site (Authenticated)]]'
- '[[Extract a Hidden File In an Image Using Steghide]]'
- '[[Enumerate a Web CMS for Usernames and Passwords]]'
- '[[Thorough Port Scan with Service Enumeration]]'
- '[[Change Password in a Writable /etc/passwd]]'
- '[[Directory Brute Force a Web App (Wfuzz)]]'
- '[[Upgrade from a Website RCE to Reverse Shell (Linux)]]'
- '[[Enumerate Linux Privilege Escalation Paths (LinEnum)]]'
tags:
- Web app
- linux
- steganography
- wordpress
- enumerate
- privilege escalation
- CTF
---

# Wordpress RCE Chain w/ Reverse Shell & Linux Priv Esc

**Description**: Web app, linux, steganography, wordpress, enumerate, privilege escalation, CTF

## Overview

This attack chain consists of 8 steps.

## Attack Steps

### Step 1: Thorough Port Scan with Service Enumeration

**Procedure**: [[Thorough Port Scan with Service Enumeration]]

> Query a computer's services by probing the ports on which it listens. Since each system potentially has 65,535 ports for TCP and UDP, it's often best to perform multiple scans, each focusing on a different technique or port range. 

---

### Step 2: Directory Brute Force a Web App (Wfuzz)

**Procedure**: [[Directory Brute Force a Web App (Wfuzz)]]

> Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

---

### Step 3: Extract a Hidden File In an Image Using Steghide

**Procedure**: [[Extract a Hidden File In an Image Using Steghide]]

> Extract a file hidden in an image (or audio file) using Steghide's steganography tools. 

---

### Step 4: Enumerate a Web CMS for Usernames and Passwords

**Procedure**: [[Enumerate a Web CMS for Usernames and Passwords]]

> Many websites reveal usernames and potential passwords in the pages themselves, hidden files, and configuration files. By enumerating a site's content with tools, username and password lists can be generated and used for login brute forcing. 

---

### Step 5: Add and Execute Code on a WordPress Site (Authenticated)

**Procedure**: [[Add and Execute Code on a WordPress Site (Authenticated)]]

> Authenticated users with the ability to edit themes can easily add PHP code to a WordPress site, which will be executed as the web application's user. 

---

### Step 6: Upgrade from a Website RCE to Reverse Shell (Linux)

**Procedure**: [[Upgrade from a Website RCE to Reverse Shell (Linux)]]

> In cases where Remote Code Execution (RCE) is achieved on a web application, the next step is usually to launch a reverse shell for terminal access. This procedure will outline a few common approaches. 

---

### Step 7: Enumerate Linux Privilege Escalation Paths (LinEnum)

**Procedure**: [[Enumerate Linux Privilege Escalation Paths (LinEnum)]]

> Automatically enumerate a Linux or Unix file environment, scanning for vulnerabilities such as permission issues, security misconfigurations, vulnerable software versions, etc. 

---

### Step 8: Change Password in a Writable /etc/passwd

**Procedure**: [[Change Password in a Writable /etc/passwd]]

> When /etc/passwd is writable, it is possible to change a user's password by entering the password hash. Passwords in /etc/passwd take priority over those found in /etc/shadow  for legacy reasons, though the same technique can be applied when /etc/shadow is writable. 

---

## Chain Summary

- **Total Steps**: 8
- **Key Procedures**: 8 procedures
