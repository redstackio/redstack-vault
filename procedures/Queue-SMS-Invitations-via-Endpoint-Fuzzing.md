---
id: proc-uber-fuzz-001
tags:
  - sms-flood
  - fuzzing
  - api-abuse
type: procedure
tools:
  - '[[tools/OWASP-ZAP]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/zap-fuzz-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.622Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Queue-SMS-Invitations-via-Endpoint-Fuzzing

## Summary

This procedure uses fuzzing to send a high volume of POST requests to Uber's driver referral endpoint, queuing unlimited SMS invitations to a target phone number without triggering immediate sends or robust rate limits.

## Description

In the context of Uber's partners portal, the /driver_invitations endpoint lacks proper sender verification, allowing unverified users to abuse the referral system. By fuzzing with OWASP ZAP, attackers can simulate rapid invitations (e.g., 10,000 requests) using the same phone number, exploiting the system's queuing mechanism. This leads to later SMS floods without per-user limits. Prerequisites include access to the portal and a valid CSRF token; outcomes include queued spam that persists via daily retries, enabling harassment, privacy issues, and potential DND violations.

## Requirements

1. OWASP ZAP installed and configured for HTTP fuzzing
2. Valid session cookie and CSRF token from https://partners.uber.com/referrals/
3. Target phone number in E.164 format (e.g., +1XXXXXXXXXX)

## Defense

Defensive measures and detection strategies:

- Implement strict rate limiting per IP/user on invitation endpoints (e.g., 5 requests/hour)
- Require verified sender accounts before queuing SMS
- Monitor for anomalous request volumes to referral APIs and block fuzzing patterns
- Enforce immediate opt-out (e.g., 'STOP' reply) and cap retry attempts

## Objectives

1. Queue large volumes of SMS invitations without immediate delivery
2. Bypass soft rate limits through high-speed fuzzing
3. Set up conditions for recurring daily spam floods

## Instructions

### Step 1: Configure OWASP ZAP for Fuzzing

**Context**: Set up the base request in ZAP to target the endpoint with the JSON payload containing the target phone.

**Command** ([[commands/zap-fuzz-endpoint]]):
```bash
# Launch OWASP ZAP, proxy traffic through it, and navigate to https://partners.uber.com/referrals/
# Capture the POST to /driver_invitations in the History tab
# Right-click > Attack > Fuzzer > Add Payloads: Set 'mobiles' field to repeat "+████████" 10,000 times
# Position: Payloads in JSON body; Number of runs: 10000
```

> This configures ZAP to fuzz the endpoint rapidly. Expected output: ZAP reports 10,000 successful requests with HTTP 200, queuing invitations server-side.

### Step 2: Execute the Fuzz Attack

**Context**: Run the fuzzer to send the requests, simulating unlimited invitations from an unverified profile.

**Command** ([[commands/zap-fuzz-endpoint]]):
```bash
# In ZAP Fuzzer window: Click 'Start Fuzzer'
# Monitor progress; adjust threads if needed for speed (default 5-10)
```

> Fuzzing completes in minutes, with no blocks due to insufficient limits. Expected output: Log of successful queues; no SMS sent yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/zap-fuzz-endpoint]]

## Tools Used

- [[tools/OWASP-ZAP]]

## Tags

- sms-flood
- fuzzing
- api-abuse
