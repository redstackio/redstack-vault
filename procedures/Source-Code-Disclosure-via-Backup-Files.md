---
id: 8c561f69-72de-438e-984c-5f117f62a8af
name: Source-Code-Disclosure-via-Backup-Files
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T12:07:58.056555+00:00'
updated_at: '2023-05-26T01:22:59.501370+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - information-disclosure
  - owasp
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/curl-fetch-robots-txt]]'
  - '[[commands/curl-access-backup-directory]]'
  - '[[commands/curl-download-backup-file]]'
platforms:
  - Web
tools: []
validated: true
---

# Source-Code-Disclosure-via-Backup-Files

## Summary

This procedure demonstrates how to identify and access backup files on a web application that may disclose sensitive source code, configuration details, or credentials. By leveraging the robots.txt file to discover hidden directories, attackers can enumerate and retrieve unprotected backup artifacts, leading to information disclosure.

## Description

Web applications often leave backup files in accessible directories during development or deployment, such as .bak, .old, or .swp files containing source code with hardcoded secrets like database passwords. The robots.txt file, intended to guide web crawlers, frequently lists disallowed paths that inadvertently reveal administrative or backup directories. This technique targets misconfigurations where developers fail to secure these files, allowing unauthorized access. It is commonly used in reconnaissance phases to gather intelligence on the application's structure, technologies, and potential vulnerabilities. Success depends on the application's exposure and lack of access controls on these paths.

## Requirements

1. Valid URL of the target web application (e.g., https://target.com).
2. Network access to the target (no authentication required for public-facing sites).
3. Tools like curl for HTTP requests or a web browser for manual inspection.
4. Basic knowledge of HTTP and file enumeration.

## Defense

Defensive measures and detection strategies:

- Remove or secure backup files by excluding them from web root directories and using .htaccess rules to deny access (e.g., RedirectMatch 403 \.(bak|old|swp)$).
- Validate and sanitize robots.txt to avoid listing sensitive paths; use Disallow: /admin/ sparingly or remove it entirely.
- Implement web application firewalls (WAF) to block requests for common backup extensions.
- Monitor access logs for suspicious patterns like requests to /backup/ or robots.txt followed by directory access.
- Conduct regular file integrity checks and use version control to avoid leaving artifacts in production.

## Objectives

1. Discover hidden directories via robots.txt enumeration.
2. Locate and access backup directories containing source code artifacts.
3. Retrieve and analyze backup files for sensitive information like hardcoded credentials.
4. Expected outcome: Exposure of application source code, potentially revealing database secrets or API keys.

## Instructions

### Step 1: Identify the Target Application

**Context**: Begin by confirming the target web application's base URL and ensuring it is accessible. This step verifies the starting point for enumeration without alerting defenses.

No specific command required; use a browser or basic HTTP GET to load https://$_TARGET_URL. Look for signs of a web application (e.g., login pages, forms).

> If the site returns a 200 OK status, proceed. Otherwise, check for redirects or errors indicating the target is down or firewalled.

### Step 2: Retrieve the robots.txt File

**Context**: Fetch the robots.txt file to identify disallowed paths, which often include sensitive directories like /backup/ or /admin/ that may contain unprotected files. This step leverages standard web conventions for discovery.

**Command** ([[commands/curl-fetch-robots-txt]]):
```bash
curl -s $_TARGET_URL/robots.txt
```

> This command silently retrieves the contents of robots.txt. Expected output includes lines like "Disallow: /backup/", revealing hidden paths. If no robots.txt exists, the response will be empty or 404, indicating manual directory guessing may be needed next.

### Step 3: Analyze robots.txt for Hidden Directories

**Context**: Review the output from robots.txt to identify potential backup or administrative directories. Common entries include /backup, /old, or /tmp, which are often left accessible due to oversight.

Manually inspect the output for Disallow directives. For automation, pipe to grep:
```bash
echo "$(curl -s $_TARGET_URL/robots.txt)" | grep -i "disallow"
```

> Look for paths like /backup/ that suggest file storage. Success is indicated by discovery of at least one non-standard directory path.

### Step 4: Access the Backup Directory

**Context**: Use the discovered path (e.g., /backup/) to enumerate contents, checking for backup files like index.html.bak or config.php.old that may contain source code.

**Command** ([[commands/curl-access-backup-directory]]):
```bash
curl -s $_TARGET_URL/backup/
```

> This lists or displays the directory contents if not protected. Expected output: HTML or plain text showing file listings (e.g., backup.tar.gz, source.zip). A 403/404 indicates protection or non-existence; try variations like /backups/ or /_backup/.

### Step 5: Download and Inspect the Backup File

**Context**: Retrieve the identified backup file to analyze its contents for sensitive data, such as hardcoded database credentials (e.g., PostgreSQL secrets).

**Command** ([[commands/curl-download-backup-file]]):
```bash
curl -O $_TARGET_URL/backup/backup-file.bak
```

> This downloads the file locally. Expected output: A saved file (e.g., backup-file.bak) that can be opened with a text editor or archiver. Inspect for code snippets revealing secrets like "postgres://user:secret@host/db". Success is confirmed by finding readable source code or configs with sensitive info.

### Step 6: Verify Disclosure

**Context**: Confirm the extracted information's value and document findings. This step ensures the disclosure is actionable for further attacks, like credential reuse.

Open the downloaded file:
```bash
cat backup-file.bak | grep -i "password\|secret\|key"
```

> Expected: Lines containing credentials (e.g., "postgres secret: mypass123"). If no secrets, the file may still reveal application logic or endpoints for other exploits.
