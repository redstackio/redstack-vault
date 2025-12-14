---
tags:
  - csrf
  - web
  - access
type: procedure
tools:
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.865Z'
sub_techniques: []
id: 7f1e0ba7-bb63-4a89-814f-ae9812d9fe1e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Slack-Help-Request-Form

## Summary

This procedure involves navigating to Slack's help request form in an authenticated session to initiate vulnerability analysis for CSRF protections.

## Description

In the context of testing Slack's web application, accessing the support request form is the entry point for inspecting form submissions. This step requires an active Slack session and targets the specific URL where new requests are created. The expected outcome is the form being loaded, ready for interaction and interception.

## Requirements

1. Authenticated Slack account with workspace access
2. Firefox browser installed
3. Network connectivity to Slack's domain

## Defense

Defensive measures and detection strategies:

- Implement session management to require re-authentication for sensitive forms
- Monitor access logs for unusual form page visits

## Objectives

1. Load the vulnerable form for submission testing
2. Confirm accessibility in authenticated context
3. Prepare for request interception

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Ensure a valid session and direct access to the form URL.

Open Firefox and log into your Slack workspace if not already authenticated. Enter the URL https://sehacure.slack.com/help/requests/new in the address bar and press Enter.

> This loads the new support request form, displaying input fields for submission details.

**Expected Output**: Page renders with form elements visible, no authentication prompts.

### Step 2: Verify Form Load

**Context**: Confirm the form is functional before proceeding.

Inspect the page source or visually check for submission fields (e.g., description, attachments).

> Successful load indicates readiness for the next steps in CSRF analysis.

**Expected Output**: Form fields present and interactive.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Tamper-Data]]

## Tags

- [[csrf]]
- [[web]]

