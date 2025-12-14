---
id: proc-1066410-001
tags:
  - api-key-leak
  - javascript
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-download-js]]'
  - '[[commands/grep-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:39.498Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Leaked Firebase API Key

## Summary

This procedure involves inspecting publicly accessible client-side JavaScript files to identify and extract hardcoded sensitive credentials, such as Google API keys for Firebase, enabling further exploitation.

## Description

In web applications, developers sometimes embed API keys directly in JavaScript files served to clients, leading to exposure. This procedure targets such files on sites like account.clario.co, searching for Firebase Dynamic Links keys to gain unauthorized access to URL shortening services. Prerequisites include public access to the target site and basic web inspection tools. Expected outcomes: Extraction of a usable API key for API calls.

## Requirements

1. Public access to the target website's JavaScript resources
2. Command-line tools like curl and grep (or browser dev tools)
3. Knowledge of Google API key formats (e.g., starting with AIzaSy)

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove sensitive keys from client-side code; use server-side proxies
- Implement API key restrictions (e.g., IP whitelisting, domain limits) in Google Cloud Console
- Monitor for anomalous API usage via Firebase logs

## Objectives

1. Uncover exposed credentials in public files
2. Validate key usability for Firebase services
3. Enable escalation to API exploitation

## Instructions

### Step 1: Download the JavaScript File

**Context**: Retrieve the client-side JS bundle containing potential secrets.

**Command** ([[commands/curl-download-js]]):
```bash
curl -o main.js https://account.clario.co/js/main.044af6485f6b0cd90809.js
```

> Downloads the file locally for offline analysis. Expected output: A JS file saved as main.js.

### Step 2: Search for API Keys

**Context**: Scan the file for hardcoded Google API keys.

**Command** ([[commands/grep-api-key]]):
```bash
grep -i 'AIzaSy' main.js
```

> Extracts lines containing API keys. Expected output: Key like AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-download-js]]
- [[commands/grep-api-key]]

## Tools Used


## Tags

- api-key-leak
- javascript
- reconnaissance
