---
id: proc-uuid-003
tags:
  - downvote
  - manipulation
  - upvote-percentage
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:32:39.100Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate Downvote to Decrease Upvote Percentage

## Summary

This procedure sends a modified downvote request to Reddit's /api/v1/vote endpoint, reducing the displayed upvote ratio for an unauthorized private post.

## Description

By setting the dir parameter to -1, the API processes the vote without access validation, altering the percentage calculation while leaving actual counts intact. This disrupts post credibility in private communities.

## Requirements

1. Modified request with private post ID in Burp Repeater
2. Ability to refresh and observe the target post page
3. Valid Reddit session for API authentication

## Defense

Defensive measures and detection strategies:

- Validate user permissions against subreddit before processing votes
- Implement vote nonce or idempotency keys to prevent replay
- Monitor for rapid percentage changes on low-traffic posts

## Objectives

1. Decrease upvote percentage (e.g., 100% to 99%)
2. Confirm manipulation without affecting real votes
3. Demonstrate integrity impact on private content

## Instructions

### Step 1: Set Direction Parameter

**Context**: Change the vote direction to downvote.

In the request body, update dir from 1 (or 0) to -1.

### Step 2: Send Request

**Context**: Forward the modified request to the server.

Click "Send" in Burp Repeater.

**Expected Output**: HTTP 200 OK response; no error messages.

### Step 3: Verify Change

**Context**: Check the post's upvote display.

Refresh the post page (if viewable) or use API to query upvote ratio.

**Expected Output**: Upvote percentage decreased, e.g., from 100% to 99%.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[downvote]]
- [[manipulation]]
- [[upvote-percentage]]
- [[idor]]
