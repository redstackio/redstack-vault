---
id: p4d5e6f7-h8i9-0123-defg-456789012345
tags:
  - csrf
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-update-security-questions]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:24.303Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-CSFR-Attack-on-Victim

## Summary

This procedure describes how the victim's browser, while authenticated, automatically submits the forged CSRF form to alter their security questions to attacker-known values.

## Description

Upon visiting the hosted PoC, the victim's browser executes the JavaScript to POST to the target's endpoint using their session cookies, bypassing any visual confirmation due to auto-submit. This changes answers to 'hacked' etc., without alerting the user.

## Requirements

1. Victim authenticated to target site
2. No browser blocking cross-site POSTs
3. Hosted PoC accessible

## Defense

Defensive measures and detection strategies:

- Implement strict CSP and referrer checks
- Alert on rapid security question changes
- Monitor for cross-origin requests in app logs

## Objectives

1. Successfully overwrite victim's security data
2. Maintain stealth during submission
3. Verify change indirectly via reset attempt

## Instructions

### Step 1: Victim Loads PoC Page

**Context**: The link leads to form auto-submission.

**Instructions**: Victim clicks URL; JavaScript triggers POST.

> Expected output: Silent form submission to target.

### Step 2: Verify Exploitation (Attacker Side)

**Context**: Optional probe to confirm change.

**Command** ([[commands/curl-update-security-questions]]):
```bash
curl -X POST https://www.█████████/member/updatesecurityquestions \
  -H "Cookie: {VICTIM-COOKIE}" \
  -d "security_questions1=1&security_question_answer1=hacked&...&submit=Save"
```

> If accessible, confirms update; otherwise, infer from reset success. Expected output: 200 OK.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-update-security-questions]]

## Tools Used

- None

## Tags

- csrf
- drive-by
