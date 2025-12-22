---
id: d24ad39f-ec51-46a8-b9e3-67ee3eb5b0de
name: Netdoc-SSRF-via-URL-Scheme
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.999934+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Netdoc]]'
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF exploitation via URL Scheme]]'
commands:
  - '[[commands/curl-netdoc-ssrf-exploit]]'
platforms:
  - Web
tools: []
validated: true
---

# Netdoc-SSRF-via-URL-Scheme

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in the Netdoc web application by leveraging URL schemes to force the server to make unauthorized requests to internal resources, such as reading local files like /etc/passwd. It allows attackers to bypass access controls and retrieve sensitive data from the server's local filesystem or internal network.

## Description

Netdoc is a web-based document storage and sharing application that processes user-supplied URLs without proper validation, enabling SSRF attacks via custom URL schemes like 'netdoc://'. An attacker can craft a request to an endpoint such as ssrf.php, injecting a malicious URL scheme that tricks the server into fetching internal resources. This technique is particularly effective against applications that handle document imports or URL processing without sanitizing inputs. The exploit can lead to disclosure of sensitive files, metadata, or even pivoting to internal services. It requires authenticated or unauthenticated access depending on the endpoint, and success relies on the server's ability to resolve the scheme to local paths. Potential business impacts include data leakage, unauthorized internal reconnaissance, and facilitation of further attacks like lateral movement.

## Requirements

1. Network access to the Netdoc web application (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the vulnerable endpoint (e.g., /ssrf.php) and supported URL schemes.
3. Tools for crafting and sending HTTP requests, such as curl or a web proxy.
4. Optional: Attacker-controlled server for advanced SSRF payloads involving external callbacks.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all URL parameters to block custom schemes and internal IPs (e.g., 127.0.0.1, localhost, file://).
- Use a whitelist of allowed protocols (e.g., http/https only) and domains for URL processing.
- Deploy web application firewalls (WAFs) to detect and block SSRF patterns, such as unusual URL schemes or internal host references.
- Monitor server logs and network traffic for anomalous outbound requests from the application server to internal resources.
- Disable unnecessary URL scheme handlers in the application and conduct regular vulnerability scans for SSRF exposures.

## Objectives

1. Force the Netdoc server to read and return contents of internal files, such as /etc/passwd, to disclose user accounts and system information.
2. Perform unauthorized reconnaissance on internal network resources accessible via the SSRF.
3. Exfiltrate sensitive data from the server's local filesystem or metadata stores.

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Confirm the presence of the SSRF-vulnerable endpoint, such as ssrf.php, which processes URL parameters without validation. This step verifies the attack surface.

Use a browser or proxy to send a test request to the endpoint with a benign URL.

**Expected Output**: A successful response from the server indicating the endpoint is active, without errors.

### Step 2: Craft and Send the SSRF Payload

**Context**: Construct a malicious request using the 'netdoc://' URL scheme to target internal files. This exploits the lack of scheme validation to read local resources.

Execute [[commands/curl-netdoc-ssrf-exploit]] to send the crafted request:

```bash
curl -X GET "http://target.netdoc/ssrf.php?url=netdoc://$_TARGET_FILE" -v
```

> This command sends an HTTP GET request to the ssrf.php endpoint with the malicious URL scheme. The 'netdoc://' scheme tricks the server into interpreting it as a local path, fetching the file contents. Replace $_TARGET_FILE with the desired path, e.g., /etc/passwd. The -v flag provides verbose output for debugging. If successful, the response body will contain the file contents.

**Expected Output**: The server's response includes the contents of the targeted file, such as user account listings from /etc/passwd.

### Step 3: Verify and Extract Data

**Context**: Analyze the response to confirm data exfiltration and check for additional sensitive information. This step validates the exploit and identifies further opportunities.

Review the output from the previous command for readable file contents. If the response is encoded or truncated, adjust the payload or use URL encoding for special characters.

**Expected Output**: Readable sensitive data, such as hashed passwords or configuration details, confirming successful SSRF exploitation.

### Step 4: Escalate if Possible

**Context**: If the initial file read succeeds, attempt to target other resources like internal metadata endpoints or cloud instance metadata (e.g., netdoc://169.254.169.254/latest/meta-data/ for AWS).

Repeat Step 2 with escalated targets, monitoring for errors or blocks.

**Expected Output**: Additional internal data or access tokens, enabling further attacks like privilege escalation.
