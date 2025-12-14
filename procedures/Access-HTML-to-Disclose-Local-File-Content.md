---
tags:
  - ssrf
  - file-disclosure
  - iframe
  - nextcloud
  - ios
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T04:39:09.531Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 10b72acf-87ed-4316-b897-a1fc8e4ce4c7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Data from Local System]]'
---
# Access-HTML-to-Disclose-Local-File-Content

## Summary

This procedure views the uploaded iframe HTML in the Nextcloud iOS app to trigger SSRF, loading and displaying the content of an arbitrary local file.

## Description

Accessing the iframe payload causes the app to fetch the targeted local file via file://, exposing its contents in the iframe without proper restrictions. This completes the SSRF chain for sensitive data exposure. Scenario: Post-upload in vulnerable app. Outcomes: Visible file content, proving arbitrary read capability.

## Requirements

1. Uploaded iframe HTML from previous procedure
2. Target file present at specified path
3. App viewer supporting iframes

## Defense

Defensive measures and detection strategies:

- Restrict local protocol access in webviews
- Monitor iframe loads for file:// usage
- Implement content security policies in app rendering

## Objectives

1. Execute SSRF to load local file
2. Display file contents via iframe
3. Confirm sensitive data exposure

## Instructions

### Step 1: Locate and Open Iframe File

**Context**: Navigate to the payload in local storage.

In the Nextcloud iOS app, go to local storage and select the iframe HTML file.

> Tap to view, initiating the load.

### Step 2: Observe File Content Disclosure

**Context**: The iframe triggers the SSRF request.

Allow the page to render; the iframe should display the target file's content.

> Expected output: Content of ssrfpoc.txt (e.g., 'test ssrf') appears in the 400x400 iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[file-disclosure]]
- [[iframe]]
- [[nextcloud]]
- [[ios]]
