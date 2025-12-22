---
type: procedure
description: >-
  Bypass path traversal filters that strip standard sequences by using double
  URL encoding to access sensitive files on a web application.
verified: true
submitted: false
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - path-traversal
  - web-applications
  - filter-bypass
  - url-encoding
commands:
  - '[[commands/curl-send-double-encoded-path-traversal]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Path-Traversal-with-Double-URL-Encoding

## Summary

This procedure outlines how to evade path traversal detection mechanisms in web applications that strip standard '../' sequences by employing double URL encoding. The technique obfuscates the traversal payload so that after one layer of decoding, the filter does not recognize it, allowing the second decode to reveal the true path and enable access to arbitrary files, such as /etc/passwd on Linux-based servers.

## Description

Path traversal vulnerabilities allow attackers to access files outside the intended directory by manipulating input parameters like 'filename' in file inclusion or download endpoints. Many applications implement basic filters to remove '../' patterns, but these can be bypassed using encoding tricks. Double URL encoding works because the application may perform only one decode before filtering: the first decode yields encoded characters (e.g., %2e%2e%2f for ../), which evade the strip, and the second decode (often implicit in path resolution) reveals the traversal. This is effective against simplistic sanitization and targets web apps with insufficient input normalization. Prerequisites include a vulnerable endpoint and the ability to intercept/modify requests.

## Requirements

1. A proxy tool like Burp Suite for request interception and modification.
2. A vulnerable web application endpoint that accepts a file path parameter (e.g., /download?file=example.txt).
3. Network access to the target application.
4. Basic knowledge of URL encoding (e.g., . = %2E, / = %2F).

## Defense

Defensive measures and detection strategies:

- Normalize and decode inputs multiple times (at least twice) before processing.
- Use absolute path whitelisting to restrict file access to safe directories.
- Implement web application firewalls (WAFs) with rules for encoded traversal patterns.
- Log and monitor requests containing multiple '%' characters or suspicious encodings.
- Validate file existence and MIME types server-side.

## Objectives

1. Obfuscate traversal sequences to bypass input filters.
2. Access sensitive system files outside the web root.
3. Confirm successful file retrieval in the response.

## Instructions

### Step 1: Intercept the Original Request

**Context**: Capture a legitimate request to the vulnerable endpoint to understand the parameter structure and baseline response. This allows isolation for modification without affecting the live session.

Configure [[tools/Burp-Suite]] as a proxy (default: 127.0.0.1:8080) and browse to the target endpoint (e.g., http://target.com/download?file=test.txt). Intercept the request in the Proxy tab.

**Expected Output**: The intercepted HTTP GET or POST request showing the 'file' parameter with a safe value.

### Step 2: Forward and Send to Repeater

**Context**: Forward the request to see the normal response, then duplicate it in Repeater for safe experimentation. Repeater allows multiple sends and response inspection without re-interception.

In Burp Proxy, forward the request once to confirm normal behavior. Right-click the request in the history and select "Send to Repeater."

**Expected Output**: Baseline response with the contents of the safe file (e.g., test.txt).

### Step 3: Generate Double-Encoded Traversal Payload

**Context**: Create an obfuscated version of the traversal path (e.g., ../../../../etc/passwd) by double URL encoding. Standard ../ becomes %2e%2e%2f after single encode; double encode to %252e%252e%252f so the filter sees non-traversable text after one decode.

In Burp Repeater or Decoder tab, input the path ../../../../etc/passwd and apply URL encode twice. The resulting payload should resemble: %252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd (adjust depth as needed for the target environment).

**Expected Output**: Encoded string ready for insertion, verifiable in Decoder by decoding once to see %2e%2e%2f (which evades strip) and twice to see ../.

### Step 4: Modify and Send the Request

**Context**: Replace the parameter value with the double-encoded payload and submit to test the bypass. This step verifies if the filter is evaded and the file is served.

In Burp Repeater, update the 'file' parameter to the encoded payload (e.g., file=%252e%252e%252f...%252fpasswd). Click Send. Alternatively, replicate via CLI with [[commands/curl-send-double-encoded-path-traversal]] for automation.

```bash
curl "http://target.com/download?file=%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd" -v
```

> This command sends the request and displays verbose output, including the response body with file contents if successful. Adjust the URL and payload depth based on the target's directory structure.

**Expected Output**: HTTP response body containing the target file's contents (e.g., root:x:0:0:root:/root:/bin/bash for /etc/passwd).
