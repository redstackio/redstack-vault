---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - subversion
  - source-code-disclosure
  - wordpress
  - insecure-scm
platforms:
  - Web
  - Linux
commands:
  - '[[commands/curl-access-svn-text-base]]'
tools: []
verified: true
validated: true
---

# Subversion Source Code Disclosure

## Summary

This procedure exploits insecurely exposed Subversion (SVN) repositories on web servers to disclose sensitive source code files, such as the WordPress wp-config.php containing database credentials. By accessing the .svn directory structure, attackers can retrieve unencrypted file contents from the text-base subdirectory, enabling further compromise like database access or privilege escalation.

## Description

Subversion is a version control system often used for managing source code. When developers deploy code from an SVN repository to a web server without properly cleaning the .svn metadata directories, attackers can access historical file versions and configurations. In a typical WordPress scenario, the wp-config.php file in .svn/text-base/ reveals database host, username, password, and authentication keys. This technique requires only HTTP access to the web root and targets misconfigured servers where .svn is not restricted via .htaccess or server rules. It applies to any platform hosting SVN-managed code, such as Apache on Linux, and can lead to full application compromise if credentials are valid.

## Requirements

1. Network access to the target web server (HTTP/HTTPS over port 80/443).
2. Knowledge of the target application's file structure, e.g., location of wp-config.php in WordPress.
3. A tool like curl for making HTTP requests (standard on most systems).
4. No authentication required if the .svn directory is publicly accessible.

## Defense

- Restrict access to .svn directories using web server configurations (e.g., Apache Location blocks or Nginx deny rules).
- Regularly scan web servers with tools like Nikto or custom scripts to detect exposed .svn paths.
- Implement proper deployment processes to strip .svn metadata before production release.
- Use web application firewalls (WAFs) to block requests to sensitive paths like /.svn/.

## Objectives

1. Retrieve sensitive configuration files from exposed SVN repositories.
2. Extract credentials or other secrets to enable lateral movement or data exfiltration.
3. Assess the impact of source code disclosure on the target's security posture.

## Instructions

### Step 1: Identify the Target Web Application and SVN Exposure

**Context**: Determine if the target web server exposes SVN metadata by probing common paths. This step verifies the vulnerability without directly accessing files, reducing detection risk.

Use a browser or basic HTTP request to check for /.svn/ directory listing. If accessible, proceed to specific file retrieval.

**Expected Output**: HTTP 200 response with directory listing or file content; 403/404 indicates no exposure.

### Step 2: Access the SVN Text-Base for Specific Files

**Context**: Once exposure is confirmed, target the text-base subdirectory where unencrypted file versions are stored. For WordPress, focus on wp-config.php.svn-base to obtain database credentials.

**Command** ([[commands/curl-access-svn-text-base]]):
```bash
curl http://target-domain.com/.svn/text-base/wp-config.php.svn-base
```

> This command fetches the raw content of the wp-config.php file from the SVN repository. Replace target-domain.com with the actual hostname. The response will display PHP code including define() statements for DB_USER, DB_PASSWORD, etc. Verify the output contains valid credentials by parsing for database-related lines.

**Expected Output**: Plaintext PHP source code, e.g., lines like "define('DB_NAME', 'wordpress_db');" and "define('DB_PASSWORD', 'sensitive_password');".

### Step 3: Validate and Utilize Retrieved Information

**Context**: Confirm the extracted data's usefulness, such as testing database credentials against the exposed host. This step ensures the disclosure leads to actionable intelligence.

Manually review the output for secrets. If database details are obtained, attempt connection using a tool like mysql client: mysql -h <db_host> -u <db_user> -p<db_password>.

**Expected Output**: Successful database connection or confirmation of credential validity; errors indicate invalid or outdated info.

**Success Indicators**:
- Retrieval of readable file contents without errors.
- Presence of sensitive data like passwords or API keys in the output.
- Ability to use extracted info for further access (e.g., DB login).
