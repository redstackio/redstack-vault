---
id: proc-weblate-locate-endpoint-001
tags:
  - recon
  - api-discovery
  - weblate
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-discover-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:10.109Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Locate Weblate API Key Regeneration Endpoint

## Summary

This procedure involves identifying the API endpoint for regenerating API keys in Weblate, a Python/Django-based translation platform, to evaluate for security controls like rate limiting. It is primarily used in reconnaissance phases of web application testing to uncover misconfigurations in authentication features.

## Description

In Weblate, API keys are managed through user profiles, and the regeneration feature allows users to generate new keys. Without proper documentation or restrictions, attackers can locate this endpoint via web interface exploration or API probing. The target environment is a web-accessible Weblate instance. Prerequisites include valid user credentials. Expected outcomes include the endpoint URL and confirmation of no throttling, setting up for abuse testing.

## Requirements

1. Valid Weblate user account with API key access.
2. Network connectivity to the Weblate instance (HTTPS).
3. Basic knowledge of REST APIs and curl for probing.

## Defense

Defensive measures and detection strategies:

- Implement API documentation with clear rate limit disclosures.
- Monitor access logs for unusual endpoint probing patterns.
- Use WAF rules to detect reconnaissance scans on admin/user endpoints.

## Objectives

1. Discover the exact URL for API key regeneration.
2. Verify absence of rate limiting headers or documentation.
3. Prepare for exploitation testing without triggering alerts.

## Instructions

### Step 1: Access Weblate User Profile

**Context**: Log in to the Weblate instance and navigate to API key management to observe the regeneration feature.

**Command** ([[commands/curl-discover-endpoint]]):
```bash
curl -X GET https://target-weblate.com/api/user/keys/ -H "Authorization: Token YOUR_API_TOKEN" -v
```

> This command fetches the current API keys and inspects verbose output for regeneration links or forms. Look for POST endpoints like `/api/user/keys/regenerate/` in the response body or headers. Successful output includes JSON with key details and no RateLimit headers.

### Step 2: Review API Documentation

**Context**: If available, consult Weblate's API docs to confirm the endpoint and check for any mentioned restrictions.

No specific command needed; manually review docs at `/api/docs/` or official Weblate documentation. Note any absence of throttling details as a vulnerability indicator.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-discover-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[api-discovery]]
- [[weblate]]
