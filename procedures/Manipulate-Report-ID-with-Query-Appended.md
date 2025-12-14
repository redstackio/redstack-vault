---
id: proc-002
tags:
  - manipulation
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/query-appended-report-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.210Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Report-ID-with-Query-Appended

## Summary

This procedure manipulates the report_id parameter by appending a '?' to alter the internal JSON fetch URL, demonstrating the endpoint's lack of strict input sanitization and setting up for path traversal.

## Description

By encoding and appending '?' to report_id (e.g., 99698?), the /bugs endpoint constructs an XHR URL like /reports/99698?.json. This reveals that the parameter is directly interpolated into the path without proper validation, allowing query string injection. This is a precursor to more severe traversals, targeting the Ruby on Rails application's routing in a web environment.

## Requirements

1. Authenticated HackerOne session
2. Knowledge of a valid report_id
3. Tool for URL encoding (built-in in curl)

## Defense

Defensive measures and detection strategies:

- Validate report_id as a strict integer using regex or type casting
- Sanitize parameters before path construction to prevent injection
- Log and alert on non-numeric report_id values

## Objectives

1. Inject query string into internal URL
2. Confirm parameter interpolation vulnerability
3. Prepare for directory escape

## Instructions

### Step 1: Append Encoded Query

**Context**: Modify report_id to include %3F (encoded '?') to alter the fetch path.

**Command** ([[commands/query-appended-report-id]]):
```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

> Expected output: XHR to /reports/99698?.json with 200 OK, showing the appended query affects URL parsing without error.

### Step 2: Inspect Altered Response

**Context**: Verify the change propagates to the internal request.

**Command** (Inspection):
```bash
# Capture with proxy or dev tools
```

> Confirm the .json endpoint accepts the modified path, indicating no validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/query-appended-report-id]]

## Tools Used


## Tags

- manipulation
- web
- injection
