---
id: proc-uuid-2
tags:
  - bypass
  - xss
  - flash
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
updated_at: '2025-12-13T23:52:55.639Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass GET Parameter Scrubbing in Flash

## Summary

This procedure crafts a GET parameter for the flashmediaelement.swf file that evades the built-in scrubbing mechanism by using invalid URL escapes, allowing a malicious 'jsinitfunction' parameter to persist in flashVars for XSS payload delivery.

## Description

The SWF attempts to delete dangerous GET parameters like 'jsinitfunction' from flashVars during parsing. However, Flash Player's lenient URL decoding strips invalid escapes (e.g., %gn to nothing), causing a mismatch: the scrubbing checks the raw name while flashVars uses the cleaned version. This 'GET Killer' bypass enables injection. Target: WordPress sites with direct SWF access. Prerequisites: SWF analysis from prior step. Outcome: Unsanitized parameter available for JS calls.

## Requirements

1. Knowledge of target SWF parameter names from analysis
2. URL encoding capabilities
3. Vulnerable WordPress instance

## Defense

Defensive measures and detection strategies:

- Block direct SWF access with Content-Disposition: attachment
- Validate all GET params server-side before serving SWF
- Log and alert on malformed URL parameters

## Objectives

1. Preserve malicious parameter in flashVars
2. Enable payload injection without deletion
3. Set up for subsequent blacklist bypass

## Instructions

### Step 1: Craft Malicious Parameter Name

**Context**: Create a name that mismatches scrubbing logic.

Use 'jsinitfunctio%gn' – Flash cleans to 'jsinitfunction', but scrubber sees raw and skips deletion.

**Expected Output**: Parameter added to URL without triggering delete.

### Step 2: Test Parameter Persistence

**Context**: Verify in browser dev tools or decompiler simulation.

Append to SWF URL: ?jsinitfunctio%gn=test

> Observe flashVars contains 'jsinitfunction': 'test'.

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
- [[xss]]
