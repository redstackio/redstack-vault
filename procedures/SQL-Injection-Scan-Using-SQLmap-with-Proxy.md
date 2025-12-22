---
id: 9e0b3793-7090-4f56-acc2-1a06e4606044
name: SQL-Injection-Scan-Using-SQLmap-with-Proxy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.429601+00:00'
updated_at: '2023-04-10T20:24:18.028839+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - SQL Injection
  - SQLmap
  - Proxy
commands:
  - '[[commands/sqlmap-sql-injection-scan-with-proxy]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# SQL-Injection-Scan-Using-SQLmap-with-Proxy

## Summary

This procedure uses SQLmap, an automated tool for detecting and exploiting SQL injection vulnerabilities in web applications, while routing traffic through a proxy to anonymize the attacker's origin and potentially bypass network restrictions. It identifies injectable parameters in a target URL and can enumerate database details, making it suitable for initial vulnerability assessment in penetration testing.

## Description

SQL injection vulnerabilities occur when user input is improperly sanitized and concatenated into SQL queries, allowing attackers to manipulate database operations. SQLmap automates the detection of these flaws by testing parameters with payloads and analyzing responses for errors or delays indicative of injection. Routing through a proxy (e.g., Burp Suite or a SOCKS proxy) hides the attacker's IP, evades IP-based blocking, and allows interception for further manipulation. This approach targets public-facing web applications using databases like MySQL, PostgreSQL, or SQL Server. Success enables data extraction, command execution, or privilege escalation, but requires a vulnerable endpoint. Use in controlled environments only, as it may trigger alerts in production systems.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS endpoint).
2. SQLmap installed on the attacker's system (see [[tools/sqlmap]] for installation).
3. A running proxy server (e.g., Burp Suite on localhost:8080 or a remote SOCKS proxy) to route traffic.
4. Basic knowledge of the target URL structure, including any query parameters to test.

## Defense

- Implement prepared statements and parameterized queries in application code to sanitize inputs.
- Deploy a web application firewall (WAF) like ModSecurity to detect and block SQL injection patterns.
- Monitor application logs and database queries for anomalies, such as unexpected error messages or union-based payloads.
- Use network intrusion detection systems (IDS) to flag repeated probing from proxies or unusual traffic patterns.

## Objectives

1. Detect SQL injection vulnerabilities in the target web application's input parameters.
2. Exploit identified vulnerabilities to retrieve database information or execute commands.
3. Maintain anonymity and evade detection by proxying all SQLmap traffic.

## Instructions

### Step 1: Set Up the Proxy Server

**Context**: Before running SQLmap, configure a proxy to intercept and anonymize traffic. This step ensures all requests are routed correctly and allows for manual inspection if needed. Common proxies include Burp Suite for HTTP or a SOCKS proxy for broader support.

Use a tool like [[tools/Burp-Suite]] or start a simple SOCKS proxy with ssh: `ssh -D 127.0.0.1:8080 user@proxy-server`. Verify the proxy is listening by checking open ports with `netstat -tuln | grep 8080`.

**Expected Output**: Proxy server confirms it's active, e.g., Burp's listener shows "Proxy listener active on 127.0.0.1:8080".

### Step 2: Identify the Target URL and Parameters

**Context**: Determine the exact URL to test, focusing on pages with user inputs like search fields, login forms, or GET parameters. Manually inspect the application to note potential injection points (e.g., ?id=1).

Browse the target site using a browser or [[commands/curl-get-request]] to fetch the page and identify parameters: `curl -x http://127.0.0.1:8080 "http://www.target.com/page?id=1"`. Review the response for dynamic content.

**Expected Output**: HTML response showing form fields or query parameters that could be injectable.

### Step 3: Run SQLmap Scan with Proxy

**Context**: Execute the SQLmap scan to detect vulnerabilities. The tool will test the URL's parameters for injection types (e.g., boolean-based, time-based) and report findings. The --proxy flag routes all traffic through the specified proxy.

**Command** ([[commands/sqlmap-sql-injection-scan-with-proxy]]):
```bash
sqlmap -u "http://www.target.com/page?id=1" --proxy="http://127.0.0.1:8080" --batch --level=3 --risk=2
```

> This command specifies the target URL (-u), routes through the proxy (--proxy), runs in batch mode (--batch) to avoid prompts, sets detection thoroughness (--level=3), and risk level (--risk=2) for more aggressive testing. SQLmap will probe parameters, inject payloads, and output vulnerability details if found. Monitor the proxy for intercepted requests.

**Expected Output**: Console output indicating vulnerability detection, e.g., "[INFO] the back-end DBMS is MySQL" followed by "Parameter: id (GET) Type: boolean-based blind Title: AND boolean-based blind - WHERE or HAVING clause Payload: id=1' AND 1234=1234--".

### Step 4: Enumerate and Verify Results

**Context**: If vulnerabilities are detected, enumerate database details to confirm exploitability. This step retrieves schema, tables, or data without immediate exploitation.

Follow up with additional SQLmap flags based on detection: `sqlmap -u "http://www.target.com/page?id=1" --proxy="http://127.0.0.1:8080" --dbs --tables --batch`. Save output to a file for analysis: `--output-dir=/path/to/results`.

**Expected Output**: List of databases (e.g., "Available databases [2]: [*] information_schema [*] webapp_db"), tables, or dumped data confirming access.

### Step 5: Clean Up and Analyze

**Context**: Review logs from the proxy and SQLmap output for evidence of success or evasion. This ensures no traces are left and prepares for further actions like exploitation.

Check proxy logs for blocked requests and SQLmap's log file (default: ~/.sqlmap/output/). If no vulnerabilities, increase --level or test other parameters.

**Expected Output**: Comprehensive log files detailing tested payloads, responses, and any extracted data.
