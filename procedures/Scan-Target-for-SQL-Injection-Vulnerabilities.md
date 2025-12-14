---
id: proc-uuid-001
name: Scan-Target-for-SQL-Injection-Vulnerabilities
tags:
  - sqli
  - scanning
  - vulnerability-detection
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-scan-user-agent]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.978Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Scan-Target-for-SQL-Injection-Vulnerabilities

## Summary

This procedure uses sqlmap to scan a target web application for SQL injection vulnerabilities, particularly in HTTP headers like User-Agent, enabling the identification of injection points for further exploitation.

## Description

In a typical web penetration testing scenario, attackers scan public-facing applications to find unsanitized inputs that allow SQL injection. This procedure targets the root URL of a website, testing parameters and headers with high-level and high-risk settings to detect blind boolean-based injections. Prerequisites include network access to the target and installation of sqlmap. Expected outcomes include detection of vulnerable points and basic database fingerprinting, setting the stage for data exfiltration or manipulation.

## Requirements

1. Network access to the target HTTPS URL (e.g., https://target.com)
2. Installed sqlmap tool (Python-based, no special credentials needed)
3. Basic understanding of HTTP requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to block anomalous SQL payloads in headers
- Use prepared statements and input parameterization in backend code to prevent injection
- Monitor logs for repeated failed requests with random User-Agents or SQL keywords

## Objectives

1. Detect SQL injection vulnerabilities in web inputs, including headers
2. Fingerprint the database management system (DBMS)
3. Identify exploitation techniques like boolean-based blind injection

## Instructions

### Step 1: Launch sqlmap Scan

**Context**: Initiate an automated scan of the target URL, focusing on comprehensive testing of headers and parameters to uncover hidden injection points.

**Command** ([[commands/sqlmap-scan-user-agent]]):
```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3
```

> This command runs sqlmap in non-interactive batch mode, using a random User-Agent to mimic legitimate traffic and evade basic detection. Level 5 tests all possible injection points including HTTP headers, while risk 3 includes advanced payloads like boolean-based and time-based blind techniques. Expected output includes vulnerability identification, such as 'Parameter: User-Agent (User-Agent) Type: boolean-based blind'.

### Step 2: Review Scan Results

**Context**: Analyze the output to confirm any detected vulnerabilities and gather initial DBMS details.

**Command** (No specific command; parse sqlmap output):

> Inspect the console output for injection confirmations and DBMS info. If vulnerable, proceed to exploitation; otherwise, adjust URL or parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-scan-user-agent]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- scanning
