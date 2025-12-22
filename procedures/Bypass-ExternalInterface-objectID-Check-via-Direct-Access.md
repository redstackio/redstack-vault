---
id: proc-uuid-4
tags:
  - bypass
  - externalinterface
  - chrome
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
updated_at: '2025-12-13T23:52:55.632Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass ExternalInterface.objectID Check via Direct Access

## Summary

This procedure exploits browser behavior to set the ExternalInterface.objectID automatically when accessing the SWF directly, bypassing the need for manual embed code and enabling JS calls from the SWF to the page context.

## Description

The SWF checks for ExternalInterface.objectID before calling JS functions like jsinitfunction to prevent unauthorized execution. Direct URL access in Chrome generates an automatic <embed> tag with an 'id' attribute, populating objectID. This SAME Origin Method Execution (SOME) bug allows cross-context calls. Prerequisites: Crafted URL with prior bypasses. Outcome: SWF can execute payloads in site origin.

## Requirements

1. Chrome browser (for auto-embed feature)
2. Direct access to SWF permitted
3. Payload-ready URL

## Defense

Defensive measures and detection strategies:

- Serve SWF with no-cache and attachment headers
- Implement Content Security Policy blocking Flash
- Remove or patch MediaElement Flash components

## Objectives

1. Set objectID without custom embedding
2. Enable ExternalInterface.call to page JS
3. Complete the execution chain

## Instructions

### Step 1: Prepare Direct URL

**Context**: Combine prior bypasses into full URL.

Base: https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?

**Expected Output**: URL ready for access.

### Step 2: Load in Browser

**Context**: Trigger auto-embed.

Navigate to the URL in Chrome.

> Inspect element: See generated <embed id="..."> setting objectID.

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
- [[chrome]]
