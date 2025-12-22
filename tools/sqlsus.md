---
type: tool
verified: true
url: 'https://github.com/antichown/sqlsus'
tags:
  - sql-injection
  - mysql
  - exploitation
  - perl
  - database
platforms:
  - Linux
  - Web
validated: true
---

# sqlsus

**Status**: Unverified

## Overview

sqlsus is an open-source MySQL injection and takeover tool written in Perl. It provides a command-line interface for exploiting SQL injection vulnerabilities in MySQL-backed web applications, allowing database enumeration, custom query execution, file operations, and server takeover via backdoor upload.

## Description

sqlsus excels in speed and efficiency for both in-band and blind SQL injections. It optimizes injection space using stacked subqueries and advanced blind algorithms to maximize data retrieval per request. Multi-threading accelerates dumping, and it mimics a MySQL console for familiar interaction. High-privilege exploits enable file downloads from the web server, crawling for writable directories, backdoor uploads, and database cloning. Supports cookies, SOCKS/HTTP proxies, and HTTPS for realistic evasion scenarios.

## Features

- Database structure retrieval (tables, columns, data types)
- Custom SQL query injection, including complex stacked queries
- File download from web server via injection
- Website crawling to identify writable directories
- Backdoor upload and remote control for server takeover
- Database cloning to local SQLite backend
- MySQL console emulation for intuitive use
- Blind injection optimization with multi-threading
- Proxy (SOCKS/HTTP) and cookie support
- HTTPS connectivity

## Installation

### Requirements

- Perl 5.8 or later
- LWP::UserAgent (for HTTP requests)
- IO::Socket::SSL (for HTTPS)
- Other standard Perl modules (usually pre-installed)

### Install Commands

```bash
# Download the tool (from archived sources or GitHub mirror)
wget https://github.com/antichown/sqlsus/raw/master/sqlsus.pl
chmod +x sqlsus.pl

# Or clone if available
# git clone https://github.com/antichown/sqlsus.git
# cd sqlsus
# chmod +x sqlsus.pl

# Verify installation
perl sqlsus.pl --help
```

On Kali Linux, it may be available via apt or manual install as above.

## Basic Usage

```perl
perl sqlsus.pl --help
```

This displays all available options and usage syntax.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify vulnerable URL (required) |
| -p, --proxy | Set proxy (socks:// or http://) |
| -c, --cookie | Provide cookie string for session |
| -S | Enable HTTPS/SSL |
| -t | Set threads for multi-threading (default: optimized) |
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

```perl
perl sqlsus.pl -u "http://target.com/vuln.php?id=1"
```

Enters interactive mode to enumerate and dump the database.

### Example 2: Advanced Usage

```perl
perl sqlsus.pl -u "https://target.com/admin.php?id=1" -S -c "PHPSESSID=abc123" -p "socks://127.0.0.1:1080"
```

Starts session over HTTPS with cookie and proxy.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component: Web Shell
- [[Network Service Scanning]] Network Service Scanning (for vuln discovery)

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Web server logs showing repeated anomalous SQL queries or stacked subqueries
- Unusual file uploads or downloads via SQL injection points
- Network traffic patterns: high-volume requests to a single endpoint with proxy headers
- Perl process spawning with HTTP libraries on compromised hosts
- Database logs revealing blind injection attempts (time-based or boolean)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]]
- [[tools/Burp-Suite]]

## References

- Original tool source (archived)
- Perl documentation for LWP::UserAgent
- MITRE ATT&CK for SQL Injection techniques
