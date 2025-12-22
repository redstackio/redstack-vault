---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - wordpress
  - publish
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:58.325Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Publish-Malicious-WordPress-Post

## Summary

Publish the post containing the malicious iframe to make it accessible to the victim.

## Description

After embedding the payload, publish the post to expose it on the frontend, allowing the victim to visit and trigger the clickjacking without suspicion.

## Requirements

1. Draft post with malicious HTML
2. Editor access

## Defense

Defensive measures and detection strategies:

- Review posts before publishing
- Use content moderation plugins

## Objectives

1. Make post live
2. Obtain shareable URL

## Instructions

### Step 1: Review Post

**Context**: Ensure payload is intact.

Preview the post.

### Step 2: Publish

**Context**: Go live.

Click Publish button.

### Step 3: Copy URL

**Context**: Prepare for distribution.

Copy the post permalink.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[publish]]
