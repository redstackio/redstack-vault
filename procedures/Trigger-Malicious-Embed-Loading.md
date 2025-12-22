---
tags:
  - xss
  - iframe
  - javascript-execution
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:08:55.611Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: ff4d3b23-b0e3-4f52-9174-398d0df385a6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Malicious-Embed-Loading

## Summary

This procedure waits for and facilitates the loading of the malicious embed in IRCCloud, where the iframe src is set to the javascript: URL from the Mastodon API, executing in the client context.

## Description

Upon link interaction, IRCCloud queries the Mastodon API, parses the JSON, and creates an iframe with src = malicious_url + '/embed'. The javascript: protocol bypasses typical restrictions, allowing access to parent.document.cookie. Targets browser-based IRC clients; requires prior link send and enabled embeds. Outcome: Arbitrary JS runs, enabling data theft.

## Requirements

1. Victim viewing the malicious link in IRCCloud
2. Mastodon API responding with javascript: URL
3. No browser CSP blocking iframe JS

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP to block javascript: URLs and inline scripts in iframes
- Validate and sanitize all embed URLs before iframe creation

## Objectives

1. Initiate API query and iframe creation
2. Execute JS payload in embed context
3. Access parent document for cookie theft

## Instructions

### Step 1: Monitor Victim Interaction

**Context**: Wait for the client to process the link.

Observe channel activity; IRCCloud automatically queries the API when the link is rendered or hovered.

> Log API hits on your Mastodon server to confirm query.

### Step 2: Verify Iframe Execution

**Context**: Ensure the malicious src loads without interruption.

The client appends '/embed' to the URL and sets iframe src; JS executes, targeting top.document.body.

> In victim browser dev tools, check for iframe creation and JS run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
