---
tags:
  - xss
  - cancellation
  - overview
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.722Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 81638063-bfda-432d-bb35-94ef3e89e7e3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Victim-Cancels-Authorization-Triggering-XSS

## Summary

This procedure exploits a reflection vulnerability during authorization cancellation, executing the stored XSS payload when the victim clicks 'Cancel my authorization' on the overview page.

## Description

Navigating to the authorization overview and selecting cancel reflects the username in the processing logic without sanitization, firing the script. This provides an additional vector beyond acceptance. Prerequisites: Established authorization; outcomes: XSS execution on cancel.

## Requirements

1. Victim with active authorization to cancel
2. Access to overview page
3. Payload already reflected

## Defense

Defensive measures and detection strategies:

- Encode all dynamic content in overview and cancel handlers
- Audit cancel endpoints for reflection
- Log cancellation attempts and scan for script patterns

## Objectives

1. Access authorization overview
2. Trigger cancel reflection
3. Execute payload

## Instructions

### Step 1: Navigate to Overview

**Context**: Reach the cancellation interface.

Go to https://mobilevikings.be/en/account/authorization/overview/.

### Step 2: Initiate Cancel

**Context**: Perform the action that reflects the username.

Click 'Cancel my authorization' for the relevant entry.

> Reflection occurs in the cancel confirmation or processing.

### Step 3: Confirm Trigger

**Context**: Check for execution.

Payload executes in the browser context.

**Expected Output**: Script runs, e.g., alert or exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[cancellation]]
- [[web]]
