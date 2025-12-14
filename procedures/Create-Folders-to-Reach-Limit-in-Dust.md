---
tags:
  - setup
  - limit-testing
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.891Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a63f3d6f-5fff-4c8d-a216-8012c194996a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Folders-to-Reach-Limit-in-Dust

## Summary

This procedure sets up the environment by creating folders in the Dust Knowledge Space until the enforced 10-folder limit is reached, confirming the quota mechanism before exploiting the race condition.

## Description

In the Dust application, the Knowledge -> Space -> Folder feature limits users to 10 folders to prevent resource abuse. This procedure involves repeated UI-based folder creations to hit the limit, followed by an attempt to create one more (which fails) and deleting one to prepare for the race. It targets the web interface's folder management endpoint and requires an authenticated session. Expected outcomes include validating the limit and creating a state with 9 folders for the subsequent exploit.

## Requirements

1. Authenticated access to Dust web application
2. Browser or proxy tool like Burp Suite for request inspection
3. No special privileges beyond standard user account

## Defense

Defensive measures and detection strategies:

- Implement server-side quota checks with database transactions to ensure atomicity
- Rate limit concurrent folder creation requests per user
- Monitor for unusual patterns of rapid folder creations/deletions

## Objectives

1. Establish the 10-folder limit as a baseline
2. Confirm error handling on limit exceedance
3. Prepare a 9-folder state post-deletion for race exploitation

## Instructions

### Step 1: Navigate and Create Initial Folders

**Context**: Access the interface and build up to the limit through sequential creations.

Submit folder creation requests via the UI, naming them sequentially (e.g., Folder1 to Folder10). Each request is a POST to the folder endpoint with parameters like name and space_id.

> No specific command; use browser UI. Expected: Success for first 10, list updates.

### Step 2: Test Limit Exceedance

**Context**: Verify the limit by attempting an 11th folder.

Click create for Folder11; intercept if using Burp to observe the rejection response.

> UI submission fails with error. Expected: HTTP 400/429 response indicating limit reached.

### Step 3: Delete a Folder

**Context**: Reduce count to 9 to open a slot, but act quickly for race.

Select and delete one folder (e.g., Folder1) via UI, confirming the count drops.

> Deletion request sent; expected: Folder removed, count at 9.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[setup]]
- [[limit-testing]]
