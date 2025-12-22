---
tags:
  - local-file-read
  - observation
type: procedure
tools:
  - '[[tools/Lavf-55.48.100]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/server-get-local-file-content]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:08:48.228Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 62456478-95cb-439c-9af6-3b6212bbddd9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Observe-Local-File-Read

## Summary

This procedure examines server logs to capture leaked local file contents from malformed requests caused by the concat protocol in Lavf processing.

## Description

The concat operation appends local file data (e.g., first line of /etc/passwd) to remote URLs, resulting in anomalous GET requests with file content in the query string. This confirms the local file read vulnerability.

## Requirements

1. Controlled server logs from prior concat upload
2. Log parsing tools
3. Awareness of expected file content patterns

## Defense

Defensive measures and detection strategies:

- Log analysis for query strings containing file-like data (e.g., user:pass patterns)
- Restrict media processing to sandboxed environments
- Alert on protocol misuse in processing logs

## Objectives

1. Extract and verify leaked file data
2. Assess sensitivity of accessed files
3. Document proof of exploitation

## Instructions

### Step 1: Monitor for Malformed Request

**Context**: Look for GET requests with appended file content.

**Command** ([[commands/server-get-local-file-content]]):
```bash
tail -f /var/log/nginx/access.log | grep "GET ?root:x:0:0:root:/root:/bin/bash HTTP/1.1" | grep "Lavf/55.48.100"
```

> Expected: 400 Bad Request (173 bytes), query revealing root user entry from /etc/passwd.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/server-get-local-file-content]]

## Tools Used

- [[tools/Lavf-55.48.100]]

## Tags

- local-file-read
- logging
