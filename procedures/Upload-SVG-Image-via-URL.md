---
tags:
  - file-upload
  - ssrf-like
  - web-vulnerability
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:12.076Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4a1efa0a-bc6e-4418-a8e1-2cb47aea94f0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-SVG-Image-via-URL

## Summary

This procedure describes attempting to upload an SVG image via URL in the Instacart store list background image field, exploiting format restrictions to trigger backend errors.

## Description

The Instacart image upload feature supports only JPEG and PNG, but allows URL inputs. Providing an SVG URL causes the rmagick library to fail during manipulation, leading to error responses. This step is key in the reconnaissance chain, as it sets up the disclosure without requiring file uploads. Targets the Ruby on Rails endpoint for list customization, assuming the list from prior steps.

## Requirements

1. Existing store list from previous procedure
2. Publicly accessible SVG file URL (e.g., hosted on a test server)
3. Developer tools in browser for request inspection

## Defense

Defensive measures and detection strategies:

- Input validation on URL formats before processing
- Sanitized error messages without path details
- WAF rules to block suspicious URL patterns

## Objectives

1. Invoke image processing with unsupported format
2. Generate server-side error during rmagick handling
3. Prepare for error response analysis

## Instructions

### Step 1: Access List Customization

**Context**: Open the background image settings for the list.

Edit the created list and navigate to the background image option.

> Interface shows upload field with URL input choice.

### Step 2: Input SVG URL

**Context**: Provide URL to trigger processing.

Select 'Add from URL' and enter SVG URL, e.g., https://example.com/test.svg, then submit.

> Backend fetches and attempts to process the file.

### Step 3: Submit Upload

**Context**: Force the validation and manipulation.

Click save or apply to initiate the upload process.

> Fails with error due to unsupported format.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[web]]
