---
tags:
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 102d2682-2f88-4982-b4db-35329ab161c7
created_at: '2025-12-14T00:11:16.440Z'
updated_at: '2025-12-14T00:11:16.440Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Scheduled Post with Link

## Summary

This procedure involves creating a new scheduled post on Reddit with an embedded hyperlink in the RichText content, setting the stage for further exploitation.

## Description

Using the Reddit user interface, a scheduled post is created to include a benign hyperlink. This step is necessary to generate the API request that can later be intercepted and modified for injecting malicious payloads. The target environment is Reddit's web platform with access to scheduled posting features.

## Requirements

1. Valid Reddit account with posting privileges
2. Web browser for accessing Reddit interface
3. Network connectivity to Reddit servers

## Defense

Defensive measures and detection strategies:

- Monitor API requests for unusual hyperlink schemes
- Implement server-side validation for all user inputs

## Objectives

1. Establish a base post for modification
2. Prepare for request interception
3. Confirm post creation without errors

## Instructions

### Step 1: Access Scheduled Post Creation

**Context**: Navigate to the post creation section in Reddit.

Log in to Reddit and go to the community where you want to schedule the post. Select the option to create a new post and choose scheduling.

### Step 2: Add Hyperlink to Content

**Context**: Insert a standard link into the RichText editor.

In the post editor, use markdown or the RichText tools to add a link, e.g., [Example](https://example.com). Save the post as scheduled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- web
