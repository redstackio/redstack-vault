---
tags:
  - automation
  - http-request-smuggling
type: procedure
tools:
  - '[[tools/Burp-Suite-Turbo-Intruder]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1bc82fa3-2d2b-4501-af14-8ec03301630f
created_at: '2025-12-13T09:01:17.624Z'
updated_at: '2025-12-13T09:01:17.624Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load and Run Turbo Intruder Script

## Summary

This procedure loads and executes a script in Burp Suite Turbo Intruder to automate the HTTP Request Smuggling attack.

## Description

The script automates the sending of multiple crafted requests to exploit the vulnerability consistently, using a file like poc.txt or script.txt containing the automation logic for desynchronization.

## Requirements

1. Burp Suite Turbo Intruder
2. Script file (poc.txt or script.txt)
3. Target configured in Burp

## Defense

Defensive measures and detection strategies:

- Rate-limit requests from single sources
- Detect automated traffic patterns

## Objectives

1. Automate smuggling requests
2. Increase exploitation reliability
3. Achieve repeated socket poisoning

## Instructions

### Step 1: Load Script into Turbo Intruder

**Context**: Import the automation script.

In Turbo Intruder, select 'Load script' and choose poc.txt or script.txt.

> This prepares the tool for automated execution.

### Step 2: Execute the Script

**Context**: Run the loaded script against the target.

Click 'Attack' to execute the script, targeting my.stripo.email.

> Expected: Multiple requests sent, exploiting the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite-Turbo-Intruder]]

## Tags

- [[automation]]
- [[http-request-smuggling]]
