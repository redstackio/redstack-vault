---
id: proc-uuid-1
tags:
  - info-disclosure
  - credentials-leak
  - php-backup
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-fetch-url]]'
  - '[[commands/curl-grep-credentials]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:25:13.372Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# View-Source-of-PHP-Backup-File-to-Extract-Credentials

## Summary

This procedure involves accessing and inspecting the source code of a publicly available PHP backup file (e.g., .php.orig) to extract hardcoded database connection credentials, such as hostname, database name, username, and password, enabling potential unauthorized access to the backend database.

## Description

In web applications developed with PHP, developers often create backup files by appending extensions like .orig or .bak. If these files are not properly secured or removed, they can be accessed publicly via a web browser. By viewing the source code, attackers can reveal sensitive configuration details embedded in plain text. This vulnerability was observed in an educational domain linked to the U.S. Department of Defense, where the file https://██████████.edu/database.php.orig exposed full database credentials. The procedure assumes no authentication is required and relies on standard web access. Expected outcomes include obtaining valid credentials for further exploitation, such as logging into the database or using them in other attack vectors.

## Requirements

1. Web browser or command-line tool like curl for HTTP requests
2. Valid target URL pointing to the backup file (e.g., /database.php.orig)
3. Network access to the target domain without firewalls blocking GET requests

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to block access to files with extensions like .orig, .bak, or .swp
- Use .htaccess rules or server configurations (e.g., in Apache/Nginx) to deny access to backup files in web roots
- Regularly scan for exposed sensitive files using tools like Nuclei or custom scripts; monitor access logs for suspicious GET requests to non-standard paths
- Enforce environment-specific configurations where credentials are not hardcoded; use secure vaults like AWS Secrets Manager

## Objectives

1. Extract database connection details for unauthorized access
2. Assess the scope of exposure to plan further attacks like SQL injection or privilege escalation
3. Validate credentials for immediate use in database tools like phpMyAdmin or MySQL clients

## Instructions

### Step 1: Access the Backup File URL

**Context**: Directly fetch the content of the suspected backup file to confirm public accessibility.

**Command** ([[commands/curl-fetch-url]]):
```bash
curl https://██████████.edu/database.php.orig
```

> This command retrieves the raw PHP source code. Successful execution returns the file contents without errors, displaying commented or variable-defined code.

### Step 2: Extract Credential Variables

**Context**: Parse the response to isolate sensitive variables containing database details.

**Command** ([[commands/curl-grep-credentials]]):
```bash
curl https://██████████.edu/database.php.orig | grep -E 'hostname|db|username|password'
```

> This filters for common credential patterns. Expected output includes lines like `$hostname = '████████.edu'; $db = '█████████'; $username = '████_user'; $password = '████';`, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-url]]
- [[commands/curl-grep-credentials]]

## Tools Used

- [[tools/curl]]

## Tags

- [[info-disclosure]]
- [[credentials-leak]]
- [[php-backup]]
