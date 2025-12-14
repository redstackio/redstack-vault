---
tags:
  - information-disclosure
  - nextcloud
  - endpoint-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-json-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.658Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d89f592b-d365-40b6-880e-0a9c6a8d9ebd
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Access Exposed Composer JSON Endpoint

## Summary

This procedure demonstrates how to access an unprotected JSON endpoint in Nextcloud's lookup service to retrieve composer installation data, which leaks sensitive details without any authentication.

## Description

The Nextcloud vendor lookup service exposes a JSON file at https://lookup.nextcloud.com/vendor/composer/installed.json, containing raw composer.json data from user installations. This includes package names, versions, authors' emails, and sources. The endpoint lacks access controls, allowing anyone to download this information, which can be used for reconnaissance, identifying vulnerable software versions, or phishing based on leaked emails.

## Requirements

1. Internet access to the public endpoint
2. HTTP client like curl or a web browser
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization on all endpoints handling sensitive data
- Use robots.txt or IP restrictions to limit access to internal files
- Monitor access logs for unusual requests to JSON endpoints
- Regularly audit public-facing URLs for unintended exposures

## Objectives

1. Retrieve leaked composer installation data
2. Confirm the absence of access controls
3. Gather initial intelligence on Nextcloud deployments

## Instructions

### Step 1: Fetch the JSON Endpoint

**Context**: Directly request the exposed URL to download the raw data, simulating an unauthenticated access.

**Command** ([[commands/curl-fetch-json-endpoint]]):
```bash
curl https://lookup.nextcloud.com/vendor/composer/installed.json -o composer_data.json
```

> This command uses curl to GET the endpoint and saves the response to a local file. Expected output is a JSON array of package objects if successful; errors indicate endpoint changes or blocks.

### Step 2: Verify Response Integrity

**Context**: Check the downloaded file for valid JSON structure to ensure complete data retrieval.

**Command** ([[commands/curl-fetch-json-endpoint]]):
```bash
curl -s https://lookup.nextcloud.com/vendor/composer/installed.json | jq type
```

> This pipes the response through jq to confirm it's an array. Successful output: "array". This step validates the data without saving.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-json-endpoint]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[nextcloud]]
- [[Reconnaissance]]
