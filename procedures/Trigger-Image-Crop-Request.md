---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - crop-trigger
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.503Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Image-Crop-Request

## Summary

This procedure performs a crop action in the editor to generate the vulnerable /edit/process request with a=crop parameters.

## Description

Selecting a crop area and applying it sends a GET request to /edit/process, passing user-controlled parameters including 'y' directly to GraphicsMagick without proper escaping, setting up the injection point.

## Requirements

1. Image editor open
2. Proxy intercepting

## Defense

Defensive measures and detection strategies:

- Sanitize crop parameters before passing to shell commands
- Use safe APIs for image processing

## Objectives

1. Generate interceptable request
2. Include vulnerable y parameter
3. Confirm parameters in proxy

## Instructions

### Step 1: Select Crop Area

**Context**: Define a crop rectangle to simulate legitimate use.

**Command** (UI action):

Drag to select random rectangle on image.

> Area highlighted. Expected output: Crop tool active.

### Step 2: Apply Crop

**Context**: Submit to trigger backend processing.

**Command** (UI action):

Click 'Apply'.

> Request sent and intercepted. Expected output: Parameters like y= numeric value in Burp.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- image-crop
