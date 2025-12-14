---
id: proc-identify-reflected-xss-search
name: Identify Reflected XSS in Search Functionality
tags:
  - xss
  - reflected-xss
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/test-basic-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:19.712Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Reflected XSS in Search Functionality

## Summary

This procedure tests web search functionalities for reflected XSS vulnerabilities by submitting basic JavaScript payloads and checking for unsanitized reflection in the response, identifying potential injection points on sites like support.rockstargames.com.

## Description

In a typical attack scenario, attackers probe public-facing web applications for input reflection without proper output encoding. Here, the search query parameter on support.rockstargames.com is tested, revealing filterable but bypassable inputs. Expected outcomes include payload reflection in HTML, enabling further exploitation for client-side attacks like session theft.

## Requirements

1. Access to curl or a web browser
2. Target URL with search functionality (e.g., support.rockstargames.com/search)
3. Basic knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Use output encoding libraries like OWASP ESAPI for all user inputs
- Monitor for anomalous search queries with script patterns in logs

## Objectives

1. Confirm if search inputs are reflected without sanitization
2. Identify filter behaviors for payload crafting
3. Validate vulnerability for escalation to exploitation

## Instructions

### Step 1: Probe with Basic Payload

**Context**: Submit a simple XSS payload to check for direct reflection.

**Command** ([[commands/test-basic-xss-payload]]):
```bash
curl -X GET "https://support.rockstargames.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E" -v
```

> This sends a URL-encoded <script>alert(1)</script> payload. Inspect the response body for the decoded payload in HTML. If reflected, an alert would trigger in a browser.

### Step 2: Verify in Browser

**Context**: Load the payload in a browser to confirm execution.

**Command** ([[commands/test-basic-xss-payload]]):
```bash
# Manually visit: https://support.rockstargames.com/search?q=<script>alert(1)</script>
```

> Open developer tools (F12) and check console/network for execution. Success if alert pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-basic-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
