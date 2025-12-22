---
type: tool
description: >-
  Setup and configuration guide for Apache mod_rewrite module, used for URL
  rewriting in web server environments during security assessments.
url: 'https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html'
tags:
  - web-server
  - apache
  - url-rewriting
  - configuration
platforms:
  - Linux
verified: true
validated: true
---

# Apache-Mod-Rewrite-Setup

**Status**: Unverified

## Overview

Apache mod_rewrite is a rule-based rewriting engine for the Apache HTTP Server. It is commonly used in offensive security to manipulate URLs, create redirects for phishing simulations, bypass web application filters, or set up custom routing in test environments. This tool document focuses on setup and basic configuration for red team infrastructure.

## Description

Mod_rewrite allows conditional rewriting of URLs based on regular expressions, server variables, and other conditions. In security testing, it's valuable for simulating server-side redirects, hiding payloads in URLs, or chaining with other web exploits. It requires Apache2 installation and proper enabling of the module. Supported on Linux distributions like Ubuntu and Debian.

## Features

- Feature 1: Rule-based URL rewriting using regex patterns
- Feature 2: Conditional directives (RewriteCond) for environment checks
- Feature 3: Integration with .htaccess files for per-directory rules
- Feature 4: Logging of rewrite actions for debugging

## Installation

### Requirements

- Root or sudo access on a Debian-based system (e.g., Ubuntu)
- Internet access for package installation

### Install Commands

First, install Apache2 which includes mod_rewrite:

```bash
[[commands/apt-install-apache2]]
```

Enable the module:

```bash
[[commands/a2enmod-rewrite]]
```

Restart Apache to apply changes:

```bash
[[commands/apache2-restart]]
```

## Basic Usage

```bash
apache2ctl -M | grep rewrite
```

### Common Options

| Option | Description |
|--------|-------------|
| `-M` | Lists loaded modules to verify rewrite is active |
| `-t` | Tests configuration syntax before restarting |

## Examples

### Example 1: Basic Usage

Verify mod_rewrite is loaded:

```bash
apache2ctl -M | grep rewrite
```

### Example 2: Advanced Usage

Create a simple .htaccess file in your web root (/var/www/html) for URL rewriting:

```apache
RewriteEngine On
RewriteRule ^old-page$ /new-page [R=301,L]
```

Then restart:

```bash
[[commands/apache2-restart]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (for web manipulation)
- [[Phishing]] Phishing (for redirect setups)

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Check Apache access/error logs for RewriteRule patterns
- Detection method 2: Scan loaded modules with `apache2ctl -M` for unexpected rewrite rules
- Detection method 3: Monitor .htaccess files for unauthorized modifications

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Apache2]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html
- Apache configuration guide: https://httpd.apache.org/docs/2.4/howto/pretty.html
