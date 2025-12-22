---
id: uuid-query-solr
tags:
  - solr
  - query
  - dod
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-request]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:37.343Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query Exposed Solr Instance

## Summary

Send queries to the exposed Solr instance to verify unauthenticated access and retrieve sensitive data from DoD-related indices.

## Description

Once the Solr port is identified, this procedure tests for access by querying the select endpoint. The response revealed .mil data, confirming the instance indexes military information without protections.

## Requirements

1. Known Solr URL (http://target-ip:port/solr/)
2. Curl or similar HTTP client
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all Solr endpoints
- Log and monitor query patterns for anomalous searches

## Objectives

1. Confirm unauthenticated access
2. Assess data sensitivity
3. Identify core names for exploitation

## Instructions

### Step 1: Send Test Query

**Context**: Probe the Solr select endpoint for data.

**Command** ([[commands/curl-get-request]]):
```bash
curl "http://target-ip:port/solr/select?q=*:*&wt=json"
```

> Returns JSON with documents from http://example.mil/, including military metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-get-request]]

## Tools Used


## Tags

- [[solr]]
- [[query]]
- [[dod]]
