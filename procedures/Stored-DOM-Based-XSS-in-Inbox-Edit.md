---
id: proc-uuid-5678
tags:
  - xss
  - stored-xss
  - dom-xss
  - javascript-url
  - inbox
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.496Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored DOM-Based XSS in Inbox Edit

## Summary

This procedure stores a javascript: URL payload in a Tumblr blog's inbox via submissions, executing as DOM-Based XSS when the victim edits the post due to improper sanitization and lack of CSP on the edit page.

## Description

Attackers submit posts with malicious links to blogs allowing submissions. When victims edit these in the inbox, the content loads unsanitized, allowing javascript: URLs to execute upon interaction. Requires blog submission enabled; results in JS execution for data exfiltration or modifications.

## Requirements

1. Target blog allows user submissions
2. Attacker can submit posts
3. Victim must edit the submission

## Defense

Defensive measures and detection strategies:

- Sanitize user-submitted content to strip javascript: URLs
- Enforce CSP on all dynamic pages including edit interfaces
- Log and review submission/edit actions for anomalies

## Objectives

1. Persist payload in victim's inbox
2. Execute JS during post edit
3. Compromise victim's account via session access

## Instructions

### Step 1: Access Submission Page

**Context**: Target a vulnerable blog.

Navigate to the blog's submission or 'suggest a post' page.

> Form loads if submissions are enabled.

### Step 2: Submit Malicious Post

**Context**: Embed the payload.

Add content with `<a href="javascript://x.com%0aalert(1);//">click me</a>` and submit.

> Post enters victim's inbox unsanitized.

### Step 3: Victim Views Inbox

**Context**: Wait for victim interaction.

Victim goes to `https://www.tumblr.com/inbox`.

> Malicious post visible.

### Step 4: Victim Edits Post

**Context**: Load payload into edit DOM.

Victim clicks 'edit', rendering the link.

> Edit page lacks CSP enforcement.

### Step 5: Trigger Payload

**Context**: Execute via interaction.

Victim clicks 'click me' and confirms 'open'.

> JS runs, e.g., alert(1).

### Step 6: Verify Impact

**Context**: Assess compromise.

Payload allows actions like cookie theft.

> Victim's session exploitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[dom-xss]]
- [[tumblr]]
