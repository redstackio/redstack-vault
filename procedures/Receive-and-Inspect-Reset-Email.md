---
tags:
  - email-inspection
  - mattermost
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Sublime-Text]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Network Sniffing]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 18b4ff39-8fdb-401e-8bb4-f5e772c302fa
created_at: '2025-12-11T06:10:15.818Z'
updated_at: '2025-12-11T06:10:15.818Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1040]]'
---
# Receive and Inspect Reset Email

## Summary

This procedure involves checking the email inbox for the Mattermost password reset link and opening it to begin inspection.

## Description

After initiating the reset, the email service delivers a message with the link. This step is key to identifying if the link uses insecure protocols, setting up for potential interception attacks in shared networks.

## Requirements

1. Access to the email account used for Mattermost
2. Web browser or email client like [[tools/Chrome]]
3. Prior reset request

## Defense

Defensive measures and detection strategies:

- Use encrypted email channels
- Alert on suspicious email access patterns

## Objectives

1. Retrieve the reset link
2. Prepare for protocol analysis
3. Identify potential vulnerabilities

## Instructions

### Step 1: Check Email Inbox

**Context**: Access the email service to find the reset message.

Use [[tools/Chrome]] to log into the email account and locate the Mattermost email.

> Expected: Email with subject related to password reset.

### Step 2: Open the Email

**Context**: View the contents of the email.

Click to open and note the reset link provided in the body.

> Expected: Visible link for password reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome]]

## Tags

- email-inspection
- mattermost
