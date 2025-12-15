---
tags:
  - rce
  - deserialization
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.662Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 70c797ff-8b85-4c3b-a117-51fe999b823f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Trigger-Deserialization-for-RCE

## Summary

This procedure triggers the Django cache fetch mechanism to deserialize the injected malicious payload, resulting in remote code execution on the server via the untrusted pickled data.

## Description

Once the cache is tampered, accessing the cached URL causes FetchFromCacheMiddleware to retrieve and unpickle the data using pickle.load(), executing the embedded code (e.g., os.system('whoami')). This exploits the lack of validation in django.core.cache.backends.db.DatabaseCache. Requires network access to the application. Outcome is arbitrary command execution, potentially leading to full compromise.

## Requirements

1. Running Django server with caching enabled
2. Injected payload in the cache table
3. Browser or tool to access the target URL

## Defense

Defensive measures and detection strategies:

- Disable or replace pickle-based caching in production
- Implement runtime deserialization checks or sandboxing
- Log and alert on unexpected command executions in server logs
- Use application monitoring for anomalous cache fetches

## Objectives

1. Force deserialization of the malicious cache entry
2. Execute arbitrary code on the server
3. Verify RCE through log output

## Instructions

### Step 1: Access Cached Page

**Context**: Reload the URL that corresponds to the tampered cache key to trigger fetch.

Visit the page in a browser, e.g., http://127.0.0.1:8000/.

> The middleware checks the cache, loads the pickled value, and deserializes it, executing the payload.

### Step 2: Monitor Server Logs

**Context**: Observe the execution output in the Django console or logs.

Watch the terminal running `python manage.py runserver`.

> Successful deserialization runs 'whoami', printing the server user (e.g., 'ubuntu') to the console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- trigger
- execution
