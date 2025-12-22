---
id: 123e4567-e89b-12d3-a456-426614174002
name: Connect-Facebook-Account-to-KitCRM
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.399Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - auth
  - integration
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Connect-Facebook-Account-to-KitCRM

## Summary

This procedure links a Facebook account to the KitCRM application via OAuth, storing connected page details including any malicious payloads in page names.

## Description

The connection process uses Facebook's OAuth to authenticate and link the account. During this, KitCRM retrieves page names from the Facebook API without sanitization, storing them for later display. Prerequisites include a pre-created Facebook page with the XSS payload "><img src=x onerror=alert(9)> in its name. This step enables the storage aspect of the stored XSS vulnerability.

## Requirements

1. Facebook account with a page named containing the payload "><img src=x onerror=alert(9)>
2. Authenticated KitCRM session
3. Facebook app permissions for KitCRM (managed via OAuth)

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs from external APIs like Facebook before storage
- Log and monitor OAuth connections for suspicious account linking

## Objectives

1. Establish integration between Facebook and KitCRM
2. Store unsanitized page data
3. Enable reflection in UI for exploitation

## Instructions

### Step 1: Initiate Connection

**Context**: Start the OAuth flow from KitCRM.

Click the 'Connect Facebook' button on the connections page.

### Step 2: Authenticate with Facebook

**Context**: Complete OAuth to link accounts.

Log in to Facebook if prompted and authorize the KitCRM app to access pages.

**Expected Output**: Confirmation of successful connection; Facebook section updates in KitCRM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth]]
- [[integration]]
- [[web]]
