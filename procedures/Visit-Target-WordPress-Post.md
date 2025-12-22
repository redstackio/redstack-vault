---
id: proc-visit-wordpress-post
tags:
  - recon
  - wordpress
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
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
updated_at: '2025-12-13T23:56:03.339Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Visit-Target-WordPress-Post

## Summary

This procedure involves navigating to a specific WordPress post on a .wordpress.com site to access the comments section, setting the stage for injecting XSS payloads via the SyntaxHighlighter plugin.

## Description

In the context of exploiting stored XSS in WordPress comments, the attacker first visits a target post to verify the environment and locate the comment form. This step ensures the site uses the vulnerable SyntaxHighlighter plugin, which processes code blocks in comments with a permissive regex that auto-links URLs, including dangerous protocols like javascript:.

## Requirements

1. Web browser (Firefox or Chrome)
2. Internet access to the target WordPress.com site
3. No authentication required if comments are public

## Defense

Defensive measures and detection strategies:

- Enable comment moderation to review posts before publishing
- Update plugins like SyntaxHighlighter to patched versions
- Monitor for unusual comment patterns with javascript: payloads

## Objectives

1. Confirm access to the target post and comments section
2. Verify SyntaxHighlighter is active
3. Prepare for payload submission

## Instructions

### Step 1: Launch Browser and Navigate

**Context**: Open a supported browser and directly access the target post to load the page.

No command required; use browser navigation:

Open Firefox or Chrome and enter the URL: https://mattstestsite128160580.wordpress.com/2019/10/03/test-post/.

> This loads the post, displaying any existing comments and the form for new ones. Expected output: Page renders with comments visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[recon]]
- [[wordpress]]
