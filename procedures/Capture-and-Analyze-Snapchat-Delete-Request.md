---
tags:
  - capture
  - analysis
  - graphql
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8d482046-f63a-437e-a375-a5bd45ccb1b8
created_at: '2025-12-11T06:10:28.971Z'
updated_at: '2025-12-11T06:10:28.971Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Capture and Analyze Snapchat Delete Request

## Summary

This procedure involves triggering a legitimate delete action in Snapchat's myposts page and capturing the associated GraphQL request using Burp Suite for analysis of parameters like 'ids'.

## Description

By intercepting a self-delete request, the GraphQL mutation structure is revealed, including the 'ids' parameter that can be manipulated for IDOR exploitation. This step is crucial for understanding the API's authorization flaws.

## Requirements
1. Burp Suite setup complete.
2. Logged into Snapchat myposts page.
3. At least one personal Spotlight post available for deletion.

## Defense

Defensive measures and detection strategies:
- Implement strict authorization checks on API parameters.
- Log and alert on unusual delete requests.

## Objectives
1. Capture the delete GraphQL mutation.
2. Analyze the request structure.
3. Identify modifiable parameters for exploitation.

## Instructions

### Step 1: Trigger Delete Action

**Context**: Initiate deletion of your own post.

On https://my.snapchat.com/myposts, select a post and click delete.

> This sends the GraphQL request to the API.

### Step 2: Intercept in Burp Suite

**Context**: Capture the request.

In Burp Suite Proxy, intercept the POST request to the GraphQL endpoint and note the mutation details.

> The request includes the 'ids' array and storyType.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- capture
- graphql
