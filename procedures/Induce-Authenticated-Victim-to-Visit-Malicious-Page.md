---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
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
updated_at: '2025-12-14T17:27:57.643Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Authenticated-Victim-to-Visit-Malicious-Page

## Summary

This procedure uses social engineering to lure an authenticated GitLab user to visit the malicious HTML page, triggering the CSRF exploit and executing the GraphQL mutation without their knowledge.

## Description

Once the malicious HTML is hosted, this step involves delivering the URL to the victim via phishing (e.g., email, chat) while they are logged into GitLab. The page loads innocuously but auto-submits the GET request, leveraging the victim's session cookies to perform the mutation. Target environment is any browser with an active GitLab session; outcomes include unauthorized actions like snippet creation, with potential for escalation to other mutations.

## Requirements

1. Hosted malicious HTML URL
2. Contact method with victim (email, Slack, etc.)
3. Victim actively logged into GitLab

## Defense

Defensive measures and detection strategies:

- Train users to verify links before clicking
- Use URL scanners or blocklists for suspicious domains
- Implement browser extensions for CSRF protection (e.g., NoScript)
- Log and alert on unexpected GraphQL calls

## Objectives

1. Ensure victim session is active during visit
2. Deliver payload via deceptive means
3. Achieve silent request submission

## Instructions

### Step 1: Prepare Phishing Delivery

**Context**: Craft a convincing message to trick the victim into clicking the link.

No command; example email: "Check out this interesting GitLab tip: https://attacker.github.io/csrf-exploit/"

> Disguise as a legitimate resource to lower suspicion.

### Step 2: Send and Monitor

**Context**: Deliver the link and wait for the victim to visit while authenticated.

No command; send via preferred channel.

**Expected Output**: Victim loads the page, form submits GET to GitLab API.

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
- [[drive-by]]
