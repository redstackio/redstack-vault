---
id: 80b8956b-d0b8-4e8c-8cb6-add962e0a8ad
name: Path-Traversal-Validation-of-File-Extension-with-Nullbyte-Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:21:04.123201+00:00'
updated_at: '2023-05-26T01:38:01.246217+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Path Traversal]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-path-traversal-nullbyte]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Path-Traversal-Validation-of-File-Extension-with-Nullbyte-Bypass

## Summary

This procedure demonstrates how to bypass file extension validation in path traversal vulnerabilities by appending a null byte (%00) followed by an allowed extension, such as .jpg, to access restricted files like /etc/passwd on a web server.

## Description

Path traversal attacks allow attackers to access files outside the intended directory by manipulating file path parameters. Some applications implement validation to ensure uploaded or requested files have safe extensions (e.g., only .jpg or .png). However, if the validation is performed in a language or context where null bytes terminate strings (like in C-based parsing), appending %00 (URL-encoded null byte) followed by an allowed extension can trick the validator into seeing only the safe extension while the backend processes the full path. This procedure uses Burp Suite to intercept and modify requests, but includes a curl equivalent for command-line testing. It targets web applications vulnerable to directory traversal with weak extension checks, commonly found in file upload or image processing endpoints.

## Requirements

1. Access to a vulnerable web application with a file path parameter (e.g., download.php?file=image.jpg).
2. Network connectivity to the target server.
3. Burp Suite or equivalent proxy tool for request interception and manipulation.
4. Basic knowledge of URL encoding and HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement proper path normalization and canonicalization to prevent traversal sequences like ../.
- Use whitelisting for allowed file paths and extensions, validating the full resolved path on the server side.
- Avoid null byte handling in string parsing; use secure languages or libraries that don't terminate on %00.
- Log and monitor requests containing ../, %00, or unusual path patterns; implement WAF rules to block them.
- Restrict file access to a chrooted or isolated directory without sensitive system files.

## Objectives

1. Identify and bypass extension validation in path traversal vulnerabilities.
2. Access restricted files such as /etc/passwd.
3. Verify successful bypass by observing file contents in the response.

## Instructions

### Step 1: Intercept the Original Request

**Context**: Use a proxy to capture the legitimate file request, which will serve as the base for modification. This allows observation of normal behavior before injecting the payload.

**Tool** ([[tools/Burp-Suite]]): Configure your browser to route traffic through Burp Suite proxy (default: 127.0.0.1:8080). Navigate to the vulnerable endpoint (e.g., http://target.com/download.php?file=image.jpg) and intercept the GET or POST request.

> This step ensures you can see the parameter structure (e.g., 'file') and the server's normal response, such as serving the image file without errors.

### Step 2: Forward to Repeater and Analyze Response

**Context**: Send the intercepted request to Burp's Repeater tab for manual manipulation. Execute the original request to confirm baseline response.

**Tool** ([[tools/Burp-Suite]]): In the Proxy tab, right-click the intercepted request and select "Send to Repeater." In Repeater, click "Send" to forward the request and observe the response, which should return the expected file content or a 200 OK status.

> Expected output includes the file contents or metadata without errors. This verifies the endpoint is functional and identifies the parameter to target (e.g., 'file=image.jpg').

### Step 3: Modify Parameter with Null Byte Bypass Payload

**Context**: Inject the path traversal sequence with null byte to bypass extension validation. The %00 terminates the string for validation, allowing access to the traversed path while appearing as a safe .jpg file.

**Command** ([[commands/curl-path-traversal-nullbyte]]):
```bash
curl -X GET "http://target.com/download.php?file=../../../etc/passwd%00.jpg" -v
```

> Alternatively, in Burp Repeater, modify the 'file' parameter to '../../../etc/passwd%00.jpg' and send the request. The server should process the path up to %00, ignoring .jpg for access but validating it as safe. This step accomplishes reading sensitive files by chaining directory traversal with the bypass.
