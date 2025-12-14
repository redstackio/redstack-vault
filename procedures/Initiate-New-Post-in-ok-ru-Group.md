---
tags:
  - xss
  - setup
  - ok.ru
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:14.522Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9894efb2-1fd5-4293-b5f4-3e6d9b26c72b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-New-Post-in-ok-ru-Group

## Summary

This procedure describes how to start a new post within an existing group on ok.ru, setting up the topic field for potential XSS payload injection.

## Description

As part of exploiting the stored XSS vulnerability, initiating a new post exposes the unsanitized topic field. This occurs in the group's discussion area and requires group admin or member access. The procedure uses standard web navigation and assumes prior group creation. Outcomes include an open post form ready for input.

## Requirements

1. Access to an existing ok.ru group (e.g., created in prior step)
2. Web browser session logged into ok.ru
3. Group posting permissions

## Defense

Defensive measures and detection strategies:

- Input validation on post initiation
- Logging of post creation events
- User activity monitoring in groups

## Objectives

1. Access the post creation interface in the target group
2. Prepare the topic field for payload insertion
3. Confirm posting functionality

## Instructions

### Step 1: Enter the Group

**Context**: Load the specific group page to access discussion features.

From the ok.ru dashboard, navigate to your groups list, select the target group, and enter its page.

> Group dashboard loads with posting options.

### Step 2: Locate and Click New Post

**Context**: Initiate the post creation process.

In the group's feed or discussions section, click the 'New Post' or 'Add Discussion' button.

> Post form opens with fields including topic.

### Step 3: Verify Form Readiness

**Context**: Ensure the topic field is available and editable.

Check that the topic input box is visible and accepts text input.

> Form is ready for further actions like payload entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[setup]]
- [[ok.ru]]
