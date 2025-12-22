---
id: proc-trigger-preview-xss
tags:
  - xss-execution
  - preview-engine
  - opengraph
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
updated_at: '2025-12-14T03:47:12.759Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Preview-and-Observe-XSS

## Summary

This procedure covers triggering the Discourse preview engine with the injected URL and observing the resulting XSS execution, confirming arbitrary JavaScript injection via OpenGraph metadata.

## Description

Once the malicious URL is in the title, the preview engine automatically fetches the page and renders OpenGraph data (title, description) without escaping HTML/JS, injecting the payload into the DOM. Saving the topic stores the vulnerability for persistent execution on view.

## Requirements

1. Injected malicious URL in composer
2. Attacker server responding with payload-laden OpenGraph
3. Browser developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Escape HTML in all rendered metadata
- Block or proxy external fetches with content security policy
- Log and alert on suspicious preview requests to non-standard domains

## Objectives

1. Execute JavaScript in preview context
2. Verify persistence in saved topic
3. Demonstrate impact on viewers

## Instructions

### Step 1: Activate Preview

**Context**: Wait for or force the engine to parse the link and fetch metadata.

Interact with the form or wait ~1-2 seconds for auto-preview.

> The preview pane updates with fetched content; inspect for injected <script> tags.

### Step 2: Confirm Execution

**Context**: Observe payload firing and save to test storage.

Add body text if needed, click 'Create Topic'; reload the topic URL.

> Alert 'XSS' pops or console logs; use payload like ?XSS55555 for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[stored-xss]]
