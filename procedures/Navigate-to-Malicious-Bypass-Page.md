---
tags:
  - web
  - origin-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postmessage-send-fake-signin]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9224409c-8713-4689-90c1-4577bc646d78
created_at: '2025-12-11T06:10:28.579Z'
updated_at: '2025-12-11T06:10:28.579Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Navigate to Malicious Bypass Page

## Summary

This procedure directs the victim to a malicious page hosted on a domain that bypasses the Digits SDK origin validation due to regex flaws.

## Description

By using a domain like 'www.d.gits.co', the String.prototype.search() method treats the dot as a wildcard, allowing the malicious page to communicate via postMessage.

## Requirements

1. Control over a bypassing domain (e.g., www.d.gits.co)
2. Hosted HTML page with exploit code
3. Victim's browser with active session

## Defense

Defensive measures and detection strategies:

- Use strict string matching instead of regex for origins
- Monitor cross-origin messages

## Objectives

1. Load malicious page in context of victim's session
2. Prepare for postMessage injection
3. Bypass origin checks

## Instructions

### Step 1: Host Malicious Page

**Context**: Set up the page on the bypassing domain.

Create and host fabric.html with JavaScript for postMessage.

> Ensure the domain matches the regex pattern flaw.

### Step 2: Direct Victim to Page

**Context**: Trick the victim into visiting the page.

Provide link: https://www.d.gits.co/fabric.html

> Expected: Page loads and is ready for interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web
- origin-bypass
