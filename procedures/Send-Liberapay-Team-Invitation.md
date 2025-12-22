---
id: proc-uuid-1
tags:
  - prerequisite
  - liberapay
  - team-management
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.280Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Send-Liberapay-Team-Invitation

## Summary

This procedure outlines sending a team invitation to a target user on Liberapay, serving as a prerequisite for exploiting the CSRF vulnerability in the acceptance process.

## Description

In the context of the CSRF attack on Liberapay, the attacker must first invite the victim to their team via the platform's legitimate invitation feature. This creates a pending invitation with an associated acceptance endpoint (e.g., https://liberapay.com/{team}/membership/accept) that can later be triggered via CSRF. The procedure assumes the attacker controls a Liberapay team and knows the victim's username or email. No technical exploitation occurs here; it's a standard platform action.

## Requirements

1. Attacker Liberapay account with team ownership
2. Victim's Liberapay username or email address
3. Web browser access to liberapay.com

## Defense

Defensive measures and detection strategies:

- Monitor team invitation logs for unusual patterns
- Educate users on verifying invitation sources
- Implement rate limiting on invitations from single accounts

## Objectives

1. Establish a valid pending invitation for the victim
2. Prepare the environment for CSRF exploitation
3. Ensure the acceptance endpoint is active without alerting the victim

## Instructions

### Step 1: Log In and Access Team Management

**Context**: Authenticate as the attacker and navigate to the team dashboard to initiate the invitation.

Log in to https://liberapay.com and go to the team's page. Click on the "Members" or "Invite" section.

### Step 2: Enter Victim Details and Send

**Context**: Specify the victim's details to send the invitation, triggering an email notification.

Enter the victim's username or email in the invitation form and submit. No additional confirmation is needed.

**Expected Output**: Invitation sent; check team dashboard for pending invites.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[prerequisite]]
- [[liberapay]]
- [[team-invitation]]
