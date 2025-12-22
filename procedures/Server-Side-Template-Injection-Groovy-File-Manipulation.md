---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[File Permissions Modification]]'
  - '[[Template Injection]]'
sub_techniques: []
tags:
  - groovy
  - ssti
  - file-manipulation
  - template-injection
commands:
  - '[[commands/groovy-read-file-text]]'
  - '[[commands/groovy-create-new-file]]'
platforms:
  - Java
  - Web
tools: []
validated: true
---

# Server-Side-Template-Injection-Groovy-File-Manipulation

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in Groovy-based Java applications to perform file manipulation operations, such as reading sensitive files or creating new ones on the server. By injecting Groovy expressions into vulnerable template inputs, an attacker can execute arbitrary code to access or modify the filesystem, enabling discovery of configuration files, credentials, or establishment of persistence through uploaded backdoors.

## Description

Server-Side Template Injection in Groovy allows attackers to inject and execute Groovy code within the template rendering process of Java web applications, such as those using Grails or custom Groovy templating engines. This procedure focuses on file manipulation techniques: reading file contents to exfiltrate sensitive data (e.g., configuration files containing credentials) and creating new files for potential persistence or lateral movement. The attack requires identifying an input point where user-supplied data is rendered as a Groovy template without proper sanitization, such as in error messages, user profiles, or dynamic content generation. Successful exploitation bypasses client-side controls and directly interacts with the server's filesystem, potentially leading to data theft, unauthorized access, or further compromise. This is particularly dangerous in environments with Groovy-enabled services like Jenkins or Spring Boot applications.

## Requirements

1. Valid user input point in the application that renders Groovy templates (e.g., via a search field, template parameter, or user-generated content).
2. Knowledge of the server's filesystem paths (e.g., common locations like /etc/passwd on Linux or C:\Windows\System32 on Windows).
3. Network access to the target application, typically over HTTP/HTTPS.
4. Tools for intercepting and modifying requests, such as Burp Suite.
5. Basic understanding of Groovy syntax for crafting injections.

## Defense

- Implement strict input validation and sanitization for all template inputs, using allowlists for permitted characters and escaping user data before rendering.
- Disable or restrict Groovy template engines in production, opting for safer alternatives like Thymeleaf or Freemarker with sandboxing.
- Monitor server logs for anomalous file access patterns, such as reads from sensitive directories or unexpected file creations.
- Deploy Web Application Firewalls (WAFs) tuned to detect SSTI payloads, including Groovy-specific expressions like ${...}.
- Enforce least-privilege filesystem permissions to limit damage from file operations.

## Objectives

1. Read contents of sensitive files on the server to extract configuration data or credentials.
2. Create new files on the server for uploading malicious payloads or establishing persistence.
3. Achieve lateral movement by leveraging read data (e.g., SSH keys) or created files (e.g., backdoors).
4. Maintain persistence through repeated file writes or modifications to startup scripts.

## Instructions

### Step 1: Identify Vulnerable Template Input

**Context**: Locate an input field or parameter in the application that processes user data through a Groovy template engine. Test for SSTI by injecting a simple expression like ${7*7} and checking if the output reflects 49, confirming code execution.

No specific command required for this reconnaissance step; use manual testing or a proxy tool like [[tools/Burp-Suite]] to submit payloads.

> If the output executes the expression, proceed to file manipulation. Otherwise, the input is not vulnerable.

### Step 2: Read File Contents Using Groovy File Access

**Context**: Once SSTI is confirmed, inject a Groovy expression to read a target file's contents. This step uses the File class to load and display text from a specified path, allowing exfiltration of sensitive information like /etc/passwd or application configs.

**Command** ([[commands/groovy-read-file-text]]):
```groovy
${String x = new File('/path/to/file').getText('UTF-8')}
```

> This command reads the file at the specified path using UTF-8 encoding and stores the content in variable x, which is then rendered in the response. Replace '/path/to/file' with a target like '/etc/passwd' on Linux or 'C:/Windows/notepad.exe' on Windows. Expected output includes the file's raw text in the HTTP response body. Verify by checking if sensitive data appears unescaped.

### Step 3: Create a New File on the Server

**Context**: After reading files, create a new file to write arbitrary content, such as a webshell or log file for persistence. This leverages Groovy's File.createNewFile() method to establish a foothold.

**Command** ([[commands/groovy-create-new-file]]):
```groovy
${new File("C:\Temp\FileName.txt").createNewFile();}
```

> This command creates an empty file at the specified path. For Windows paths, use double backslashes; for Linux, use forward slashes. Expected output is a boolean true in the response if successful, or an exception if permissions are denied. Follow up by reading the file in a subsequent request to confirm creation.

### Step 4: Combine Operations for Advanced Manipulation

**Context**: For more complex scenarios, chain multiple expressions in a single injection to read and then write based on the read data, enhancing persistence or data modification.

**Code** ([[codes/groovy-ssti-file-manipulation-snippet]]):

> Embed the full snippet in the vulnerable input. This performs a read operation first (e.g., on notepad.exe), then a parameterized read, and finally creates a new file. Observe the response for concatenated outputs or errors indicating success/failure. Use this for scenarios requiring sequential file ops in one request.

### Step 5: Verify and Exfiltrate Results

**Context**: After injection, capture the response to extract file contents or confirm creation. Use a proxy to log outputs and manually verify no errors occurred.

No specific command; inspect HTTP responses for rendered Groovy output.

> Success is indicated by file contents appearing in the page or a confirmation of file creation without exceptions. If content is truncated, adjust paths or encoding.
