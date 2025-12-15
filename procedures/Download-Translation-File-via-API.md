---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - file-download
  - translation-exposure
  - api-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-file-download]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.903Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Translation-File-via-API

## Summary

This procedure downloads a full translation file from the Weblate API using the file URL obtained from project details, allowing unauthorized exposure of potentially sensitive translation content as an anonymous user.

## Description

Using the endpoint /api/translations/{project}/{component}/{language}/file/, this step performs an unauthenticated GET request to retrieve the raw translation file (e.g., .po format). The API's failure to enforce Guest permission removal enables this data exfiltration, contrasting with UI protections.

## Requirements

1. file_url from previous API response
2. curl for HTTP download
3. Write permissions on local filesystem for output file

## Defense

Defensive measures and detection strategies:

- Restrict file download endpoints to authenticated users only
- Validate permissions in file-serving views
- Log and block suspicious file access patterns

## Objectives

1. Exfiltrate translation file content
2. Confirm full unauthorized access
3. Assess potential data exposure

## Instructions

### Step 1: Request File Download

**Context**: Fetch the translation file using the extracted URL.

Execute [[commands/curl-file-download]] with the specific endpoint:

```bash
curl -X GET "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/" -o translation.po
```

> Expected: Binary download of the .po file containing all translation strings.

### Step 2: Validate Downloaded Content

**Context**: Inspect the file to confirm sensitivity.

Open translation.po in a text editor to review contents.

> Expected: Full list of translatable strings; no errors in download.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-file-download]]

## Tools Used


## Tags

- [[file-download]]
- [[translation-exposure]]
- [[api-bypass]]
