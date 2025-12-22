---
type: procedure
description: >-
  Perform a denial-of-service attack by sending a malicious XML payload that
  exploits entity expansion in XML parsers.
verified: true
tactics:
  - '[[Impact]]'
techniques:
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - owasp
  - xml-bomb
  - billion-laughs
  - dos
  - web-applications
  - xml
commands:
  - '[[commands/curl-send-xml-bomb]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# XML-Bomb-Billion-Laughs-Attack

## Summary

The XML Bomb, also known as the Billion Laughs attack, is a denial-of-service technique that targets XML parsers by crafting a document with recursive entity definitions. When processed, these entities expand exponentially, consuming excessive memory and CPU resources, leading to application or server unresponsiveness. This procedure outlines how to identify a vulnerable XML endpoint, craft the payload, and deliver it to trigger the attack.

## Description

This attack exploits the XML External Entity (XXE) vulnerability variant focused on entity expansion, where the parser builds a Document Type Definition (DTD) with nested entities that multiply in size during resolution. For example, a small payload can expand to billions of characters, causing resource exhaustion. It is effective against web applications handling XML input, such as SOAP APIs, login forms, or file uploads, especially those using vulnerable parsers like older libxml2, Java's SAX, or PHP's SimpleXML without protections. The target environment is any web server parsing user-supplied XML without limits on entity depth or expansion. Prerequisites include network access to the endpoint and knowledge of its XML structure. Success results in the server timing out or crashing, denying service to legitimate users.

## Requirements

1. Network access to a web application endpoint that accepts and parses XML input (e.g., POST /login with XML body).
2. Tools for request interception and modification, such as [[tools/Burp-Suite]], or direct HTTP clients like curl.
3. Basic understanding of the target's request format, obtained via legitimate testing or reconnaissance.
4. A controlled environment for testing to avoid unintended impacts.

## Defense

Defensive measures and detection strategies:

- Configure XML parsers to disable DTD processing and entity expansion (e.g., set FEATURE_EXTERNAL_GENERAL_ENTITIES to false in Xerces, or use libxml_set_external_entity_loader(NULL) in PHP).
- Implement entity expansion limits, such as capping recursion depth to 10 levels and total expansions to 100,000 characters.
- Use secure XML libraries like defusedxml (Python), OWASP ESAPI (Java), or validate input with JSON alternatives where possible.
- Monitor server logs for XML parsing errors, unusual memory usage, or CPU spikes correlated with XML requests; employ WAF rules to block requests containing multiple <!ENTITY> declarations.
- Rate-limit XML endpoints and scan for XXE vulnerabilities using tools like OWASP ZAP.

## Objectives

1. Identify and capture a legitimate XML request to a target endpoint.
2. Embed the Billion Laughs payload into the XML to exploit entity expansion.
3. Deliver the malicious request to exhaust server resources.
4. Confirm the attack by observing server unresponsiveness or timeouts.

## Instructions

### Step 1: Capture Legitimate XML Request

**Context**: Begin by identifying an XML-processing endpoint, such as a login form that submits credentials in XML format. Use [[tools/Burp-Suite]] to intercept traffic and capture a valid request, noting the Content-Type header (typically application/xml) and the structure of the XML body. This step ensures the payload can be seamlessly integrated without altering the request syntax.

If using Burp Suite, configure your browser proxy to 127.0.0.1:8080 and enable interception on the target site.

### Step 2: Prepare the XML Bomb Payload

**Context**: Create or modify the XML to include the Billion Laughs entity definitions. Use the [[codes/XML-Billion-Laughs-Bomb-Payload]] snippet as the core payload. Embed it within the original XML structure, for example, by replacing a simple <user> element with the exploding entity reference. This step weaponizes the input while maintaining compatibility with the endpoint's expected format. Save the modified XML to a file (e.g., bomb.xml) for transmission.

Decision point: If the endpoint requires specific XML namespaces or schemas, validate the payload against them to avoid immediate rejection; otherwise, proceed directly.

### Step 3: Send the Malicious XML Request

**Context**: Deliver the payload to the server to trigger parsing and entity expansion. This uses a direct HTTP client for simplicity and verifiability. Monitor the response time; a successful attack will result in a timeout or no response as the parser hangs on expansion.

**Command** ([[commands/curl-send-xml-bomb]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data-binary @bomb.xml http://target.example.com/login
```

> This command sends the XML bomb file to the login endpoint. The --data-binary flag preserves the XML formatting. Expected: Connection timeout (e.g., >30 seconds) or HTTP 500 error due to resource exhaustion. If using Burp, paste the payload into the Repeater tab and forward the request instead.

### Step 4: Verify Attack Success

**Context**: Confirm the DoS by attempting additional requests to the endpoint or monitoring server metrics. Legitimate follow-up requests should fail or degrade in performance. This step validates the exploit and assesses impact scope.

Use a simple curl probe:
```bash
curl -X POST -H "Content-Type: application/xml" -d '<login><user>test</user><pass>test</pass></login>' http://target.example.com/login
```

Expected: Repeated timeouts or errors, indicating sustained resource drain until server recovery or restart.
