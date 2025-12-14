---
id: proc-uuid-004
tags:
  - upvote
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
updated_at: '2025-12-14T17:32:39.097Z'
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
# Simulate Upvote to Further Alter Upvote Percentage

## Summary

This procedure follows a downvote with an upvote simulation on the same unauthorized post, further manipulating the upvote percentage to show the vulnerability's repeatability.

## Description

After a downvote shifts the ratio, an upvote (dir=1) can push it to an uneven value like 67%, highlighting how repeated unauthorized votes can degrade post trust without real tally changes.

## Requirements

1. Previous downvote request successful
2. Burp Repeater session active with modified ID
3. Observation access to the post's vote display

## Defense

Defensive measures and detection strategies:

- Rate-limit votes per user-post pair
- Audit logs for dir changes on restricted posts
- Cross-verify vote impacts with access logs

## Objectives

1. Adjust upvote percentage post-downvote (e.g., 99% to 67%)
2. Prove multiple manipulations possible
3. Emphasize lack of authorization enforcement

## Instructions

### Step 1: Reset Direction Parameter

**Context**: Switch from downvote to upvote.

Update dir to 1 in the request body.

### Step 2: Resend Request

**Context**: Submit the upvote to the API.

Click "Send" in Burp Repeater.

**Expected Output**: HTTP 200 OK; successful processing.

### Step 3: Observe Further Change

**Context**: Validate the compounded effect.

Refresh the post and note the new ratio.

**Expected Output**: Upvote percentage altered again, e.g., to 67%.

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

- [[upvote]]
- [[manipulation]]
- [[upvote-percentage]]
- [[idor]]
