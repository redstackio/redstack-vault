---
id: ef3dfdaa-cae1-4b04-a1bb-6509ae0c5861
name: jsql-injection
type: tool
verified: true
created_at: '2019-08-28T21:17:34.830698+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
  - Solaris
tags:
  - sql-injection
  - exploitation
  - database
url: 'https://github.com/ron190/jsql-injection'
validated: true
---

# jsql-injection

**Status**: Unverified

## Overview

jSQL Injection is a lightweight, open-source tool designed for exploiting SQL injection vulnerabilities to extract database information from remote servers. It supports automated detection of injection points, database enumeration, and data dumping, making it useful for penetration testing and vulnerability assessment in web applications.

## Description

jSQL Injection automates the process of identifying and exploiting SQL injection flaws in web applications. It supports various DBMS types (MySQL, PostgreSQL, Oracle, etc.) and injection techniques (boolean-based blind, time-based blind, error-based). The tool is cross-platform and runs on Java, providing a GUI for interactive use or limited CLI options for scripting. Common use cases include reconnaissance of database structures, credential harvesting, and data exfiltration during red team engagements.

## Features

- Feature 1: Automatic detection of SQL injection vulnerabilities in URL parameters, cookies, and headers.
- Feature 2: Support for multiple injection payloads and DBMS-specific optimizations.
- Feature 3: Database enumeration including tables, columns, and data dumping to files.
- Feature 4: Proxy integration for traffic interception and customization.
- Feature 5: Cross-platform compatibility via Java runtime.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- Network access to the target application.

### Install Commands

```bash
# Download the JAR file from GitHub
wget https://github.com/ron190/jsql-injection/releases/download/v0.2.1/jsql-injection-0.2.1.jar -O jsql-injection.jar

# On Kali/Ubuntu (Java is often pre-installed; install if needed)
apt update && apt install default-jre

# Verify installation
java -version
```

For Windows/macOS, download the JAR directly and ensure Java is installed via official Oracle site or package managers like Homebrew (brew install java).

## Basic Usage

```bash
java -jar jsql-injection.jar
```

This launches the GUI. Enter the target URL, select the injection parameter, choose the DBMS, and start the scan.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify target URL |
| -p, --param | Injection parameter name |
| -t, --type | Injection type (boolean, time, error) |
| --dbms | Target DBMS (mysql, postgresql, etc.) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Launch GUI for manual testing:

```bash
java -jar jsql-injection.jar
```

In the GUI, input URL like http://example.com/page?id=1, select 'id' as parameter, and run vulnerability check.

### Example 2: Advanced Usage

Test injection via CLI (limited support):

```bash
java -jar jsql-injection.jar -u "http://example.com/page?id=1" -p id -t boolean --dbms mysql
```

This detects if the 'id' parameter is vulnerable to boolean-based blind SQLi.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component: Web Shell (for injection payloads)

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP requests with SQL payloads (e.g., ' OR 1=1 --) in web server logs.
- Detection method 2: Java process spawning with jsql-injection.jar on compromised hosts.
- Detection method 3: Network traffic anomalies to database ports or repeated failed queries.

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
- [[Burp-Suite]]

## References

- Official GitHub: https://github.com/ron190/jsql-injection
- Documentation: Included in JAR or GitHub README

*Last updated: 2023-10-01*
