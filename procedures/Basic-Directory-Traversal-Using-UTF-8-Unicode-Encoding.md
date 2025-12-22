---
id: 2be02cf2-ff88-4fe8-a5f8-fb77ec8b5bb4
name: Basic-Directory-Traversal-Using-UTF-8-Unicode-Encoding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.837492+00:00'
updated_at: '2023-04-10T20:22:07.225560+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Basic exploitation]]'
  - '[[tags/Directory Traversal]]'
  - '[[tags/UTF-8 Unicode encoding]]'
  - directory-traversal
  - web-exploitation
  - unicode-bypass
commands:
  - '[[commands/curl-utf8-directory-traversal]]'
platforms:
  - Web
tools: []
validated: true
---

# Basic-Directory-Traversal-Using-UTF-8-Unicode-Encoding

## Summary

This procedure demonstrates a basic directory traversal attack using UTF-8 overlong encoding to bypass web application filters that block standard path traversal sequences like '../'. By encoding characters such as '/' and '.' with invalid UTF-8 byte sequences, attackers can access files outside the intended directory, such as sensitive configuration files or system logs, on vulnerable web servers.

## Description

Directory traversal vulnerabilities occur when a web application fails to properly sanitize user-supplied input used in file path construction, allowing attackers to navigate the file system. Standard traversals like '../../../../etc/passwd' are often detected by web application firewalls (WAFs) or input validation. This procedure uses UTF-8 overlong encodings—invalid representations of ASCII characters using multiple bytes—to evade such filters. For example, '/' can be encoded as %c0%af, which decodes to '/' on the server but appears benign to filters expecting standard URL encoding. This technique targets file inclusion or download endpoints in web apps, enabling unauthorized file access for reconnaissance or data exfiltration. It is effective against applications on Linux/Unix systems where files like /etc/passwd reveal user information.

## Requirements

1. Network access to a vulnerable web application endpoint that processes file paths from user input (e.g., via GET/POST parameters).
2. Knowledge of the target server's file system structure (e.g., common paths like /etc/passwd on Linux).
3. Tools like curl for sending HTTP requests; no special privileges required beyond external connectivity.
4. Optional: A proxy like Burp Suite to intercept and modify requests for testing.

## Defense

- Implement strict input validation and sanitization to canonicalize file paths, rejecting any traversal sequences (use libraries like Python's os.path.realpath).
- Deploy WAFs configured to detect overlong UTF-8 encodings and multi-byte representations of ASCII characters.
- Enforce least-privilege file access for the web server process, using chroot jails or containerization to limit directory navigation.
- Enable web server logging and monitor for anomalous file access patterns, such as requests to /etc/ or /proc/ directories.

## Objectives

1. Bypass input filters to access restricted files outside the web root.
2. Retrieve sensitive system information, such as user accounts from /etc/passwd.
3. Gather reconnaissance data to support further attacks, like identifying software versions or configurations.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a web application parameter that influences file paths, such as a 'file' or 'path' query string in a download or include feature. Test with benign inputs to confirm the endpoint responds with file content.

Use a basic curl request to probe the endpoint without traversal.

**Command** ([[commands/curl-basic-file-request]]):
```bash
curl -X GET "http://target.com/download?file=allowed.txt"
```

> This step verifies the endpoint works. Expected output is the content of allowed.txt. If it returns file data, proceed to traversal testing.

### Step 2: Prepare Encoded Traversal Sequences

**Context**: Use UTF-8 overlong encodings to represent traversal characters. Refer to the encoding mappings in [[codes/UTF-8-Overlong-Encodings-for-Directory-Traversal]] for equivalents of '.', '/', and '\'. Construct a path like '%c0%af..' to simulate '../' without triggering filters.

Embed the encodings directly in your request payload.

### Step 3: Execute Encoded Directory Traversal

**Context**: Inject the encoded traversal into the vulnerable parameter to navigate to a target file, such as /etc/passwd. Start with minimal traversals (e.g., one '../') and increase depth as needed to reach system directories.

**Command** ([[commands/curl-utf8-directory-traversal]]):
```bash
curl -X GET "http://target.com/download?file=%c0%af.%c0%af.%c0%af.%c0%af.%c0%afetc%2fpasswd" -v
```

> Replace 'download' and 'file' with the actual endpoint and parameter. The '-v' flag shows verbose output for debugging. Expected output includes the contents of /etc/passwd if successful, such as user account lines. If blocked, try alternative encodings from the code reference or increase traversal depth.
