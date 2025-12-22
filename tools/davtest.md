---
id: aaf6bf9b-0f80-46f4-b1a1-7ae01a77e0f3
name: davtest
type: tool
verified: true
created_at: '2019-08-28T21:17:26.294459+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - webdav
  - exploitation
  - upload
  - penetration-testing
url: 'https://github.com/harmj0y/davtest'
validated: true
---

# davtest

**Status**: Unverified

## Overview

DAVTest is a Perl-based tool designed for penetration testers to assess the exploitability of WebDAV-enabled servers. It automates the upload of test executable files (such as ASP, JSP, PHP, and EXE) to determine if the server allows file uploads that could lead to remote code execution or other malicious actions.

## Description

DAVTest targets Web Distributed Authoring and Versioning (WebDAV) services, which extend HTTP to support file management operations like uploading and moving files. The tool is particularly useful in web application penetration testing to identify misconfigurations in services like Microsoft IIS, Apache with mod_dav, or other WebDAV implementations. It supports uploading randomized files to evade detection, handling authentication, and cleaning up test artifacts. Common use cases include initial reconnaissance of web servers and exploiting upload vulnerabilities during red team engagements.

## Features

- Automatic upload of test executables in multiple formats (ASP, ASPX, JSP, PHP, EXE, etc.)
- Support for basic and digest authentication
- Randomization of upload directories and filenames to avoid detection
- Option to upload custom files for targeted payloads
- Automatic cleanup of uploaded files to minimize footprint
- SSL/TLS support for HTTPS WebDAV endpoints
- MOVE method testing to rename uploaded files to executable extensions

## Installation

### Requirements

- Perl 5 (with LWP::UserAgent and other standard modules)
- Access to a Perl environment
- No additional dependencies beyond core Perl libraries

### Install Commands

```bash
# Clone from GitHub (recommended)
git clone https://github.com/harmj0y/davtest.git
cd davtest
chmod +x davtest.pl

# Or download the script directly
wget https://raw.githubusercontent.com/harmj0y/davtest/master/davtest.pl
chmod +x davtest.pl
```

On Windows, use Strawberry Perl or ActivePerl and run via command prompt.

## Basic Usage

```bash
perl davtest.pl -url http://target.com/webdav/
```

### Common Options

| Option | Description |
|--------|-------------|
| -url | Target WebDAV URL (required) |
| -auth | Authentication credentials in format user:pass |
| -file | Path to a custom file to upload |
| -randdir | Use randomized directory for uploads |
| -cleanup | Automatically remove uploaded files after testing |
| -ssl | Enable SSL for HTTPS connections |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
perl davtest.pl -url http://192.168.1.100/webdav/
```

This performs a standard test upload without authentication.

### Example 2: Advanced Usage

```bash
perl davtest.pl -url https://target.com/dav/ -auth admin:password -ssl -randdir -cleanup
```

Tests an authenticated HTTPS endpoint with randomization and cleanup.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Upload Malware]] Dynamic Resolution (for WebDAV URLs)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual file uploads to WebDAV directories (monitor logs for PROPFIND, PUT, MOVE methods)
- Presence of test files with randomized names in web roots
- Network traffic to WebDAV endpoints from pentest IPs
- Perl process spawning with LWP::UserAgent module
- Authentication attempts on WebDAV services

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/cURL]]
- [[tools/Burp-Suite]]
- [[tools/metasploit]]

## References

- Official GitHub Repository: https://github.com/harmj0y/davtest
- WebDAV Protocol: https://www.ietf.org/rfc/rfc4918.txt
- Related Blog Post: https://pentestlab.blog/2012/06/05/webdav-exploitation/

*Last updated: 2023-10-01*
