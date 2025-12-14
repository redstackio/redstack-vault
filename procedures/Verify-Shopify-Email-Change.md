---
tags:
  - shopify
  - verification
  - session
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T17:28:58.530Z'
sub_techniques: []
id: df33da55-ad13-4a02-966e-136797596a2c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Shopify-Email-Change

## Summary

This procedure confirms that the Shopify account email has been successfully updated, ensuring the change is active while observing that existing sessions remain intact.

## Description

After initiating an email change, verification ensures the new address is set as primary. In the context of this vulnerability, this step highlights that Shopify does not terminate sessions linked to the old email, allowing potential unauthorized access. It uses the same browser session to check the profile without re-authentication.

## Requirements

1. Recently changed Shopify account email
2. Access to the original browser session
3. [[tools/Firefox]] for continuity

## Defense

Defensive measures and detection strategies:

- Log all email changes and correlate with active sessions
- Automatically log out all devices on profile updates
- Alert on verification attempts from new IPs

## Objectives

1. Confirm new email as primary
2. Note persistence of current session
3. Prepare for cross-browser testing

## Instructions

### Step 1: Check Account Profile

**Context**: Refresh the account settings to view the updated email.

In [[tools/Firefox]], navigate back to Account Settings > Profile and verify the displayed email matches the new one.

### Step 2: Test Session Integrity

**Context**: Perform a simple action to ensure the session is still valid.

Attempt to access a store dashboard or run a basic admin query to confirm no logout occurred.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- shopify
- verification
