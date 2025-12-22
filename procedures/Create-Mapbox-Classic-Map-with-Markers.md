---
tags:
  - mapbox
  - map-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.385Z'
sub_techniques: []
id: 0b3152f6-76a7-41d0-9386-ee542ef36679
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Mapbox-Classic-Map-with-Markers

## Summary

This procedure outlines creating a basic map using the Mapbox online classic map editor and adding markers, setting the stage for injecting malicious payloads in subsequent steps of a stored XSS attack.

## Description

In the context of exploiting a stored XSS vulnerability in Mapbox v3/v4 classic maps, this initial step involves accessing the public-facing Mapbox editor to build a map. The editor runs on the web platform and requires a Mapbox account. Markers are added via the UI, which later allows title injection. This step ensures the map is ready for payload insertion without triggering defenses prematurely. Expected outcome: A functional map with placeholders for exploitation.

## Requirements

1. Valid Mapbox account with access to the classic map editor
2. Web browser with JavaScript enabled
3. Internet connectivity to mapbox.com

## Defense

Defensive measures and detection strategies:

- Monitor Mapbox account activity for unusual map creations
- Implement rate limiting on editor usage
- Log marker additions for anomaly detection

## Objectives

1. Establish a malicious map as the vector for XSS storage
2. Prepare markers for payload injection
3. Validate map functionality before exploitation

## Instructions

### Step 1: Access Mapbox Classic Editor

**Context**: Log in to Mapbox and navigate to the classic map editor to start a new project.

No specific command; use the web UI at https://www.mapbox.com/map-editor/ (classic version).

> Browser navigation to the editor; successful login indicated by dashboard access.

### Step 2: Build Map and Add Markers

**Context**: Create a new map layer and add at least one marker to the map canvas.

Use the editor's drag-and-drop interface to place markers.

> Markers appear on the map preview; titles are editable fields ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mapbox]]
- [[web-exploit]]
