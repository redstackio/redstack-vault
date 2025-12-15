---
tags:
  - bypass
  - referer
  - double-intent
type: procedure
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.489Z'
sub_techniques: []
id: 57ebea9c-91e1-4823-9f74-80344343dddf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Referer-Restrictions-with-Intent

## Summary

This procedure uses Twitter's intent functionality twice to set the Referer header to twitter.com, enabling the unescaped processing of the original_referer payload.

## Description

After the initial intent load, the 'Return to previous site' link reloads the page from within Twitter, setting Referer: twitter.com. This bypasses external referer checks and t.co interference, inserting the payload 'as is' into the page.

## Requirements

1. Victim in intent dialog
2. Access to 'Return to previous site' link
3. Twitter session active

## Defense

Defensive measures and detection strategies:

- Enforce referer policy (strict-origin)
- Escape all dynamic attributes
- Audit intent reload patterns

## Objectives

1. Set valid Referer
2. Process payload without filtering
3. Insert into DOM

## Instructions

### Step 1: Initial Intent Invocation

**Context**: Open dialog first time.

Load sets up the environment.

### Step 2: Trigger Return Link

**Context**: Reload with proper Referer.

Click 'Return to previous site' to invoke intent second time.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
