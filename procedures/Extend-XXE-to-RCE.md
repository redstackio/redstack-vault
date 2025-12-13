---
tags:
  - xxe
  - rce
type: procedure
tools:
  - '[[tools/viewgen]]'
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 7bb87dec-67a9-47ff-ba84-e099fdac0678
created_at: '2025-12-13T09:00:27.853Z'
updated_at: '2025-12-13T09:00:27.853Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Extend XXE to RCE

## Summary

This procedure extends XXE exploitation to read sensitive configuration files like web.config and uses tools to generate viewstate for achieving remote code execution.

## Description

After reading web.config via XXE, tools like viewgen can generate valid viewstates, potentially allowing code execution in ASP.NET applications.

## Requirements

1. Successful XXE file read access
2. viewgen tool installed
3. Extracted web.config contents

## Defense

Defensive measures and detection strategies:

- Secure configuration files from read access
- Implement viewstate validation and MAC checks
- Monitor for file access anomalies and RCE attempts

## Objectives

1. Read sensitive configs
2. Generate viewstate for RCE
3. Achieve code execution

## Instructions

### Step 1: Target Sensitive Files

**Context**: Modify XXE payload to read web.config.

Adjust the entity in the XML to reference web.config paths.

### Step 2: Generate Viewstate

**Context**: Use viewgen with extracted data.

Install and run viewgen on the web.config output to create a malicious viewstate.

> Leverage the tool to craft payloads for RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/viewgen]]

## Tags

- xxe
- rce
