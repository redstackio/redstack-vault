---
id: 95711378-5247-47c0-956e-b348bf95e0b0
name: Freemarker-SSTI-to-Read-Server-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.031899+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Freemarker]]'
  - '[[tags/Freemarker-Read-File]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Freemarker-SSTI-to-Read-Server-Files

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in applications using the Freemarker template engine to read arbitrary files from the server filesystem. By injecting a malicious Freemarker expression, an attacker can access sensitive files like configuration files containing credentials, enabling further compromise such as data exfiltration or lateral movement.

## Description

Freemarker is a Java-based template engine commonly used in web applications for dynamic content generation. SSTI in Freemarker occurs when user input is unsafely interpolated into templates, allowing execution of arbitrary Freemarker Template Language (FTL) expressions. This procedure focuses on using the `include` directive and Java reflection to resolve and read file contents as byte arrays, which are then converted to readable ASCII. It is typically applied after identifying an injection point, such as a search field, user profile, or URL parameter that processes user input through Freemarker. Success depends on the application's configuration, such as whether file access is restricted, and can reveal paths to sensitive data like /etc/passwd, application configs, or database credentials. This technique is effective in reconnaissance and discovery phases, providing insights into the server's environment for subsequent attacks.

## Requirements

1. Identification of a Freemarker-powered web application with an SSTI-vulnerable input point (e.g., via fuzzing with payloads like `${7*7}` to confirm injection).
2. Knowledge of potential target file paths on the server (e.g., common locations like /etc/passwd or application-specific configs).
3. Network access to the injection endpoint, typically over HTTP/HTTPS.
4. A tool like Burp Suite or curl for crafting and sending requests with the payload.

## Defense

- Update Freemarker to the latest version and apply security configurations to disable dangerous directives like `include`.
- Implement strict input validation, sanitization, and whitelisting to prevent template expression injection.
- Use least-privilege file system permissions to restrict template engine access to sensitive directories.
- Enable web application firewall (WAF) rules to detect and block common SSTI payloads.
- Monitor application logs for anomalous template evaluations and file access attempts.

## Objectives

1. Inject a Freemarker payload to read arbitrary server files.
2. Extract sensitive information such as credentials or configuration details.
3. Use discovered data to facilitate further system compromise or data exfiltration.

## Instructions

### Step 1: Identify the Injection Point and Confirm Freemarker Usage

**Context**: Locate a user-controlled input field processed by Freemarker and verify SSTI by testing a benign expression that evaluates to a non-string output, confirming template execution without disrupting the application.

Inject a test payload like `${7*7}` into the input field (e.g., a search box) and submit the request. Observe if the response reflects the result (49) instead of the literal input.

**Expected Output**: The application renders "49" in the response, indicating successful template evaluation.

### Step 2: Craft and Inject the File Read Payload

**Context**: Use Java reflection via the Freemarker expression to access the filesystem and read the target file's contents. This step assumes a context object like 'product' is available in the template scope; adjust based on reconnaissance (e.g., replace 'product' with other accessible objects like 'user' or 'request').

Reference the payload code: [[codes/Freemarker-File-Read-Payload]]

Inject the payload into the identified input point, replacing 'path_to_the_file' with the absolute path to the target file (e.g., '../../../etc/passwd'). Submit via the application's form or API endpoint.

**Expected Output**: The response contains the file contents as a space-separated ASCII string (e.g., root:x:0:0:root:/root:/bin/bash for /etc/passwd).

### Step 3: Interpret and Verify the Output

**Context**: Convert the byte-joined output back to a readable format if needed, and validate that the file contents are accurate and useful for further objectives.

Manually parse the space-separated bytes into ASCII characters using a tool like CyberChef or a simple script. Cross-reference known file formats to ensure integrity (e.g., check for expected headers in config files).

**Expected Output**: Readable file contents confirming access to sensitive data, such as hashed passwords or API keys.

### Step 4: Iterate on Additional Files

**Context**: If successful, chain reads to access more files, escalating discovery (e.g., read web.xml for application paths or database configs for credentials).

Repeat Step 2 with new paths derived from initial findings, such as relative paths from the application's working directory.

**Expected Output**: Additional sensitive files retrieved, expanding the attack surface.
