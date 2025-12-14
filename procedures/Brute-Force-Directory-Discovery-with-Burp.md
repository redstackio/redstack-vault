---
tags:
  - brute-force
  - directory-discovery
  - reconnaissance
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: aee15210-4928-49a8-b256-ea7c7d41305a
created_at: '2025-12-14T17:29:56.717Z'
updated_at: '2025-12-14T17:29:56.717Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Brute-Force-Directory-Discovery-with-Burp

## Summary

This procedure uses Burp Suite Intruder to brute-force common web directories, uncovering hidden paths like /dashboard that may expose sensitive files such as phpinfo.php.

## Description

Directory brute-forcing systematically tests for accessible paths on a web server, often revealing administrative interfaces or leftover files. In this scenario, targeting a PHP-based site on Windows, the technique identifies /dashboard leading to phpinfo.php. Burp Suite proxies requests and automates payload insertion from a wordlist. Prerequisites include Burp setup and a directory wordlist (e.g., SecLists common directories). Outcomes include HTTP status codes indicating valid paths (200 OK) versus forbidden (403).

## Requirements

1. Burp Suite Professional or Community Edition installed
2. Wordlist of common directories (e.g., /admin, /info, /dashboard)
3. Proxy configuration to intercept browser traffic to the target
4. Network access to the target domain

## Defense

Defensive measures and detection strategies:

- Deploy directory traversal protections in web servers (e.g., Apache mod_rewrite)
- Log and alert on high-volume requests to non-existent paths
- Remove or secure debugging files like phpinfo.php

## Objectives

1. Discover hidden directories without authentication
2. Identify potential information disclosure endpoints
3. Map the web application's structure for further attacks

## Instructions

### Step 1: Configure Burp Proxy and Target

**Context**: Set up Burp to intercept traffic and define the target scope.

Launch Burp Suite, configure the browser proxy to 127.0.0.1:8080, and navigate to the target domain to capture the initial request.

> Right-click the request in Proxy > HTTP history, select "Send to Intruder" to prepare for brute-forcing.

### Step 2: Set Up Intruder Attack

**Context**: Define payload positions for directory paths and load a wordlist.

In Intruder, mark the directory parameter (e.g., §path§ in /§path§/), select Sniper attack type, and load a wordlist like common.txt from SecLists. Start the attack, analyzing responses for 200 status.

> Filter results by response length or status code to spot anomalies, such as discovery of /dashboard.

### Step 3: Validate Discoveries

**Context**: Manually verify promising paths.

Access identified directories (e.g., /dashboard) in the browser to confirm contents.

> Look for files like info.php or phpinfo.php in the output.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[brute-force]]
- [[directory-discovery]]
- [[Reconnaissance]]
