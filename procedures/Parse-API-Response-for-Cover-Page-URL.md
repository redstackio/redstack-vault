---
id: p4d5e6f7-g8h9-0123-defg-456789012345
tags:
  - response-parsing
  - data-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.337Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Parse-API-Response-for-Cover-Page-URL

## Summary

This procedure analyzes the API response from the IDOR request to extract the URL of the unauthorized offline publication's cover page.

## Description

The vulnerable Publitas API returns a JSON object containing a cover page URL when an invalid SOURCE_ID is used, often embedding user and publication IDs. Parsing involves inspecting the response body for keys like 'cover_url' or similar, using tools like jq or manual review. This step bridges the exploitation to actual content access, confirming sensitive data exposure.

## Requirements

1. Raw API response from previous step
2. JSON parsing tool (e.g., jq) or text editor
3. Knowledge of response structure

## Defense

Defensive measures and detection strategies:

- Sanitize API responses to exclude sensitive URLs for unauthorized requests
- Implement data loss prevention (DLP) on API outputs

## Objectives

1. Identify and isolate the cover page URL
2. Note embedded sensitive identifiers
3. Prepare for content retrieval

## Instructions

### Step 1: Capture Response

**Context**: Save the full API output.

Redirect curl output to a file: curl ... > response.json

### Step 2: Inspect JSON Structure

**Context**: Locate the URL field.

Open response.json and search for URL-related keys (e.g., "url": "https://cdn.publitas.com/cover/...").

### Step 3: Extract and Verify

**Context**: Copy the URL and check for IDs.

Note any user_id or pub_id in the URL path/query; validate it's not yours.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[response-parsing]]
- [[data-extraction]]
