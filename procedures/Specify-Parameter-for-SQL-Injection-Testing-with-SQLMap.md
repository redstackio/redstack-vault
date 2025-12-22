---
id: b997e6c8-d982-439a-b2df-3b2b1581e548
name: Specify-Parameter-for-SQL-Injection-Testing-with-SQLMap
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T17:40:37.509883+00:00'
updated_at: '2023-05-26T18:11:17.788508+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - sqli
  - sqlmap
  - web-applications
commands:
  - '[[commands/sqlmap-specify-parameter]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Specify-Parameter-for-SQL-Injection-Testing-with-SQLMap

## Summary

This procedure demonstrates how to use SQLMap to test a specific parameter in a URL for SQL injection vulnerabilities. By specifying the parameter with the -p option, SQLMap focuses its payloads on that input, enabling efficient detection and exploitation of SQLi flaws in web applications.

## Description

SQL injection (SQLi) vulnerabilities allow attackers to inject malicious SQL code into queries via unsanitized user inputs, potentially leading to data leakage, authentication bypass, or full database compromise. SQLMap automates the detection and exploitation of these vulnerabilities. This procedure focuses on targeting a specific GET parameter (e.g., 'user' in a login form) to streamline testing, reducing noise and false positives. It is applicable in scenarios where reconnaissance has identified potentially injectable parameters, such as through manual fuzzing or Burp Suite scans. The technique aligns with exploiting public-facing web applications and requires HTTP access to the target.

## Requirements

1. SQLMap installed and accessible in the PATH (see [[tools/sqlmap]] for installation).
2. Network access to the target web application (e.g., via direct IP or domain).
3. Basic understanding of the target's URL structure and parameters (identified via tools like Burp Suite or browser inspection).
4. A wordlist or default payloads (SQLMap uses built-in ones, but custom dictionaries can enhance results).

## Defense

Defensive measures include input validation/sanitization using prepared statements (e.g., PDO in PHP), web application firewalls (WAFs) like ModSecurity to block SQL payloads, and database activity monitoring for anomalous queries. Detection strategies involve logging HTTP requests for suspicious patterns (e.g., single quotes, UNION SELECT) and using tools like Snort or OSSEC for intrusion detection.

## Objectives

1. Identify if a specific URL parameter is vulnerable to SQL injection.
2. Confirm the backend DBMS and injectable techniques (e.g., boolean-based blind, error-based).
3. Gather payloads and injection points for further exploitation.
4. Log results for reporting or chaining into data exfiltration procedures.

## Instructions

### Step 1: Prepare the Target URL and Parameter

**Context**: Identify the full URL with query parameters and select the one to test (e.g., 'user' in a login endpoint). This ensures SQLMap targets only the relevant input, optimizing the scan.

Use reconnaissance tools to confirm the URL. Then, execute the SQLMap command to test the specified parameter.

**Command** ([[commands/sqlmap-specify-parameter]]):
```bash
sqlmap -u "$_TARGET_URL" -p $_PARAMETER
```

> This command initiates the SQLi test on the specified parameter. SQLMap will probe for various injection types, confirm the DBMS, and report vulnerabilities. Replace $_TARGET_URL with the full endpoint (e.g., http://example.com/login.php?user=test&pass=test) and $_PARAMETER with the injectable field (e.g., user). Expected output includes heuristic tests, payload trials, and confirmation of injectable types like boolean-based blind or error-based.

### Step 2: Review and Verify Results

**Context**: Analyze SQLMap's output to confirm vulnerability and DBMS. If injectable, note the payloads for manual verification or further enumeration.

Examine the console output for sections like "[INFO] GET parameter '$_PARAMETER' appears to be 'AND boolean-based blind' injectable". If prompted, follow redirects (Y) and include extended tests for the DBMS (Y). Success is indicated by identified injection points and payloads.

**Command** ([[commands/sqlmap-specify-parameter]]):
```bash
sqlmap -u "$_TARGET_URL" -p $_PARAMETER --batch
```

> The --batch flag automates responses for non-interactive runs. Expected output lists injection types, payloads, and backend details (e.g., MySQL >= 5.0). Logs are saved to ~/.sqlmap/output/ for review.

### Step 3: Optional Enumeration if Vulnerable

**Context**: If SQLi is confirmed, extend the scan to enumerate database details without specifying -p to test all parameters, or chain to database dumping.

For basic enumeration:

**Command** ([[commands/sqlmap-specify-parameter]]):
```bash
sqlmap -u "$_TARGET_URL" -p $_PARAMETER --dbs
```

> This lists available databases. Expected output: Database names like 'information_schema', 'mysql'. Use this to pivot to procedures like database table enumeration.
