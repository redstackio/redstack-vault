---
id: p-trigger-permission-change
name: Save-Cookies-Using-curl-to-Trigger-Permission-Change
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.782Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - exploitation
  - curl
  - libcurl
  - information-disclosure
commands:
  - '[[commands/curl-save-cookies-to-jar]]'
platforms:
  - Linux
tools:
  - '[[tools/curl]]'
  - '[[tools/libcurl]]'
skill_level: basic
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Save-Cookies-Using-curl-to-Trigger-Permission-Change

## Summary

This procedure uses the curl command-line tool, powered by libcurl, to fetch a website and save received cookies to an existing jar file, exploiting a vulnerability that forces the file permissions to 0644 (group and world readable), potentially exposing sensitive data.

## Description

The vulnerability, present in libcurl since version 7.72.0 due to a specific GitHub commit, causes CURLOPT_COOKIEJAR (or -c flag in curl) to set new permissions ignoring the existing file's mode. By pointing curl to a pre-existing secure file and fetching a site like Google, cookies are written, and permissions are overwritten. This occurs on Linux systems with default umask 022. The scenario targets local multi-user environments where other users could access the exposed file. Expected outcome: Cookies saved, but file now readable by group/world, leading to info disclosure.

## Requirements

1. libcurl version 7.72.0 or later installed.
2. Internet access for the curl fetch.
3. Existing cookie.jar file with 0600 permissions from prior setup.

## Defense

Defensive measures and detection strategies:

- Avoid using existing files for CURLOPT_COOKIEJAR; use temporary or new files.
- Monitor curl/libcurl usage and file permission changes with tools like inotify or SELinux.
- Update to patched libcurl versions if available, or use wrappers to preserve permissions.

## Objectives

1. Trigger the permission overwrite via cookie save.
2. Store fetched cookies in the jar.
3. Enable unauthorized read access to demonstrate exposure.

## Instructions

### Step 1: Execute curl to Fetch and Save Cookies

**Context**: This command fetches https://www.google.com silently, saves cookies to the existing cookie.jar, discards body output, and triggers the libcurl permission change.

**Command** ([[commands/curl-save-cookies-to-jar]]):
```bash
curl -s -c cookie.jar https://www.google.com -o /dev/null
```

> curl operates in silent mode (-s), uses -c for cookie jar, targets the URL, and outputs to /dev/null. Expected output: None visible, but file updated with cookies and permissions changed to 0644.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/curl-save-cookies-to-jar]]

## Tools Used

- [[tools/curl]]
- [[tools/libcurl]]

## Tags

- exploitation
- curl
- libcurl
- information-disclosure
