---
id: proc-uuid-7
tags:
  - ssh-key-theft
  - metadata
  - gcp
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-ssh-keys]]'
verified: false
platforms:
  - GCP
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T03:46:09.533Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Retrieve-Project-SSH-Keys-from-Metadata

## Summary

Exploit SSRF to access project attributes in GCP metadata and exfiltrate SSH public keys associated with users.

## Description

Curl the metadata endpoint for project/attributes/ssh-key to retrieve SSH keys, including user emails like tomasz@gitlab.com and expiration dates, enabling potential unauthorized access to instances.

## Requirements

1. SSRF access to Google metadata
2. Permissions via service account (implicit)
3. curl in CI environment

## Defense

- Remove or rotate SSH keys in project metadata
- Restrict metadata queries from untrusted runners
- Implement SSH key auditing and just-in-time access

## Objectives

1. Steal SSH credentials
2. Enable lateral movement
3. Complete data exfiltration

## Instructions

### Step 1: Curl SSH Key Endpoint

**Context**: Access project attributes for keys.

**Command** ([[commands/curl-retrieve-ssh-keys]]):
```bash
curl http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-key
```

> Expected: SSH key strings with users and expirations.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-ssh-keys]]

## Tools Used

- [[tools/curl]]

## Tags

- ssh-key-theft
- gcp
