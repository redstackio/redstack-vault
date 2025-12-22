---
type: procedure
description: >-
  Exploit XML External Entity (XXE) vulnerabilities to perform Local File
  Inclusion (LFI) attacks by injecting malicious entities into XML requests to
  read sensitive local files.
verified: true
submitted: true
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - LFI
  - XXE
  - OWASP
  - Web Applications
  - XML
commands:
  - '[[commands/curl-post-xml-with-xxe]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# LFI-Through-XML-External-Entities-XXE

## Summary

This procedure demonstrates how to exploit XML External Entity (XXE) vulnerabilities in web applications that parse XML input insecurely, allowing attackers to perform Local File Inclusion (LFI) to read arbitrary files on the server, such as /etc/passwd. It involves intercepting and modifying XML-based requests, typically from login forms, to inject external entities that reference local files.

## Description

XXE vulnerabilities occur when an application processes XML input without disabling external entity resolution, enabling attackers to define entities that pull in external resources or local files. In this scenario, targeted at web applications with XML POST requests (e.g., login endpoints), the attack modifies the XML payload to include a SYSTEM entity pointing to a local file path. Upon parsing, the application echoes the file contents in the response, achieving LFI. This is common in legacy systems or misconfigured XML parsers like those in Java or PHP. The technique maps to exploiting public-facing applications and file discovery for data collection.

## Requirements

1. Access to a web application with an XXE-vulnerable XML endpoint (e.g., login form accepting XML).
2. Network access to the target application (e.g., via browser or proxy).
3. Tools like Burp Suite for request interception and modification, or curl for direct HTTP requests.
4. Basic knowledge of XML structure and file paths on the target OS (e.g., /etc/passwd on Linux).

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers (e.g., set DTD to false in Java's DocumentBuilderFactory).
- Use input validation to reject or sanitize XML payloads containing DOCTYPE declarations.
- Implement web application firewalls (WAFs) to block XXE patterns like <!ENTITY or SYSTEM.
- Monitor server logs for anomalous file access or XML parsing errors.
- Enable least privilege for the web server process to limit file read access.

## Objectives

1. Intercept and identify XML-based requests in the application.
2. Inject an XXE payload to reference and retrieve a local file.
3. Confirm successful LFI by observing file contents in the response.
4. Expand to read other sensitive files if initial success is achieved.

## Instructions

### Step 1: Identify and Intercept the XML Request

**Context**: Locate the XML endpoint, such as a login form, and capture the legitimate request to understand its structure. This step ensures you can replicate the request while preparing for modification.

Use [[tools/Burp-Suite]] to proxy traffic: Configure your browser to route through Burp, then submit a normal login with username and password.

Intercept the POST request, which should contain XML data like <user><username>admin</username><password>pass</password></user>.

**Expected Output**: Raw HTTP request in Burp Proxy, showing Content-Type: application/xml and the XML body.

### Step 2: Send Request to Repeater for Modification

**Context**: Move the intercepted request to Burp Repeater for safe experimentation without affecting the live session. This allows iterative testing of payloads.

In Burp Proxy, right-click the request and select "Send to Repeater." Review the XML structure to identify insertion points, typically before the root element.

**Expected Output**: Request loaded in Repeater tab, ready for editing.

### Step 3: Inject XXE Payload for LFI

**Context**: Modify the XML to include a DOCTYPE declaration defining an external entity that references the target file. This exploits the parser to include local file contents when the entity is referenced.

Edit the XML body to add the XXE payload. Use the following structure:

First, prepare the payload using [[codes/XXE-LFI-XML-Payload]]:

```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<user><username>&xxe;</username><password>pass</password></user>
```

Alternatively, send directly via [[commands/curl-post-xml-with-xxe]]:

```bash
curl -X POST -H "Content-Type: application/xml" -d '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><user><username>&xxe;</username><password>pass</password></user>' http://target.com/login
```

Forward the modified request in Repeater or execute the curl command.

If the parser resolves the entity, the response will include the file contents.

**Expected Output**: HTTP response echoing the /etc/passwd contents within the XML (e.g., in the username field) or as an error message containing the file data.

### Step 4: Verify and Iterate

**Context**: Confirm the LFI success and test for broader impact, such as reading other files like configuration or SSH keys.

Check the response for file contents (e.g., root:x:0:0:root...). If successful, modify the entity path (e.g., file:///etc/shadow) and resend.

**Expected Output**: Readable file data in the response body.

> If the application sanitizes output or the parser is hardened, the response may show parsing errors—indicating partial vulnerability. Adjust the payload (e.g., use parameter entities for blind XXE) if needed.
