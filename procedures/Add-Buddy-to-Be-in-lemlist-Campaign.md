---
id: proc-add-buddy-lemlist
tags:
  - web
  - lemlist
  - campaign
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
updated_at: '2025-12-14T03:47:18.072Z'
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
# Add-Buddy-to-Be-in-lemlist-Campaign

## Summary

This procedure sets up a new buddy entry in the Buddies-to-Be section of a lemlist campaign, providing the foundation for injecting malicious payloads into form fields like the LinkedIn URL.

## Description

In the lemlist web application, campaigns allow personalization through the Buddies-to-Be feature, where users add contact details. This step involves navigating to the campaign interface and creating a new buddy entry, exposing fields vulnerable to input manipulation. It requires authenticated access and targets the web-based dashboard, enabling subsequent exploitation steps without triggering immediate alerts.

## Requirements

1. Authenticated session in lemlist with campaign edit permissions
2. Web browser access to the lemlist dashboard
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit campaign editing
- Monitor for unusual buddy additions in audit logs
- Use client-side validation to flag suspicious field inputs early

## Objectives

1. Access the Buddies-to-Be section for new entry creation
2. Prepare the form for payload injection
3. Ensure the entry is saved without errors

## Instructions

### Step 1: Navigate to Campaign Interface

**Context**: Log in and locate the target campaign to access the editing features.

No command required; use the web UI to select or create a campaign, then click into the Buddies-to-Be section.

> Browser navigation leads to the form; confirm the section loads successfully.

### Step 2: Input Basic Buddy Details

**Context**: Fill minimal required fields to enable the LinkedIn URL input.

Enter placeholder data like name and email in the respective fields, then proceed to the LinkedIn field in the next step.

> Form partially completes; LinkedIn field becomes available without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[lemlist]]
