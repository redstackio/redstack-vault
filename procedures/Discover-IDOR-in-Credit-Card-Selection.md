---
id: proc-yelp-discover-idor-001
tags:
  - idor
  - discovery
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.204Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Discover-IDOR-in-Credit-Card-Selection

## Summary

This procedure tests the /checkout/transaction_platform endpoint for Insecure Direct Object Reference (IDOR) by manipulating the credit_card_id parameter, revealing a lack of ownership validation that allows access to other users' saved cards.

## Description

Targeting Yelp's checkout system integrated with Grubhub, this involves intercepting and modifying API requests during payment selection. The vulnerability stems from direct object referencing without server-side checks, potentially exposing all 1,500,000+ saved cards. Prerequisites include a captured legitimate request; outcomes confirm if arbitrary IDs are accepted.

## Requirements

1. Captured legitimate request from Step 1
2. Browser developer tools or proxy for request modification
3. Knowledge of parameter structure (e.g., credit_card_id as integer ID)

## Defense

Defensive measures and detection strategies:

- Enforce server-side ownership verification using session tokens or user IDs
- Implement indirect object references (e.g., hashed IDs) to obscure direct access
- Monitor for parameter tampering via anomaly detection in logs

## Objectives

1. Identify lack of authorization on credit_card_id
2. Confirm IDOR existence
3. Assess scope of accessible objects

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Capture a standard checkout request to baseline the parameter.

During checkout, use developer tools to copy the POST request to /checkout/transaction_platform as cURL or raw form data. Note the value of credit_card_id (your own).

### Step 2: Modify and Test Parameter

**Context**: Attempt to reference an unauthorized object.

Edit the credit_card_id to an arbitrary value (e.g., your_id + 1). Resubmit the request via tools or browser console. Check server response for acceptance.

**Expected Output**: 200 OK response or successful processing without auth errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[Discovery]]
- [[authorization-bypass]]
