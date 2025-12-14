---
tags:
  - business-logic
  - license-management
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.294Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 6f1165ff-8834-4a40-91bc-a022816b12c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Activate-Existing-PortSwigger-License

## Summary

This procedure ensures an existing PortSwigger license is active and visible in the management interface, establishing the baseline for observing modifications from subsequent purchases.

## Description

In the context of exploiting business logic flaws in PortSwigger's licensing system, this step involves logging into the account and confirming the details of an active multi-user license. The target environment is the web-based PortSwigger dashboard, requiring an authenticated session. Expected outcomes include visibility of license parameters like user count and expiry date, which will be altered in later steps due to incorrect purchase processing logic.

## Requirements

1. Authenticated PortSwigger account with an existing license (e.g., 4-user plan)
2. Web browser with cookies enabled for session persistence
3. Internet access to the PortSwigger domain

## Defense

Defensive measures and detection strategies:

- Monitor account login events for unusual access patterns
- Implement client-side validation of license details before purchases
- Use server-side logging to track license modifications post-purchase

## Objectives

1. Confirm active license as prerequisite for flaw exploitation
2. Document baseline user count and expiry for comparison
3. Ensure account state is ready for new purchase triggering

## Instructions

### Step 1: Log In to PortSwigger Account

**Context**: Access the authenticated session to reach license management.

Navigate to the PortSwigger login page and enter credentials. Upon success, proceed to the support or account section.

### Step 2: Navigate to License Management

**Context**: Locate and view existing license details.

Click on the licensing or support tab, then select the option to view active licenses. Note the details: e.g., "4 users, expires [date]".

**Expected Output**: License card or table showing user count, expiry, and status as active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[license-management]]
