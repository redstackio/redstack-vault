---
tags:
  - ssrf
  - path-disclosure
  - javascript
  - nextcloud
  - ios
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:39:09.539Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d981045f-c15f-40fd-a6e4-9b0c412b8a42
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-HTML-to-Reveal-App-Path

## Summary

This procedure accesses the uploaded manipulated HTML file in the Nextcloud iOS app to trigger JavaScript execution, revealing the local application path essential for SSRF exploitation.

## Description

By viewing the disguised HTML file in the app's local storage viewer, the onload JavaScript executes, writing the document.location to the page. This discloses the file:// path to the app's directory, enabling targeted SSRF requests. The scenario assumes prior upload success. Outcomes include visible path output, confirming executable content handling flaws.

## Requirements

1. Uploaded HTML payload from previous procedure
2. Nextcloud iOS app with local storage access
3. Viewer capable of rendering HTML/JS

## Defense

Defensive measures and detection strategies:

- Disable JavaScript in file viewers
- Sanitize rendered content to prevent script execution
- Monitor for path disclosure attempts in app telemetry

## Objectives

1. Trigger JavaScript to output app path
2. Capture the base path for file:// usage
3. Validate SSRF potential

## Instructions

### Step 1: Navigate to Uploaded File

**Context**: Locate the manipulated file in local storage.

Open the Nextcloud iOS app and browse to the local storage section.

> Select the disguised HTML file for viewing.

### Step 2: View File to Execute Payload

**Context**: Load the file to run the JavaScript.

Tap to open the file, allowing the SVG onload to execute document.write(document.location).

> Expected output: The application path (e.g., file:///var/mobile/Containers/Data/Application/.../) is displayed on screen.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[path-disclosure]]
- [[JavaScript]]
- [[nextcloud]]
- [[ios]]
