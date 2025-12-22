---
id: proc-uuid-003
tags:
  - xss
  - discourse
  - post-injection
  - execution
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:37.872Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Submit-Malicious-URL-in-Discourse-Post

## Summary

This procedure covers submitting the crafted XSS payload in a Discourse post or comment, triggering the markdown parser to render and execute injected JavaScript in the victim's browser context.

## Description

Once the payload is ready, it is embedded in markdown image syntax within a forum post. When viewed, the parser generates vulnerable HTML, executing the onerror handler (e.g., alert(1) or $.getScript for external loads). This compromises sessions or steals data. Prerequisites include a user account on the target Discourse; outcomes range from pop-ups to full code execution, potentially leading to account takeover.

## Requirements

1. Registered user account on the target Discourse forum
2. Crafted payload from prior procedure
3. Victim access to view the post (e.g., public forum)

## Defense

Defensive measures and detection strategies:

- Patch Discourse to version fixing quote escaping (post-2015)
- Moderate posts for suspicious markdown patterns
- Implement client-side CSP to prevent JS execution from images

## Objectives

1. Deliver payload to trigger XSS on post render
2. Achieve arbitrary JS execution in victim sessions
3. Demonstrate impact like data theft or script loading

## Instructions

### Step 1: Prepare Post Content

**Context**: Embed the payload in valid markdown to blend in.

Create post text: "Check this image: ![Cool Image](http://example.com/path/to/image'onerror=alert(1);//.png)"

> Ensures it looks innocuous.

### Step 2: Submit to Forum

**Context**: Post or comment in a visible thread.

Log in to Discourse, navigate to a topic, and submit the post containing the markdown.

> The server processes and stores the markdown.

### Step 3: Trigger and Verify Execution

**Context**: Have a victim (or self in incognito) view the post.

Load the post URL in a browser; inspect for execution.

> Expected output: JS runs, e.g., alert(1) or network request to external script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[discourse]]
- [[post-injection]]
