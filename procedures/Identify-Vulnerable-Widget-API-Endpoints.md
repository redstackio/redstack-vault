---
tags:
  - recon
  - web-endpoints
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
id: ad9b073e-89d0-44a5-bfe9-3901dcb354fb
created_at: '2025-12-14T03:15:26.586Z'
updated_at: '2025-12-14T03:15:26.586Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Widget-API-Endpoints

## Summary

This procedure involves examining public-facing widget API endpoints to identify query parameters that may be susceptible to injection attacks like XSS.

## Description

In the context of Zomato's widget APIs, this step reviews the endpoints https://www.zomato.com/widgets/all_collections.php and https://www.zomato.com/widgets/o2.php. The goal is to map out parameters such as city_id and language_id for subsequent testing. This reconnaissance helps pinpoint potential entry points for reflected XSS by understanding how user input is handled in the responses, which are likely embedded as scripts or HTML in web pages.

## Requirements

1. Internet access to reach public endpoints
2. Web browser or curl for initial probing
3. Basic knowledge of URL parameters and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement API documentation to limit endpoint exposure
- Use web application firewalls (WAF) to monitor unusual parameter testing
- Log and alert on repeated requests to widget endpoints with malformed parameters

## Objectives

1. Catalog accessible widget API endpoints
2. Identify query parameters for input testing
3. Establish baseline for vulnerability scoping

## Instructions

### Step 1: Probe Endpoints

**Context**: Access the endpoints to confirm availability and inspect response structure.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://www.zomato.com/widgets/all_collections.php"
```

> This fetches the default response, allowing inspection for parameter usage in generated HTML/JS. Repeat for o2.php. Look for dynamic insertion points.

### Step 2: Document Parameters

**Context**: Manually note parameters from documentation or response analysis.

No command needed; use browser dev tools to explore.

> Expected: Parameters like city_id and language_id identified as user-supplied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- recon
- web-api
