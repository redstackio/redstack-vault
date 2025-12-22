---
tags:
  - recon
  - api
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/access-basic-api-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:11.125Z'
sub_techniques: []
id: 5f794200-4f4c-43d3-9e2b-c7a823103426
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Starbucks-API-Endpoint

## Summary

This procedure involves accessing the Starbucks OpenAPI search endpoint to identify parameters like siteBaseUrl that may be vulnerable to injection attacks such as XSS.

## Description

In a web application security assessment, the first step is to map out public-facing endpoints and their accepted parameters. For the Starbucks API at openapi.starbucks.com/searchasyoutype/v1/search, parameters including x-api-key, query, partnerid, and siteBaseUrl are used. Testing reveals that siteBaseUrl reflects user input without sanitization, setting the stage for XSS exploitation. This procedure assumes access to API keys from prior reconnaissance or testing.

## Requirements

1. Public internet access to the endpoint
2. Valid x-api-key and partnerid values (redacted in POCs)
3. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement API gateway with parameter validation
- Log and monitor unusual parameter values in requests
- Use WAF rules to block suspicious URL encodings like %0a

## Objectives

1. Confirm endpoint accessibility and parameter acceptance
2. Observe response structure for reflection points
3. Establish baseline for further testing

## Instructions

### Step 1: Send Initial Request

**Context**: Craft a basic GET request to the endpoint with standard parameters to verify functionality.

**Command** ([[commands/access-basic-api-endpoint]]):
```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://example.com"
```

> This command sends a query for 'coffe' and sets a benign siteBaseUrl. Expected output is a JSON response with search results, confirming the endpoint processes the siteBaseUrl parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/access-basic-api-endpoint]]

## Tools Used


## Tags

- recon
- api
- endpoint-discovery
