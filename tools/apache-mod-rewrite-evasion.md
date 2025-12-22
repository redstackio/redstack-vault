---
type: tool
description: >-
  Apache mod_rewrite module for URL rewriting, used in web security testing to
  evade sandboxes and WAFs by manipulating request paths and headers.
url: 'https://httpd.apache.org/docs/current/mod/mod_rewrite.html'
tags:
  - evasion
  - web
  - apache
  - sandbox-bypass
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# Apache Mod Rewrite Evasion

**Status**: Unverified

## Overview

Apache mod_rewrite is a powerful URL manipulation module for the Apache HTTP server. In offensive security, it's commonly used to craft rewrite rules in .htaccess files or server configurations to evade vendor sandboxes, web application firewalls (WAFs), and detection mechanisms by obfuscating malicious requests, redirecting traffic, or normalizing suspicious paths.

## Description

Mod_rewrite allows conditional rewriting of URLs based on regular expressions, enabling attackers to bypass filters in analysis environments (e.g., by encoding payloads in rewritten paths or forcing redirects to internal resources). It's particularly useful in red team engagements targeting Apache-hosted applications, where custom rules can hide command injection or SSRF attempts from sandbox heuristics.

## Features

- Feature 1: Rule-based URL rewriting using regex patterns for path, query string, and header manipulation.
- Feature 2: Conditional directives (RewriteCond) for environment-specific evasion, like user-agent or IP checks.
- Feature 3: Support for redirects (301/302) and internal proxies to chain attacks without direct exposure.

## Installation

### Requirements

- Apache HTTP Server 2.2 or later
- Root or sudo access on the target server

### Install Commands

On Ubuntu/Debian:
```bash
a2enmod rewrite
systemctl restart apache2
```

On CentOS/RHEL:
```bash
yum install httpd
LoadModule rewrite_module modules/mod_rewrite.so  # Add to httpd.conf
systemctl restart httpd
```

For development/testing (Kali Linux, pre-installed):
```bash
# Already available; enable in virtual host config
```

## Basic Usage

```bash
# View available rewrite options
apachectl -M | grep rewrite
```

### Common Options

| Option | Description |
|--------|-------------|
| RewriteEngine On | Enables the rewrite engine |
| RewriteRule | Defines the rewrite pattern and substitution |
| RewriteCond | Adds conditions before applying a rule |
| [L] flag | Last rule flag; stops processing further rules |

## Examples

### Example 1: Basic Evasion Rule (Path Obfuscation)

Add to .htaccess:
```apache
RewriteEngine On
RewriteRule ^evil/(.*)$ /benign/$1 [L]
```

Test with curl:
```bash
curl -v http://target.com/evil/cmd.exe
```

This rewrites /evil/cmd.exe to /benign/cmd.exe, evading path-based sandbox filters.

### Example 2: Advanced Evasion (User-Agent Condition)

```apache
RewriteEngine On
RewriteCond %{HTTP_USER_AGENT} ^Mozilla [NC]
RewriteRule ^test/(.*)$ /internal/$1 [L]
```

Use in scenarios where sandboxes use specific agents; normal browsers trigger the rewrite to internal paths.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for hiding payloads in rewritten URLs)
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (manipulating web requests)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Apache access/error logs for unusual RewriteRule applications or 301/302 redirects.
- Detection method 2: Scan .htaccess files and httpd.conf for suspicious RewriteCond patterns (e.g., regex matching evasion strings).
- Detection method 3: WAF logs showing normalized vs. original request paths.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Apache-HTTP-Server]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://httpd.apache.org/docs/current/mod/mod_rewrite.html
- Related resources: OWASP URL Rewrite Evasion Guide
