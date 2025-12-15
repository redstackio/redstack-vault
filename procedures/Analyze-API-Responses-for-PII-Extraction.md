---
tags:
  - data-extraction
  - pii-analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-waitlist-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:45.222Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7c9ca07f-b005-4f68-8e35-21f921ef696e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Analyze-API-Responses-for-PII-Extraction

## Summary

Review and parse the JSON responses from the brute-forced API calls to extract sensitive user data such as mobile numbers, names, zipcodes, and IDs, compiling evidence of the information disclosure.

## Description

Post-brute-force, this procedure focuses on filtering successful responses (200 OK) and extracting key PII fields from the JSON payloads. It demonstrates the vulnerability's impact by aggregating data across users. Use in reporting or further analysis; no additional tools beyond response viewer needed.

## Requirements

1. Burp Intruder results with responses
2. JSON parsing knowledge or tool (e.g., jq for command-line)
3. Spreadsheet for data compilation

## Defense

Defensive measures and detection strategies:

- Redact sensitive fields in API responses (e.g., omit phoneNumber)
- Encrypt PII at rest and in transit
- Audit logs for data access patterns

## Objectives

1. Identify and collect all disclosed PII
2. Validate data completeness and accuracy
3. Document impact for remediation

## Instructions

### Step 1: Filter Intruder Results

**Context**: Isolate successful responses indicating valid emails.

In Burp Intruder, sort results by status code (200) and response length; inspect hits.

> Look for JSON keys like 'phoneNumber', 'zipcode', 'name', '_id'.

### Step 2: Extract Data with Manual or curl Replay

**Context**: For detailed verification, replay specific requests using [[commands/curl-waitlist-lookup]].

Execute [[commands/curl-waitlist-lookup]] for a hit email:

```bash
curl -X POST https://website-api.production.curve.app/api/waitlist/us \
  -H "Content-Type: application/json" \
  -d '{"email":"valid@example.com"}'
```

> Parse output: e.g., pipe to jq '.phoneNumber' for extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/curl-waitlist-lookup]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[data-extraction]]
- [[pii-analysis]]
