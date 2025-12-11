---
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b546372a-b04b-424f-aa82-69be32794dfc
created_at: '2025-12-11T06:10:28.402Z'
updated_at: '2025-12-11T06:10:28.402Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject Payload into Imgur Album

## Summary

This procedure involves submitting the crafted HTML entity payload during Imgur album creation to store the XSS vulnerability persistently.

## Description

The payload is entered into the album creation form, resulting in it being stored and reflected on the user's profile page. This enables execution on any visitor's browser, targeting Imgur's storage mechanism.

## Requirements

1. Crafted payload from previous step.
2. Imgur account with album creation privileges.
3. Web access to Imgur.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user inputs on storage.
- Implement output encoding on profile pages.

## Objectives

1. Store the malicious payload.
2. Confirm album creation.
3. Set up for triggering on profile view.

## Instructions

### Step 1: Access Album Creation

**Context**: Navigate to Imgur's album creation interface.

Log in to Imgur and start creating a new album.

> Prepare to input the payload in relevant fields.

### Step 2: Submit Payload

**Context**: Insert the payload and complete creation.

Enter "/>&lt;script>alert(1)&lt;/script>"/ in the album field and submit.

> Verify successful creation without errors.

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
- [[injection]]
