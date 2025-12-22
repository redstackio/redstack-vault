---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - web-applications
  - directory-enumeration
  - web-recon
commands:
  - '[[commands/Gobuster-Directory-Enumeration]]'
platforms:
  - Web
tools:
  - '[[tools/Gobuster]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Directory-Brute-Forcing-with-Gobuster

## Summary

This procedure uses the Gobuster tool to perform directory brute-forcing on a web application, attempting to discover hidden directories and endpoints by testing a wordlist of common directory names against the target URL. It identifies existent directories based on HTTP status codes such as 200 (OK), 301 (Moved Permanently), or 403 (Forbidden), which indicate potential points of interest like admin panels or sensitive files.

## Description

Directory brute-forcing is a reconnaissance technique commonly used during web application penetration testing to map out the attack surface. Gobuster, a fast and simple tool, sends HTTP requests for each entry in a provided wordlist, appending it to the base URL, and analyzes the responses. Successful discoveries are those returning status codes that suggest the resource exists, helping attackers identify unprotected areas. This procedure is applicable in scenarios where directory listing is disabled on the web server, and it maps to MITRE ATT&CK technique T1083 (File and Directory Discovery) under the Discovery tactic. It requires network access to the target and a suitable wordlist, such as common directories like /admin, /backup, or /images.

## Requirements

1. Gobuster tool installed on the attacker's machine.
2. A wordlist file containing potential directory names (e.g., directory-list-2.3-medium.txt from SecLists).
3. Network connectivity to the target web application.
4. Basic understanding of HTTP status codes to interpret results.

## Defense

- Implement a Web Application Firewall (WAF) to detect and block brute-force patterns based on user-agent, request rate, or payload signatures.
- Enable rate limiting on the web server to throttle excessive requests from a single IP.
- Use directory traversal protections and ensure sensitive directories are not publicly accessible or return consistent error codes (e.g., 404 for all non-existent paths).
- Monitor server logs for unusual GET requests to common paths and anomalous status code patterns.

## Objectives

1. Discover hidden directories on the target web application that may expose sensitive information or functionality.
2. Identify potential entry points for further exploitation, such as administrative interfaces.
3. Map the web application's structure without relying on enabled directory listings.

## Instructions

### Step 1: Prepare the Wordlist

**Context**: Select or create a wordlist of common directory names to test. This step ensures you have a comprehensive list tailored to web applications, avoiding generic or overly large lists that could increase detection risk or execution time.

If using a standard wordlist, download it from a repository like SecLists. No command is needed here, but verify the file exists and contains entries like 'admin', 'backup', 'images'.

> Ensure the wordlist is in plain text format with one entry per line. Common sources include Kali Linux's /usr/share/wordlists/dirbuster/.

### Step 2: Execute Gobuster for Directory Enumeration

**Context**: Run Gobuster in directory mode to brute-force the target URL with the wordlist. Specify status codes to consider as successful (e.g., 200, 204, 301, 302, 307, 403) to filter out false negatives from redirects or forbidden accesses that still confirm existence.

**Command** ([[commands/Gobuster-Directory-Enumeration]]):
```bash
gobuster dir -w $_WORDLIST -u $_TARGET_URL -s "200,204,301,302,307,403" -t 50
```

> This command initiates the brute-force scan. The -t 50 flag sets 50 threads for faster execution. Expected output includes a summary of the scan parameters followed by discovered directories with their status codes, such as /admin (Status: 301). Redirects (301/302) often indicate existent directories. Save output to a file with -o results.txt for later analysis. If no discoveries are made, try a larger wordlist or adjust status codes.

### Step 3: Analyze and Verify Discoveries

**Context**: Review the Gobuster output to identify promising directories, then manually verify them in a browser or with curl to confirm accessibility and content. This step validates findings and checks for further vulnerabilities like exposed files.

Use a browser or [[commands/curl-basic-request]] to access discovered paths, e.g., curl -I http://target.com/admin.

> Look for directories returning 200 (content served), 301/302 (redirects to login or subpages), or 403 (forbidden but existent). Ignore 404s. Document findings, such as /admin leading to a login page, which could be targeted next for credential attacks. If 403s appear, consider bypassing with techniques like case variation or encoding.
