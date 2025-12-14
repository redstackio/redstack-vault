---
tags:
  - setup
  - linkedin
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
techniques: []
updated_at: '2025-12-14T17:30:47.238Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 11e019c3-b1b8-4786-9107-afd6fe7db145
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-LinkedIn-Newsletter

## Summary

This procedure sets up a test newsletter on LinkedIn to facilitate capturing legitimate API requests for subsequent IDOR exploitation.

## Description

In the context of testing LinkedIn's newsletter feature, create a new newsletter using the platform's UI. This provides a controlled environment to observe API interactions without affecting production data. Prerequisites include a valid LinkedIn account. Expected outcome is a functional newsletter with an assigned NewsletterId.

## Requirements

1. Authenticated LinkedIn session
2. Access to LinkedIn's publishing tools
3. Basic familiarity with web navigation

## Defense

Defensive measures and detection strategies:

- Monitor for unusual newsletter creation patterns
- Implement rate limiting on newsletter actions

## Objectives

1. Generate a legitimate NewsletterId for request capture
2. Establish baseline API behavior
3. Prepare for request interception

## Instructions

### Step 1: Log In and Navigate to Publishing

**Context**: Access the newsletter creation interface.

No specific command; use LinkedIn web UI to go to 'Me' > 'Create a Newsletter'.

> Fill in title and description, then publish.

### Step 2: Confirm Creation

**Context**: Verify the newsletter is active.

Navigate to the newsletter page and note the seriesUrn in the URL.

> Expected: Newsletter page loads with unique ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[linkedin]]
