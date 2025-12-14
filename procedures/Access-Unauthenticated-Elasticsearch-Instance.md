---
tags:
  - elasticsearch
  - auth-bypass
  - initial-access
type: procedure
tools:
  - '[[tools/estk]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-30T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.291Z'
sub_techniques: []
id: dbb244c5-0761-4d42-a712-2e8aa40bf666
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Unauthenticated-Elasticsearch-Instance

## Summary

This procedure verifies access to an Elasticsearch instance exposed without authentication, confirming the vulnerability by retrieving basic cluster information via direct HTTP access.

## Description

In scenarios where Elasticsearch (e.g., version 2.7.0) is misconfigured to run openly on port 9200 without auth, attackers can directly browse to the endpoint to gain initial access. This step establishes the attack surface, revealing the service's presence and version, paving the way for further enumeration and exploitation. Expected outcomes include immediate confirmation of unrestricted access, leading to risks like data leakage.

## Requirements

1. Network connectivity to the target on port 9200
2. Web browser (e.g., Chrome, Firefox)
3. No credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Enforce authentication (e.g., X-Pack security or basic auth) on Elasticsearch
- Restrict port 9200 access via firewall to trusted IPs only
- Monitor access logs for anomalous HTTP requests to / endpoint

## Objectives

1. Confirm live, unauthenticated Elasticsearch service
2. Retrieve version and cluster details for further targeting
3. Validate no auth barriers exist

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Use a browser to probe the target URL and observe the response, confirming open access.

No command needed; manually enter the URL https://elasticsearch.example.com:9200 in the browser address bar.

> The response will be a JSON object with cluster name, version (2.7.0), and node details, indicating success without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/estk]]

## Tags

- [[elasticsearch]]
- [[auth-bypass]]
