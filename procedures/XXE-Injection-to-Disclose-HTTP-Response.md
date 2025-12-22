---
id: 9c567193-5133-4a9b-bca6-a42f1601f287
name: XXE-Injection-to-Disclose-HTTP-Response
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.729985+00:00'
updated_at: '2023-04-10T20:24:42.660186+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - xxe
  - disclose-http-response
  - windows-local-dtd
  - side-channel-leak
  - xml-external-entity
commands:
  - '[[commands/curl-post-xml-payload]]'
platforms:
  - Web
  - Windows
tools: []
validated: true
---

# XXE-Injection-to-Disclose-HTTP-Response

## Summary

This procedure demonstrates how to exploit an XML External Entity (XXE) vulnerability in a web application to disclose the contents of an HTTP response from an internal or external URL. By injecting a crafted XML payload that leverages a local DTD on a Windows target system, the attacker can force the XML parser to fetch and include sensitive HTTP data in the response, enabling data exfiltration without direct file access.

## Description

XML External Entity Injection (XXE) targets applications that parse untrusted XML input without proper entity resolution controls. In this technique, the attacker submits XML containing external entity declarations that reference a local DTD file (e.g., on Windows systems at C:\Windows\System32\wbem\xml\cim20.dtd). This DTD is used to define a super-class entity that indirectly fetches HTTP content via a side-channel mechanism, embedding the response in the parsed output. This is particularly useful for disclosing internal HTTP responses, such as from backend services, when direct SSRF is blocked. The attack requires a vulnerable XML-processing endpoint (e.g., SOAP APIs, file uploaders) and assumes the parser resolves external entities. Success results in the target HTTP content being reflected in the application's error or response body, allowing collection of sensitive data like API responses or configuration details.

## Requirements

1. Access to a web application endpoint that accepts and parses XML input (e.g., POST /api/xml-upload).
2. Knowledge of the target system's OS (Windows for local DTD exploitation) and a reachable HTTP URL to disclose (e.g., an internal service).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. The XML parser must be configured to resolve external entities (common in outdated libraries like older Xerces or libxml).

## Defense

- Disable external entity processing in XML parsers (e.g., set 'disallow-doctype-decl' to true in PHP's libxml).
- Implement strict input validation to reject or sanitize XML payloads containing DOCTYPE declarations.
- Use a Web Application Firewall (WAF) to detect XXE patterns, such as entity references or DTD inclusions.
- Update XML parsing libraries to versions that mitigate XXE by default (e.g., OWASP ESAPI).

## Objectives

1. Inject a malicious XML payload to trigger external entity resolution.
2. Leverage a local DTD to fetch and disclose HTTP response content.
3. Extract sensitive data from the disclosed HTTP response for further exploitation.

## Instructions

### Step 1: Identify Vulnerable XML Endpoint

**Context**: Locate an application endpoint that processes XML input, such as a login form, file upload, or API. Test for XXE by submitting a basic external entity payload and checking if it resolves (e.g., error messages revealing file contents).

Use [[commands/curl-post-xml-payload]] to send a test XML:

```bash
curl -X POST http://target.com/api/xml-endpoint -H "Content-Type: application/xml" -d '<!DOCTYPE test [<!ENTITY test SYSTEM "file:///etc/passwd">]><test>&test;</test>'
```

> This step verifies if the parser resolves entities. If file contents appear in the response or error, the endpoint is vulnerable to XXE.

### Step 2: Craft and Submit XXE Payload for HTTP Disclosure

**Context**: Prepare the advanced payload using a Windows local DTD to bypass restrictions and fetch HTTP content. The payload defines entities that load the DTD, create a dynamic entity for the target URL, and trigger an error that leaks the content.

Embed the payload from [[codes/Windows-XXE-Payload-Using-Local-DTD-for-HTTP-Fetch]] in your request. Replace the URL in the entity definition with your target (e.g., https://internal.company.com/api/data).

Use [[commands/curl-post-xml-payload]] to submit:

```bash
curl -X POST http://target.com/api/xml-endpoint -H "Content-Type: application/xml" --data-binary @xxe-payload.xml
```

> The payload will cause the parser to fetch the HTTP response and include it in the output via the error entity. Monitor the response body or error logs for the leaked content.

### Step 3: Analyze and Extract Disclosed Data

**Context**: Review the server's response for the embedded HTTP content. If the side-channel leak succeeds, the target response (headers, body) will appear in the XML output or an error message.

Parse the response manually or with tools like grep:

```bash
curl ... | grep -o 'HTTP content here'
```

> Success is indicated by the presence of the target URL's response data. If no leak occurs, adjust the payload for different DTD paths or entity encodings.
