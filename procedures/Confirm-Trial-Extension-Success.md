---
id: proc-shopify-confirm-trial-extension
tags:
  - shopify
  - trial-status
  - validation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software Discovery]]'
updated_at: '2025-12-14T17:30:26.782Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Software Discovery]]'
---
# Confirm-Trial-Extension-Success

## Summary

This procedure verifies the impact of the trial extension by checking the store's subscription status, confirming the unauthorized prolongation of free access without triggering billing.

## Description

After mutation execution, Shopify updates the trial end date internally. This procedure inspects the admin panel or API response to validate the change. Scenario: Post-exploitation in trial store. Prerequisites: Admin or staff access. Outcome: Visible extension in status, proving bypass success.

## Requirements

1. Access to admin panel post-mutation
2. Web browser or API query tool
3. Original trial end date for comparison

## Defense

Defensive measures and detection strategies:

- Alert on trial status changes without payment events
- Audit GraphQL responses for extension messages
- Periodic reconciliation of trial dates vs. billing records

## Objectives

1. Validate extended trial duration
2. Confirm no userErrors in mutation
3. Assess prolonged free access impact

## Instructions

### Step 1: Check Subscription Status

**Context**: Navigate to view trial details.

**Instructions**: Log in as admin, go to Settings > Plan. Note the new end date.

> Expected output: Trial extended by 14 days from original.

### Step 2: Review Mutation Response

**Context**: If logged, inspect the GraphQL response for confirmation.

**Instructions**: Review the 'message' field in the response JSON.

> Expected output: '14 days extension added to your trial period'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Software Discovery]] Software Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- confirmation
- status-check
- impact-validation
