---
id: uuid-for-search-procedure
tags:
  - android
  - credential-leak
  - api-keys
type: procedure
tools:
  - '[[tools/keyhacks]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/grep-search-strings]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:39.123Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Search-for-Hardcoded-API-Keys-in-Decompiled-Files

## Summary

This procedure scans decompiled Android app files, particularly strings.xml, for hardcoded sensitive information like Google Maps and MapBox API keys, followed by validation to assess their usability for malicious impersonation.

## Description

After decompilation, attackers search for credential patterns in resource files. This exploits cleartext storage, allowing extraction of keys that can be used to send unauthorized API requests, potentially polluting data or accessing services. Targets apps using Google Maps API and MapBox API. Outcomes include live, permissive keys ready for abuse, though server-side checks may mitigate full impact.

## Requirements

1. Decompiled APK directory from prior procedure
2. keyhacks tool cloned and installed (Python-based)
3. Internet access to validate keys against API endpoints

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding keys; use runtime fetching or environment variables
- Rotate keys regularly and monitor for unusual usage spikes
- Employ API rate limiting and client authentication beyond keys

## Objectives

1. Locate and extract potential API keys from strings
2. Validate keys for activity and over-permissiveness
3. Enable follow-on attacks like data exfiltration via impersonation

## Instructions

### Step 1: Search for Sensitive Strings

**Context**: Use pattern matching to find hardcoded credentials in XML files.

Navigate to the decompiled resources and grep for common API key prefixes:

**Command** ([[commands/grep-search-strings]]):
```bash
grep -r "AIza\|mapbox" decompiled_dir/res/values/strings.xml
```

> Outputs lines containing potential keys, e.g., <string name="google_maps_key">AIza...</string>.

### Step 2: Validate Extracted Keys

**Context**: Test if keys are active using a specialized tool.

Clone keyhacks if not installed, then run validation for Google Maps:

**Command** ([[commands/keyhacks-validate]]):
```bash
python keyhacks.py --google-maps AIzaSyD...
```

> Returns details on key validity, quotas, and permissions, confirming if it's exploitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used

- [[commands/grep-search-strings]]
- [[commands/keyhacks-validate]]

## Tools Used

- [[tools/keyhacks]]

## Tags

- api-keys
- validation
- credential-extraction
