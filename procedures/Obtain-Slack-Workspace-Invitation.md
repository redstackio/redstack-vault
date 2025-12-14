---
id: proc-slack-invitation-001
tags:
  - recon
  - slack
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:47.031Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Obtain-Slack-Workspace-Invitation

## Summary

This procedure involves generating or receiving a Slack workspace invitation to extract the team ID, which is used as a starting point for manipulating signup requests in subsequent attack steps.

## Description

In the context of exploiting Slack's signup vulnerability, obtaining an invitation provides the necessary team ID parameter. This can be done by requesting an invite from a known workspace or using a test account. The invitation email contains a one-time password or link with the team ID, enabling interception and modification in the signup flow. This step assumes access to an email service and basic knowledge of Slack's invitation process. Expected outcome is possession of a valid team ID for tampering.

## Requirements

1. Valid email address for receiving invitations
2. Access to a Slack workspace for generating invites (or social engineering to obtain one)
3. Basic web browsing capability

## Defense

Defensive measures and detection strategies:

- Monitor for unusual invitation requests from internal users
- Implement email filtering for suspicious Slack domains
- Educate users on verifying invitation sources

## Objectives

1. Acquire a Slack invitation containing a team ID
2. Prepare for request interception in signup process
3. Enable parameter manipulation for unauthorized access

## Instructions

### Step 1: Request Invitation

**Context**: Initiate the process to get an invitation email.

Use Slack's web interface or app to request an invite to a workspace. Alternatively, have someone send you an invite.

**Expected Output**: Email arrives with invitation link or one-time password.

### Step 2: Extract Team ID

**Context**: Identify the team ID from the invitation details.

Open the email and inspect the link (e.g., `https://slack.com/signup?team=T123456789`). The team ID is the alphanumeric string after `team=`, such as `T123456789`.

**Expected Output**: Noted team ID value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[slack]]
