---
id: tool-htaccess-001
name: Apache-htaccess
type: tool
verified: false
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.290Z'
platforms:
  - Linux
  - Windows
tags:
  - web-config
  - apache
url: null
validated: true
submitted: true
---

# Apache-htaccess

**Status**: Unverified

## Overview

.htaccess is a configuration file for Apache HTTP Server that controls directory-level settings, commonly used for URL rewriting to map requests to specific scripts without changing the URL.

## Description

In this attack, .htaccess uses mod_rewrite to route /user/check_email requests to check_email.php, enabling the attacker server to handle Smule-mimicking endpoints seamlessly.

## Features

- Feature 1: URL rewriting via RewriteRule
- Feature 2: Conditional rules with RewriteCond
- Feature 3: Per-directory configuration without server restart

## Installation

### Requirements

- Apache with mod_rewrite enabled

### Install Commands

```bash
# Enable mod_rewrite
sudo a2enmod rewrite
sudo systemctl restart apache2
# Create .htaccess in web root
```

## Basic Usage

Create .htaccess file in directory.

### Common Options

| Option | Description |
|--------|-------------|
| RewriteEngine On | Enable rewriting |
| RewriteRule | Define rewrite pattern |

## Examples

### Example 1: Basic Usage

```apache
RewriteEngine On
RewriteRule ^user/check_email$ check_email.php [NC,L]
```

### Example 2: Advanced Usage

As used: RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1.php [NC,L]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous .htaccess files in web roots
- Rewrite logs showing unusual mappings

## Related Procedures


## Related Tools

- [[Related Tool: Nginx Config]]
- [[Related Tool: IIS web.config]]

## References

- Official documentation: https://httpd.apache.org/docs/2.4/howto/htaccess.html
- Related resources: Apache Mod_Rewrite Guide
