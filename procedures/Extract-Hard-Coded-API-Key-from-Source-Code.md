---
tags:
  - credential-access
  - source-code
type: procedure
tools:
  - '[[tools/GitHub]]'
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-jumpcloud-systems]]'
  - '[[commands/curl-jumpcloud-systemusers]]'
  - '[[commands/curl-jumpcloud-applications]]'
platforms:
  - Web
techniques:
  - '[[Credentials in Files]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3a1aa3a5-966d-4deb-ad93-df03a57638b4
created_at: '2025-12-11T06:10:28.764Z'
updated_at: '2025-12-11T06:10:28.764Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552.001]]'
---
# Extract Hard-Coded API Key from Source Code

## Summary

This procedure extracts hard-coded credentials, such as API keys, from publicly accessible source code files in repositories.

## Description

After identifying a relevant file, the attacker manually reviews the code to find lines where credentials are directly embedded, such as in HTTP headers. This targets Go source files in this case, but applies to any language. No tools are needed beyond viewing the file, and it enables credential access for further attacks.

## Requirements

1. Access to the identified repository file
2. Basic code reading skills
3. No special permissions required

## Defense

Defensive measures and detection strategies:

- Avoid hard-coding secrets; use environment variables or secret managers
- Implement code review processes to catch leaks
- Use automated tools to detect secrets in code

## Objectives

1. Obtain the exact credential value
2. Confirm it's usable (not expired or revoked)
3. Prepare for exploitation

## Instructions

### Step 1: Review Source Code

**Context**: Open and inspect the file for credential patterns.

In getSystemUsers.go, locate the line: req.Header.Add("x-api-key", "████████").

> This directly reveals the key without obfuscation.

### Step 2: Copy the Key

**Context**: Extract the value for use.

Copy the string "████████" from the header addition line.

> Store it securely for testing in the next phase.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credentials in Files]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitHub]]

## Tags

- [[credential-access]]
- [[source-code]]
