---
tags:
  - captcha-bypass
  - misconfiguration
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 40c5d8fd-2202-4afc-a14e-f3579c1fa404
created_at: '2025-12-14T17:24:18.902Z'
updated_at: '2025-12-14T17:24:18.902Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Captcha-Reuse-Bypass

## Summary

This procedure exploits a misconfiguration in the captcha system where uniqueness is not enforced, allowing the same solved captcha to be reused for multiple submissions. It is primarily used to automate actions on web applications that rely on captchas for bot prevention, such as form submissions or API calls.

## Description

In the VK.com implementation, the captcha mechanism failed to validate or regenerate tokens per request, permitting attackers to solve a captcha once and replay the token indefinitely. This bypasses the intended protection against automated abuse, enabling high-volume operations without human intervention. The attack targets the submission endpoint, typically involving JSON payloads with captcha ID and solution fields. Prerequisites include access to the protected endpoint and the ability to inspect or craft HTTP requests. Expected outcomes include successful processing of repeated actions without captcha re-solving.

## Requirements

1. Access to a browser or HTTP client for capturing and replaying requests.
2. A solved captcha token from an initial legitimate submission.
3. Knowledge of the target endpoint URL and payload structure (e.g., via dev tools).

## Defense

Defensive measures and detection strategies:

- Enforce strict uniqueness checks on captcha tokens with server-side validation and short expiration times.
- Implement rate limiting at the IP or session level independent of captcha retries.
- Monitor for anomalous patterns like repeated use of the same captcha ID across multiple requests.

## Objectives

1. Reuse a single captcha solution to bypass repeated solving requirements.
2. Automate protected actions without triggering additional verifications.
3. Demonstrate the vulnerability for reporting or exploitation.

## Instructions

### Step 1: Obtain Initial Captcha Solution

**Context**: Solve the captcha legitimately to acquire a valid token for reuse.

Navigate to the protected page on VK.com, complete the captcha challenge, and inspect the network request in browser dev tools to capture the captcha_id and solution_value from the successful submission payload.

### Step 2: Replay Captcha Token

**Context**: Submit multiple requests using the captured token to verify reuse acceptance.

Craft and send repeated POST requests to the endpoint, substituting the same captcha details:

```bash
curl -X POST 'https://vk.com/api/submit' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: session_id=your_session' \
  -d '{"captcha_id": "captured_id", "captcha_solution": "captured_solution", "action": "submit_form"}'
```

> This command sends a submission with the reused captcha. Expected output is a JSON response indicating success (e.g., {"status": "ok"}), without errors for invalid captcha. Repeat 5-10 times to confirm no uniqueness enforcement.

### Step 3: Validate Bypass

**Context**: Confirm the bypass by attempting actions that would normally require new captchas.

Monitor server responses for any degradation or blocks; if none occur, the bypass is successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[captcha-bypass]]
- [[misconfiguration]]
