---
id: deliver-phishing-link-csrf
tags:
  - phishing
  - social-engineering
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
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:33:06.538Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Deliver Phishing Link for CSRF

## Summary

This procedure involves sending a deceptive link to the victim that leads to the malicious CSRF webpage, tricking them into executing the email change while authenticated in IRCCloud.

## Description

Social engineering is used to lure the victim to the attacker's hosted page, disguised as innocuous content (e.g., a video or article). When clicked, the page triggers the CSRF form submission using the victim's browser session. This relies on the victim being logged into IRCCloud at the time of visit. No technical exploits beyond the link delivery are needed, but effectiveness depends on trust-building via email, chat, or IRC.

## Requirements

1. Valid link to the hosted CSRF page
2. Communication channel with victim (email, IRC, social media)
3. Plausible pretext to encourage clicking

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks and link verification
- Implement browser extensions for CSRF protection (e.g., NoScript)
- Monitor login sessions for unusual activity post-click
- Use email filters to block suspicious links

## Objectives

1. Induce victim to visit malicious site while logged in
2. Ensure click occurs during active IRCCloud session
3. Maintain deception to avoid suspicion

## Instructions

### Step 1: Craft Deceptive Message

**Context**: Create a convincing lure to prompt the victim to click the link.

**Instructions**: Compose a message like "Hey, check out this hilarious cat video: http://example.com/cat.html". Send via email, IRC, or other channels where the victim is active.

**Expected Output**: Victim receives and interacts with the message.

### Step 2: Monitor for Visit

**Context**: Track if the victim accesses the page to confirm trigger.

**Instructions**: Use server logs on the hosting site to detect visits from the victim's IP or user-agent.

**Expected Output**: Log entry showing page load and form submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Malicious File]] User Execution: Malicious Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
