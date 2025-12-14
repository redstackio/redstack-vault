---
id: uuid-for-proc2
tags:
  - xss
  - slack
  - post-creation
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
updated_at: '2025-12-14T03:16:31.259Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Post-in-Slack-Workspace

## Summary

This procedure creates a neutral post or file in a Slack workspace, serving as a vehicle to trigger the stored XSS payload during the sharing process without raising immediate suspicion.

## Description

Slack allows users to create posts or upload files via its web interface, which can then be shared internally. This step involves navigating to the creation interface and generating innocuous content. It requires basic authenticated access and sets up the delivery mechanism for the malicious user name payload. The post itself is benign, but sharing it exploits the vulnerability in the menu's rendering of recipient names.

## Requirements

1. Authenticated session in the target Slack workspace
2. Permissions to create posts or files
3. Access to the files creation URL (e.g., https://workspace.slack.com/files/create/space)

## Defense

Defensive measures and detection strategies:

- Limit post creation to verified users and scan uploads for anomalies
- Log all post creations and shares for anomaly detection
- Use rate limiting on sharing actions to prevent abuse

## Objectives

1. Generate a shareable post for payload delivery
2. Maintain stealth by using neutral content
3. Obtain a post link or ID for the next step

## Instructions

### Step 1: Navigate to Creation Interface

**Context**: Access the post or file creation area in Slack.

Open Slack in a browser and go to the workspace's files section or use the '+' icon to create a new message/post.

### Step 2: Create the Post

**Context**: Add simple content to create the post without triggering any filters.

Enter neutral text like "Test post" or upload a harmless file, then save or post it.

> The post is now available in the workspace for sharing.

### Step 3: Note Post Details

**Context**: Record the post for sharing in the next procedure.

Copy the post URL or ID from the address bar or share preview.

**Expected Output**: Confirmation message or visible post in the channel/files.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- slack
- post
- creation
