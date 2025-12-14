---
id: proc-uuid-002
tags:
  - pii-exposure
  - data-collection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.495Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-User-Profile-PII

## Summary

After authentication bypass, this procedure retrieves sensitive PII from the compromised user's profile, such as phone numbers and personal details.

## Description

With an active session from the bypassed login, the attacker navigates to the profile section where data is displayed without access controls. This exposes PII directly in the browser, allowing collection for further attacks like social engineering. The root cause is insufficient authorization checks post-login.

## Requirements

1. Active session from authentication bypass
2. Web browser
3. Target profile accessible via dashboard menu

## Defense

Defensive measures and detection strategies:

- Encrypt and restrict PII display in profiles
- Implement session-based access controls
- Monitor profile views for unusual patterns

## Objectives

1. Collect PII for reconnaissance or sale
2. Identify additional attack vectors
3. Prepare for profile modification exploits

## Instructions

### Step 1: Navigate to Profile

**Context**: Locate the profile management area in the dashboard.

After login, click on the profile or account settings link.

**Expected Output**: Profile page loads with editable and viewable fields.

### Step 2: Inspect PII Fields

**Context**: Review stored personal data without restrictions.

Examine fields like phone number, address, and full name for unredacted information.

**Expected Output**: Visible PII such as phone numbers displayed in plain text.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pii-exposure]]
- [[data-collection]]
