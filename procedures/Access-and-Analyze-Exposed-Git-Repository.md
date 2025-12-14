---
tags:
  - git-exposure
  - credential-leak
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
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:58.004Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 46f96ba6-520e-4437-94b4-6c44e22ef54e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Access and Analyze Exposed Git Repository

## Summary

Extract sensitive data from an exposed .git directory, including credentials from log files.

## Description

Exposed Git repos often leak configs and logs. Clone from https://github.com/bounty-pay-code/request-logger.git, access bp_web_trace.log, base64-decode to get username brian.oliver, password V7h0inzX, challenge_answer bD83Jk27dQ.

## Requirements

1. Access to exposed .git/config
2. Git client for cloning
3. Base64 decoder (browser or tool)

## Defense

Defensive measures: Remove .git from production servers, use .gitignore for secrets; Detection: Scan for exposed repos with tools like git-dumper.

## Objectives

1. Clone and inspect repo
2. Decode logs for creds
3. Expected outcome: Valid login details

## Instructions

### Step 1: Clone Repository

**Context**: Retrieve full Git history.

Use git clone https://github.com/bounty-pay-code/request-logger.git (inferred from config).

> Expected output: Local repo with PHP logger.

### Step 2: Decode Log File

**Context**: Extract plaintext credentials.

Access https://app.bountypay.h1ctf.com/bp_web_trace.log, base64 decode content.

> Expected output: Credentials revealed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- git-exposure
- credential-leak
