---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - csrf
  - forgery
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:23.186Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Comment-Forgery-via-Browser-Submission

## Summary

This procedure details the final execution where the victim's browser submits the forged POST request to WordPress's wp-comments-post.php, resulting in an arbitrary comment being posted due to missing CSRF validation.

## Description

Once the malicious page loads, the form submits POST data including the comment text, post ID, and parent ID. The endpoint processes this as legitimate because it trusts the authenticated session without token checks. This can lead to spam, defacement, or phishing via comments. Target environment: Vulnerable WordPress installations without plugins enforcing CSRF.

## Requirements

1. Victim authenticated to target site
2. Malicious page loaded in victim's browser
3. Target post ID known and comment-enabled

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens via nonces in WordPress core or plugins like Wordfence
- Validate referer headers on sensitive endpoints
- Rate-limit comment submissions per user/IP

## Objectives

1. Successfully post unauthorized comment
2. Maintain stealth by using victim's credentials
3. Demonstrate vulnerability for reporting

## Instructions

### Step 1: Trigger Form Submission

**Context**: The page auto-submits or prompts the user to click, sending the POST.

In the loaded page, the JavaScript executes: document.getElementById('csrfForm').submit(); This sends data to http://target/wp-comments-post.php.

> Expected output: HTTP 200 response, redirect to post page with comment visible.

### Step 2: Verify Comment Posting

**Context**: Check the target post for the forged comment.

Visit the post (e.g., ID 29) on the WordPress site and confirm the comment 'csrf_comment' appears as a top-level entry.

> Expected output: Comment listed under the post, attributed to victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[comment-forgery]]
- [[web-exploitation]]
