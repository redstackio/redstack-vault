---
id: proc-uuid-2
tags:
  - xss
  - input-manipulation
  - shopify
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
updated_at: '2025-12-14T03:15:36.305Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Modify-Upload-Field-to-URL-Type

## Summary

This procedure changes the artwork upload input from file to URL type, bypassing restrictions to allow javascript: scheme injection for stored XSS.

## Description

Targeting the custom gift card design upload on Shopify's site, this step manipulates the input selector to enable URL entry. This exploits insufficient validation in the web interface, storing the input for later rendering on checkout. Prerequisites include having the design page loaded; outcome is an active URL field vulnerable to payload insertion.

## Requirements

1. Active design interface from previous access
2. Browser developer tools for inspection if needed
3. No network restrictions

## Defense

Defensive measures and detection strategies:

- Enforce strict input type validation on client-side
- Log changes to upload field types

## Objectives

1. Switch upload to URL mode
2. Expose vulnerability for payload entry
3. Maintain design session integrity

## Instructions

### Step 1: Locate Upload Field

**Context**: Identify the artwork upload section in the design interface.

No command required.

> In the design page, find the file upload dropdown or selector for artwork.

### Step 2: Change to URL Type

**Context**: Alter the input to accept URLs instead of files.

No command required; manual UI interaction.

> Select 'URL' from the upload type options. The field should now prompt for a URL input without errors.

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
- [[input-manipulation]]
- [[shopify]]
