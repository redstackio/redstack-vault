---
tags:
  - xss-trigger
  - deletion-modal
  - gitlab
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
updated_at: '2025-12-14T03:16:20.313Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 97f799db-5182-4f03-97ac-24cf7a2906d8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Project-Deletion-to-Execute-XSS

## Summary

This procedure navigates to the project deletion settings and opens the confirmation modal, causing the malicious username to be rendered via jQuery .html(), executing the stored XSS payload.

## Description

The vulnerability lies in the modal's rendering of the project owner's username without escaping, interpreting the <img> tag and triggering the onerror alert. This executes in the context of the user viewing the modal (e.g., Master access holder), limited to the project's scope.

## Requirements

1. Master access to the target personal project
2. Malicious username already set
3. Web browser

## Defense

Defensive measures and detection strategies:

- Refactor UI renders to use safe methods like .text()
- Implement input validation on username storage
- Monitor JavaScript errors and alerts in browser logs

## Objectives

1. Render the stored payload in the modal
2. Achieve JavaScript execution
3. Validate impact like session exposure

## Instructions

### Step 1: Access Danger Zone

**Context**: Reach the advanced project settings for deletion.

Go to Project Settings > General > Advanced > Danger Zone.

**Expected Output**: Danger Zone section expands.

### Step 2: Initiate Deletion

**Context**: Click to open the modal and trigger rendering.

Click the 'Remove Project' button.

**Expected Output**: Modal opens, rendering username and executing payload (alert fires).

### Step 3: Confirm Execution

**Context**: Observe the JavaScript outcome.

Look for the alert popup displaying the document domain.

**Expected Output**: Alert box with 'gitlab.com' or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[Execution]]
