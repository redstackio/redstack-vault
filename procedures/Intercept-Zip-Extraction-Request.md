---
tags:
  - request-interception
  - proxy
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:22.497Z'
sub_techniques: []
id: 4e77e943-2e6e-43d7-9867-89583ceceb79
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Zip-Extraction-Request

## Summary

Capture the POST request triggered by extracting the uploaded zip to enable modification for path traversal.

## Description

The Extract app handles extraction via /index.php/apps/extract/ajax/extractHere.php. Intercepting this request allows inspection and alteration of parameters like nameOfFile and directory before processing, exploiting the lack of validation.

## Requirements

1. Proxy tool like Burp Suite configured for browser traffic
2. Uploaded zip in root folder
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Implement request signing or CSRF tokens
- Log all extraction attempts
- Detect proxy interception via timing anomalies

## Objectives

1. Halt normal extraction flow
2. Expose vulnerable parameters
3. Prepare for payload injection

## Instructions

### Step 1: Configure Proxy

**Context**: Route traffic through interception tool.

Set browser proxy to Burp (e.g., 127.0.0.1:8080) and enable interception.

### Step 2: Trigger and Intercept

**Context**: Initiate extraction to capture request.

Right-click zip, select 'Extract here'. Intercept the POST to extractHere.php.

**Expected Output**: Request body with parameters visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- request-interception
- proxy
