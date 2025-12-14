---
tags:
  - information-disclosure
  - configuration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-config]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:48.365Z'
sub_techniques: []
id: 35732abc-4738-4867-816f-21084c169288
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Retrieve-Cortex-Configuration

## Summary

This procedure retrieves the configuration details of an exposed Cortex server, disclosing internal settings, storage paths, and operational parameters that could aid in further attacks.

## Description

The /config endpoint on Cortex provides a dump of the server's runtime configuration when unprotected. In the Shopify incident, this revealed employee-specific details and API integrations, highlighting risks of misconfigured monitoring tools in cloud setups using Golang-based services.

## Requirements

1. Successful access to the home endpoint
2. HTTP GET capability
3. Target URL with exposed /config path

## Defense

Defensive measures and detection strategies:

- Restrict config endpoints to internal networks or authenticated sessions
- Enable rate limiting on sensitive paths
- Log and alert on config access attempts

## Objectives

1. Extract server configuration for reconnaissance
2. Identify sensitive operational details
3. Assess potential for lateral movement

## Instructions

### Step 1: Query Configuration Endpoint

**Context**: Directly request the config to obtain JSON or YAML with server details.

**Command** ([[commands/curl-access-config]]):
```bash
curl https://cortex-ingest.shopifycloud.com/config
```

> Expect a response with fields like 'server', 'storage', and 'limits', potentially including paths to internal resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-config]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[configuration]]
