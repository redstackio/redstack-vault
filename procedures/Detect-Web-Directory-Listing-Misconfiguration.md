---
type: procedure
description: >-
  Identifies enabled directory listing on web servers, which can disclose
  sensitive file structures and contents.
verified: true
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - directory-listing
  - misconfiguration
  - owasp
  - web-applications
commands:
  - '[[commands/curl-check-directory-listing]]'
platforms:
  - Web
tools:
  - '[[tools/cURL]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Detect-Web-Directory-Listing-Misconfiguration

## Summary

This procedure detects if a web server has directory listing enabled, a common misconfiguration that allows unauthorized users to view the contents of directories without an index file. By appending known or guessed directory names to the target URL, attackers can enumerate files and subdirectories, potentially exposing sensitive information like configuration files, backups, or source code. This is particularly useful during web application reconnaissance to identify information disclosure vulnerabilities aligned with OWASP Top 10 (A05:2021 - Security Misconfiguration).

## Description

Directory listing occurs when a web server (e.g., Apache, Nginx) is configured to automatically generate an HTML index of files in a directory if no default file (like index.html) is present. This feature, intended for convenience, becomes a security risk in production environments as it reveals the server's file structure, application paths, and potentially sensitive files. The procedure involves manually or programmatically accessing suspected directory paths via a browser or HTTP client like curl. Success is indicated by an 'Index of /' response showing file listings. This technique maps to MITRE ATT&CK T1083 (File and Directory Discovery) under the Discovery tactic, aiding in mapping the attack surface for further exploitation such as downloading sensitive files or identifying upload points.

## Requirements

1. Valid base URL of the target web application (e.g., http://example.com).
2. List of common or observed directory names (e.g., /admin/, /images/, /vcart/ from application navigation).
3. Web browser (e.g., Firefox, Chrome) or command-line tool like [[tools/cURL]] for automated checks.
4. Network access to the target (no authentication required for public directories).

## Defense

- Disable directory listing on web servers: For Apache, add 'Options -Indexes' in .htaccess or server config; for Nginx, use 'autoindex off;' in the location block.
- Implement web application firewalls (WAF) to block requests to common administrative paths.
- Use directory traversal protections and monitor access logs for anomalous directory requests.
- Regularly scan with tools like Nikto or OWASP ZAP to detect enabled listings.

## Objectives

1. Confirm if directory listing is enabled on target paths, exposing file structures.
2. Enumerate visible files and subdirectories for potential sensitive data disclosure.
3. Gather intelligence on application layout to support further reconnaissance or exploitation.
4. Validate success by observing unprompted file listings without authentication.

## Instructions

### Step 1: Identify Potential Directory Paths

**Context**: Begin by navigating the target web application to observe visible directories in URLs, error messages, or source code comments. Common directories include /admin, /backup, /images, /uploads, or application-specific ones like /vcart. This step builds a list of paths to test, focusing on areas likely to lack index files.

No command required; perform manually in a web browser by exploring the site.

> If directories are not obvious, use common wordlists (e.g., from SecLists) for brute-forcing, but start with observed ones to avoid noise.

### Step 2: Access and Test Directory URL

**Context**: Append the suspected directory to the base URL and access it. If listing is enabled, the server will return an auto-generated index page showing files and subfolders. This step verifies the misconfiguration and allows enumeration of contents.

**Command** ([[commands/curl-check-directory-listing]]):
```bash
curl -i $_TARGET_URL/$_DIRECTORY_NAME/
```

> This command sends an HTTP HEAD and GET request to the directory path. Look for a 200 OK status and HTML content starting with 'Index of /$_DIRECTORY_NAME'. If a 403 Forbidden or 404 Not Found appears, the listing is disabled or the directory doesn't exist. Repeat for multiple directories. In a browser, simply enter the URL (e.g., http://example.com/vcart/) and check for a file list table.

### Step 3: Analyze Response for Disclosure

**Context**: Review the output for sensitive files (e.g., config.php, .env, backups.zip). Download any exposed files using wget or browser for further analysis. Document findings, including file names, sizes, and last modified dates, to assess impact.

Use the browser's save feature or extend the curl command with -O to download:
```bash
curl -O $_TARGET_URL/$_DIRECTORY_NAME/$_FILE_NAME
```

> Success is confirmed if files are listed without authentication. If no listing appears but files are guessable, this may indicate partial protections—escalate to fuzzing with tools like dirbuster.
