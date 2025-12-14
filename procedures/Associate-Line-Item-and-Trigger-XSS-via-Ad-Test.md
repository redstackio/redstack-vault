---
id: proc-mopub-associate-trigger-001
tags:
  - xss
  - execution
  - ad-test
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
updated_at: '2025-12-14T03:46:37.924Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Associate-Line-Item-and-Trigger-XSS-via-Ad-Test

## Summary

This procedure associates a malicious line item with an ad unit in MoPub and triggers the XSS payload by testing the ad, causing JavaScript execution in the authenticated user's browser.

## Description

Once a link item with an XSS payload is prepared, it must be linked to an ad unit under the inventory section. The 'test ad' feature then previews the ad, invoking the javascript: URL and executing the payload. This targets users testing ads, such as admins or invited collaborators in shared inventories, leading to immediate code execution for cookie theft. The procedure uses MoPub's UI and requires knowledge of ad unit IDs; outcomes include visible alerts or network exfiltration requests.

## Requirements

1. Malicious link item with payload injected
2. Existing ad unit ID accessible via /advertise/inventory/
3. Authenticated session with ad management permissions

## Defense

Defensive measures and detection strategies:

- Disable or sandbox ad test features with isolated iframes
- Implement strict URL validation before preview rendering
- Monitor browser console and network logs for unexpected JS execution during tests

## Objectives

1. Bind the payload-carrying item to a testable ad unit
2. Invoke execution via the test interface
3. Confirm payload activation in the victim context

## Instructions

### Step 1: Associate with Ad Unit

**Context**: Link the line item to an ad unit to integrate it into the ad serving flow.

Edit the line item at https://app.mopub.com/advertise/line_items/, select an ad unit from the inventory dropdown, and save.

> Association confirmed. Expected output: Item shows linked ad unit.

### Step 2: Test the Ad to Trigger XSS

**Context**: Use the test feature to render and execute the ad preview.

Navigate to https://app.mopub.com/advertise/inventory/, select the ad unit, and click 'Test Ad' on the right panel.

> This loads the preview, firing the javascript: payload. Expected output: Alert or exfiltration in dev tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[ad-test]]
