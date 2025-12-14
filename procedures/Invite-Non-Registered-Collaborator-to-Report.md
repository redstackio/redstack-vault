---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - access-control
  - hackerone
  - email-invite
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:27.582Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Invite-Non-Registered-Collaborator-to-Report

## Summary

This procedure describes inviting a collaborator to a HackerOne report using an email address from a non-registered user, which populates the participant list and enables subsequent disclosure via API endpoints lacking proper controls.

## Description

HackerOne's invitation feature allows adding collaborators by email, even for non-registered users, without validating registration status. This action updates the /reports/<id>/participants endpoint, exposing the email in responses due to missing authorization. The procedure targets web UI interactions on the authenticated report page.

## Requirements

1. Access to an owned report (from prior procedure).
2. An email address not associated with a HackerOne account (e.g., personal Gmail).
3. Standard web browser session.

## Defense

Defensive measures and detection strategies:

- Enforce email validation and registration checks before adding to participant lists.
- Audit invitation logs for suspicious emails and monitor API access patterns.

## Objectives

1. Trigger backend update of participant data with a non-registered email.
2. Confirm invitation without errors.
3. Set up conditions for email exposure in API responses.

## Instructions

### Step 1: Locate Invitation UI

**Context**: Find the collaborator addition feature on the report page.

On the opened report page, navigate to the participants or collaborators section and click 'Invite Collaborator' or similar button.

### Step 2: Submit Invitation

**Context**: Enter and send the non-registered email to complete the process.

Input the target email (e.g., test@example.com) in the form field and submit. The system will process the invitation, sending an email and updating internal records.

**Expected Output**: Success message like 'Invitation sent'; no validation errors for non-registered emails.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[hackerone]]
