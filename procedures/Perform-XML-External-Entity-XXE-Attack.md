---
type: procedure
description: >-
  Crafts and sends malicious XML payloads to exploit XXE vulnerabilities in XML
  parsers, enabling file disclosure, DoS, or SSRF.
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - xxe
  - xml
  - external-entity
commands:
  - '[[commands/curl-send-xxe-payload]]'
tools: []
platforms:
  - web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Perform-XML-External-Entity-XXE-Attack

## Summary

This procedure demonstrates how to execute an XML External Entity (XXE) attack by crafting XML payloads with external entity definitions and submitting them to a vulnerable application endpoint that parses XML input. It targets weakly configured XML parsers to achieve outcomes like local file disclosure (e.g., reading /etc/passwd), denial of service via billion laughs attack, or server-side request forgery (SSRF).

## Description

XXE attacks exploit the ability of XML parsers to process external entity references, allowing attackers to include references to external resources or local files. When the parser resolves these entities, it can lead to unintended data leakage or resource exhaustion. This procedure assumes a web application endpoint (e.g., a SOAP or REST API) that accepts XML POST requests without proper parser hardening. The attack requires identifying an XML-processing endpoint via reconnaissance (e.g., using tools like Burp Suite to inspect traffic). Success depends on the parser allowing external entities (e.g., libxml2 with DTD processing enabled). Common targets include legacy web services or misconfigured APIs in environments like Java (SAXParser) or PHP (SimpleXML).

## Requirements

1. Network access to the target application's XML-processing endpoint (e.g., HTTP/HTTPS POST to /api/upload).
2. Knowledge of the endpoint's expected XML structure (e.g., via documentation or traffic interception).
3. Tools for sending HTTP requests (e.g., curl or Burp Suite).
4. A listening server for SSRF payloads (optional, for advanced exfiltration).

## Defense

- Disable external entity and DTD processing in XML parsers (e.g., set FEATURE_SECURE_PROCESSING to true in Java).
- Implement strict input validation to reject or sanitize XML payloads containing entity declarations.
- Use modern parsers like Python's defusedxml or .NET's XmlReader with secure settings.
- Monitor for anomalous file access or outbound requests from the application server.

## Objectives

1. Disclose sensitive local files from the server (e.g., configuration files, credentials).
2. Perform SSRF to access internal network resources.
3. Cause resource exhaustion via recursive entity expansion (DoS).
4. Achieve remote code execution if combined with other vulnerabilities (e.g., log poisoning).

## Instructions

### Step 1: Craft Internal Entity for Testing

**Context**: Start by defining a basic internal entity to verify XML parsing without external resolution. This tests if the endpoint processes entities at all, providing a baseline before attempting external reads. Use the internal entity definition to embed a simple value that should be echoed back.

**Code** ([[codes/xml-internal-entity-definition]]):

```xml
<!ENTITY entity_name "entity_value">
```

> Embed this in a full XML document's DOCTYPE and reference &entity_name; in the body. Expected: The value "entity_value" appears in the response, confirming entity expansion.

If the response echoes the entity value, proceed; otherwise, the parser may have entities disabled.

### Step 2: Define External Entity for File Disclosure

**Context**: Create an external entity using SYSTEM to reference a local file. This step exploits the parser's attempt to fetch the "URI" (file:///path), reading and including the file content in the response. Common targets: /etc/passwd on Linux or C:\Windows\System32\drivers\etc\hosts on Windows. Adjust the path based on the target OS.

**Code** ([[codes/xml-external-entity-definition]]):

```xml
<!ENTITY entity_name SYSTEM "file:///etc/passwd">
```

> Insert this into the DOCTYPE of your XML payload. Reference &entity_name; in an element that gets processed/returned (e.g., <data>&entity_name;</data>). Expected: Response includes the contents of /etc/passwd, such as user entries starting with "root:x:0:0:root:".

Decision point: If file content appears, XXE is confirmed; if error (e.g., "Invalid URI"), try blind XXE techniques like OOB exfiltration.

### Step 3: Send the Malicious XML Payload

**Context**: Submit the crafted XML to the target endpoint using an HTTP POST request. This delivers the payload and triggers the parser. Use Content-Type: application/xml to ensure proper handling. Monitor the response for included file data or errors indicating resolution attempts.

**Command** ([[commands/curl-send-xxe-payload]]):

```bash
curl -X POST -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY entity_name SYSTEM \"file:///etc/passwd\">]><root>&entity_name;</root>" $_TARGET_URL
```

> This sends a complete inline XML payload with the external entity. Expected: HTTP 200 response with the XML body expanded to include file contents. If the endpoint expects multipart or specific structure, save to a file (@payload.xml) and adjust.

Verify success by checking if sensitive data (e.g., usernames) is in the response body.
