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
updated_at: '2025-12-14T03:16:14.525Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3047bc7b-4f8c-4f7a-a719-6bf6fbbcf0b1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-New-Group-on-ok-ru

## Summary

This procedure outlines the steps to create a new group on the ok.ru social platform, which is a prerequisite for accessing the vulnerable group posting feature in an XSS attack scenario.

## Description

In the context of testing for stored XSS in ok.ru's group features, creating a new group provides a controlled environment to initiate posts without affecting existing groups. The process involves logging into the platform and using the group creation interface. This step assumes the attacker has a valid account and is performed in a web browser. Expected outcomes include a fully functional group ready for posting.

## Requirements

1. Valid ok.ru user account with group creation permissions
2. Web browser with JavaScript enabled
3. Internet access to ok.ru

## Defense

Defensive measures and detection strategies:

- Rate limiting on group creation to prevent abuse
- Account verification to ensure legitimate users
- Monitoring for unusual group creation patterns

## Objectives

1. Establish a test group for vulnerability exploitation
2. Verify user permissions on the platform
3. Prepare environment for subsequent posting steps

## Instructions

### Step 1: Log In to ok.ru

**Context**: Access the platform with authenticated credentials to enable group management features.

Navigate to https://ok.ru, enter your username and password, and complete any CAPTCHA if prompted.

> Successful login redirects to the user dashboard.

### Step 2: Navigate to Groups Section

**Context**: Locate the interface for managing and creating groups.

Click on the 'Groups' tab in the main menu and select 'Create Group' or equivalent option.

> The group creation form appears.

### Step 3: Fill Group Details and Submit

**Context**: Provide minimal required information to create the group.

Enter a group name (e.g., 'Test Group'), optional description, and privacy settings, then click 'Create'.

> Confirmation message indicates group creation success.

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
