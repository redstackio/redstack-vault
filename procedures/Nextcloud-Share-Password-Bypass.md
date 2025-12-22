---
tags:
  - nextcloud
  - authentication-bypass
  - session-persistence
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
updated_at: '2025-12-14T17:31:30.487Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 314e1994-ec8c-4126-be9c-9431303ebac5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Nextcloud-Share-Password-Bypass

## Summary

This procedure exploits an improper authentication vulnerability in Nextcloud's password-protected sharing feature, where updating the share password does not invalidate existing sessions, allowing users with prior access to bypass the new password and continue accessing shared resources without re-authentication.

## Description

The vulnerability arises from Nextcloud's failure to invalidate or require re-authentication for active sessions after a password change on a protected share. An attacker or unauthorized user who has previously accessed the share can maintain access indefinitely, even after the owner updates the password for security reasons. This affects web-based shares in Nextcloud instances and can lead to data exposure. The procedure involves creating a protected share, granting initial access, changing the password, and verifying persistent access. It requires standard user access to Nextcloud and is demonstrated via the web interface without additional tools.

## Requirements

1. Valid Nextcloud user account with sharing permissions (for share creator)
2. Recipient account or browser session for initial access
3. Nextcloud instance with password-protected sharing enabled (affected versions)
4. Web browser for accessing the interface and share link

## Defense

Defensive measures and detection strategies:

- Update Nextcloud to the latest version to patch session invalidation issues
- Implement session timeouts and force re-authentication on sensitive shares
- Monitor share access logs for anomalous persistent sessions post-password change
- Use multi-factor authentication (MFA) for share access where possible

## Objectives

1. Gain unauthorized access to protected shares by exploiting session persistence
2. Demonstrate the failure of password changes to enforce security
3. Highlight risks of improper session management in collaborative platforms

## Instructions

### Step 1: Create and Configure Password-Protected Share

**Context**: Establish the vulnerable share setup.

Log in to Nextcloud as the share owner. Select a file or folder, click the share icon, enable "Password protect" in the sharing settings, set an initial password (e.g., "oldpass"), and generate the share link.

> This creates a session-based access point that will not be properly invalidated later.

### Step 2: Grant Initial Access to Recipient

**Context**: Allow the target user to establish a persistent session.

Share the generated link with the recipient. The recipient opens the link, enters the initial password, and accesses the content to create an active session.

> Successful access confirms session establishment; browser cookies handle authentication.

### Step 3: Update Share Password

**Context**: Simulate a security update that exposes the vulnerability.

As the owner, edit the share settings, change the password to a new value (e.g., "newpass"), and apply the changes.

> The system updates the password but does not log out or invalidate existing sessions.

### Step 4: Verify Bypass with Persistent Session

**Context**: Confirm unauthorized access persists.

The recipient refreshes the share page or navigates back without clearing browser data. Access the content without entering the new password.

> If access is granted, the vulnerability is confirmed; no new authentication is required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[authentication-bypass]]
- [[session-persistence]]
