---
id: 8028cdc0-349d-4f2e-80f6-c34f825ff619
name: XXE-File-Retrieval-via-Base64-Encoding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.168196+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - xxe
  - file-retrieval
  - base64-encoding
  - xml-external-entity
  - information-disclosure
commands:
  - '[[commands/curl-send-xxe-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# XXE-File-Retrieval-via-Base64-Encoding

## Summary

This procedure exploits an XML External Entity (XXE) vulnerability in a web application to retrieve sensitive files from the target server by encoding the file contents in Base64 format within the response. It is useful for disclosing configuration files, password lists, or other local system data during reconnaissance or post-exploitation phases.

## Description

XML External Entity (XXE) processing allows attackers to define external entities in XML documents that reference local files or remote resources. In this technique, a malicious XML payload is crafted to read a target file (e.g., /etc/passwd on Linux) and encode its contents using Base64 to bypass direct output restrictions or filtering. The encoded data is then embedded in the application's response, allowing the attacker to decode and access the file offline. This method targets applications that parse user-supplied XML without disabling external entity resolution, such as those using outdated XML libraries like libxml2. Success depends on the parser's configuration and the application's error handling, which may echo entity expansions in responses.

## Requirements

1. Network access to a web application endpoint that accepts and parses XML input (e.g., via POST requests to an API or upload form).
2. Knowledge of the target file path (e.g., /etc/passwd for Linux user enumeration).
3. Tools for sending HTTP requests with custom XML payloads, such as curl or a proxy like Burp Suite.
4. Basic understanding of Base64 encoding/decoding for post-exploitation analysis.

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set 'expandEntities' to false in Java's DocumentBuilderFactory or use secure configurations in PHP's libxml).
- Implement strict input validation and sanitization to reject or strip DOCTYPE declarations and entity definitions from user-supplied XML.
- Deploy a web application firewall (WAF) to detect and block payloads containing external entity references or Base64-encoded file reads.
- Monitor application logs for anomalous XML parsing errors or unexpected file access attempts on the server.
- Use least-privilege file permissions to restrict XML parser processes from accessing sensitive files.

## Objectives

1. Exploit XXE to read and exfiltrate the contents of a sensitive local file from the target server.
2. Obtain Base64-encoded file data in the application response for offline decoding and analysis.
3. Identify credentials, configurations, or system details to support further attacks like lateral movement or privilege escalation.

## Instructions

### Step 1: Identify Vulnerable XML Endpoint

**Context**: Locate an application endpoint that processes XML input, such as a user registration form, API upload, or SOAP service. Test for XXE by sending a basic external entity payload to confirm if the parser resolves entities.

Use Burp Suite or curl to send a test request and observe if entities are expanded in the response.

### Step 2: Craft Malicious XML Payload

**Context**: Create an XML document with a DOCTYPE declaration defining an external entity that reads the target file and encodes it in Base64. This payload uses a data URI scheme to trigger the encoding during entity resolution.

Embed the payload from [[codes/XXE-Base64-File-Retrieval-Payload]] in your request body.

For example, replace the file path in the entity with your target (e.g., 'file:///etc/passwd').

### Step 3: Send Payload and Retrieve Encoded Response

**Context**: Submit the crafted XML via an HTTP POST request to the vulnerable endpoint. The parser will resolve the entity, read the file, encode it, and include it in the response if the application echoes entity expansions.

**Command** ([[commands/curl-send-xxe-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d @payload.xml http://target.com/vulnerable-endpoint
```

> This command sends the XML payload file to the endpoint. If successful, the response body will contain the Base64-encoded file contents embedded in the XML output or error message.

### Step 4: Decode and Analyze Retrieved Data

**Context**: Extract the Base64 string from the response and decode it to view the file contents. Use tools like base64 command-line utility or online decoders.

**Command** (base64 decode example):
```bash
echo "BASE64_STRING_FROM_RESPONSE" | base64 -d > retrieved_file.txt
```

> Verify the decoded file matches expected content (e.g., user accounts in /etc/passwd). If the encoding fails or data is truncated, adjust the payload for different file paths or encoding methods.

### Step 5: Iterate for Additional Files

**Context**: If successful, repeat with other sensitive files like /etc/shadow, application configs, or SSH keys to gather more intelligence. Monitor for rate limiting or IDS alerts.
