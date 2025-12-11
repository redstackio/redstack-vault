---
tags:
  - reconnaissance
  - github-enterprise
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f4e8633c-09e3-4d42-ab45-acb09cc45c78
created_at: '2025-12-11T03:47:39.291Z'
updated_at: '2025-12-11T03:47:39.291Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Identify Vulnerable GitHub Enterprise Server Instance

## Summary

This procedure involves reconnaissance to identify if a target GitHub Enterprise Server is running a vulnerable version prior to 3.5 and confirm the presence of an active management console with a logged-in user.

## Description

The attack begins with scanning for GitHub Enterprise Server instances and checking their versions against known vulnerable releases. This sets the stage for exploiting the path traversal vulnerability in the management console, which requires targeting an active logged-in session. Expected outcomes include confirmation of vulnerability and endpoint accessibility.

## Requirements

1. Network access to the target server
2. Tools for version fingerprinting (e.g., web browser or HTTP client)
3. Knowledge of GitHub Enterprise Server endpoints

## Defense

Defensive measures and detection strategies:

- Regularly update GitHub Enterprise Server to patched versions
- Monitor access logs for unusual reconnaissance attempts on management console

## Objectives

1. Confirm vulnerable version
2. Identify active management console
3. Prepare for exploitation

## Instructions

### Step 1: Version Fingerprinting

**Context**: Access the target server and retrieve version information from exposed endpoints or headers.

Navigate to the management console URL and inspect responses for version details.

### Step 2: Confirm Logged-in User

**Context**: Verify an active session exists by observing traffic or known user activity.

Monitor for indicators of logged-in sessions without direct interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Reconnaissance]]
- #github-enterprise
