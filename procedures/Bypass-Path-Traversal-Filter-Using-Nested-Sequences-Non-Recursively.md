---
id: b1e10fa8-2c4f-4134-b661-c0387f79c16e
name: Bypass-Path-Traversal-Filter-Using-Nested-Sequences-Non-Recursively
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T15:54:57.463041+00:00'
updated_at: '2023-05-26T01:13:15.182245+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Path Traversal]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-path-traversal-test]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Path-Traversal-Filter-Using-Nested-Sequences-Non-Recursively

## Summary

This procedure demonstrates a technique to bypass web application filters that strip path traversal sequences (like ../) non-recursively by using nested traversal payloads such as ....//. This allows unauthorized access to sensitive files on the server, such as /etc/passwd, by exploiting incomplete normalization in the input sanitization process.

## Description

Path traversal vulnerabilities occur when user-supplied input is used to construct file paths without proper validation, allowing attackers to read arbitrary files. In this scenario, the application strips single instances of ../ but fails to handle nested sequences like ....//, which normalize to ../ after partial stripping. This non-recursive filtering can be bypassed by crafting payloads with multiple dots and slashes that resolve to traversal paths upon server-side processing. The technique is commonly tested against file download or include endpoints in web applications. Success grants access to system files, potentially exposing user data, configurations, or credentials. This maps to MITRE ATT&CK technique T1083 (File and Directory Discovery) under the Discovery tactic.

## Requirements

1. Access to a web application with a vulnerable endpoint that accepts a 'filename' parameter for file retrieval (e.g., /download?file=example.txt).
2. Network access to intercept and modify HTTP requests, typically via a proxy tool like Burp Suite.
3. Basic knowledge of HTTP requests and URL encoding.
4. Target server running a Unix-like OS (e.g., Linux) where /etc/passwd exists.

## Defense

Defensive measures and detection strategies:

- Implement recursive path normalization and canonicalization to handle nested traversal sequences.
- Use whitelisting for allowed file paths instead of blacklisting traversal patterns.
- Validate file access against a secure base directory and log all file read attempts.
- Deploy web application firewalls (WAFs) with rules to detect anomalous traversal payloads.
- Enable server-side logging for file system access and monitor for unusual paths like /etc/.

## Objectives

1. Intercept and modify an HTTP request to a file retrieval endpoint.
2. Inject a nested traversal payload to bypass filtering and access a sensitive file.
3. Verify successful file disclosure by observing the response content.
4. Expected outcome: Retrieval of server file contents, such as /etc/passwd, confirming the bypass.

## Instructions

### Step 1: Intercept the Original Request

**Context**: Begin by capturing a legitimate request to the vulnerable endpoint to understand the baseline behavior and prepare for modification. This step establishes the request structure, such as the filename parameter.

Use Burp Suite [[tools/Burp-Suite]] to intercept traffic from your browser or a testing tool. Configure your browser proxy to route through Burp (default: 127.0.0.1:8080).

**Expected Output**: A captured HTTP GET or POST request, e.g., GET /download?file=example.txt HTTP/1.1, showing the original filename parameter.

### Step 2: Forward to Repeater for Modification

**Context**: Send the intercepted request to Burp's Repeater tab to allow safe iteration and testing of payloads without affecting the live application repeatedly. This isolates the testing environment.

In Burp Proxy, right-click the request and select "Send to Repeater." Review the request headers, method, and parameters.

**Expected Output**: The request appears in the Repeater tab, ready for editing, with no response yet sent.

### Step 3: Test the Original Request

**Context**: Send the unmodified request to confirm normal behavior and baseline the response. This verifies the endpoint functions as expected before attempting the bypass.

Click "Send" in Repeater to forward the request to the server.

**Expected Output**: A 200 OK response with the contents of the requested file (e.g., example.txt) or a benign error if the file doesn't exist.

### Step 4: Inject Nested Traversal Payload

**Context**: Modify the filename parameter with a nested traversal sequence to bypass the filter. The payload ....//....//....//etc/passwd uses quadruple dots and double slashes, which strip to ../ after non-recursive processing, navigating to the root directory.

Edit the filename parameter to: ....//....//....//etc/passwd. Ensure proper URL encoding if needed (e.g., %2e%2e%2e%2e%2f%2f for ....//). Click "Send."

Alternatively, test directly with [[commands/curl-path-traversal-test]] from the command line for verification without a proxy:

```bash
curl "http://target.com/download?file=....//....//....//etc/passwd"
```

> This command sends the modified request and displays the response. The nested sequences bypass the filter, causing the server to resolve the path to /etc/passwd.

**Expected Output**: A 200 OK response containing the contents of /etc/passwd, such as user account listings (e.g., root:x:0:0:root:/root:/bin/bash).

### Step 5: Verify and Iterate

**Context**: Confirm the bypass success and test variations to ensure robustness. If the payload fails, adjust nesting depth (e.g., more ....//) based on the filter's behavior.

Inspect the response for sensitive data. If blocked, try encoding or alternative payloads like ..%2f..%2f..%2fetc%2fpasswd.

**Expected Output**: Consistent file disclosure across multiple sends, with no errors indicating filtering.

**Success Indicators**:
- Response body includes /etc/passwd or similar sensitive file contents.
- No 403 Forbidden or sanitization errors in the response.
