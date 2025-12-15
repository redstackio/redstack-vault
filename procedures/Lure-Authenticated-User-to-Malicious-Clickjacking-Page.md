---
id: proc-tiktok-lure-user-001
tags:
  - phishing
  - social-engineering
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.247Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure-Authenticated-User-to-Malicious-Clickjacking-Page

## Summary

This procedure focuses on socially engineering an authenticated TikTok Ads user to visit the clickjacking page, resulting in unintended interactions that perform actions like creating or deleting campaigns.

## Description

The final stage involves distributing the malicious page URL to targets who are logged into TikTok Ads. Methods include phishing links disguised as promotions or ads. Once visited, the invisible iframe captures clicks, exploiting the victim's session. This leads to account disruption and requires no further technical exploits beyond hosting. Outcomes include unauthorized campaign modifications, reported as low severity in the original disclosure.

## Requirements

1. Hosted malicious page from prior procedure.
2. List of target users (e.g., via social media scraping).
3. Phishing delivery channels (email, DMs).

## Defense

Defensive measures and detection strategies:

- User training on suspicious links and verifying URLs.
- Monitor Ads logs for anomalous actions (e.g., bulk creations/deletions).
- Implement session checks for unexpected UI interactions.

## Objectives

1. Induce visit from an authenticated user.
2. Capture clicks leading to unauthorized actions.
3. Confirm impact via follow-up verification.

## Instructions

### Step 1: Craft Luring Message

**Context**: Create enticing content to direct users to the malicious page.

Draft a phishing email or post: "Click here to claim your free TikTok ad credits: [MALICIOUS_URL]". Ensure the page mimics a legitimate offer to encourage interaction.

> No command; focus on persuasive language targeting Ads users.

### Step 2: Distribute and Monitor

**Context**: Send to targets and observe results.

Distribute via email lists or social platforms. If possible, add JavaScript to log visits/clicks:

```javascript
window.onload = function() { console.log('User visited'); };
document.querySelector('button').addEventListener('click', function() { fetch('/log?clicked=true'); });
```

Check server logs or victim's account for changes.

> Expected output: Logs show visit and click; victim's dashboard shows new/deleted campaigns.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[clickjacking]]
- [[tiktok]]
