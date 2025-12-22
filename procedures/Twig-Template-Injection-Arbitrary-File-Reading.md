---
id: 54536d94-3f0c-4ff4-a13c-69377e574eeb
name: Twig-Template-Injection-Arbitrary-File-Reading
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.337269+00:00'
updated_at: '2023-04-10T20:23:50.814255+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Server Side Template Injection]]'
  - '[[tags/Twig]]'
  - '[[tags/Twig - Arbitrary File Reading]]'
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Twig-Template-Injection-Arbitrary-File-Reading

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in PHP applications using the Twig template engine to perform arbitrary file reading. By injecting malicious Twig templates into user-controlled inputs, an attacker can extract sensitive file contents, such as user account lists from /etc/passwd or database credentials from configuration files like wp-config.php, enabling further compromise of the target system.

## Description

Twig is a flexible, fast, and secure template engine for PHP, commonly used in web applications like WordPress plugins or custom frameworks to generate dynamic HTML. When improperly configured—such as with the 'autoescape' option disabled or sandbox mode not enforced—Twig allows injection of arbitrary template expressions. This leads to SSTI, where attackers can execute Twig functions like 'file_excerpt' to read file portions or 'include' to load entire files.

In a typical scenario, an attacker identifies a vulnerable input field (e.g., a search parameter or template variable) in a web form. By submitting a crafted payload, they trigger the Twig engine to interpret and execute the injection, outputting sensitive data directly in the response. For example, reading /etc/passwd reveals system users, while including wp-config.php exposes database credentials, potentially allowing database access or full site takeover. This technique is particularly dangerous in misconfigured hosting environments where file permissions are lax.

The procedure assumes the target is a Linux-based web server (e.g., Apache/Nginx with PHP-FPM) and focuses on non-destructive file reads to maintain stealth. Success depends on the Twig version (vulnerable in versions before strict sandboxing) and application context.

## Requirements

1. Valid HTTP access to a vulnerable PHP web application using Twig templates (e.g., via browser or proxy like Burp Suite).
2. Knowledge of common file paths on the target server, such as /etc/passwd for user enumeration or application-specific configs like wp-config.php.
3. A tool for intercepting and modifying HTTP requests (e.g., browser dev tools or proxy) to inject and test payloads.
4. Basic understanding of the application's input points where Twig rendering occurs (e.g., user profile templates or search results).

## Defense

Defensive measures and detection strategies:

- Configure Twig with autoescaping enabled and sandbox mode active to restrict dangerous functions like 'file_excerpt' and 'include'.
- Validate and sanitize all user inputs before passing them to Twig templates, using whitelisting for allowed characters and rejecting template syntax (e.g., {{ }}).
- Run the application with least-privilege file permissions, restricting web server access to sensitive directories like /etc and application configs.
- Monitor web server logs for anomalous requests containing Twig syntax (e.g., {{ or |file_excerpt) and implement WAF rules to block them.
- Regularly update Twig and PHP dependencies to patch known SSTI vulnerabilities.

## Objectives

1. Confirm the presence of a Twig SSTI vulnerability in the target application.
2. Extract contents of sensitive files to gather reconnaissance data, such as user accounts or credentials.
3. Use extracted information to pivot to further attacks, like database access via wp-config.php credentials.
4. Achieve this with minimal noise to avoid detection during red team operations.

## Instructions

### Step 1: Identify Vulnerable Injection Point

**Context**: Locate user-controlled inputs that are rendered through Twig templates, such as form fields, URL parameters, or API endpoints. Common points include search boxes, username displays, or dynamic content sections in WordPress themes.

Test for injection by submitting a simple payload like '{{7*7}}' and checking if the response evaluates to '49' instead of literal output. This confirms Twig interpretation without file access.

> If the output shows '49', proceed; otherwise, the input is not vulnerable or escaped.

### Step 2: Craft and Inject File Reading Payload

**Context**: Use Twig's built-in filters and functions to read files. The 'file_excerpt' filter extracts lines from a file, while 'include' loads entire file contents. Start with a low-risk file like /etc/passwd to verify, then target high-value files like wp-config.php.

Prepare the payload using the Twig arbitrary file read code snippet:

**Code** ([[codes/Twig-Arbitrary-File-Read-Payload]]):

```twig
"{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{include("wp-config.php")}}
```

Inject this into the vulnerable parameter via HTTP POST/GET (e.g., using curl or a proxy). For example, if the endpoint is /search?q=<input>, set q to the payload URL-encoded.

> The '@' separates outputs to avoid syntax errors. Adjust line numbers in file_excerpt for larger files.

### Step 3: Retrieve and Analyze Output

**Context**: Submit the request and capture the response. Successful injection will embed file contents in the HTML output, often visible in the page source or response body.

Decode any URL encoding if needed and parse the output for sensitive data. For /etc/passwd, look for user entries; for wp-config.php, extract DB_HOST, DB_USER, and DB_PASSWORD.

> If output is truncated, chain multiple requests with adjusted line ranges (e.g., file_excerpt(31,60)). Verify no errors like 'Twig_Error_Runtime' appear, indicating sandbox restrictions.

### Step 4: Verify and Document Findings

**Context**: Confirm the data's validity and assess impact. Cross-reference extracted users with known system accounts and test wp-config.php credentials against the database if possible.

Save outputs securely and note any detection artifacts, such as increased log entries for file access.
