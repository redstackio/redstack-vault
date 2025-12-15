---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/showReviewModal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.274Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Exfiltrate-Internal-URL-via-Agent-Review

## Summary

This procedure escalates self-XSS in the support portal by triggering an agent review modal, executing the payload on the agent's browser to exfiltrate their internal URL and user agent.

## Description

After CSP bypass, running showReviewModal() in the console opens a rating modal. Submitting a low rating prompts the agent to review chat logs, where the injected script executes client-side on their machine. The script beacons the agent's location.href (e.g., https://localhost:3000/support/review/...) and user agent (revealing headless Chrome) to an attacker-controlled server via img src. This discloses internal infrastructure details for further exploitation.

## Requirements

1. Self-XSS payload already injected in portal
2. Access to browser console
3. Attacker server (e.g., http://evil/image.png) for exfiltration

## Defense

Defensive measures and detection strategies:

- Sanitize chat content before agent rendering
- Implement client-side CSP enforcement on agent tools
- Monitor for anomalous img requests or beaconing from internal IPs
- Use isolated environments for agent reviews

## Objectives

1. Trigger agent interaction to execute XSS
2. Exfiltrate internal URLs and browser details
3. Identify internal ports/services

## Instructions

### Step 1: Trigger Review Modal

**Context**: Open modal to prompt agent review.

Execute [[commands/showReviewModal]] in console:

```javascript
showReviewModal();
```

> Modal opens for rating. Expected output: UI prompt for 1-5 stars.

### Step 2: Submit Rating to Escalate

**Context**: Force agent to load vulnerable chat.

Give 1-star rating and submit.

> Agent reviews logs, executing XSS. Expected output: Exfiltration hit on attacker server.

### Step 3: Receive Exfiltrated Data

**Context**: Analyze beaconed information.

Check server logs for ?loc= parameter with internal URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/showReviewModal]]

## Tools Used


## Tags

- xss
- information-disclosure
