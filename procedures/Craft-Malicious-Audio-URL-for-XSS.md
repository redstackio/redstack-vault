---
id: proc-uuid-002
tags:
  - xss
  - payload-crafting
  - audio-parser
  - attribute-injection
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
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.909Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Audio-URL-for-XSS

## Summary

This procedure crafts a malicious audio URL exploiting the lack of single quote sanitization in Discourse's audio parser, injecting an onerror attribute to execute arbitrary JavaScript in the victim's browser.

## Description

The audio_onebox.rb parser in Discourse's onebox engine inserts URLs directly into <audio> tags without escaping quotes, allowing attackers to close the src attribute and inject event handlers. Posting such a URL in a forum thread triggers the parser, rendering malicious HTML. The target is any Discourse instance; outcomes include JS execution for session hijacking or data theft.

## Requirements

1. Forum posting access
2. Knowledge of HTML attribute injection
3. Test environment (local Discourse or vulnerable instance)

## Defense

Defensive measures and detection strategies:

- Sanitize URLs by escaping special characters in all onebox parsers
- Validate embedded media URLs against whitelists
- Enable strict CSP to block unsafe-inline scripts

## Objectives

1. Inject onerror handler via crafted URL
2. Execute JavaScript in forum context
3. Demonstrate potential for account takeover

## Instructions

### Step 1: Design Payload

**Context**: Create a URL that breaks out of the src attribute using a single quote.

Form the base URL as `http://host/path'onerror=alert(1);//k.mp3`, where the quote closes src and injects onerror.

> The '//' comments out the rest to avoid syntax errors.

### Step 2: Post in Forum

**Context**: Trigger the onebox parser by embedding the URL.

In a Discourse thread, post a message containing the malicious URL, e.g., "Check this audio: http://host/path'onerror=alert(1);//k.mp3".

> The parser will generate <audio src="http://host/path'onerror=alert(1);//k.mp3">, executing alert(1) on load error.

### Step 3: Verify Execution

**Context**: Confirm XSS by observing JS behavior.

Load the thread in a browser and check for the alert popup or console errors triggering the handler.

> Success: Arbitrary code runs, e.g., replace alert(1) with document.cookie stealing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
