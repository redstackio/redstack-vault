---
tags:
  - id-extraction
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:29:44.609Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a6d7687d-fd55-4e5e-8305-95b90e6d5863
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Extract-Course-ID-from-Response

## Summary

This procedure parses the metadata edit response to retrieve the unique course ID generated during upload, essential for locating the deployed webshell.

## Description

The response HTML contains 'strCourseId' in attributes like NavigatingURL of the ReuploadCourse link. Searching for this string yields the GUID (e.g., F6BAC72B45D64B34ACB662BB001D8523), which forms the path to the shell.

## Requirements

1. Captured HTML response from metadata endpoint
2. Text editor or Burp search functionality
3. Knowledge of response structure

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove sensitive IDs from client-side responses
- Use server-side rendering for metadata
- Log ID generations and associate with users

## Objectives

1. Locate strCourseId in HTML
2. Copy the GUID value
3. Validate format (32-char hex)

## Instructions

### Step 1: Search Response

**Context**: Inspect the intercepted response body.

In Burp or editor, search for 'strCourseId'.

> Expected output: Match in <a href...NavigatingURL...strCourseId=F6BAC72B45D64B34ACB662BB001D8523>

### Step 2: Extract and Note ID

**Context**: Isolate the value for use.

Copy the GUID after strCourseId=.

> Expected output: Clean ID string ready for URL construction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- id-extraction
- discovery
