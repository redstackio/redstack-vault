---
tags:
  - token-leak
  - github
  - discovery
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python-import-os]]'
  - '[[commands/python-import-requests]]'
  - '[[commands/python-import-sys]]'
  - '[[commands/python-set-pull-number]]'
  - '[[commands/python-construct-pull-url]]'
  - '[[commands/python-initialize-payload]]'
  - '[[commands/python-add-authorization-header]]'
  - '[[commands/python-print-payload]]'
  - '[[commands/python-requests-get]]'
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b2867429-2920-4c83-9962-7f9739bd7e57
created_at: '2025-12-11T06:10:28.338Z'
updated_at: '2025-12-11T06:10:28.338Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Discover Public Repository with Leaked Token

## Summary

This procedure involves searching for and accessing public GitHub repositories that contain sensitive information, such as hardcoded API tokens, by browsing publicly available code files.

## Description

In this attack scenario, an attacker discovers a public GitHub repository where a developer has committed a Python script with a hardcoded GitHub API token for an internal enterprise instance. The procedure focuses on initial discovery without any tools beyond a web browser, targeting web-based platforms like GitHub. Expected outcomes include identifying the exact file and location of the leaked token.

## Requirements

1. Internet access to public GitHub repositories
2. Web browser for viewing code
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Implement secrets scanning in CI/CD pipelines to detect hardcoded tokens
- Use GitHub's secret scanning alerts for repositories

## Objectives

1. Locate public repositories with sensitive code
2. Identify hardcoded credentials
3. Prepare for token extraction

## Instructions

### Step 1: Access Public Repository

**Context**: Navigate to the known public GitHub repository URL to view the sensitive file.

Use a web browser like [[tools/Firefox]] to access https://github.com/█████/leetcode/blob/0eec6434940a01e490d5eecea9baf4778836c54e/TopicMatch.py.

> This step allows viewing the Python script containing the leaked token.

### Step 2: Scan for Sensitive Information

**Context**: Manually review the code for hardcoded tokens or credentials.

Inspect the file contents for strings like 'Authorization' or 'token'.

> Expected to find the token '9db9ca3440e535d90408a32a9c03d415979da910' in the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]

## Tags

- token-leak
- github
- discovery
