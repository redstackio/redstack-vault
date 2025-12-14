---
id: proc-induce-admin-edit
tags:
  - social-engineering
  - xss
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.130Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Induce-Admin-to-Edit-Vulnerable-Comment

## Summary

This procedure uses social engineering via a follow-up comment to trick a WordPress administrator into editing the previously submitted vulnerable comment, triggering payload processing.

## Description

After injecting the encoded payload, submit a second comment claiming a typo in the URL of the first comment. This prompts the admin to edit the original comment for correction, activating the wp_rel_nofollow_callback() during save, which decodes the payload. Targets non-technical admins on sites with active comment moderation, relying on human interaction rather than technical exploits.

## Requirements

1. The first comment with payload already submitted
2. Comments enabled and admin notifications active
3. Ability to post multiple comments

## Defense

Defensive measures and detection strategies:

- Train admins to avoid editing unverified comments without review
- Use automated moderation tools to flag suspicious comment patterns
- Implement approval workflows for all comments
- Log and alert on rapid successive comment submissions

## Objectives

1. Prompt admin interaction with the vulnerable comment
2. Ensure editing occurs to process the encoded payload
3. Bridge pre-auth injection to privileged processing

## Instructions

### Step 1: Submit Follow-Up Comment

**Context**: Create a plausible reason for the admin to revisit and edit the first comment.

Navigate back to the same post and submit:

```
I just noticed a typo in the URL! Could you please change it from dummysite.com to dummysite2.com? Thank you so much
```

Submit the comment.

> This appears helpful, increasing chances of admin edit. Expected output: Second comment posts, potentially notifying admin.

### Step 2: Monitor for Admin Response

**Context**: Wait for the admin to act on the suggestion.

Observe the comments section or use site monitoring to confirm edit occurs.

> No direct command; relies on social engineering success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[xss]]
- [[wordpress]]
