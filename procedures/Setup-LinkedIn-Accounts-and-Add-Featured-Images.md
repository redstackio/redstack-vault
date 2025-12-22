---
id: proc-setup-linkedin-accounts
tags:
  - setup
  - linkedin
  - account-creation
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:47.469Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Setup-LinkedIn-Accounts-and-Add-Featured-Images

## Summary

This procedure prepares the attack environment by creating attacker and victim LinkedIn accounts and adding featured images to both, simulating a realistic scenario for IDOR exploitation testing.

## Description

In the context of testing LinkedIn's IDOR vulnerability, this step involves registering two accounts to represent the attacker and victim. Featured images are then uploaded to ensure the target functionality (deletion API) is active. This setup requires no special privileges and uses standard LinkedIn registration and profile editing features. Expected outcomes include verifiable images on both profiles, setting the stage for request capture and modification.

## Requirements

1. Access to email addresses for account registration
2. Standard web browser
3. Internet connection to LinkedIn

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on registration to deter automation

## Objectives

1. Establish controlled attacker and victim environments
2. Populate profiles with testable featured media
3. Ensure API endpoints are accessible for subsequent steps

## Instructions

### Step 1: Create Accounts

**Context**: Register separate accounts to isolate attacker and victim actions.

Navigate to linkedin.com and complete the registration process for two accounts using different email addresses.

### Step 2: Add Featured Images

**Context**: Upload images to the featured section of each profile to enable deletion testing.

Log in to each account, go to Profile > Add Profile Section > Recommended > Add Featured, and upload an image file (e.g., JPG under 5MB).

**Expected Output**: Image appears in the Featured section upon profile refresh.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[linkedin]]
- [[account-creation]]
