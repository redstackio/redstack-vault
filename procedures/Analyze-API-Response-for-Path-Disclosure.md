---
id: proc-003
tags:
  - response-analysis
  - path-disclosure
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:12.091Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-API-Response-for-Path-Disclosure

## Summary

This procedure parses the JSON response from the Nextcloud cloud/user API to extract and validate the exposed `storageLocation` field, revealing the server's internal data path.

## Description

Following the API query, the response contains a `users` array with objects including `storageLocation`, which discloses the absolute filesystem path without sanitization. This aids in mapping the server's directory structure for attacks like LFI or path traversal. Targets authenticated Nextcloud users on PHP environments. Outcome is actionable reconnaissance data.

## Requirements

1. JSON response from the API query
2. Text editor or JSON parser (e.g., jq for automation)
3. Knowledge of expected path formats (e.g., Linux absolute paths)

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud to version where paths are redacted (if available)
- Audit API responses server-side to strip sensitive fields
- Enable logging of response contents for anomaly detection

## Objectives

1. Identify the `storageLocation` field in the response
2. Extract the full server path for analysis
3. Assess potential for chained exploits based on disclosed info

## Instructions

### Step 1: Inspect Raw Response

**Context**: Review the JSON output manually or save to file for examination.

Save the API response to a file:

```bash
echo '{"ocs":{"meta":{"..."},"data":{"users":[{"displayname":"...","storageLocation":"/home/bohwaz/www/tmp/nextcloud/data/bohwaz",...}]}}}' > response.json
```

> Look for the `storageLocation` key in the `users` array. Expected: A string like `/home/user/www/nextcloud/data/user`.

### Step 2: Parse with jq (Optional)

**Context**: Automate extraction of the path for scripting.

```bash
jq '.ocs.data.users[0].storageLocation' response.json
```

> Outputs the path value directly. Expected: The full disclosed path printed to stdout.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[response-analysis]]
- [[path-disclosure]]
- [[Reconnaissance]]
