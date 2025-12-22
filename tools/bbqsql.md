---
id: cbc7312a-e829-4716-acdb-d99131149213
name: bbqsql
type: tool
verified: true
created_at: '2019-08-28T21:17:37.778539+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sqli
  - blind-sqli
  - exploitation
  - web-vulnerability
  - framework
url: 'https://github.com/t0w3nt/bbqsql'
validated: true
---

# bbqsql

**Status**: Unverified

## Overview

BBQSQL is a Python-based framework designed for exploiting blind SQL injection vulnerabilities in web applications. It is particularly useful for time-based or boolean-based blind SQLi where traditional tools may fail due to custom application logic or tricky injection points. The tool supports database-agnostic attacks, allowing customization of payloads, threading for speed (via gevent), and an intuitive interactive UI for setup.

## Description

Blind SQL injection exploitation often requires custom tooling when standard tools like sqlmap encounter issues with non-standard responses or complex request flows. BBQSQL addresses this by providing a semi-automatic framework that lets users define HTTP requests, injection points, and response parsing logic. It uses asynchronous requests for efficiency and supports features like custom encodings, proxy integration, and payload optimization. Commonly used in penetration testing to extract data from databases without direct error messages or union-based outputs.

## Features

- Feature 1: Interactive configuration wizard for HTTP requests (URL, method, headers, cookies, POST data).
- Feature 2: Database-agnostic support with customizable SQL syntax for MySQL, PostgreSQL, MSSQL, etc.
- Feature 3: Asynchronous execution using gevent for fast boolean/time-based injections.
- Feature 4: Custom response filters to handle application-specific behaviors.
- Feature 5: Support for proxies, HTTP auth, and file uploads in requests.
- Feature 6: Payload generation and optimization for extracting data like database names, tables, and records.

## Installation

### Requirements

- Python 2.7 or 3.x (gevent library required for async).
- Git for cloning the repository.
- pip for dependencies.

### Install Commands

```bash
# Clone the repository
 git clone https://github.com/t0w3nt/bbqsql.git
 cd bbqsql

# Install dependencies (Python 2/3 compatible)
 pip install gevent requests

# Run directly without installation
 python bbqsql.py
```

On Kali Linux, it may be available via apt, but building from source is recommended for the latest version.

## Basic Usage

```python
python bbqsql.py
```

This launches the interactive mode where you configure the attack step-by-step.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available options |
| --url | Specify target URL directly |
| --method | HTTP method (GET/POST) |
| --data | POST data string |
| --headers | Custom headers as key=value pairs |
| --proxy | Proxy server for requests |
| --threads | Number of concurrent threads (default uses gevent) |

## Examples

### Example 1: Basic Usage

Launch interactive mode for a GET-based injection:

```python
python bbqsql.py
```

Enter prompts: URL = http://target.com/page?id=1, Method = GET, Injection Point = id parameter.

### Example 2: Advanced Usage

Configure a POST request with custom headers:

```python
python bbqsql.py --url "http://target.com/login" --method POST --data "user=$_INJ&pass=abc" --headers "Cookie: session=xyz" --proxy "http://127.0.0.1:8080"
```

Then define the injection point in $_INJ and start dumping data.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component (for SQL database manipulation)

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection (data exfiltration via SQL queries)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP request patterns with repeated boolean/time-delay payloads (e.g., SLEEP(5) in MySQL).
- Detection method 2: High volume of similar requests from a single IP to vulnerable endpoints, monitor via WAF logs.
- Detection method 3: Python process spawning gevent-related threads on attacker machines; network anomalies like proxy traffic to Burp/ZAP.
- Detection method 4: Database logs showing anomalous queries without direct errors (e.g., conditional SELECTs).

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
- [[ZAP]]

## References

- Official GitHub: https://github.com/t0w3nt/bbqsql
- Documentation: Included in repo README
- Related resources: OWASP SQL Injection Cheat Sheet
