---
id: d0328130-b732-48bb-8234-939096e1a7c7
name: Perform-Unicode-Directory-Traversal
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.812849+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/16-bits-Unicode-encoding]]'
  - '[[tags/Basic-exploitation]]'
  - '[[tags/Directory-Traversal]]'
  - directory-traversal
  - unicode-bypass
  - web-exploitation
commands:
  - '[[commands/curl-unicode-directory-traversal]]'
platforms:
  - Web
tools: []
validated: true
---

# Perform-Unicode-Directory-Traversal

## Summary

This procedure demonstrates how to bypass web application filters for directory traversal attacks by encoding traversal sequences like '../' in 16-bit Unicode format. It allows attackers to access files outside the web root, such as sensitive configuration files or system logs, by crafting HTTP requests with encoded payloads.

## Description

Directory traversal vulnerabilities occur when user-supplied input is used to construct file paths without proper sanitization, enabling access to unintended directories. Standard traversals like '../etc/passwd' are often blocked by web application firewalls (WAFs) or input filters that detect common patterns. Unicode encoding exploits the fact that some parsers or filters may not decode or normalize 16-bit Unicode representations (e.g., %u002e for '.', %u2215 for '/'), allowing the traversal to slip through. This technique is particularly effective against applications using JavaScript or legacy systems that handle Unicode inconsistently. The target is typically a web parameter like 'file' or 'path' in a file inclusion endpoint. Success reveals file contents, potentially leading to further compromise like credential theft or RCE if combined with other flaws.

## Requirements

1. Network access to a vulnerable web application with a file inclusion or path parameter.
2. Knowledge of the target server's directory structure (e.g., Linux /etc/passwd or Windows boot.ini).
3. Tools like curl for sending HTTP requests or a proxy like Burp Suite for interception and modification.
4. Basic understanding of URL encoding and HTTP requests.

## Defense

- Implement strict input validation and path normalization to canonicalize all file paths before use.
- Use whitelisting for allowed file paths and directories, rejecting any traversal indicators even after decoding.
- Deploy WAF rules that decode and inspect Unicode/percent-encoded inputs for traversal patterns.
- Enable web server logging and monitor for anomalous file access attempts outside the web root.

## Objectives

1. Bypass directory traversal filters using 16-bit Unicode encoding.
2. Retrieve contents of sensitive files outside the web root.
3. Validate the vulnerability for potential escalation to data exfiltration or further attacks.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a parameter in the web application that accepts file paths, such as a file viewer or include function. Test with benign inputs to confirm it reads files from the web root.

Use browser developer tools or a proxy to inspect requests and identify the parameter (e.g., ?file=report.pdf).

**Expected Output**: Successful load of a known file from the web root, confirming the endpoint processes the parameter as a file path.

### Step 2: Encode Traversal Payload in Unicode

**Context**: Convert standard traversal strings to 16-bit Unicode to evade filters. Common mappings include '.' as %u002e, '/' as %u2215 (or %u002f for standard slash), and '\' as %u2216. For example, '../etc/passwd' becomes '%u002e%u002e%u2215etc%u2215passwd'.

Reference this Unicode encoding table for directory traversal characters:

| Character | Unicode Encoding |
|-----------|------------------|
| .         | %u002e           |
| /         | %u2215           |
| \        | %u2216           |

Craft the full payload by repeating '../' for the required depth (e.g., '%u002e%u002e%u2215%u002e%u002e%u2215etc%u2215passwd' to go up two directories).

**Expected Output**: Encoded string ready for insertion into the URL parameter.

### Step 3: Send Encoded Request

**Context**: Inject the Unicode-encoded traversal into the vulnerable parameter and send the HTTP request to retrieve the target file.

**Command** ([[commands/curl-unicode-directory-traversal]]):
```bash
curl -X GET "http://target.com/vulnerable?file=%u002e%u002e%u2215etc%u2215passwd" -v
```

> This command sends a GET request with the encoded traversal. The -v flag enables verbose output to inspect headers and response. Replace the URL and encoding as needed. If the application uses POST, adjust accordingly.

**Expected Output**: HTTP 200 response containing the contents of /etc/passwd (or equivalent file), such as user account listings. Errors like 404 indicate insufficient traversal depth or blocking; adjust encodings or depth iteratively.
