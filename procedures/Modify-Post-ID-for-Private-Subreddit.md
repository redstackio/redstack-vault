---
id: proc-uuid-002
tags:
  - idor
  - modify
  - post-id
  - private-subreddit
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
updated_at: '2025-12-14T17:32:39.103Z'
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
# Modify Post ID for Private Subreddit

## Summary

This procedure alters the post ID parameter in a captured Reddit /api/vote request to reference a post in a private subreddit, bypassing access checks via IDOR.

## Description

Reddit's vote API fails to validate subreddit membership or visibility for the provided post ID, enabling direct object manipulation. The attacker must first obtain the target post ID through methods like enumeration or partial access leaks.

## Requirements

1. Intercepted legitimate vote request in Burp Repeater
2. Knowledge of the target private post ID (e.g., t3_abc123 format)
3. Valid session cookies preserved in the request
4. Access to view the post's upvote percentage for verification

## Defense

Defensive measures and detection strategies:

- Enforce subreddit-specific authorization checks on all API endpoints
- Log and alert on vote attempts for inaccessible posts
- Use indirect object references (e.g., slugs) instead of direct IDs

## Objectives

1. Replace the public post ID with a private one
2. Maintain request integrity for successful submission
3. Enable unauthorized vote simulation on restricted content

## Instructions

### Step 1: Identify Target Post ID

**Context**: Obtain the ID of the private subreddit post.

Use browser dev tools or enumeration to get the ID (e.g., from URL or API responses where partially visible).

### Step 2: Edit Request in Repeater

**Context**: Modify the id parameter in the JSON body.

In Burp Repeater, change {"id": "old_id", "dir": 1} to {"id": "private_post_id", "dir": 1}.

**Expected Output**: Updated request body reflecting the new ID.

### Step 3: Preserve Headers

**Context**: Ensure authentication headers remain intact.

Verify Cookie and X-Modhash headers are unchanged to simulate a legitimate session.

**Expected Output**: Request ready without auth errors.

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

- [[idor]]
- [[modify]]
- [[post-id]]
- [[private-subreddit]]
