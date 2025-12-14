---
id: proc-uuid-3
tags:
  - xss
  - persistence
  - card-creation
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:53.088Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Persistent-Malicious-Card

## Summary

This procedure submits the form with the injected XSS payload to store it persistently in the Twitter Ads backend, making the vulnerability available for later triggering.

## Description

Following payload injection, this step completes the card creation process on ads.twitter.com, where the unsanitized card[name] is saved to the database. The web platform's lack of server-side validation allows the malicious HTML/JS to persist. Expected outcome: A new card with a unique URL ID containing the payload. Prerequisites: Payload already in the form.

## Requirements

1. Completed form with payload in card[name]
2. Any mandatory fields filled (e.g., card type specifics)
3. Active authenticated session

## Defense

Defensive measures and detection strategies:

- Scan stored data for script tags during creation
- Use content security policy (CSP) to block inline scripts

## Objectives

1. Persist the XSS payload in backend storage
2. Obtain a viewable card URL for triggering
3. Ensure no immediate detection during submission

## Instructions

### Step 1: Complete Form Fields

**Context**: Fill remaining required inputs to enable submission.

Add minimal data to other fields as needed for validation.

> Form ready for submission without errors.

### Step 2: Submit and Confirm Creation

**Context**: Send the request to create the card.

Click the submit button or equivalent to process the form.

> Success message appears; note the generated URL ID (e.g., 42qj).

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
- [[Persistence]]
