---
tags:
  - account-takeover
  - data-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.124Z'
sub_techniques: []
id: e3c3b808-425f-4540-b396-4612ef1d1550
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Access Victim Profile

## Summary

This procedure leverages the forged session to navigate to and view the victim's personal profile, confirming full account takeover and enabling data exfiltration.

## Description

With the session active as the victim, the application treats the attacker as authenticated, allowing access to user-specific pages. This exploits the cookie's direct role in security decisions, exposing profile data in the DoD system.

## Requirements

1. Active impersonated session
2. UI elements visible (e.g., dropdown menu)
3. No additional auth barriers

## Defense

Defensive measures and detection strategies:

- Role-based access controls beyond session cookies
- Audit logs for profile access with anomaly detection
- Multi-factor authentication for sensitive actions

## Objectives

1. Load victim profile
2. View personal information
3. Demonstrate takeover impact

## Instructions

### Step 1: Open User Dropdown

**Context**: Access profile navigation.

Click the top-right corner dropdown menu, which now displays 'Welcome [Victim's Name]'.

**Expected Output**: Dropdown expands with options like 'My Profile'.

### Step 2: Select and Load Profile

**Context**: Retrieve user data.

Click 'My Profile' to navigate to the profile page.

**Expected Output**: Profile page loads, showing victim's details such as name, ID, and personal info.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[data-access]]
