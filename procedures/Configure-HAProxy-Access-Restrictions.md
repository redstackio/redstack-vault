---
tags:
  - haproxy
  - proxy
  - restriction
type: procedure
tools:
  - '[[tools/HAProxy]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a57f9329-9d60-4c56-9152-c0dee17a9042
created_at: '2025-12-13T09:01:22.225Z'
updated_at: '2025-12-13T09:01:22.225Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure HAProxy Access Restrictions

## Summary

This procedure sets up HAProxy to restrict access to specific URIs, such as denying requests to /flag, to simulate a protected environment for demonstrating bypass vulnerabilities.

## Description

HAProxy is configured as a reverse proxy with ACL rules to block forbidden paths. This creates a scenario where HTTP Request Smuggling can be used to bypass these restrictions. The target environment involves HAProxy version 1.5.3 forwarding to a backend server on port 8080.

## Requirements

1. HAProxy installed and accessible
2. Configuration file with ACL for denying /flag
3. Localhost network access

## Defense

Defensive measures and detection strategies:

- Use strict header validation in proxies
- Monitor for anomalous Transfer-Encoding headers in logs

## Objectives

1. Establish access controls to test bypass
2. Simulate real-world proxy restrictions
3. Verify denial of direct /flag access

## Instructions

### Step 1: Create HAProxy Configuration

**Context**: Define global settings, defaults, frontend, and backend with ACL to deny /flag.

Use HAProxy version 1.5.3 configuration: global daemon maxconn 256, defaults mode http, frontend bind *:80 with ACL path_beg /flag http-request deny, backend servers to 127.0.0.1:8080.

### Step 2: Start HAProxy

**Context**: Run HAProxy with the configuration to enforce restrictions.

Start the HAProxy service.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/HAProxy]]

## Tags

- [[tools/HAProxy]]
- [[proxy]]
