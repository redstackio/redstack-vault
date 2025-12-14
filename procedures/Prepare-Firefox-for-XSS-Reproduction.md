---
id: proc-firefox-xss-prep
tags:
  - xss
  - browser-setup
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:24.248Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Firefox-for-XSS-Reproduction

## Summary

This procedure sets up Firefox browser, which is essential for reproducing the XSS exploit due to its specific handling of URL-encoded characters like %u0022 in payloads.

## Description

In the context of the Starbucks UK XSS vulnerability, Firefox is required because it properly decodes and interprets the encoded quote (%u0022) in the query parameters reflected into the HTML canonical link tag, allowing the injection of malicious attributes without triggering WAF rules. This step ensures the environment is ready for subsequent navigation and payload delivery.

## Requirements

1. Firefox browser installed (version supporting Unicode encoding, e.g., latest stable).
2. Internet access to the target website.
3. No additional credentials or tools needed at this stage.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual browser user-agent strings or encoded payloads in logs.
- Implement client-side encoding validation in web applications.

## Objectives

1. Launch a compatible browser for exploit reproduction.
2. Verify encoding support for WAF bypass.
3. Prepare for authenticated session establishment.

## Instructions

### Step 1: Launch Firefox

**Context**: Start the browser to handle the exploit's encoding requirements.

No specific command; manually open Firefox via desktop shortcut or terminal:

```bash
firefox
```

> This launches the browser. Confirm it loads without issues. Expected output: Browser window opens, ready for URL entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[browser-setup]]
