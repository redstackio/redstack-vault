---
id: proc-wordpress-uploads-listing
tags:
  - directory-listing
  - wordpress
  - information-disclosure
  - file-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-list-directory]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:10.069Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-WordPress-Uploads-Directory-Listing

## Summary

This procedure exploits an enabled directory listing on a WordPress site's /wp-content/uploads/ endpoint to unauthorizedly enumerate and access uploaded files and folders, potentially exposing sensitive information such as private documents, images, or configuration files stored in the uploads directory.

## Description

In a typical WordPress installation, the uploads directory under /wp-content/uploads/ is used to store media and files uploaded via the admin interface or plugins. If the web server (e.g., Apache or Nginx) is misconfigured—such as lacking an index.php or index.html file, or having Options +Indexes enabled—directory browsing is permitted. An attacker can directly access this endpoint via a browser or HTTP client, revealing a listing of subdirectories (often organized by year and month) and files. This leads to information exposure, as anyone with the URL can download files without authentication. The attack requires no special privileges and works over standard HTTP/HTTPS, making it a low-effort reconnaissance technique that could reveal confidential data like user-submitted files or backups.

## Requirements

1. Publicly accessible WordPress site with known base URL (e.g., http://target.com)
2. Web browser or HTTP client like curl for accessing the endpoint
3. No authentication or prior access needed; assumes the /wp-content/uploads/ path follows standard WordPress conventions

## Defense

Defensive measures and detection strategies:

- Disable directory listing on web servers by adding an empty index.php or index.html to the uploads directory, or configuring server settings (e.g., in .htaccess: Options -Indexes)
- Use WordPress security plugins like Wordfence or iThemes Security to monitor and block anomalous access to sensitive paths
- Implement web application firewall (WAF) rules to detect and block requests to /wp-content/uploads/ from non-admin IPs
- Regularly audit server configurations and file permissions to ensure uploads are not publicly browsable

## Objectives

1. Enumerate the contents of the uploads directory to identify exposed files
2. Download potentially sensitive uploaded data for further analysis or exploitation
3. Assess the scope of information disclosure in the WordPress environment

## Instructions

### Step 1: Identify and Access the Uploads Endpoint

**Context**: Confirm the presence of the WordPress uploads directory and exploit the listing feature to view contents.

**Command** ([[commands/curl-list-directory]]):
```bash
curl -s http://www.mtn.co.sz/wp-content/uploads/ | html2text -nobs
```

> This command fetches the raw HTML response from the directory endpoint and converts it to readable text using html2text (install via apt install html2text if needed). The output will show a list of directories and files, such as <pre>Index of /wp-content/uploads/
Name                    Last modified      Size  Description
<hr>
2019/                   01-Jan-2019 00:00    -
2020/                   01-Jan-2020 00:00    -
image.jpg               15-Mar-2020 10:30   2.5M
</pre>. If successful, no 403 Forbidden or redirect occurs; instead, the listing is displayed.

### Step 2: Enumerate and Download Specific Files

**Context**: Once the listing is visible, navigate deeper into subdirectories or download individual files to extract sensitive data.

**Command** ([[commands/curl-download-file]]):
```bash
curl -O http://www.mtn.co.sz/wp-content/uploads/2020/01/confidential.pdf
```

> This downloads the specified file directly to the current directory. Repeat for other files identified in the listing. Expected output is the file saved locally, confirming access without authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-list-directory]]
- [[commands/curl-download-file]]

## Tools Used


## Tags

- [[directory-listing]]
- [[wordpress]]
- [[information-disclosure]]
