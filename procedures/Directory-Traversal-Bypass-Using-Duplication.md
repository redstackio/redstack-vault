---
id: 7f5f9349-9024-493f-9b53-3c1c5afed5d8
name: Directory-Traversal-Bypass-Using-Duplication
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.856182+00:00'
updated_at: '2023-04-10T20:22:08.582264+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Basic exploitation]]'
  - '[[tags/Bypass ../ replaced by ]] '
  - '[[tags/Directory Traversal]]'
  - directory-traversal
  - waf-bypass
commands:
  - '[[commands/curl-directory-traversal-bypass]]'
tools:
  - '[[tools/cURL]]'
platforms:
  - Web
validated: true
---

# Directory-Traversal-Bypass-Using-Duplication

## Summary

This procedure demonstrates how to bypass Web Application Firewalls (WAFs) that filter out '../' sequences in directory traversal attacks by duplicating the traversal patterns, such as using '..././' for Unix-like systems or '...\.\.' for Windows. It allows attackers to access restricted files or directories on the server by evading simple string replacement filters.

## Description

Directory traversal vulnerabilities enable attackers to read or manipulate files outside the intended web root by manipulating path parameters with '../' sequences. Many WAFs implement basic defenses by removing or replacing '../' in input strings, but this can be bypassed by repeating the pattern multiple times (e.g., '../../' becomes '.../../' after partial removal, still allowing traversal). This technique targets naive WAF rules that do not account for redundancy or encoding variations. It is commonly used against file inclusion parameters in web applications like image viewers or log downloaders. The target environment is typically a web server (Apache, Nginx) with a vulnerable application, and success depends on the WAF's exact filtering logic. Expected outcomes include retrieving sensitive files like /etc/passwd or web.config.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS endpoint accepting file path parameters).
2. Knowledge of the vulnerable parameter (e.g., ?file= or ?path=).
3. Installed tools: curl for command-line testing or a proxy like Burp Suite for interception.
4. Basic understanding of the target's OS (Unix or Windows) to craft appropriate payloads.

## Defense

- Implement strict input validation and sanitization to normalize paths and block any traversal attempts, using libraries like OWASP ESAPI.
- Configure WAFs with advanced rules that detect redundant patterns, encodings (e.g., %2e%2e%2f), and absolute paths, not just simple string replacement.
- Monitor application logs and web traffic for anomalous file access patterns, such as requests to /etc/passwd or unusual path lengths.

## Objectives

1. Evade WAF filtering on standard directory traversal payloads.
2. Traverse to restricted directories and retrieve sensitive files.
3. Validate the bypass by accessing known sensitive files like /etc/passwd on Unix or C:\Windows\system.ini on Windows.

## Instructions

### Step 1: Identify the Vulnerable Endpoint and Parameter

**Context**: Determine the input parameter that handles file paths and confirm basic directory traversal without bypass. This step verifies the vulnerability exists before applying the bypass.

Use [[commands/curl-directory-traversal-bypass]] with a standard payload to test:

**Command** ([[commands/curl-directory-traversal-bypass]]):
```bash
curl "http://target.com/vulnerable?file=../../../etc/passwd" -v
```

> This sends a basic traversal request. If blocked by WAF, the response will show an error or filtered output. Expected output for a vulnerable but unfiltered app: contents of /etc/passwd. If filtered, proceed to bypass; why: confirms the parameter is injectable and WAF is active.

### Step 2: Craft and Apply Bypass Payload

**Context**: Use duplicated traversal sequences to evade the WAF's '../' removal. Reference the bypass strings from [[codes/Directory-Traversal-Bypass-Payloads]] and insert them into the request to chain multiple traversals.

For Unix targets, replace '../' with '..././' repeated as needed (e.g., for two levels up: '..././..././'). For Windows, use '...\.\.'. Adjust the count based on filter strength.

**Command** ([[commands/curl-directory-traversal-bypass]]):
```bash
curl "http://target.com/vulnerable?file=..././..././..././etc/passwd" -v
```

> This duplicates the traversal to survive removal of individual '../' instances. Expected output: successful retrieval of file contents if bypass works. Why: redundancy ensures residual traversal after filtering. If still blocked, increase repetitions or try URL encoding.

### Step 3: Verify Access and Extract Data

**Context**: Confirm success by checking for sensitive data in the response and iterate if partial success (e.g., access logs but not root files).

Review the response for file contents. If successful, use the same method to target other files like /etc/shadow or configuration files.

> Decision point: If output shows partial path resolution, add more duplications (e.g., four '..././'). Expected output: raw file data. Why: validates the bypass and allows further enumeration.
