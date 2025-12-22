---
tags:
  - phishing
  - verification
  - email
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Email
techniques:
  - '[[T1566.002]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 14c1e76c-5fea-47ec-b67d-5856ae9b8bb2
created_at: '2025-12-14T17:33:24.142Z'
updated_at: '2025-12-14T17:33:24.142Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Send-Invite-and-Verify-Injection

## Summary

This procedure finalizes the attack by sending the tainted invitation email and confirming the HTML injection's success through rendering in the inbox.

## Description

After payload insertion, this triggers the email delivery via Mattermost's system, where the unsanitized HTML is embedded. Verification involves checking the recipient email for active malicious elements, confirming exploitability for phishing. This step realizes the impact, such as luring clicks to attacker-controlled sites.

## Requirements

1. Completed invite form with injected payload
2. Access to the recipient email inbox
3. Email client capable of rendering HTML

## Defense

Defensive measures and detection strategies:

- Strip or escape HTML in outbound emails at the server level
- Use DMARC/SPF/DKIM to prevent spoofing
- Monitor email logs for anomalous content

## Objectives

1. Deliver the injected email successfully
2. Validate rendering of malicious HTML
3. Assess phishing potential

## Instructions

### Step 1: Submit the Invite

**Context**: Send the email to embed the payload.

Click the "Invite" button in the form.

> Invitation processes; email is queued and sent.

### Step 2: Check Recipient Inbox

**Context**: Observe the exploitation in action.

Open the target email account and locate the Mattermost invitation.

> Email displays with rendered `<a href=evil.com>click</a>` as a link and `<input type=x>` as a form element.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[verification]]
- [[email]]
