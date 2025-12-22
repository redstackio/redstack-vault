---
id: proc-uuid-placeholder
tags:
  - directory-listing
  - information-disclosure
  - wordpress
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:10.201Z'
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
# Browse-WordPress-Uploads-for-Directory-Listing-Enumeration

## Summary

This procedure exploits a common web server misconfiguration where directory listing is enabled on the WordPress `/wp-content/uploads/` directory, allowing attackers to browse and access uploaded files without authentication. It is primarily used in reconnaissance to identify sensitive information exposure, such as private documents or media, on public-facing WordPress sites.

## Description

WordPress sites often store user-uploaded files in the `/wp-content/uploads/` directory, organized by date (e.g., `/2023/10/`). By default, web servers like Apache or nginx should disable directory indexing to prevent unauthorized browsing. However, if `Options Indexes` is enabled in Apache or equivalent in nginx without restrictions, navigating directly to the directory URL reveals a listing of files and subfolders. This vulnerability was reported on mtn.ci, where accessing `https://www.mtn.ci/wp-content/uploads/` exposed the folder structure, potentially leaking confidential data uploaded by the site's administrators. The procedure requires no special tools—just a browser—and works over standard HTTP/HTTPS. Expected outcomes include viewing file names, sizes, and direct downloads, which could reveal metadata or sensitive content.

## Requirements

1. Publicly accessible WordPress website (no VPN or internal network needed)
2. Standard web browser with JavaScript enabled (though not required for basic listing)
3. Knowledge of the target site's base URL to construct the uploads path

## Defense

Defensive measures and detection strategies:

- Disable directory listing in web server config: For Apache, remove `Options Indexes` or add `Options -Indexes` in `.htaccess` or server block; for nginx, ensure `autoindex off;` in the location block.
- Implement access controls like IP whitelisting or authentication on the uploads directory.
- Monitor web server logs for anomalous GET requests to `/wp-content/uploads/` without referer headers.
- Use WordPress security plugins like Wordfence to scan for and alert on exposed directories.

## Objectives

1. Enumerate files and directories in the uploads folder to identify potential sensitive data.
2. Download or view exposed assets for further analysis.
3. Confirm the presence of the misconfiguration for vulnerability reporting.

## Instructions

### Step 1: Construct and Navigate to Uploads URL

**Context**: Identify the standard WordPress uploads path and access it directly to trigger the directory listing. This step accomplishes initial discovery of the exposed structure.

No specific command is needed; use a web browser.

Open your browser and enter the URL in the address bar:

```url
https://www.example.com/wp-content/uploads/
```

> Replace `www.example.com` with the target domain (e.g., `www.mtn.ci`). If the directory listing is enabled, the page will render an auto-generated index showing folders like `2023/10/` and files such as `document.pdf` (last modified dates and sizes may also appear). If disabled, you should see a 403 Forbidden or blank page.

### Step 2: Explore and Download Files

**Context**: Once the listing appears, interact with the exposed elements to enumerate deeper or retrieve content. This step accomplishes data collection from the vulnerability.

Click on hyperlinks to subfolders or files directly in the browser.

For downloading a file (manual step):

Right-click on a file link and select "Save link as..." or use browser dev tools to copy the full URL and download via `curl` if desired (though not required here).

> Successful exploration yields direct access to files, e.g., viewing an image or downloading a sensitive PDF. Look for indicators like unusual file names or recent uploads that might contain confidential info.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- directory-listing
- information-disclosure
- wordpress
- misconfiguration
