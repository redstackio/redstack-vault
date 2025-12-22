---
tags:
  - enumeration
  - account-discovery
  - reddit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:06.308Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bef06012-ae5c-456e-96e3-b8b9905c46c0
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Reddit-Username-Enumeration-via-Email-Lookup

## Summary

This procedure uses Reddit's username lookup feature to enumerate all accounts registered with a specific email address, revealing associated usernames for targeting.

## Description

After multiple registrations, the attacker queries the username lookup endpoint with the shared email, triggering an automated email response listing all linked usernames. This works because Reddit does not restrict lookups or hide multi-account associations. The target is the web-based lookup form, requiring email access to receive results. Outcomes include a complete list of usernames, enabling identification of victim accounts without brute force.

## Requirements

1. Verified multiple accounts with the target email
2. Web browser
3. Access to the email inbox for results

## Defense

Defensive measures and detection strategies:

- Disable or restrict username lookup to prevent enumeration
- Limit lookup requests per IP/email and require CAPTCHA
- Log and alert on lookups for emails with multiple accounts
- Sanitize responses to avoid listing all associations

## Objectives

1. Discover all usernames tied to the email
2. Identify the victim's specific account
3. Gather intel for targeted reset without direct access

## Instructions

### Step 1: Access Username Lookup

**Context**: Submit the email to trigger enumeration.

**Action**:
Go to `https://www.reddit.com/username`, enter `account@gmail.com`, and click submit.

> Form processes the request and queues an email response.

### Step 2: Receive Enumeration Results

**Context**: Collect the list of usernames.

**Action**:
Monitor the email inbox for the automated response from Reddit.

> Email arrives containing usernames like `attacker1` and `user1`.

### Step 3: Extract Victim Username

**Context**: Parse the list to find the target.

**Action**:
Review the email content and note the victim's username (e.g., `user1`).

> Username ready for reset phase.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- enumeration
- account-discovery
- reddit
