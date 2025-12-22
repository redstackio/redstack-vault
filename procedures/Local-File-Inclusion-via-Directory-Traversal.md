---
id: bfac301f-8e8d-47f8-abc2-6760d2ea1f09
name: Local-File-Inclusion-via-Directory-Traversal
type: procedure
verified: true
submitted: true
created_at: '2020-07-22T17:12:11.994395+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/LFI]]'
  - '[[tags/Local File Inclusion]]'
  - '[[tags/Web Applications]]'
  - directory-traversal
commands:
  - '[[commands/curl-lfi-basic-test]]'
  - '[[commands/curl-lfi-traversal-to-etc-passwd]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
validated: true
---

# Local-File-Inclusion-via-Directory-Traversal

## Summary

This procedure demonstrates how to exploit Local File Inclusion (LFI) vulnerabilities in web applications by manipulating file path parameters to include sensitive local files, such as /etc/passwd, using directory traversal techniques like '../' sequences. It is commonly used during web application penetration testing to assess information disclosure risks.

## Description

Local File Inclusion (LFI) occurs when a web application includes a file specified by user input without proper validation, allowing attackers to read arbitrary files on the server. By injecting directory traversal payloads (e.g., '../../../etc/passwd'), attackers can navigate outside the intended directory and access system files. This technique is effective against applications using functions like include() in PHP or similar in other languages. It requires a vulnerable parameter (e.g., ?page= or ?file=) that directly influences file loading. Success depends on the server's file permissions and whether null byte injection or encoding is needed to bypass filters. This maps to MITRE ATT&CK techniques for file discovery and exploiting public-facing applications.

## Requirements

1. Access to a web application with a vulnerable file inclusion parameter (e.g., GET or POST parameter like 'file' or 'page').
2. Network connectivity to the target web server.
3. Tools like curl for command-line testing or Burp Suite for intercepting and modifying requests.
4. Basic knowledge of the target's directory structure (e.g., Linux /etc/passwd for user enumeration).

## Defense

Defensive measures and detection strategies:

- Input validation: Whitelist allowed file paths and reject traversal patterns like '../'.
- Use absolute paths or basename() to strip directories.
- Enable web application firewall (WAF) rules to block common LFI payloads.
- Monitor access logs for suspicious file paths and anomalous response sizes.
- Run the application in a chrooted environment or with minimal file permissions.

## Objectives

1. Identify and confirm the LFI vulnerability by including a known local file.
2. Traverse directories to access sensitive system files like /etc/passwd.
3. Gather information for further exploitation, such as user accounts or configuration details.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Determine the parameter that controls file inclusion by testing basic inputs and observing if the application loads different files.

Use [[commands/curl-lfi-basic-test]] to send a request with a legitimate file path:

```bash
curl "http://target.com/vulnerable.php?file=index.php"
```

> This command fetches the page with a standard file. If the response includes content from index.php, the parameter is likely vulnerable to manipulation.

### Step 2: Test Directory Traversal

**Context**: Inject traversal sequences to attempt reading files outside the web root, starting with null or simple payloads to bypass basic filters.

Proceed with [[commands/curl-lfi-traversal-to-etc-passwd]] for a targeted test:

```bash
curl "http://target.com/vulnerable.php?file=../../../etc/passwd"
```

> This traverses up three directories to reach /etc and includes passwd. Look for user account hashes or details in the response. If filtered, try URL encoding (%2e%2e%2f) or null bytes (%00).

### Step 3: Verify and Enumerate Further

**Context**: Confirm success by checking for expected file content and extend to other files like /etc/shadow or application configs.

Intercept and modify requests using [[tools/Burp-Suite]] if command-line tests fail due to CSRF tokens or sessions. Repeat Step 2 with variations:

- For Windows: `..\..\..\windows\system32\drivers\etc\hosts`
- Encode payloads if needed: `..%2f..%2f..%2fetc%2fpasswd`

> Success is indicated by leaked file contents in the HTTP response body. If blocked, chain with other techniques like log poisoning for RCE escalation.
