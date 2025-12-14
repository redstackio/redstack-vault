---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - recon
  - php
  - soap
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-soap-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:19.538Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify PHP SOAP Service

## Summary

This procedure scans a target web application to identify exposed PHP SOAP services, confirming the presence of the SOAP extension which is prerequisite for exploiting type confusion vulnerabilities.

## Description

In the context of PHP SOAP RCE attacks, discovering an active SOAP endpoint is crucial as the vulnerability resides in the serialize_function_call function. This involves probing common paths for SOAP/WSDL files and sending basic XML requests to elicit responses that reveal PHP SOAP handling. The target environment is typically a web server running PHP with the SOAP extension enabled, often on public-facing applications.

## Requirements

1. Network access to the target web server (ports 80/443).
2. Basic HTTP client like curl.
3. Knowledge of common SOAP endpoint paths (e.g., /soap, /wsdl.php).

## Defense

Defensive measures and detection strategies:

- Disable unused SOAP endpoints or the SOAP extension if not required.
- Implement web application firewall (WAF) rules to block anomalous XML requests.
- Monitor access logs for SOAP probes (e.g., XML payloads to /soap paths).

## Objectives

1. Confirm existence of PHP SOAP service.
2. Gather endpoint details for crafting exploits.
3. Validate target vulnerability prerequisites.

## Instructions

### Step 1: Probe for SOAP Endpoint

**Context**: Send a minimal SOAP envelope to common paths to check for service availability.

**Command** ([[commands/curl-soap-probe]]):
```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>' -i
```

> This command sends an empty SOAP body and inspects the response headers/body for XML faults or PHP errors indicating SOAP processing. Expected output includes a 200 OK with SOAP XML or a WSDL reference.

### Step 2: Request WSDL for Confirmation

**Context**: If the endpoint responds, fetch the WSDL to confirm PHP SOAP usage.

**Command** ([[commands/curl-wsdl-fetch]]):
```bash
curl http://target.com/soap?wsdl
```

> Look for PHP-generated WSDL content, such as namespaces or schema definitions tied to PHP classes. Success confirms the target uses PHP's SOAP extension.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/curl-soap-probe]]
- [[commands/curl-wsdl-fetch]]

## Tools Used

- None

## Tags

- [[recon]]
- [[php]]
- [[soap]]
