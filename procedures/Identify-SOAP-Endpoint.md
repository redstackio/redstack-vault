---
tags:
  - recon
  - soap
  - xxe
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-soap-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 367ff09a-a727-4e52-8d08-8b5e1ba99f08
created_at: '2025-12-13T09:00:27.934Z'
updated_at: '2025-12-13T09:00:27.934Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify SOAP Endpoint

## Summary

This procedure involves reconnaissance to locate and confirm the availability of a SOAP endpoint, setting the stage for vulnerabilities like XXE injection by verifying the target's XML processing capabilities.

## Description

In web application testing, identifying SOAP endpoints is crucial for exploiting XML-based vulnerabilities. This procedure targets public-facing APIs, such as the Starbucks Singapore endpoint, to ensure it accepts XML payloads without authentication. Expected outcomes include confirming the endpoint's responsiveness and basic structure.

## Requirements
1. Network access to the target URL
2. Tool: Curl for sending HTTP requests
3. Basic knowledge of SOAP structure

## Defense

Defensive measures and detection strategies:
- Implement rate limiting on API endpoints
- Monitor for unusual XML payloads in logs

## Objectives
1. Verify endpoint accessibility
2. Confirm SOAP compatibility
3. Prepare for payload injection

## Instructions

### Step 1: Send Test Request

**Context**: Send a benign SOAP request to check if the endpoint is live.

**Command** ([[commands/curl-send-soap-request]]):
```bash
curl -X POST https://www.starbucks.com.sg/RestApi/soap11 -H "Content-Type: text/xml" -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><test/></soapenv:Body></soapenv:Envelope>'
```

> This command tests the endpoint's response to XML input, expecting a SOAP envelope in return.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-send-soap-request]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[recon]]
- [[soap]]
