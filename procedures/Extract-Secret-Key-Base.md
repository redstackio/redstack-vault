---
tags:
  - gitlab
  - secret-extraction
type: procedure
tools:
  - '[[tools/Rails-Console]]'
  - '[[tools/curl]]'
  - '[[tools/cat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/rails-request-setup]]'
  - '[[commands/rails-set-serializer]]'
  - '[[commands/rails-cookie-jar]]'
  - '[[commands/rails-erb-payload]]'
  - '[[commands/rails-deprecated-proxy]]'
  - '[[commands/rails-set-signed-cookie]]'
  - '[[commands/rails-print-cookie]]'
  - '[[commands/curl-send-malicious-cookie]]'
  - '[[commands/cat-verify-file]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ba6a8950-3855-4b68-8f1d-743e7435966f
created_at: '2025-12-11T06:10:40.437Z'
updated_at: '2025-12-11T06:10:40.437Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1550]]'
---
# Extract Secret Key Base

## Summary

Use the file read vulnerability to retrieve the secret_key_base from secrets.yml.

## Description

Target the file /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml using the traversal method to obtain keys for signing malicious payloads.

## Requirements

1. Successful file read setup
2. Knowledge of secrets.yml path

## Defense

Defensive measures and detection strategies:

- Restrict file system access
- Encrypt sensitive configurations

## Objectives

1. Obtain secret_key_base
2. Prepare for RCE escalation

## Instructions

### Step 1: Target Secrets File

**Context**: Adjust the traversal payload to reference secrets.yml and move the issue.

Access the copied file in the new project.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- gitlab
- secret-extraction
