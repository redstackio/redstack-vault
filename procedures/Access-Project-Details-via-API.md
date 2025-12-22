---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - api-access
  - project-details
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-api-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.905Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Project-Details-via-API

## Summary

This procedure retrieves project and translation details from the Weblate API as an anonymous user, exploiting the lack of permission enforcement to obtain metadata including file URLs for further exploitation.

## Description

Targeting the endpoint /api/components/{project}/{component}/translations/, this step sends an unauthenticated GET request to fetch JSON data. Despite Guest permissions being removed, the API returns full details due to improper handling in the Django permission layer, allowing reconnaissance of translation resources.

## Requirements

1. Accessible Weblate API on port 8000
2. curl or similar HTTP client
3. Known project and component names (e.g., testproject, testcomponent)

## Defense

Defensive measures and detection strategies:

- Add explicit anonymous user checks in API views
- Require API keys or JWT for all translation endpoints
- Alert on high-volume anonymous API calls

## Objectives

1. Obtain project metadata without authentication
2. Extract file URLs for downloads
3. Demonstrate API-UI permission discrepancy

## Instructions

### Step 1: Query Translations Endpoint

**Context**: Send GET request to fetch translation list and details.

Execute [[commands/curl-api-get]] to access the API:

```bash
curl -X GET "http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/"
```

> Expected: JSON with array of translations, including 'file_url' for languages like en_CA.

### Step 2: Parse Response for URLs

**Context**: Identify downloadable resources from the output.

Use jq or manual inspection to extract 'file_url' from the JSON.

> Expected: URL like /api/translations/testproject/testcomponent/en_CA/file/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-get]]

## Tools Used


## Tags

- [[api-access]]
- [[project-details]]
- [[bypass]]
