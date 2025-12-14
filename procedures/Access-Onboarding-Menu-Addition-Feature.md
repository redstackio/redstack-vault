---
id: proc-uber-onboarding-001
tags:
  - onboarding
  - web-exploration
  - uber-eats
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.543Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Onboarding-Menu-Addition-Feature

## Summary

This procedure details navigating the Uber Eats restaurant onboarding process to reach the menu addition section, exposing the vulnerable file upload endpoint.

## Description

Post-signup, the onboarding workflow guides users through setup steps, including menu configuration. The menu addition feature includes an upload mechanism for item images or files, which lacks validation, allowing progression to exploitation. This step involves manual navigation without automated tools.

## Requirements

1. Active Uber Eats restaurant account from signup
2. Web browser session maintained
3. Patience for any guided tour elements in onboarding

## Defense

Defensive measures and detection strategies:

- Restrict onboarding access to verified accounts only
- Log navigation patterns in onboarding to detect rapid progression to upload features
- Implement session timeouts during extended onboarding

## Objectives

1. Reach the menu setup interface
2. Identify and access the file upload component
3. Set stage for malicious upload

## Instructions

### Step 1: Enter Onboarding Dashboard

**Context**: Begin the post-signup setup process.

After signup confirmation, the dashboard loads. Follow any prompts to start onboarding, selecting options related to business setup.

### Step 2: Navigate to Menu Addition

**Context**: Locate the specific feature for adding menu items.

Proceed through onboarding steps until reaching 'Add Menu' or similar. Click to enter the menu editor, where file upload options appear for images or custom files.

> The upload endpoint is now accessible, typically via a form submission to an internal API.

### Step 3: Inspect Upload Interface

**Context**: Confirm the upload feature is unrestricted.

Examine the form for any file type restrictions; none are enforced, allowing HTML/SVG uploads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[onboarding]]
- [[web-exploration]]
- [[uber-eats]]
