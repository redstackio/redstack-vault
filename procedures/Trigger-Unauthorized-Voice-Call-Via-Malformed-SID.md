---
id: proc-vk-voice-spam-001
tags:
  - api-vulnerability
  - input-validation
  - voice-spam
  - auth-bypass
  - vk.com
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/vk-auth-validatephone-voice-spam]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:01.682Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Trigger-Unauthorized-Voice-Call-Via-Malformed-SID

## Summary

This procedure builds on the sid validation bypass to trigger voice calls instead of SMS, using the 'voice=1' parameter alongside a malformed sid, allowing attackers to spam phone calls to VK.com users without authentication.

## Description

By appending 'voice=1' to the API request with a malformed sid, the auth.validatePhone method initiates an automated voice call to deliver the activation code. This bypasses 2FA checks and proper sid validation, enabling voice spam. The attack leverages the same root cause as SMS exploitation but escalates impact through calls, which may incur costs or greater annoyance to targets.

## Requirements

1. Internet access for API requests
2. Target user ID
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Validate sid strictly and require voice parameter only with authenticated sessions
- Rate limit voice call initiations per user/IP
- Audit logs for voice=1 requests with invalid sids
- Disable unauthenticated phone actions entirely

## Objectives

1. Initiate unauthorized voice call to target user
2. Confirm escalation from SMS to voice spam
3. Highlight authorization bypass in API behavior

## Instructions

### Step 1: Craft Request with Voice Parameter

**Context**: Use a tested malformed sid and add voice=1 to switch from SMS to call.

**Command** ([[commands/vk-auth-validatephone-voice-spam]]):
```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла&voice=1"
```

> The request triggers a voice call to user 66748. Expected output is a successful API response, with the target receiving an incoming call from VK's system.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/vk-auth-validatephone-voice-spam]]

## Tools Used

- None

## Tags

- [[api-vulnerability]]
- [[voice-spam]]
- [[auth-bypass]]
