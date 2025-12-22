---
type: procedure
description: >-
  Exploit XML External Entity (XXE) vulnerabilities to perform Server-Side
  Request Forgery (SSRF) attacks, allowing access to internal resources.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - xxe
  - ssrf
  - xml-external-entity
  - web-exploitation
commands:
  - '[[commands/curl-send-xxe-payload]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# SSRF-via-XXE-Injection

## Summary

This procedure exploits XML External Entity (XXE) processing in vulnerable web applications to perform Server-Side Request Forgery (SSRF) attacks. By crafting an XML payload with an external entity that references an internal URL, the application is tricked into making unauthorized requests to backend resources, such as internal APIs, metadata services, or file systems, potentially leading to data disclosure or further compromise.

## Description

XXE vulnerabilities occur when an XML parser processes user-supplied input without disabling external entity resolution. In an SSRF context, attackers define an external entity (e.g., using SYSTEM keyword) that points to an internal resource like http://localhost/admin or http://169.254.169.254/metadata (AWS instance metadata). When the parser resolves the entity, the server fetches the resource on behalf of the attacker, bypassing firewall restrictions. This is particularly effective against public-facing applications that accept XML uploads or POST data, such as document parsers, SOAP services, or file import features. The attack requires no authentication if the endpoint is unauthenticated, but can be adapted for authenticated sessions. Success enables internal network discovery, credential theft from metadata, or port scanning via timing differences in responses.

## Requirements

1. Access to a web application endpoint that accepts and parses XML input (e.g., via POST or file upload).
2. Knowledge of potential internal targets (e.g., localhost services, cloud metadata endpoints like http://169.254.169.254/latest/meta-data/).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Basic understanding of the target's network architecture to craft effective internal URLs.

## Defense

- Disable external entity processing in XML parsers (e.g., setFeature("http://xml.org/sax/features/external-general-entities", false) in Java).
- Use security-focused XML libraries like libxml2 with XXE protection enabled or JSON alternatives where possible.
- Implement network segmentation to restrict server outbound connections to internal resources.
- Monitor application logs for anomalous XML parsing errors and network traffic for unexpected internal requests.
- Validate and sanitize all XML inputs, whitelisting allowed elements and entities.

## Objectives

1. Inject a malicious XXE payload to force the server to request an internal resource.
2. Retrieve sensitive data from the response, such as file contents or metadata.
3. Demonstrate SSRF capability for further internal reconnaissance or exploitation.

## Instructions

### Step 1: Identify Vulnerable XML Endpoint

**Context**: Locate an application feature that processes XML, such as a user profile update, document upload, or API endpoint. Test for XXE by sending a basic external entity payload and observing if it resolves (e.g., via error messages or reflected content).

Use reconnaissance tools or manual testing to confirm the endpoint accepts XML. For example, inspect API documentation or fuzz parameters with XML data.

**Expected Output**: Confirmation that the endpoint parses XML without errors, potentially reflecting entity content.

### Step 2: Craft XXE Payload for SSRF

**Context**: Create an XML document defining an external entity that points to an internal URL. Reference the payload code [[codes/XXE-SSRF-Payload-XML]] to build the malicious XML.

Replace the URL in the entity (e.g., "http://internal.service/secret_pass.txt") with a target internal resource, such as "http://127.0.0.1:8080/admin" or cloud metadata endpoints.

**Expected Output**: A valid XML file or string ready for submission, with no syntax errors when validated.

### Step 3: Send Payload and Trigger SSRF

**Context**: Submit the crafted XML to the vulnerable endpoint using an HTTP client. This forces the server to resolve the external entity and fetch the internal resource.

**Command** ([[commands/curl-send-xxe-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data @xxe-payload.xml http://target.com/vulnerable-endpoint
```

> This command sends the XML payload via POST. Monitor the response for leaked internal data. If the endpoint expects file upload, use -F "file=@xxe-payload.xml". Use --proxy for interception if needed. The WHY: This step executes the SSRF by leveraging the parser's entity resolution.

**Expected Output**: Server response containing the contents of the internal resource (e.g., file data or HTTP response from internal service) or blind indicators like delays/timing for port scans.

### Step 4: Analyze Response and Iterate

**Context**: Review the output for successful data exfiltration. If blind SSRF (no direct reflection), use out-of-band techniques like DNS exfiltration or timing attacks to confirm.

Save the response to a file for analysis: `curl ... > response.txt`. If no data leaks, adjust the entity URL (e.g., try file:// paths for local files) and resubmit.

**Expected Output**: Evidence of internal access, such as retrieved credentials or service responses.

**Success Indicators**:
- Internal data appears in the application response.
- No XML parsing errors; entity resolves without rejection.
- Network logs (if accessible) show requests to internal IPs.
