---
id: proc-solr-access-core-admin
tags:
  - solr
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:36.734Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Solr-Core-Admin-Interface

## Summary

This procedure involves accessing the unauthenticated Core Admin interface of an exposed Apache Solr instance to enumerate cores and paths, confirming vulnerability to exploitation like CVE-2019-0193.

## Description

In scenarios where Apache Solr is publicly exposed without authentication, attackers can directly access the /solr/admin/cores endpoint to list available cores. This step is crucial for identifying targets for configuration updates leading to code injection. The procedure assumes network access to the Solr URL and targets versions like 5.5.1 vulnerable to CVE-2019-0192 and CVE-2019-0193. Expected outcomes include path enumeration without errors, enabling subsequent exploitation steps.

## Requirements

1. Direct HTTP/HTTPS access to the Solr endpoint (e.g., https://target/solr/)
2. Web browser or HTTP client like curl
3. Knowledge of Solr's default admin paths

## Defense

Defensive measures and detection strategies:

- Implement authentication on Solr instances (e.g., Basic Auth or IP whitelisting)
- Monitor access logs for anomalous GET requests to /admin/cores
- Use WAF rules to block unauthenticated admin access

## Objectives

1. Enumerate available Solr cores and paths
2. Confirm unauthenticated access
3. Prepare for configuration manipulation

## Instructions

### Step 1: Navigate to Core Admin

**Context**: Access the Solr root to verify exposure and reach the Core Admin.

Use curl or a browser to GET the admin cores endpoint:

```bash
curl -k https://target/solr/admin/cores
```

> This command fetches the list of cores in JSON format. Successful output shows core names and status without requiring credentials.

### Step 2: Copy Relevant Path

**Context**: Identify and note the path for the target core to use in updates.

Inspect the response and copy the core path (e.g., /solr/core_name).

```bash
curl -k https://target/solr/ | grep -i core
```

> Expected output includes core identifiers. Manually note the path for the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[solr]]
- [[recon]]
- [[web]]
