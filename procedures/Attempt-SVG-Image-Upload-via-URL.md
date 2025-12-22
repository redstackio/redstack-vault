---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - information-disclosure
  - file-upload
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:10.061Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Attempt-SVG-Image-Upload-via-URL

## Summary

This procedure describes uploading an invalid SVG image via a remote URL in the Instacart store list background feature to trigger a processing error in the rmagick library.

## Description

The Instacart application uses Ruby on Rails with rmagick for image processing. By providing a URL to an SVG file, which is unsupported, the library fails during temporary file handling, leading to the next step's error disclosure. This step exploits the URL-based upload endpoint without file selection, relying on remote fetching.

## Requirements

1. Existing store list from prior step
2. Accessible remote SVG file (e.g., hosted on a public server)
3. Web browser developer tools for monitoring requests

## Defense

Defensive measures and detection strategies:

- Validate and sanitize input URLs for supported formats before processing
- Restrict upload sources to whitelisted domains
- Log and alert on failed image processing attempts

## Objectives

1. Initiate remote image fetch and processing
2. Force rmagick failure on unsupported SVG format
3. Set up conditions for error message leakage

## Instructions

### Step 1: Access Background Image Settings

**Context**: Open the upload interface for the store list.

Edit the created store list and navigate to the background image customization section.

### Step 2: Input Remote SVG URL

**Context**: Provide an invalid image source to trigger failure.

In the URL field for background image, enter a link to an SVG file, such as https://example.com/test.svg, and submit the form.

### Step 3: Submit Upload Request

**Context**: Send the request to the backend endpoint.

Click 'Save' or 'Upload' to process the URL.

**Expected Output**: Server-side processing attempt with immediate failure response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- file-upload
- web
