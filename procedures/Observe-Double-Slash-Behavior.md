---
id: proc-observe-double-slash-behavior
tags:
  - double-slash
  - url-parsing
  - bypass
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.330Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Double Slash Behavior

## Summary

This procedure tests URL parsing inconsistencies on hackerone.com using double slashes (//) in the path, comparing valid and invalid domains to reveal access differences that hint at broader redirect vulnerabilities.

## Description

Double slashes can confuse server parsers, leading to varied behaviors: valid domains like //hackerone.com may resolve normally, while invalid ones like //hackerone1.com fail or trigger security measures. This step explores these anomalies in a web environment, requiring only browser access, and sets up for deeper exploitation like redirects. Outcomes include observed parsing flaws exploitable for evasion.

## Requirements

1. Web browser for testing
2. Access to hackerone.com
3. Ability to note loading differences

## Defense

Defensive measures and detection strategies:

- Normalize URLs to remove redundant slashes before processing
- Log and alert on double-slash patterns in requests
- Enforce strict path validation in web servers

## Objectives

1. Identify parsing inconsistencies with double slashes
2. Differentiate valid vs. invalid domain handling
3. Inform subsequent redirect bypass techniques

## Instructions

### Step 1: Test Valid Double Slash URL

**Context**: Access a URL with double slashes pointing to a valid domain to establish baseline behavior.

Navigate to: `https://hackerone.com//hackerone.com`

> The server treats this as a normal request, loading the site. Expected output: Page loads successfully, confirming no immediate block on double slashes.

### Step 2: Test Invalid Double Slash URL

**Context**: Compare with an invalid domain to observe failure modes.

Navigate to: `https://hackerone.com//hackerone1.com`

> Invalid domains do not load or trigger errors, highlighting selective parsing. Expected output: Access denied or error page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- double-slash
- url-parsing
