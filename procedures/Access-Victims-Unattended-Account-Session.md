---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - initial-access
  - session-hijacking
  - unattended-session
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.035Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Victims-Unattended-Account-Session

## Summary

This procedure describes gaining unauthorized access to a Coursera account by exploiting an unattended browser session on a shared or public computer, providing initial entry without credentials.

## Description

In scenarios like public libraries, cafes, or offices, users may leave their browser sessions open on Coursera.org. An attacker can opportunistically access this session to perform malicious actions. This relies on physical proximity to the device and no session timeout enforcement. The outcome is temporary access to the victim's account dashboard, enabling further manipulation.

## Requirements

1. Physical access to a shared/public computer
2. Active Coursera browser session left open by the victim
3. Internet connectivity to coursera.org

## Defense

Defensive measures and detection strategies:

- Implement strict session timeouts (e.g., 5-10 minutes of inactivity)
- Educate users on logging out from shared devices
- Monitor for unusual login locations or IP changes

## Objectives

1. Establish initial unauthorized access to the account
2. Confirm active session without triggering alerts
3. Prepare for subsequent account modifications

## Instructions

### Step 1: Locate Shared Device

**Context**: Identify a device where the victim has left their session open.

Search for public computers or unattended workstations displaying an open browser tab on coursera.org.

### Step 2: Confirm Session Access

**Context**: Verify the session is active and belongs to the target.

Navigate to the Coursera homepage or dashboard. Check for the victim's profile name or enrolled courses visible without a login prompt.

**Expected Output**: Access to account settings or personal data without authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[initial-access]]
- [[session-hijacking]]
