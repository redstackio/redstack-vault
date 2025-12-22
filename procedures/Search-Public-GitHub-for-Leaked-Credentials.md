---
tags:
  - reconnaissance
  - github
  - credential-leak
type: procedure
tools:
  - '[[tools/GitHub]]'
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-jumpcloud-systems]]'
  - '[[commands/curl-jumpcloud-systemusers]]'
  - '[[commands/curl-jumpcloud-applications]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3bb32ce5-4eb1-47aa-882b-9ea12b3f6cb8
created_at: '2025-12-11T06:10:28.768Z'
updated_at: '2025-12-11T06:10:28.768Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1595]]'
---
# Search Public GitHub for Leaked Credentials

## Summary

This procedure involves searching public GitHub repositories to discover leaked sensitive information, such as API keys, in source code files related to a target organization.

## Description

In this attack scenario, an attacker uses GitHub's search functionality to find public repositories associated with the target (e.g., Starbucks). The goal is to identify files containing hard-coded credentials without any access controls. This is a reconnaissance step that can lead to initial access if credentials are found. The procedure targets web-based platforms and requires no special tools beyond a web browser.

## Requirements

1. Internet access to GitHub
2. Knowledge of target-related keywords (e.g., organization name, service like JumpCloud)
3. No authentication required for public searches

## Defense

Defensive measures and detection strategies:

- Regularly scan and remove sensitive data from public repositories
- Use secret scanning tools like GitHub's built-in scanner
- Monitor for unusual repository access or searches

## Objectives

1. Identify public repositories with potential leaks
2. Locate specific files containing credentials
3. Enable further exploitation steps

## Instructions

### Step 1: Perform GitHub Search

**Context**: Use GitHub's search bar to query for repositories related to the target.

Navigate to https://github.com and search for "Starbucks JumpCloud" or similar terms to find the repository at https://github.com/██████████/Project.

> This reveals public repos without authentication.

### Step 2: Inspect Repository Files

**Context**: Browse the repository to find source files.

Open the file getSystemUsers.go in the identified repository.

> Look for code snippets that might contain hard-coded values.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitHub]]

## Tags

- [[Reconnaissance]]
- [[tools/GitHub]]
