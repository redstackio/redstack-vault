---
id: proc-003
tags:
  - path-traversal
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/path-traversal-escape]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:30.206Z'
sub_techniques:
  - '[[T1083.002]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Perform-Path-Traversal-to-Escape-Directory

## Summary

This procedure uses encoded '../' sequences in report_id to traverse out of the /reports directory, enabling access to arbitrary root-level paths without CSRF protection.

## Description

The report_id is not validated as an integer, allowing '../' (encoded as %2F..%2F) to navigate up directories. Setting report_id to ../../../99698? results in an internal GET to /99698?.json, bypassing the /reports restriction and exposing the request to CSRF if delivered via HTML. This exploits the Rails path handling in the web app.

## Requirements

1. Valid session cookie
2. URL encoder for '../' sequences
3. Target subject parameter

## Defense

Defensive measures and detection strategies:

- Canonicalize paths and block traversal sequences
- Restrict internal fetches to /reports/* only
- Implement integer casting for report_id with error on failure

## Objectives

1. Escape /reports directory
2. Trigger root-level GET without CSRF
3. Confirm arbitrary path access

## Instructions

### Step 1: Construct Traversal Payload

**Context**: Encode multiple '../' to reach root and append original manipulation.

**Command** ([[commands/path-traversal-escape]]):
```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2F99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

> Expected output: Internal GET to /99698?.json with CSRF token in header, succeeding as root request.

### Step 2: Validate Escape

**Context**: Check if path resolution hits unintended endpoints.

**Command** (Test variation):
```bash
# Adjust traversal depth if needed
```

> Success if no 404 and request processes from root.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- [[T1083.002]] Software Discovery

## Commands Used

- [[commands/path-traversal-escape]]

## Tools Used


## Tags

- path-traversal
- web
- escape
