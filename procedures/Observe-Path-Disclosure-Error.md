---
tags:
  - information-disclosure
  - error-leak
  - reconnaissance
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
updated_at: '2025-12-14T17:26:12.072Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 941db24f-c706-45dc-a6cb-73ad9512aa95
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Observe-Path-Disclosure-Error

## Summary

This procedure involves capturing and analyzing the JSON error response from the failed SVG upload to disclose internal server file paths in Instacart's rmagick processing.

## Description

Upon SVG upload failure, the Ruby on Rails application returns a JSON error embedding the full temporary file path from rmagick's exception. This leaks filesystem structure, aiding reconnaissance for further attacks like path traversal. Use browser dev tools or proxy to inspect the response. The vulnerability stems from unsanitized error messages in image manipulation.

## Requirements

1. Failed upload from previous procedure
2. Browser developer tools or network proxy (e.g., Burp Suite)
3. Knowledge of JSON parsing for error fields

## Defense

Defensive measures and detection strategies:

- Custom error handlers to strip paths from messages
- Logging errors without exposure to clients
- Monitoring for repeated failed uploads from same IP

## Objectives

1. Extract leaked file paths from error payload
2. Map server environment for reconnaissance
3. Identify temporary directories and structure

## Instructions

### Step 1: Inspect Network Response

**Context**: Capture the AJAX response from the upload attempt.

Open browser dev tools (F12), go to Network tab, and retry the upload.

> Locate the failed request (e.g., POST to /lists/update).

### Step 2: Analyze JSON Error

**Context**: Parse the response body for rmagick details.

View the response JSON and search for error strings containing paths.

> Example: {"error": "ImageMagick error: no decode delegate for this image format </tmp/uploads/xyz.svg>"}.

### Step 3: Document Disclosed Path

**Context**: Record the path for analysis.

Note the full path, e.g., /var/www/instacart/tmp/uploads/, and infer server config.

> Path reveals temporary storage and potential attack vectors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[Reconnaissance]]
