---
tags:
  - readermode
  - csp
  - nonce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - WebView
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.813Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2cd25b92-304e-4593-842c-2bc2390dbb8f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Activate-ReaderMode-in-Brave-iOS

## Summary

This procedure triggers the ReaderMode feature in Brave iOS on a loaded malicious page, causing the unescaped insertion of the author meta content into the ReaderMode template and replacement of placeholders like %READER-TITLE-NONCE%, leading to script execution.

## Description

ReaderMode in Brave iOS uses Swift code (ReaderModeUtils.swift) to process the original page and generate a new view at localhost:6571. The vulnerability arises from a commit relaxing the CSP to permit scripts with the %READER-TITLE-NONCE% and failing to escape HTML from the <meta name='author'> tag when filling %READER-CREDITS%. Activating ReaderMode executes the injected script in the context of the localhost page, which has access to cross-origin iframes and the uuidkey parameter for privileged access.

## Requirements

1. Malicious page loaded in Brave iOS
2. ReaderMode feature enabled (default in Brave)
3. Device with iOS and Brave installed

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in author meta content before template insertion
- Audit CSP changes and nonce usage in ReaderMode commits
- Log ReaderMode activations and monitor localhost:6571 traffic

## Objectives

1. Invoke ReaderMode to process the malicious meta content
2. Generate the vulnerable localhost page with uuidkey
3. Enable script execution context

## Instructions

### Step 1: Locate ReaderMode Button

**Context**: Identify the UI element to activate the feature.

In the address bar of the loaded page, look for the ReaderMode icon (often a 'Aa' or paragraph symbol).

> Ensure the page content is compatible with ReaderMode parsing.

### Step 2: Tap to Activate

**Context**: Trigger the processing pipeline in ReaderModeUtils.swift.

Tap the ReaderMode button to switch views.

> The browser will fetch and render the new page at http://localhost:6571/reader-mode?uri={encoded_uri}&uuidkey={generated_value}, inserting the unescaped author content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- readermode
- csp
- nonce
