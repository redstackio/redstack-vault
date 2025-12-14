---
tags:
  - login
  - authentication
  - mavenlink
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.697Z'
sub_techniques: []
id: 0c2463e2-c908-42a9-a3e3-53d37ad7600b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Login-to-Mavenlink-with-Multiple-Users

## Summary

Authenticates two distinct users into Mavenlink via separate browser sessions to prepare for project-based privilege testing.

## Description

Logging in establishes authenticated sessions necessary for accessing project management features. This step ensures User A can manage projects and User B can interact with them, setting the stage for escalation. The web interface at https://app.mavenlink.com uses standard form-based login; no advanced auth like MFA is assumed here. Outcome: Active sessions for both users on the dashboard.

## Requirements

1. User A and B credentials (email/password)
2. Isolated browsers as prepared in prior step
3. Access to Mavenlink without IP blocks

## Defense

Defensive measures and detection strategies:

- Enforce MFA for logins
- Monitor login patterns for anomalies from multiple IPs
- Rate-limit login attempts

## Objectives

1. Gain authenticated access for admin and target user
2. Verify session establishment
3. Position for project creation

## Instructions

### Step 1: Navigate and Authenticate User A

**Context**: Secure admin access in primary session.

In Browser X, go to https://app.mavenlink.com, enter User A's credentials, and submit the login form.

### Step 2: Authenticate User B

**Context**: Establish target user session.

In Browser Y, repeat the process with User B's credentials to reach the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[authentication]]
- [[mavenlink]]
