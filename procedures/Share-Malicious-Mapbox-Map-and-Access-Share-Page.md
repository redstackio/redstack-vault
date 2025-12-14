---
tags:
  - map-sharing
  - xss-trigger
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
updated_at: '2025-12-14T03:15:47.377Z'
sub_techniques: []
id: 08fdea01-a4d8-4320-86ec-d11790c0a803
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Malicious-Mapbox-Map-and-Access-Share-Page

## Summary

This procedure covers generating a share URL for the malicious Mapbox map and verifying the XSS payload's rendering on the share page, where it becomes executable due to DOM insertion.

## Description

After injecting the payload, save the map and use the share feature to create a public URL like https://a.tiles.mapbox.com/v4/[map-id]/page.html?access_token=.... Accessing the share page loads /v3/embed/share.js or /v4/embed/share.js, which processes marker titles via the vulnerable stripHTML function, decoding and executing the payload on image load error. This step confirms persistence before victim distribution. Target: *.tiles.mapbox.com. Outcomes: Functional share URL with payload in DOM.

## Requirements

1. Saved Mapbox classic map with injected payload
2. Access token for sharing (auto-generated)
3. Web browser for testing the share page

## Defense

Defensive measures and detection strategies:

- Audit share.js for entity decoding issues
- Restrict share URLs to authenticated users
- Scan shared maps for XSS patterns pre-publication

## Objectives

1. Expose the stored payload via public share URL
2. Validate rendering and potential execution on share page
3. Prepare for victim delivery

## Instructions

### Step 1: Generate Share URL

**Context**: Use the Mapbox editor's share button to create and copy the public URL.

Click 'Share' in the editor and select 'Public URL'.

> URL format: https://a.tiles.mapbox.com/v4/[map-id]/page.html?access_token=...; copy for distribution.

### Step 2: Load and Inspect Share Page

**Context**: Visit the share URL to check if marker titles render with the payload.

Open the URL in a browser and inspect the DOM for the list of titles.

> Payload appears as <img src=x onerror=alert(1) " in the page source; alert may trigger if not sanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[web]]
