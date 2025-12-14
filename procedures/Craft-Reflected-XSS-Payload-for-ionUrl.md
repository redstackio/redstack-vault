---
tags:
  - xss-payload
  - javascript
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 955ce793-e61e-494f-8da4-6e54a9f60009
created_at: '2025-12-14T03:47:23.552Z'
updated_at: '2025-12-14T03:47:23.552Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Reflected XSS Payload for ionUrl

## Summary

This procedure crafts a reflected XSS payload exploiting the weak URL validation in Evernote's ionUrl parameter, using a javascript: URI with a comment to bypass the substring check.

## Description

The payload leverages the fact that the validation uses `indexOf` for substring matching, allowing `javascript:alert(document.cookie)//https://www.evernote.com/` to pass while executing the JS first. This leads to arbitrary code execution in the victim's browser, enabling cookie theft or further attacks. Targets public shared note viewers.

## Requirements

1. Vulnerable /client/snv endpoint URL
2. Text editor for payload construction
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Enforce URL scheme whitelisting (only https:)
- Escape or reject non-standard protocols
- WAF rules to block javascript: in parameters

## Objectives

1. Build payload that evades substring check
2. Test execution in browser
3. Verify JS injection success

## Instructions

### Step 1: Construct Base Payload

**Context**: Create the malicious ionUrl.

Form the string: `javascript:alert(document.cookie)//https://www.evernote.com/`. The // comments out the rest, so JS runs first.

> Payload ready for parameter injection.

### Step 2: Append to Endpoint and Test

**Context**: Inject into view parameter.

Add `?view=after-save-note&ionUrl=[PAYLOAD]` to `https://www.evernote.com/shard/s1/client/snv`. Load in browser.

> Alert should pop with cookies; no redirect to invalid URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-payload]]
- [[JavaScript]]
- [[bypass]]
