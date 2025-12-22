---
id: 7e2b0bda-cbce-4488-a184-fe8218ba8fc3
name: XXE-File-Retrieval-via-XInclude-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.218474+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File-and-Directory-Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - xxe
  - xml-external-entity
  - xinclude
  - file-retrieval
  - web-exploitation
commands:
  - '[[commands/curl-send-xml-payload]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# XXE-File-Retrieval-via-XInclude-Attack

## Summary

This procedure demonstrates how to exploit an XML External Entity (XXE) vulnerability using XInclude to retrieve sensitive files from the target server's local file system, such as /etc/passwd on Linux systems. It targets web applications that parse user-supplied XML input without proper entity resolution restrictions, allowing attackers to include and read arbitrary files.

## Description

XML External Entity (XXE) injection exploits weaknesses in XML parsers that process external entities defined in user input. By crafting an XML payload with an XInclude directive, an attacker can force the parser to include and return the contents of local files, leading to information disclosure. This technique is particularly effective against applications using libraries like libxml2 without disabling external entity processing. The attack assumes the target endpoint accepts XML via POST requests and echoes back parsed content in responses. Success enables retrieval of configuration files, credentials, or system details, providing a foothold for further exploitation in reconnaissance or lateral movement phases.

## Requirements

1. A vulnerable web application endpoint that accepts and parses XML input (e.g., via SOAP or custom XML APIs).
2. Knowledge of the target URL and HTTP method for XML submission.
3. Network access to the target server (e.g., direct or via proxy).
4. Tools like curl for sending HTTP requests (available on most Linux systems).
5. Basic understanding of XML structure and the target's parser configuration.

## Defense

- Configure XML parsers to disable external entity resolution (e.g., set 'expand_entities' to false in libxml2).
- Sanitize and validate all XML input, rejecting documents with external entity declarations.
- Use web application firewalls (WAFs) to detect and block XXE payloads, including XInclude references.
- Implement least-privilege file access for the application server process to limit readable files.
- Enable logging of XML parsing errors and monitor for anomalous file access patterns.

## Objectives

1. Retrieve sensitive files from the target system's file system, such as /etc/passwd or application configs.
2. Disclose internal data to support further attacks like credential theft or system enumeration.
3. Establish information superiority by exposing server internals without direct shell access.

## Instructions

### Step 1: Identify Vulnerable XML Endpoint

**Context**: Determine the target URL that processes XML input and returns parsed content. This could be found via reconnaissance or known API documentation. Test with a benign XML payload to confirm parsing without errors.

**Command** ([[commands/curl-send-xml-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<test>benign</test>' $_TARGET_URL
```

> This step verifies the endpoint accepts XML. Replace $_TARGET_URL with the actual endpoint (e.g., http://target.com/xml-endpoint). Look for successful parsing in the response without rejection.

### Step 2: Craft and Send XInclude Payload

**Context**: Use the XInclude payload to reference a local file. The XML declares the XInclude namespace and includes the target file URI. Submit it to the endpoint to trigger file inclusion in the response.

Embed the payload [[codes/XInclude-XXE-Payload-to-Retrieve-Local-Files]] in the request body.

**Command** ([[commands/curl-send-xml-payload]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d @payload.xml $_TARGET_URL
```

> Save the XML payload to a file named payload.xml and send it. The response should include the contents of the referenced file if vulnerable. If the parser supports XInclude and external entities are enabled, the file data will be echoed back.

### Step 3: Analyze Response and Iterate

**Context**: Inspect the response for the included file contents. If partial or no data is returned, adjust the file path (e.g., for Windows: file:///C:/Windows/system.ini) or try blind XXE variations if direct retrieval fails.

> Parse the HTTP response body for the file data. Success is indicated by visible file contents like user lists in /etc/passwd. If blocked, use out-of-band techniques (e.g., exfil to attacker DNS) for blind retrieval.

**Expected Output**: The response body contains the raw file contents, e.g.,
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```
