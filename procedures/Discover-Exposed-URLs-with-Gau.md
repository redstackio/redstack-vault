---
tags:
  - reconnaissance
  - url-discovery
  - api-key-exposure
type: procedure
tools:
  - '[[tools/gau]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/gau-fetch-historical-urls]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Search Engines]]'
updated_at: '2025-12-14T17:32:39.417Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2ba8f6c0-3030-4588-874a-2d383e55a0f1
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Engines]]'
---
# Discover-Exposed-URLs-with-Gau

## Summary

This procedure uses the gau tool to passively gather historical URLs from public archives like the Wayback Machine and AlienVault, enabling the identification of exposed sensitive data such as API keys in archived endpoints.

## Description

In scenarios where applications inadvertently log or expose secrets in URLs, public archiving services retain this information indefinitely. This procedure targets domains like wakatime.com to fetch and scan these URLs for leaks, such as the API key waka_edf47c40-cabf-46e7-9f88-f1b44f00431f found in a historical WakaTime endpoint. Prerequisites include installing gau and having internet access; no target interaction is needed beyond domain specification.

## Requirements

1. gau tool installed and in PATH
2. Internet access to query archive services
3. Basic text processing skills to review output for secrets

## Defense

Defensive measures and detection strategies:

- Regularly scan public archives for exposed secrets using tools like gau on your own domains
- Implement secret scanning in CI/CD pipelines to prevent commits with keys
- Use short-lived or revocable API keys to minimize exposure impact

## Objectives

1. Collect historical URLs associated with a target domain
2. Identify URLs containing sensitive parameters like API keys
3. Enable follow-on validation of discovered credentials

## Instructions

### Step 1: Fetch Historical URLs

**Context**: Query public archives for all known URLs linked to the target domain to surface potential exposures.

**Command** ([[commands/gau-fetch-historical-urls]]):
```bash
gau wakatime.com > historical_urls.txt
```

> This command retrieves URLs from sources including Wayback Machine and AlienVault, saving them to a file. Expected output is a list of URLs; grep for patterns like 'api_key=' to find secrets.

### Step 2: Review for Exposures

**Context**: Manually or scripturally inspect the output for sensitive data in query parameters.

**Command** (grep for API keys):
```bash
grep -i 'api_key' historical_urls.txt
```

> Filters URLs containing 'api_key'. In this case, it reveals the exposed key in the WakaTime summaries endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Search Engines]] Search Open Websites/Domains

### Sub-Techniques


## Commands Used

- [[commands/gau-fetch-historical-urls]]
- grep (standard Unix tool for pattern matching)

## Tools Used

- [[tools/gau]]

## Tags

- [[Reconnaissance]]
- [[url-discovery]]
- [[api-key-exposure]]
