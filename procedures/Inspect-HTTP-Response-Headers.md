---
id: proc-uuid-2
tags:
  - information-disclosure
  - header-inspection
  - nginx
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:55.984Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Software]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-HTTP-Response-Headers

## Summary

This procedure focuses on examining HTTP response headers from a web server to detect information disclosures, such as server software versions. It is essential for reconnaissance, as exposed details like nginx versions can guide targeted vulnerability exploitation.

## Description

Following access to an endpoint like jenkins.brew.sh/login, the response headers are parsed for the 'Server' field. Default nginx configurations include the full version (e.g., nginx/1.18.0), which attackers can use to search for CVEs. This low-effort technique reveals the tech stack without further interaction.

## Requirements

1. Prior HTTP response from the target endpoint
2. Ability to parse text output (e.g., grep for headers)
3. Knowledge of common header fields like 'Server'

## Defense

Defensive measures and detection strategies:

- Use 'server_tokens off;' in nginx.conf to minimize or remove version info
- Deploy header inspection tools like ModSecurity to strip sensitive headers
- Monitor logs for tools like curl or frequent header-only requests

## Objectives

1. Extract the 'Server' header value
2. Identify the software and version for vulnerability assessment
3. Document the disclosure for reporting or further research

## Instructions

### Step 1: Fetch and Filter Headers

**Context**: Retrieve headers and isolate the Server line to quickly spot disclosures.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://jenkins.brew.sh/login | grep -i server
```

> The -I fetches headers, grep filters for 'Server'. Expected output: 'Server: nginx/1.x.x', confirming disclosure.

### Step 2: Analyze for Version Details

**Context**: If using browser dev tools, open Network tab, reload the page, and inspect the response headers manually.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://jenkins.brew.sh/login > headers.txt && cat headers.txt
```

> Save to file for review. Look for unredacted version info; success if version is explicit (not just 'nginx').

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- [[Software]]

## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[headers]]
- [[Reconnaissance]]
