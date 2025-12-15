---
id: proc-udemy-app-readme-001
tags:
  - information-disclosure
  - wordpress
  - readme-exposure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:56.077Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Access-WordPress-Application-Readme

## Summary

This procedure accesses an exposed readme.html file on a WordPress installation to disclose the core application version, facilitating reconnaissance for known vulnerabilities.

## Description

In misconfigured WordPress setups, the readme.html file in the root directory may remain publicly accessible, revealing the exact version of WordPress. This information allows attackers to cross-reference with vulnerability databases like CVE or Exploit-DB to find exploitable flaws. The procedure targets subdomains or main sites where file permissions are not restricted, as seen in the Udemy about subdomain case.

## Requirements

1. Network access to the target HTTP endpoint
2. Knowledge of the subdomain or base URL (e.g., http://about.udemy.com)
3. Web browser or command-line tool like curl for retrieval

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to readme files via .htaccess rules (e.g., deny public access to /readme.html)
- Monitor web server logs for anomalous GET requests to sensitive files
- Use web application firewalls (WAF) to block access to plugin and core directories

## Objectives

1. Extract WordPress core version for vulnerability scouting
2. Confirm exposure of configuration files
3. Enable chained attacks based on version-specific exploits

## Instructions

### Step 1: Retrieve Readme Content

**Context**: Directly fetch the readme.html to inspect version details without authentication.

**Command** ([[commands/curl-access-url]]):
```bash
curl http://about.udemy.com/readme.html
```

> This command sends a GET request and outputs the HTML content. Look for meta tags or body text indicating the version, such as "WordPress X.Y.Z". If using a browser, simply visit the URL and view source.

### Step 2: Analyze Output

**Context**: Parse the response to identify the version string.

No specific command needed; manually review the output for lines like "<title>WordPress X.Y.Z</title>" or changelog entries.

> Successful analysis confirms the version, e.g., exposing WordPress 3.9.1 as in the original report.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[wordpress]]
- [[Reconnaissance]]
