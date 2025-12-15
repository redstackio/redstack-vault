---
id: proc-vimeo-copy-track-id-3
tags:
  - network-inspection
  - id-extraction
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.812Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Copy-Track-ID-from-Cart-Request

## Summary

This procedure inspects the POST request from the add-to-cart action to extract the track_id parameter, which is key to bypassing download permissions.

## Description

In the Vimeo exploit, the track_id is exposed in the /cart/music POST request body or query parameters during cart addition for paid tracks. Using browser tools, copy this ID (e.g., track_id=110947). This enables direct access to download endpoints without purchase validation. Target environment is web-based; requires prior cart interaction.

## Requirements

1. Captured POST request from add-to-cart step.
2. Browser DevTools or proxy tool for inspection.
3. Basic knowledge of HTTP request parsing.

## Defense

Defensive measures and detection strategies:

- Avoid exposing internal IDs in client-side requests; use server-generated tokens.
- Audit network traffic for repeated cart additions without checkout.
- Encrypt or hash sensitive parameters in transit.

## Objectives

1. Locate and copy the track_id from the request.
2. Validate the ID corresponds to a paid track.
3. Prepare for download URL construction.

## Instructions

### Step 1: Inspect POST Request

**Context**: Analyze the network tab to find the /cart/music request.

In DevTools Network tab, locate the POST to /cart/music triggered by add-to-cart.

> Click the request to view details; track_id appears in the Request payload or Form Data section.

### Step 2: Extract and Copy ID

**Context**: Isolate the track_id value for reuse.

Copy the value of track_id (e.g., 110947) from the parameters.

> Store it securely; verify by checking if it's a numeric ID for the selected track.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- network-inspection
- id-extraction
