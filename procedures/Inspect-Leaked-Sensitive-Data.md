---
tags:
  - information-disclosure
  - data-analysis
  - json-parsing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/jq-parse-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:26:00.648Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b9384f78-6e52-4c72-b0db-0da13f915fa9
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Inspect Leaked Sensitive Data

## Summary

This procedure involves parsing and analyzing the JSON data obtained from the exposed Nextcloud composer endpoint to extract sensitive information like usernames, emails, software versions, and installation details for reconnaissance purposes.

## Description

Once the JSON file is downloaded, it contains an array of composer packages with fields such as name, version, authors (including emails), and sources. Inspecting this data reveals details about Nextcloud user installations, which could include outdated versions vulnerable to known exploits or personal emails for social engineering. The procedure uses tools like jq for structured parsing, highlighting leaked elements that aid in targeted attacks.

## Requirements

1. Downloaded JSON file from the endpoint
2. JSON parsing tool like jq installed
3. Basic knowledge of JSON structure

## Defense

Defensive measures and detection strategies:

- Sanitize and anonymize data in public endpoints
- Encrypt sensitive fields like emails before storage
- Implement data loss prevention (DLP) monitoring for exposed files
- Conduct regular vulnerability assessments on third-party services like composer repositories

## Objectives

1. Extract personal identifiable information (PII) such as emails
2. Identify software versions for exploit research
3. Compile a list of potential targets for further attacks

## Instructions

### Step 1: Parse Authors and Emails

**Context**: Filter the JSON to extract author details, focusing on emails which are directly leaked.

**Command** ([[commands/jq-parse-json]]):
```bash
jq '.[] | .authors[] | .email' composer_data.json
```

> This jq query iterates over packages and authors, outputting email addresses. Expected output: A list of strings like "user@example.com", revealing contact info for phishing.

### Step 2: Extract Package Versions

**Context**: Identify software versions to assess vulnerabilities in Nextcloud deployments.

**Command** ([[commands/jq-parse-json]]):
```bash
jq '.[] | {name: .name, version: .version}' composer_data.json
```

> This selects package names and versions. Expected output: Objects like {"name": "nextcloud/core", "version": "20.0.5"}, useful for targeting outdated installs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/jq-parse-json]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[data-analysis]]
- [[Reconnaissance]]
