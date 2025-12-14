---
tags:
  - setup
  - test-environment
  - web
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.810Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: aa689a81-8215-4c70-90b1-6328dca60200
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Test-Applications-and-Users-in-Fabric-io

## Summary

This procedure establishes a controlled test environment in Fabric.io by creating multiple applications and users with varying roles to simulate attacker and victim scenarios for testing authorization bypasses.

## Description

In the context of exploiting Fabric.io's authorization vulnerabilities, this setup involves logging into the platform, creating two distinct applications (VictimApp and HackerApp), and assigning admin and member roles to users. IDs for apps and accounts are retrieved from the dashboard to enable precise parameter targeting in subsequent HTTP requests. This prepares the environment without triggering alerts, as it uses legitimate creation flows.

## Requirements

1. Valid Fabric.io account with admin privileges
2. Web browser access to fabric.io
3. Ability to create new applications (no special permissions beyond basic signup)

## Defense

Defensive measures and detection strategies:

- Monitor for rapid creation of multiple test apps from single IP
- Implement rate limiting on app/user creation endpoints
- Log all app and user ID retrievals for anomaly detection

## Objectives

1. Simulate isolated victim and attacker app environments
2. Gather necessary IDs for request tampering
3. Ensure no cross-contamination in test data

## Instructions

### Step 1: Create VictimApp and Users

**Context**: Establish the target application and its legitimate users to later verify unauthorized deletions.

Log in to Fabric.io, navigate to dashboard > New App, create "VictimApp". Add users: Alice as admin and Alice as member (note distinct account IDs).

**Expected Output**: VictimApp ID (e.g., 54ad5e03a25bb8136b000002), Aliceadmin ID (54aa4c616bb166b8f300134a), Alicemember ID (54af48304d8f5b12ff0000fd).

### Step 2: Create HackerApp and Users

**Context**: Set up the attacker's controlled app for generating legitimate requests to intercept.

Repeat creation for "HackerApp". Add Hacker as admin and Hacker as member.

**Expected Output**: HackerApp ID (e.g., 54aeafc28bfc55053d000028), relevant account IDs noted.

### Step 3: Retrieve and Document IDs

**Context**: Collect all identifiers from app settings pages for use in request modification.

Navigate to each app's settings > Team to view and copy IDs.

**Expected Output**: Documented list of app_id and account_id pairs.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- setup
- test-environment
- web
