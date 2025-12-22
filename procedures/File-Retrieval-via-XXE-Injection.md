---
id: f37f1f17-d8b5-4df1-a59b-144a144f79db
name: File-Retrieval-via-XXE-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.139243+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Exploitation for Defense Evasion|T1211 - Exploitation for
    Defense Evasion]]
sub_techniques: []
tags:
  - '[[tags/Classic XXE]]'
  - '[[tags/Exploiting XXE to retrieve files]]'
  - '[[tags/XML External Entity]]'
  - xxe
  - file-exfiltration
  - xml-injection
commands:
  - '[[commands/curl-send-xxe-payload]]'
platforms:
  - Web
  - Linux
  - Windows
tools: []
validated: true
---

# File-Retrieval-via-XXE-Injection

## Summary

File Retrieval via XXE Injection exploits XML External Entity vulnerabilities in applications that parse untrusted XML input, allowing attackers to read arbitrary files from the server filesystem, such as /etc/passwd on Linux or boot.ini on Windows. This procedure outlines crafting and sending XXE payloads to exfiltrate sensitive files for reconnaissance or further compromise.

## Description

XML External Entity (XXE) injection occurs when an XML parser processes external entities defined in user-supplied input, potentially leading to file disclosure if the parser resolves local file URIs like 'file:///etc/passwd'. This is common in web applications handling XML uploads, API endpoints, or SOAP services without proper entity resolution disabled. The technique evades defenses by leveraging the application's own parser and can target configuration files, password stores, or internal documents. Success depends on the parser configuration (e.g., libxml2 in PHP/Java) and server permissions. Use this in scenarios where initial access to a web app is gained, such as after discovering an upload feature vulnerable to XXE.

## Requirements

1. Access to a web endpoint that accepts and parses XML input (e.g., POST /upload-xml).
2. Knowledge or identification of the XXE vulnerability through testing (e.g., via Burp Suite or curl).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Awareness of target file paths (e.g., /etc/passwd for Linux users, c:/boot.ini for Windows systems).
5. Attacker-controlled environment to receive and analyze exfiltrated data.

## Defense

- Disable external entity processing in XML parsers (e.g., set LIBXML_NO_ENT in PHP's libxml).
- Implement strict input validation to reject or sanitize XML DOCTYPE declarations.
- Deploy a Web Application Firewall (WAF) to detect and block common XXE patterns like 'SYSTEM' or 'file://' entities.
- Monitor application logs for XML parsing errors and network traffic for unexpected file access indicators.
- Use least-privilege file permissions to limit readable sensitive files.

## Objectives

1. Craft and inject an XXE payload to reference a target file on the server.
2. Trigger the XML parser to resolve the external entity and include file contents in the response.
3. Exfiltrate and analyze the retrieved file data for usernames, paths, or credentials to enable further attacks like lateral movement.

## Instructions

### Step 1: Identify the Vulnerable XML Endpoint

**Context**: Confirm the endpoint processes XML input and is vulnerable to XXE by sending a basic test payload. This step verifies the attack surface without exfiltrating data yet.

If the endpoint is known, proceed; otherwise, use reconnaissance tools to find XML-handling features.

**Expected Output**: Server response echoing or processing the XML without errors, indicating potential vulnerability.

### Step 2: Craft the XXE Payload for File Retrieval

**Context**: Select an appropriate XXE payload based on the target OS and file. Use predefined snippets to define an external entity that references the file URI. This step prepares the malicious XML for injection.

Choose from variations:
- For Linux /etc/passwd: Use [[codes/XXE-Payload-Read-Etc-Passwd]] or [[codes/XXE-Payload-Alternative-Read-Etc-Passwd]] for different syntax.
- For encoded or alternative parsing: Use [[codes/XXE-Payload-Encoded-Read-Etc-Passwd]].
- For Windows: Use [[codes/XXE-Payload-Windows-Boot-Ini]] to target c:/boot.ini.

Modify the entity if needed (e.g., change file path), but test incrementally to avoid detection.

**Expected Output**: Valid XML structure with DOCTYPE and entity definition, ready for submission.

### Step 3: Send the XXE Payload and Retrieve File

**Context**: Submit the crafted XML via HTTP request to the vulnerable endpoint. This triggers the parser to resolve the entity and embed file contents in the response.

Use [[commands/curl-send-xxe-payload]] to POST the payload:

```bash
curl -X POST -H "Content-Type: application/xml" -d "@payload.xml" http://target.com/vulnerable-endpoint
```

Replace the endpoint URL and save the payload to payload.xml. If using GET, adjust accordingly. Intercept with a proxy for modifications.

> This command sends the XML payload, exploiting the parser to include the file contents. If successful, the response body will contain the file data inline with the parsed XML.

**Expected Output**: HTTP response with XML output embedding the target file's contents, e.g., user entries from /etc/passwd like 'root:x:0:0:root:/root:/bin/bash'.

### Step 4: Verify and Analyze Retrieved Data

**Context**: Confirm the exfiltrated file contents and assess for actionable intelligence, such as user enumeration or credential hints.

Parse the response for the entity expansion (e.g., grep for known file markers). If partial, iterate with smaller files or OOB techniques if direct retrieval fails.

**Expected Output**: Readable file contents confirming successful disclosure, without parser errors.
