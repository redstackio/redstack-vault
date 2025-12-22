---
tags:
  - account-setup
  - invitation
  - read-only-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:29:36.396Z'
sub_techniques:
  - '[[T1078.004]]'
id: 0da7769a-c5b2-4206-adb4-c9a3e7b8b353
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Accounts-and-Invite-Read-Only-User

## Summary

This procedure establishes two user accounts on the Helium console: an admin account (A) to serve as the victim and a read-only invited account (B) as the attacker, setting the stage for authorization bypass testing.

## Description

In the Helium console, create separate registrations for Account A (admin) and Account B (attacker). From A, form an organization and invite B with read-only permissions. This simulates a legitimate invitation scenario where B should only view resources but not modify them. The procedure ensures B gains visibility into A's organization without initial write access, priming for later IDOR exploitation. Expected outcome: B can list devices but delete/update actions fail with permission errors.

## Requirements

1. Internet access to console.helium.com
2. Valid email addresses for two account registrations
3. Browser for web interface navigation

## Defense

Defensive measures and detection strategies:

- Implement strict invitation validation and role-based access control (RBAC) to prevent over-privileging
- Monitor for unusual account creation patterns or invitation spikes
- Log all permission checks and alert on failed write attempts from read-only roles

## Objectives

1. Create admin organization in Account A
2. Grant read-only access to Account B via invitation
3. Verify B's limited access to A's resources

## Instructions

### Step 1: Register Admin Account A

**Context**: Create the victim admin account and set up an organization.

Navigate to console.helium.com and complete registration for Account A using a unique email. After login, create a new organization via the dashboard (e.g., click "Create Organization" and provide a name).

> No specific command; this is a web UI action. Expected: Organization dashboard accessible with admin privileges.

### Step 2: Register Attacker Account B

**Context**: Create the read-only attacker account.

In a new browser or incognito session, register Account B with a different email on console.helium.com.

> Expected: Account B dashboard ready, no organization yet.

### Step 3: Invite Account B from A with Read-Only Permissions

**Context**: Send invitation to grant limited access.

Log in as A, navigate to organization settings > Invitations, enter B's email, and select "Read-Only" role. Send the invite.

> Expected: Email sent to B; upon acceptance, B sees A's organization in read-only mode.

### Step 4: Accept Invitation as B

**Context**: Activate the read-only access.

Log in as B, check email for invite link, and accept. Verify access by browsing A's devices (view-only).

> Expected Output: B can list devices but update/delete buttons are disabled or fail.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-setup
- invitation
- read-only-access
