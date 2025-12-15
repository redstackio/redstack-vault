---
id: proc-browser-cache-extract
tags:
  - browser-forensics
  - credential-extraction
  - cache-dump
type: procedure
tools:
  - '[[tools/Browser-Forensic-Tools]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Browser
  - Windows
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T17:32:01.711Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials from Web Browsers]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials from Web Browsers]]'
  - '[[Credential Dumping]]'
---
# Extract-Cached-Data-from-Browser

## Summary

This procedure details the recovery of sensitive data, such as API keys, from a web browser's cache using forensic tools, targeting vulnerabilities like improper caching in applications such as Kadira.

## Description

Once sensitive data is cached due to missing headers, attackers with device access can use forensic utilities to dump browser storage. This includes HTTP cache files, localStorage, or IndexedDB. The procedure assumes device compromise (e.g., malware or physical access) and focuses on common browsers like Chrome or Firefox. Technical approach involves locating browser data directories and parsing cache entries for plaintext keys. Prerequisites include admin access on the device; outcomes enable unauthorized API usage, leading to data breaches or further compromise.

## Requirements

1. Physical or remote access to the target device with the browser
2. Forensic tools installed (e.g., on a live USB for stealth)
3. Knowledge of browser data paths (e.g., ~/Library/Caches on macOS)

## Defense

Defensive measures and detection strategies:

- Enable full-disk encryption and browser sandboxing
- Use EDR tools to monitor file access in browser directories
- Regularly clear browser cache and implement key rotation policies

## Objectives

1. Locate and dump browser cache contents
2. Identify and extract API keys or credentials
3. Validate extracted data for usability

## Instructions

### Step 1: Locate Browser Cache Directory

**Context**: Identify the storage location for cached data based on OS and browser.

For Chrome on Windows: Navigate to %LocalAppData%\Google\Chrome\User Data\Default\Cache. For Firefox: %AppData%\Mozilla\Firefox\Profiles\<profile>\cache2.

### Step 2: Launch Forensic Tool

**Context**: Use a tool to scan and export cache entries.

Run a browser forensic tool like NirSoft's ChromeCacheView or sqlite3 on the Cache SQLite DB to query for entries containing 'api' or key patterns.

**Expected Output**: List of cache files with URLs and data blobs.

### Step 3: Parse and Extract Keys

**Context**: Filter and decode cached responses for sensitive strings.

Open extracted files in a hex editor or use strings command to grep for API key formats (e.g., sk- or ak- prefixes). Copy the plaintext keys.

**Expected Output**: Readable API key strings ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers

## Commands Used


## Tools Used

- [[tools/Browser-Forensic-Tools]]

## Tags

- [[browser-forensics]]
- [[credential-extraction]]
- [[cache-dump]]
