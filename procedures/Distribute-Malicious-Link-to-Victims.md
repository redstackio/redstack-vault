---
id: proc-uuid-2
tags:
  - social-engineering
  - phishing
  - web
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
  - '[[User Execution]]'
updated_at: '2025-12-14T17:27:50.454Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Distribute-Malicious-Link-to-Victims

## Summary

This procedure covers sharing the crafted CSRF link with targeted LinkedIn users to induce clicks, resulting in automatic connection invitations from their accounts to the attacker.

## Description

Once the malicious link is ready, the attacker distributes it through channels like email or messaging, often disguised as a professional recommendation or shared resource. The link exploits the victim's authenticated session on LinkedIn, executing the CSRF request upon click without prompts. This leads to spam, unwanted connections, and potential further social engineering. The attack relies on user trust and requires no additional technical access beyond communication.

## Requirements

1. Crafted CSRF link from prior procedure
2. Contact method with victim (e.g., email address, DM platform)
3. Social engineering pretext to encourage clicking

## Defense

Defensive measures and detection strategies:

- Educate users on verifying links before clicking, especially unsolicited ones
- Implement URL scanning in email gateways for suspicious patterns (e.g., LinkedIn endpoints with odd parameters)
- Rate-limit invitation sends per user/session
- Log and alert on cross-origin requests to sensitive endpoints

## Objectives

1. Deliver the link to authenticated victims
2. Trick victims into executing the CSRF via click
3. Receive unsolicited connection requests for network expansion

## Instructions

### Step 1: Prepare Distribution Channel

**Context**: Select and set up a method to send the link, ensuring it's clickable and contextually relevant.

Choose email or messaging; craft a message like "Check out this LinkedIn recommendation: [link]".

> Expected: Message ready for sending without raising suspicion.

### Step 2: Send Link to Victim

**Context**: Transmit the link to the target, timing it when the victim is likely authenticated on LinkedIn.

Send via chosen channel; e.g., email with subject "People You May Know on LinkedIn".

> Expected: Victim receives and potentially clicks the link.

### Step 3: Monitor for Success

**Context**: Check attacker's LinkedIn for incoming invitations from the victim.

Log into attacker's account and review 'Invitations' section.

> Expected: New connection request from victim's profile, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[user-execution]]
