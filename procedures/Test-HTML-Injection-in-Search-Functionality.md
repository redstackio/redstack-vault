---
id: proc-001
tags:
  - xss
  - injection-test
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/egrep]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-egrep-verify-xss-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.338Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-HTML-Injection-in-Search-Functionality

## Summary

This procedure tests for DOM-based XSS in the search functionality by injecting a payload into the 's' parameter and verifying breakout from the data-currentquery HTML attribute.

## Description

The search query is inserted into a JSON-like attribute without proper HTML encoding, allowing a single-quote to escape and inject tags. This step confirms the vulnerability using a simple payload like '%27%3E%3Ctest%3E%3C' on https://www.secnews.gr. Prerequisites include curl and egrep installed, and public access to the target site.

## Requirements

1. curl and egrep tools available
2. Internet access to the target URL
3. Basic understanding of URL encoding

## Defense

Defensive measures and detection strategies:

- Implement proper HTML encoding for user input in attributes (e.g., use htmlspecialchars in PHP)
- Enable Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous search queries with encoded quotes

## Objectives

1. Confirm attribute breakout and tag injection
2. Validate vulnerability existence
3. Prepare for exploitation

## Instructions

### Step 1: Send Payload and Verify Injection

**Context**: Fetch the search page with the injected payload and extract the response to confirm the <test> tag appears outside the attribute.

**Command** ([[commands/curl-egrep-verify-xss-injection]]):
```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

> This command silently fetches the page, then uses egrep to output the matching HTML snippet showing the breakout. Expected output confirms the injection point in the div's data-currentquery attribute.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-egrep-verify-xss-injection]]

## Tools Used

- [[tools/curl]]
- [[tools/egrep]]

## Tags

- [[xss]]
- [[injection-test]]
