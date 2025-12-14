---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - social-engineering
  - phishing
  - team-invite
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T03:15:47.355Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Demonstrate-Social-Engineering-Attack-Scenario

## Summary

This procedure outlines a social engineering attack using HackerOne's team features to trick a victim into clicking a crafted link, exploiting window.opener for potential DOM manipulation.

## Description

Invite a victim to a controlled team, tamper with a URL to a sensitive endpoint like /triggers, and embed it in a report to lure clicks. The default target='_blank' without rel='noopener' allows the attacker's page to access the opener window. Targets HackerOne's collaboration tools; outcomes include simulated access to victim sessions, though limited by trust relationships.

## Requirements

1. HackerOne account with team creation/invite permissions
2. Test victim account or simulated environment
3. Crafted malicious URL (e.g., javascript: payload in context)

## Defense

Defensive measures and detection strategies:

- Require approval for team invites and link sharing
- Disable or warn on target='_blank' links in user content
- Monitor for suspicious team activities and URL tampering

## Objectives

1. Gain victim interaction via team invite
2. Trick click on exploitable link
3. Achieve window.opener access for manipulation

## Instructions

### Step 1: Invite Victim to Team

**Context**: Establish a trust relationship to deliver the malicious link.

Use HackerOne's team invite feature to add the victim, providing a pretext like 'Review this report'.

> Expected output: Victim joins the team and accesses shared content.

### Step 2: Craft and Embed Malicious Link

**Context**: Tamper with a URL to point to an attacker-controlled or sensitive endpoint.

In a report, embed: [Click for details](https://hackerone.com/<program-handle>/triggers?malicious-param)

> The link opens in new tab; attacker page can then script: window.opener.document.body.innerHTML = 'hacked'; to manipulate DOM.

### Step 3: Lure and Exploit

**Context**: Trick the victim into clicking and verify exploitation.

Send notification or message urging click; monitor for opener access.

> Expected output: Successful DOM alteration if victim clicks from opener context.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
- [[team-invite]]
