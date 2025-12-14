---
tags:
  - cache-poisoning
  - persistent-xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/modify-upload-parameters]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: b9f42ee1-5009-4a0d-8f7c-17d93067675f
created_at: '2025-12-13T23:56:20.127Z'
updated_at: '2025-12-13T23:56:20.127Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Escalate to Cache Poisoning

## Summary

This procedure escalates the XSS to persistent cache poisoning by uploading an HTML5 AppCache manifest, allowing control over domain contents in the victim's browser even after file removal.

## Description

Using the upload bypass, inject a cache manifest file that poisons the browser's cache. This results in persistent XSS or replacement of contents on ton.twitter.com, as the cache serves malicious data indefinitely.

## Requirements

1. Successful XSS injection from prior steps
2. Knowledge of HTML5 AppCache manifests
3. Victim access to the poisoned file

## Defense

Defensive measures and detection strategies:

- Restrict upload of manifest files
- Implement cache controls and monitoring for poisoning attempts

## Objectives

1. Upload and serve cache manifest
2. Poison victim's browser cache
3. Achieve persistent control over domain contents

## Instructions

### Step 1: Upload Cache Manifest

**Context**: Modify upload to include AppCache manifest with malicious entries.

**Command** ([[commands/modify-upload-parameters]]):

```bash
# Set _content_ to CACHE MANIFEST with malicious fallback
```

> This poisons the cache when accessed.

### Step 2: Trigger Poisoning

**Context**: Access the file to apply the cache.

> Victim visits the signed URL, applying the poisoned cache.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/modify-upload-parameters]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- cache-poisoning
- persistent-xss
