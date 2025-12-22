---
id: uuid-intercept-modify
tags:
  - intercept
  - burp-suite
  - http-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:25:47.319Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
---

# Intercept-and-Modify-Curate-Request

## Summary

This procedure uses Burp Suite to capture and alter the POST request for comment curation, enabling IDOR exploitation by changing the comment_id parameter.

## Description

The curation endpoint at `/extensions/checkout_comments/curate_comment` is vulnerable due to missing shop domain validation. Intercepting a legitimate publish action reveals the request structure, which can be modified in Repeater to target foreign IDs. Prerequisites: Test comment created, Burp proxy active. Outcomes: Modified request sent, response analyzed for unauthorized data.

## Requirements

1. Burp Suite running with browser proxy configured
2. Access to admin comments page
3. Valid session cookies for judge.me

## Defense

Defensive measures and detection strategies:

- Implement request signing or CSRF tokens tied to shop domain
- Log anomalous comment_id accesses and alert on cross-shop attempts

## Objectives

1. Capture baseline curation request
2. Modify parameters for unauthorized access
3. Test response for data leakage

## Instructions

### Step 1: Navigate to Comments Page

**Context**: Locate the test comment for publishing.

No command; go to `/admin/apps/checkout-comments/extensions/checkout_comments/comments` in Shopify admin.

> Page loads with list of comments.

### Step 2: Publish and Intercept

**Context**: Trigger the vulnerable request while proxying.

Use browser with Burp proxy; click publish on test comment.

> Request appears in Burp Proxy history: POST to curate_comment with comment_id.

### Step 3: Send to Repeater and Modify

**Context**: Alter the request for exploitation.

In Burp, right-click request > Send to Repeater. Edit `comment_id` to a foreign value (e.g., 1), keep `curated=ok`, send.

> Response includes JSON with unauthorized buyer info.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- burp-suite
- http-modification

