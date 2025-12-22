---
id: 89db9662-89b5-4ab8-b1ca-84a063b5e0c9
name: Enumerate-Directories-from-Robots-Txt-using-Nmap
type: procedure
verified: true
submitted: false
created_at: '2020-09-01T17:18:29.832974+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - web
  - reconnaissance
  - nmap
  - robots-txt
  - owasp
  - owasp top 10
  - web-applications
commands:
  - '[[commands/nmap-fetch-robots-txt]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-Directories-from-Robots-Txt-using-Nmap

## Summary

This procedure uses Nmap's http-robots.txt script to retrieve and parse the robots.txt file from a target web server, identifying disallowed directories that may contain sensitive information such as admin panels, configuration files, or other hidden paths not intended for public access.

## Description

The robots.txt file is a standard file used by web servers to instruct search engine crawlers on which paths to avoid indexing. However, attackers can leverage this file during reconnaissance to discover potentially sensitive directories like /admin/, /backup/, or /config/ that might expose vulnerabilities or confidential data. This technique is particularly useful in web application assessments to map the attack surface early in the engagement. It targets HTTP services on port 80 by default but can be adapted for HTTPS on port 443. The procedure assumes the target is a web application and requires network connectivity to the server.

## Requirements

1. Network access to the target web server (e.g., firewall allows outbound connections to port 80/443).
2. Nmap tool installed on the attacker's machine.
3. Basic knowledge of web protocols and reconnaissance techniques.
4. Target IP address or hostname resolved.

## Defense

Defensive measures and detection strategies:

- Regularly review and minimize entries in robots.txt to avoid exposing unnecessary paths; use more restrictive configurations or remove the file if not needed.
- Implement web application firewalls (WAFs) to monitor and block unusual scanning patterns, such as repeated requests to /robots.txt from unknown IPs.
- Enable logging for HTTP requests to /robots.txt and correlate with other reconnaissance indicators like directory brute-forcing.
- Use content security policies (CSP) and access controls on discovered sensitive directories to prevent unauthorized access.

## Objectives

1. Retrieve the contents of the target's robots.txt file.
2. Identify and list disallowed directories for further investigation.
3. Map potential sensitive areas of the web application without direct exploitation.
4. Expected outcome: A list of hidden paths that can guide subsequent enumeration or testing.

## Instructions

### Step 1: Run Nmap Script to Fetch Robots.txt

**Context**: This step executes the Nmap http-robots.txt script to connect to the target web server, retrieve the robots.txt file, and parse it for disallowed entries. The script sends an HTTP GET request to /robots.txt and displays any User-agent directives and disallowed paths. This provides immediate insight into restricted areas without manual parsing.

**Command** ([[commands/nmap-fetch-robots-txt]]):
```bash
nmap -p80 --script http-robots.txt $_TARGET_IP
```

> Replace $_TARGET_IP with the IP address or hostname of the target web server. The -p80 flag specifies the port to scan (use -p443 for HTTPS). The script will output the number of disallowed entries and list the paths. If the file does not exist, Nmap will report that no robots.txt was found. Verify the output for paths like /admin/ or /private/ which may warrant further probing with tools like dirbuster or gobuster.

### Step 2: Analyze and Verify Discovered Paths

**Context**: After retrieving the robots.txt content, manually verify the listed directories by attempting to access them via a browser or curl to confirm if they are accessible and contain sensitive information. This step helps prioritize paths for deeper enumeration.

**Command** (use a basic curl command for verification, not linked as a full procedure command):
```bash
curl -i http://$_TARGET_IP/path-from-robots-txt
```

> For each disallowed path from the Nmap output, substitute it into the URL and run curl. Look for HTTP 200 responses indicating accessibility, or 403/401 for restricted but existent paths. Document any interesting findings, such as login pages or error messages revealing technologies.
