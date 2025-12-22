---
id: 5a61a802-2a16-4a10-9fd9-602ea5276a1a
name: Nmap-Directory-Enumeration-in-Web-Application
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T17:09:05.224000+00:00'
updated_at: '2023-05-26T18:51:33.032919+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - web
  - reconnaissance
  - nmap
  - owasp
  - owasp top 10
  - web applications
commands:
  - '[[commands/nmap-http-enum-directory-scan]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Nmap-Directory-Enumeration-in-Web-Application

## Summary

This procedure uses Nmap's http-enum script to enumerate hidden or unreferenced directories and files in a web application, helping identify potential entry points, sensitive information, or misconfigurations during reconnaissance.

## Description

Web applications often contain directories and files that are not linked from the main site, such as administrative panels, backup files, or configuration directories. The http-enum script in Nmap performs brute-force enumeration against a predefined wordlist of common paths, sending HTTP requests to check for existence via status codes or content patterns. This technique is useful in the initial reconnaissance phase to map the attack surface of public-facing web applications. It maps to MITRE ATT&CK technique T1595 (Active Scanning) under the Reconnaissance tactic, as it actively probes the target for discoverable resources. Prerequisites include network access to the target web server, typically over port 80 or 443, and Nmap installed on the attacker's machine.

## Requirements

1. Nmap tool installed (version 7.0 or later for http-enum script support).
2. Network connectivity to the target web server (firewall rules allowing outbound HTTP requests).
3. Basic knowledge of target IP or hostname and the web port (default 80 for HTTP).
4. Optional: Custom wordlist for more targeted enumeration if default paths are insufficient.

## Defense

Defensive measures include deploying web application firewalls (WAFs) to detect and block anomalous scanning patterns, implementing rate limiting on HTTP requests, and using directory listing protections (e.g., Apache's Options -Indexes). Monitor server logs for repeated 404/403 responses from unknown paths, and employ intrusion detection systems (IDS) to flag Nmap-like traffic signatures.

## Objectives

1. Identify hidden directories and files not referenced in the application.
2. Discover potential sensitive endpoints like admin panels or backups.
3. Map the web application's structure for further exploitation planning.
4. Validate findings by checking for directory listings or error messages.

## Instructions

### Step 1: Verify Target Accessibility

**Context**: Before enumeration, confirm the target web server is reachable and the specified port is open to avoid false negatives.

Use a basic Nmap scan to check port status.

**Command** ([[commands/nmap-basic-port-scan]]):
```bash
nmap -p80 $_TARGET_IP
```

This step ensures the web service is running. If the port is closed, check for HTTPS on port 443 or adjust firewall rules.

### Step 2: Run Directory Enumeration with http-enum

**Context**: Execute the http-enum script to brute-force common directories and files. The script uses Nmap's built-in wordlist of over 2,000 paths, categorizing findings as 'interesting' based on responses like 200 OK or directory listings.

**Command** ([[commands/nmap-http-enum-directory-scan]]):
```bash
nmap -p80 --script http-enum $_TARGET_IP
```

Review the output for paths marked as potentially interesting. If needed, add verbosity with -v for more details or specify a custom wordlist with --script-args http-enum.basepath=/customlist.txt.

### Step 3: Validate and Manually Check Findings

**Context**: Nmap's output may include false positives; manually verify discovered paths using a browser or curl to inspect content, such as directory listings or login pages.

For example, if /admin/ is found, navigate to http://$_TARGET_IP/admin/ and note any accessible resources.

**Expected Output**: Confirmation of directory contents, e.g., index pages or error messages revealing server details.

If no interesting paths are found, consider running against HTTPS (-p443 --script ssl-enum-ciphers,http-enum) or expanding the scan scope.
