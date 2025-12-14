---
tags:
  - curl-example
  - multi-threaded
  - timeout
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - POSIX
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:18.701Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1781508b-9f7b-4876-8ff0-25f47b09a5f4
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Modify and Compile Multi-Threaded curl Example

## Summary

Adapts the official libcurl multi-threaded example to include a short timeout, compiling it against the vulnerable library to trigger the race condition.

## Description

The example from curl.se/libcurl/c/multithread.html is modified by adding curl_easy_setopt(curl, CURLOPT_TIMEOUT, 2) in the pull_one_url function. This forces quick DNS timeouts, exacerbating the race in multi-threaded resolutions using the alarm path.

## Requirements

1. Vulnerable libcurl built
2. GCC compiler
3. Example source from https://curl.se/libcurl/c/multithread.html

## Defense

Defensive measures and detection strategies:

- Set longer timeouts or use async DNS in applications
- Avoid multi-threading with synchronous libcurl resolvers
- Fuzz test multi-threaded curl usage for crashes

## Objectives

1. Integrate short timeout to force alarm triggers
2. Compile executable linked to vulnerable libcurl
3. Prepare for DNS timeout simulation

## Instructions

### Step 1: Download and Modify Example

**Context**: Fetch and edit the source to add timeout.

**Command** (Manual Edit after wget):
```bash
wget https://curl.se/libcurl/c/multithread.html -O multithread.c  # Then edit to add: curl_easy_setopt(curl, CURLOPT_TIMEOUT, 2);
```

> Modify in pull_one_url function. Expected output: Updated C file with timeout set.

### Step 2: Compile Example

**Context**: Link against custom libcurl.

**Command** (GCC):
```bash
gcc -o multithread multithread.c -L./lib/.libs -lcurl -lpthread
```

> Builds executable using vulnerable library. Expected output: ./multithread binary created.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- multi-thread
- curl
- compilation

