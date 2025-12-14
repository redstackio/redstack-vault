---
id: proc-001
tags:
  - csrf
  - web
  - preparation
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:30.012Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Prepare-Friend-Request-on-XVIDEOS

## Summary

This procedure sets up the attack by authenticating to XVIDEOS, sending a friend request to a target user, and preparing the cancellation action to expose the vulnerable endpoint.

## Description

In the context of exploiting a CSRF vulnerability, the attacker first needs a pending friend request to target. This involves logging in, initiating the request, and navigating to the sent requests page to trigger the cancellation flow. The target environment is the XVIDEOS web platform, and the outcome is a confirmed pending request ready for interception. Prerequisites include an attacker account and basic web navigation skills.

## Requirements

1. Valid XVIDEOS account credentials
2. Web browser access to https://www.xvideos.com
3. Target user profile identifiable

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for unusual friend request patterns or cancellations
- Educate users on phishing links and suspicious HTML attachments

## Objectives

1. Establish a pending friend request as the attack vector
2. Position for request interception
3. Confirm endpoint accessibility

## Instructions

### Step 1: Authenticate and Send Request

**Context**: Log in to create an authenticated session and initiate the friend request.

Navigate to https://www.xvideos.com, log in with your account, go to the target user's profile (e.g., /profiles/USER123), and click to send a friend request.

### Step 2: Verify Sent Request

**Context**: Confirm the request is pending to ensure it's cancellable.

Access https://www.xvideos.com/account/friends/requests/sent and validate the request to USER123 is listed.

### Step 3: Prepare Cancellation

**Context**: Select the request to trigger the vulnerable action.

On the sent requests page, select USER123 and click the 'Cancel' button to open the confirmation popup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
