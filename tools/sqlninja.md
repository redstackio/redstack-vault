---
id: 15f71396-b4b3-4356-84e1-9487ade87ec2
name: sqlninja
type: tool
verified: true
created_at: '2019-08-28T21:17:19.221119+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - mssql
  - exploitation
  - remote-access
url: 'http://sqlninja.sourceforge.net/'
commands:
  - '[[commands/sqlninja-test-connection]]'
  - '[[commands/sqlninja-guess-dbms]]'
  - '[[commands/sqlninja-retrieve-password-hash]]'
  - '[[commands/sqlninja-upload-shell]]'
  - '[[commands/sqlninja-launch-shell]]'
validated: true
---

# sqlninja

**Status**: Unverified

## Overview

sqlninja is a Perl-based tool designed to exploit SQL injection vulnerabilities in web applications backed by Microsoft SQL Server. It automates the process of escalating from a SQLi vulnerability to remote shell access on the database server, even in restricted environments. Common use cases include penetration testing, red teaming, and vulnerability assessment for MSSQL-backed web apps.

## Description

sqlninja takes advantage of SQL injection flaws to perform actions like DBMS fingerprinting, data retrieval, file uploads, and shell execution. It supports multiple exploitation modes and can bypass certain security measures, such as uploading UPX-packed shells and modifying registry keys to disable Data Execution Prevention (DEP). The tool requires a configuration file specifying the target URL, injection point, and other parameters. It's particularly useful for automating tedious manual SQLi exploitation steps.

## Features

- **Test Mode**: Validates SQLi vulnerability without deeper exploitation.
- **Guess Mode**: Fingerprints the DBMS version.
- **Retrieve Mode**: Dumps database content via custom SQL queries.
- **Upload Mode**: Transfers executable shells to the target server.
- **Shell Mode**: Launches an interactive remote shell.
- **DNS Mode**: Exfiltrates data via DNS tunneling for blind SQLi.
- **Direct Mode**: Establishes direct connections post-exploitation.
- Automatic generation of Metasploit-compatible payloads.

## Installation

### Requirements

- Perl 5.8 or higher
- Modules: DBI, DBD::ODBC (or similar for MSSQL connectivity)
- wget or curl for downloads
- UPX packer for shell compression (optional but recommended)

### Install Commands

```bash
# Clone from SourceForge or download tarball
git clone https://github.com/NGnius/sqlninja.git  # Or download from official site
cd sqlninja

# Install Perl dependencies
cpan DBI
cpan DBD::ODBC  # For ODBC support, or use FreeTDS for alternative

# Make executable
chmod +x sqlninja.pl

# On Kali/Debian (may need manual install if not in repos)
apt update
apt install libdbd-odbc-perl libdbi-perl
```

For macOS:
```bash
brew install perl
cpan DBI DBD::ODBC
```

## Basic Usage

```bash
./sqlninja.pl -h
```

Create a configuration file (sqlninja.conf) with details like:
```
target: http://target.com/page.asp?id=1
submission_method: GET
injection_point: 3
```

Then run modes sequentially.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output |
| -w FILE | Specify configuration file |
| -m MODE | Set exploitation mode (test, guess, etc.) |

## Examples

### Example 1: Basic Usage

Test vulnerability:
```bash
./sqlninja.pl -m test -w sqlninja.conf
```

### Example 2: Advanced Usage

Retrieve data and upload shell:
```bash
./sqlninja.pl -m retrieve -w sqlninja.conf -Q "SELECT @@version"
./sqlninja.pl -m upload -w sqlninja.conf --shell upxshell.exe
./sqlninja.pl -m shell -w sqlninja.conf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component: SQL Server
- [[Unsecured Credentials]] Unsecured Credentials
- [[Hijack Execution Flow]] Hijack Execution Flow: Disable or Modify Tools

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests with SQL injection patterns (e.g., ' or 1=1--).
- DNS tunneling traffic if using DNS exfiltration mode.
- Suspicious file uploads to database server directories (e.g., cmdasp.exe in temp folders).
- Registry modifications for DEP disablement on Windows servers.
- Perl process spawning on attacker machines connecting to web apps.
- Monitor web server logs for repeated failed SQL queries or time-based delays.

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
- [[tools/metasploit]]

## References

- Official website: http://sqlninja.sourceforge.net/
- GitHub mirror: https://github.com/NGnius/sqlninja
- Documentation: Included in the tool's README and man page
- Blog post: "sqlninja: a tool for SQL Server pentesting"
