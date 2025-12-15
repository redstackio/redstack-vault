---
tags:
  - directory-listing
  - information-disclosure
  - reconnaissance
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-listing]]'
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 43a4c9e8-d8bc-47ff-89f6-6ae4d6f4ee89
created_at: '2025-12-14T17:26:17.419Z'
updated_at: '2025-12-14T17:26:17.419Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Exposed-Directories-via-Listing

## Summary

This procedure involves checking for and exploiting directory listing vulnerabilities on web servers, such as those running Nextcloud, to enumerate files in unprotected directories like /assets/, /css/, and /js/. It reveals sensitive file structures, asset details, and server information, aiding in reconnaissance for further attacks.

## Description

Directory listing occurs when a web server is configured to display the contents of a directory if no index file (e.g., index.html) is present. In the case of the Nextcloud demo site at https://try.nextcloud.com, this misconfiguration allows unauthorized users to view listings of static assets, exposing file names, potentially sensitive configurations, and server version via headers. This technique is low-effort and requires no special privileges, making it a common starting point for web application reconnaissance. Expected outcomes include identifying exploitable paths and gathering intel on the technology stack, such as Apache or Nginx versions, which could inform targeted exploits.

## Requirements

1. Direct network access to the target web server over HTTP/HTTPS
2. A web browser or command-line tool like curl for making requests
3. Knowledge of common web directory paths (e.g., /assets/, /css/, /js/)

## Defense

Defensive measures and detection strategies:

- Disable directory browsing in web server configurations: For Apache, add "Options -Indexes" in .htaccess or httpd.conf; for Nginx, set "autoindex off;" in the server block
- Implement web application firewalls (WAFs) to block suspicious path traversals or enumeration attempts
- Monitor access logs for repeated requests to non-existent or asset directories, using tools like Fail2Ban or SIEM systems to alert on anomalous patterns

## Objectives

1. Confirm if directory listing is enabled on target paths
2. Extract file listings and metadata for reconnaissance
3. Identify server details to map the technology stack

## Instructions

### Step 1: Test for Directory Listing on Assets Path

**Context**: Begin with a common static assets directory to check if the server returns a file listing instead of an error or redirect.

**Command** ([[commands/curl-directory-listing]]):
```bash
curl -i https://try.nextcloud.com/assets/
```

> This command sends a HEAD request with headers (-i flag) to the /assets/ path. If listing is enabled, expect a 200 OK status, Content-Type: text/html, and body content with file links (e.g., <a href="file.js">file.js</a>). Headers may reveal Server: Apache/2.4.x or similar, indicating the web stack.

### Step 2: Enumerate CSS and JS Directories

**Context**: Extend the test to stylesheet and script directories, which often hold application-specific files that could expose version info or custom code.

**Command** ([[commands/curl-directory-listing]]):
```bash
curl -i https://try.nextcloud.com/css/
curl -i https://try.nextcloud.com/js/
```

> Successful responses will list CSS/JS files, potentially including minified sources or themes that reveal Nextcloud version or dependencies. Look for patterns like versioned filenames (e.g., nextcloud-20.0.4.css) to infer software versions.

### Step 3: Analyze and Document Findings

**Context**: Review the output for actionable intelligence, such as downloadable files or version details.

**Command** ([[commands/curl-directory-listing]]):
```bash
curl -i https://try.nextcloud.com/assets/ | grep -i "server\|version"
```

> Pipe the output through grep to filter for server-related strings. This helps quickly identify exposed metadata without manual parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-listing]]

## Tools Used


## Tags

- [[directory-listing]]
- [[information-disclosure]]
- [[Reconnaissance]]
- [[nextcloud]]
