---
tags:
  - persistence-verification
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2646322b-8502-41a8-a6f1-ffb331b83169
created_at: '2025-12-13T23:52:50.016Z'
updated_at: '2025-12-13T23:52:50.016Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-Stored-XSS-Persistence

## Summary

This procedure confirms the stored nature of the XSS by reloading the console and re-triggering the payload, proving it persists across page loads and sessions.

## Description

Stored XSS differs from reflected by surviving in backend storage (e.g., plan name database). Reloading simulates a new victim session, and re-triggering validates exploitation against multiple users. This step is crucial for assessing severity in vulnerability reports.

## Requirements

1. Previously created plan with confirmed XSS trigger
2. Ability to reload the browser session
3. Same or different user context for broader impact testing

## Defense

Defensive measures and detection strategies:

- Regularly scan stored data for XSS patterns using automated tools
- Implement server-side validation to reject HTML/script in inputs
- Audit plan names and actions in logs for anomalies

## Objectives

1. Confirm payload storage and retrieval
2. Re-execute to validate persistence
3. Document for impact assessment

## Instructions

### Step 1: Reload Console Page

**Context**: Simulate a fresh session to test storage.

Revisit https://mc-beta-cloud.acronis.com/ui/ or refresh the current page.

> Session may persist; re-authenticate if needed.

### Step 2: Re-Navigate to Plans

**Context**: Access the list to locate the stored plan.

Click 'PLANS' > 'Protection'.

> Plans list reloads, showing the payload-named plan.

### Step 3: Re-Select and Trigger Stop

**Context**: Repeat the trigger to verify execution.

Check the plan's box, click 'Stop' in Actions, and confirm.

> XSS fires again, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[Persistence]]
