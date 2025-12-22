---
id: e16fcd59-6c09-464c-8664-18bfa5f43dee
name: XML-Billion-Laughs-Delayed-Interpretation-DoS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.315383+00:00'
updated_at: '2023-04-10T20:24:38.336947+00:00'
tactics:
  - '[[tactics/Impact|TA0040 - Impact]]'
techniques:
  - '[[techniques/Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - '[[tags/Exploiting XXE to perform a deny of service]]'
  - '[[tags/Parameters Laugh attack]]'
  - '[[tags/XML External Entity]]'
commands:
  - '[[commands/curl-post-xml-payload]]'
platforms:
  - Web
tools:
  - '[[tools/cURL]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# XML-Billion-Laughs-Delayed-Interpretation-DoS

## Summary

This procedure demonstrates a variant of the Billion Laughs XML denial-of-service attack using delayed interpretation of parameter entities to cause exponential entity expansion, overwhelming the target XML parser with excessive memory and CPU usage, leading to service disruption or crash.

## Description

The XML Billion Laughs Attack with Delayed Interpretation exploits the XML external entity (XXE) processing feature in vulnerable parsers by defining nested parameter entities that recursively expand during the DOCTYPE declaration phase. This delayed expansion evades some basic entity limits and causes the parser to generate billions of characters from a compact payload, resulting in resource exhaustion. It targets web applications, APIs, or services that parse untrusted XML input without proper entity expansion controls, such as those using libxml2, Xerces, or similar libraries. The attack is remote, requires no authentication, and can be delivered via a single HTTP POST request. Success disrupts availability, potentially causing downtime for the affected endpoint.

## Requirements

1. Knowledge of the target endpoint that accepts and parses XML input (e.g., SOAP API, XML upload form).
2. Network access to the target service (e.g., HTTP/HTTPS connectivity).
3. A tool like curl for sending the crafted XML payload.
4. Optional: A text editor to customize the XML if needed for specific parsers.

## Defense

Defensive measures and detection strategies:

- Disable external entity and parameter entity expansion in XML parsers (e.g., set libxml2 features to LIBXML_NO_ENT).
- Use secure XML libraries like defusedxml in Python or validate input against a strict schema.
- Implement rate limiting, request size limits (<1MB), and entity expansion depth limits (e.g., max 1000 entities).
- Monitor for high CPU/memory usage during XML parsing and log anomalous DOCTYPE declarations.
- Deploy web application firewalls (WAFs) with XXE signatures to block recursive entity patterns.

## Objectives

1. Craft a malicious XML payload that triggers exponential entity expansion.
2. Deliver the payload to the target XML parser.
3. Overwhelm the target's resources to cause denial of service.
4. Verify disruption through service unavailability or error responses.

## Instructions

### Step 1: Prepare the Malicious XML Payload

**Context**: Create the XML file containing the delayed parameter entity expansion to exploit the parser's DOCTYPE processing. This step uses a predefined payload that nests entities recursively for exponential growth.

**Code** ([[codes/XML-Billion-Laughs-Delayed-Parameter-Entity-Payload]]):

Embed the code snippet here as a file named payload.xml.

> Save the XML content to a file (e.g., payload.xml). This payload defines parameter entities (pe_1 to pe_4) that reference each other with HTML comments and percent signs to delay interpretation until the final %pe_4; expansion, leading to billions of recursive DOCTYPEs and resource exhaustion.

### Step 2: Send the Payload to the Target Endpoint

**Context**: Transmit the crafted XML to the vulnerable service using an HTTP POST request, mimicking legitimate XML input. This step assumes the target accepts XML via POST to an endpoint like /api/upload or /soap.

**Command** ([[commands/curl-post-xml-payload]]):

```bash
curl -X POST -H "Content-Type: application/xml" --data-binary @payload.xml $_TARGET_URL
```

> This command sends the XML file as the request body to the target URL. Replace $_TARGET_URL with the actual endpoint (e.g., http://target.com/parse-xml). Expected output includes a server error (e.g., 500 Internal Server Error) or timeout if the parser crashes. Monitor the target's response time and availability post-request to confirm DoS.
