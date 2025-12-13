---
tags:
  - setup
  - dependencies
type: procedure
tools:
  - '[[tools/bundle]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/bundle-install]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6b95f870-7267-4c21-8068-a622d4b1c5f8
created_at: '2025-12-13T09:01:16.902Z'
updated_at: '2025-12-13T09:01:16.902Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install Dependencies with Bundle

## Summary

This procedure installs the required Ruby gems using Bundler to prepare the environment for running the UJS test server.

## Description

Bundler resolves and installs dependencies specified in the Gemfile, ensuring all necessary components are available for the vulnerable server to run.

## Requirements

1. Inside actionview directory
2. Ruby and Bundler installed

## Defense

Defensive measures and detection strategies:

- Monitor gem installations
- Use dependency scanning for vulnerabilities

## Objectives

1. Install all required gems
2. Prepare for server startup

## Instructions

### Step 1: Run Bundle Install

**Context**: Install gems from Gemfile.

**Command** ([[commands/bundle-install]]):
```bash
bundle install
```

> Lists installed gems upon completion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/bundle-install]]

## Tools Used

- [[tools/bundle]]

## Tags

- setup
- dependencies
