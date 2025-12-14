---
id: proc-uuid-3
tags:
  - xss
  - propagation
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Slack Apps
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.613Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Malicious-Slack-App-Link

## Summary

This procedure involves distributing the compromised app link to victims, leveraging Slack's sharing features to trigger XSS execution in their browsers for broader impact.

## Description

The malicious URL, when shared within or outside the workspace, directs victims to the tainted app page. Upon clicking, the stored payload executes, enabling attacks like keylogging or credential theft in the trusted Slack domain. This amplifies the stored XSS into a phishing-like vector.

## Requirements

1. Valid malicious app URL from prior steps
2. Access to communication channels (e.g., Slack DMs, email)
3. Social engineering knowledge to entice clicks

## Defense

Defensive measures and detection strategies:

- Educate users on verifying links before clicking
- Implement URL scanning in Slack integrations
- Revoke suspicious app permissions promptly

## Objectives

1. Propagate the exploit to multiple victims
2. Achieve remote code execution without direct access
3. Facilitate data exfiltration or account takeover

## Instructions

### Step 1: Copy the Malicious URL

**Context**: Prepare the shareable link post-verification.

Copy the full URL: https://[workspace].slack.com/apps/[appid]--[payload].

> Ensure the payload is URL-safe; encode if necessary.

### Step 2: Distribute to Victims

**Context**: Send the link via trusted channels to maximize click-through.

Paste the URL into a Slack message, email, or chat, e.g., "Check out this new app: [malicious URL]".

> Victims clicking it will execute the payload in their session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Phishing]]
- [[propagation]]
