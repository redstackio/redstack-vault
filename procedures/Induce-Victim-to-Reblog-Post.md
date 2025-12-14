---
tags:
  - social-engineering
  - phishing
  - tumblr
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1566.001]]'
id: 09d84926-cf07-4880-84c1-1be077ccc3bf
created_at: '2025-12-14T03:46:26.712Z'
updated_at: '2025-12-14T03:46:26.712Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Induce-Victim-to-Reblog-Post

## Summary

This procedure uses social engineering to encourage a victim to reblog the attacker's malicious Tumblr post, thereby storing the XSS payload on the victim's blog for later triggering.

## Description

Tumblr's reblog feature copies post content to the victim's blog without re-sanitizing HTML, preserving the stored XSS. The attacker promotes the post through shares, comments, or trending topics to lure interaction. Once reblogged, the payload is ready for execution in the victim's edit mode. This step relies on victim behavior rather than technical exploits.

## Requirements

1. Publicly visible malicious post
2. Access to social channels for promotion (e.g., Twitter, Discord)
3. Understanding of victim targeting (e.g., shared interests)

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious post interactions
- Implement reblog previews with sanitization warnings
- Log and alert on mass reblogs of flagged content

## Objectives

1. Transfer payload to victim's blog
2. Maintain stealth until edit mode
3. Increase attack surface via victim's network

## Instructions

### Step 1: Promote the Post

**Context**: Increase visibility to attract reblogs.

Share the post link on social media or Tumblr communities with enticing captions.

### Step 2: Monitor Interactions

**Context**: Wait for victim engagement.

Check post analytics or notifications for reblogs from target victims.

### Step 3: Confirm Storage

**Context**: Verify payload persistence post-reblog.

If possible, view the victim's blog to ensure the form HTML is copied intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used

- None

## Tools Used

- None

## Tags

- [[social-engineering]]
- [[Phishing]]
- [[tumblr]]
