---
id: proc-003
tags:
  - phishing
  - email-observation
  - link-hijacking
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T03:16:08.389Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Observe-Email-Notification-Redirection

## Summary

This procedure involves monitoring the recipient's email for the notification and verifying how the injected HTML alters links, confirming the second-order XSS exploitation.

## Description

After payload injection, the chat system sends an automated email notification from the official server, including the unsanitized message. The base href tag causes relative links (e.g., 'new message' button) to resolve to the attacker's domain, appending parameters like sysparm_channelID. This step uses a test recipient account to observe the effect in an email client, potentially a webmail interface where further XSS could execute. The scenario assumes the platform is ServiceNow-based; outcomes validate phishing potential without alerting the target.

## Requirements

1. Access to the recipient's email account (use a secondary test account)
2. Email client (e.g., Gmail web interface) to view HTML rendering
3. Knowledge of the expected channelID from the chat URL

## Defense

Defensive measures and detection strategies:

- Render email content through a secure proxy that strips dangerous HTML elements
- Implement email link validation to block external redirections
- Monitor email server logs for anomalous link patterns in notifications

## Objectives

1. Receive and inspect the notification email
2. Confirm link alteration to attacker domain
3. Assess potential for victim interaction (e.g., clickjacking)

## Instructions

### Step 1: Check Recipient Email Inbox

**Context**: Wait for the automated notification triggered by the new message.

No command required; manual check:

- Log into the recipient's email (e.g., via webmail).
- Refresh inbox and locate the 'New Message' notification from Air University Service Desk.

> Email arrives within seconds to minutes; subject includes chat details.

### Step 2: Inspect Link in Email

**Context**: Examine the HTML source or hover over links to verify redirection.

No command required; use browser dev tools:

- Open the email in a web client.
- Right-click the 'View Message' link and inspect element.
- Look for href like `https://un4.gi/███████sysparm_channelID=████`.

> Link src modified by base href; test hover shows attacker domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection (gathering victim clicks via phishing)

### Techniques

- [[T1566.001]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[email]]
