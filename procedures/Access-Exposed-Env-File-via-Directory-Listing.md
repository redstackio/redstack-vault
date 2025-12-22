---
tags:
  - information-disclosure
  - directory-listing
  - env-file
  - aws
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - AWS
techniques:
  - '[[Credentials In Files]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 0b9affa5-d96e-4697-84ed-a3bc45f8219a
created_at: '2025-12-14T17:25:17.273Z'
updated_at: '2025-12-14T17:25:17.273Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Access-Exposed-Env-File-via-Directory-Listing

## Summary

This procedure exploits a web server misconfiguration where directory listing is enabled, allowing unauthenticated access to an exposed .env file containing sensitive application configurations such as database and email credentials. It is commonly used in reconnaissance phases to gather credentials for further exploitation of connected services like databases and SMTP servers.

## Description

In this attack scenario, an AWS-hosted web server has directory listing enabled, which lists all files in a directory when no index file is present. Attackers can simply navigate to the URL of the directory or directly to the .env file, revealing key environment variables without any authentication. The target environment typically involves a public-facing web application on AWS (e.g., EC2 with Apache or Nginx), where the .env file is inadvertently placed in an accessible web root. Expected outcomes include obtaining credentials that could lead to unauthorized database queries, email spoofing, or lateral movement. Prerequisites include public accessibility of the server and knowledge of the URL path to the .env file.

## Requirements

1. Public internet access to the target AWS web server URL
2. A standard web browser (no special permissions needed)
3. Basic understanding of URL structures and HTTP responses

## Defense

Defensive measures and detection strategies:

- Disable directory listing on web servers (e.g., set Options -Indexes in Apache .htaccess or Nginx config)
- Store .env files outside the web root or use proper file permissions (e.g., chmod 600)
- Implement web application firewalls (WAF) to block access to sensitive file paths
- Monitor server logs for anomalous GET requests to .env or config files
- Use environment variable management tools like AWS Secrets Manager instead of plaintext files

## Objectives

1. Retrieve sensitive credentials from the exposed .env file
2. Identify connected services (e.g., database hosts, email providers) for potential follow-on attacks
3. Assess the scope of information disclosure without triggering alerts

## Instructions

### Step 1: Launch Web Browser

**Context**: Begin the procedure by opening a browser to establish a connection to the target server.

No command required; simply open the browser application.

> Launching the browser prepares the interface for URL navigation. Expected output is an empty browser window ready for input.

### Step 2: Navigate to Exposed URL

**Context**: Directly access the directory or file path where directory listing exposes the .env file.

Enter the target URL in the address bar, such as http://target-domain.com/.env, and load the page.

> The browser sends an HTTP GET request to the server. If directory listing is enabled, the response will display file contents or a directory index. Expected output includes the raw .env file text if directly accessed.

### Step 3: Extract and Document Contents

**Context**: Review the displayed sensitive data and save it for analysis.

Visually inspect the page content, copy the relevant variables (e.g., DB_PASSWORD=secret123), and note them in a secure location.

> This step captures the disclosure. Expected output is a list of key-value pairs like APP_KEY=base64:..., DB_HOST=localhost. Validate by checking for credentials that match known services.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[information-disclosure]]
- [[directory-listing]]
- [[aws]]
