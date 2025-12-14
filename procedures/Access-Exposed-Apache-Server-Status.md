---
tags:
  - information-disclosure
  - apache
  - reconnaissance
  - server-status
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-server-status]]'
platforms:
  - Web
  - Apache
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Software]]'
id: 595e708e-a165-403e-9bfa-acff4bbb0cf5
created_at: '2025-12-14T17:25:12.851Z'
updated_at: '2025-12-14T17:25:12.851Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Exposed-Apache-Server-Status

## Summary

This procedure exploits a misconfigured Apache mod_status module to access the /server-status/ endpoint, disclosing real-time server metrics, active connections, and log data. It is commonly used in reconnaissance phases to gather intelligence on web server health, traffic, and potential vulnerabilities without requiring authentication.

## Description

Apache's mod_status provides a diagnostic page for server administrators, showing details like uptime, request rates, worker threads, and the last 63 requests (including client IPs, HTTP methods, and URIs). When enabled without restrictions (e.g., no IP allow/deny in httpd.conf), this page becomes publicly accessible, leaking sensitive information. In the reported incident on a U.S. DoD system, direct URL access revealed performance metrics and logs, aiding attackers in planning targeted exploits like DDoS or further enumeration. Prerequisites include a publicly facing Apache server; no exploits or payloads are needed—just a simple HTTP GET request.

## Requirements

1. Network access to the target web server (e.g., via internet or internal network)
2. Knowledge of the base URL (e.g., https://target.com)
3. Optional: curl or a web browser for verification

## Defense

Defensive measures and detection strategies:

- Disable mod_status entirely or restrict access via Apache config (e.g., <Location /server-status> Require ip 127.0.0.1 </Location>)
- Monitor access logs for repeated /server-status/ requests from unknown IPs using tools like Fail2Ban or SIEM rules
- Use web application firewalls (WAF) to block unauthenticated access to admin endpoints

## Objectives

1. Gather server performance and connection data for reconnaissance
2. Extract log entries to identify users, paths, or anomalies
3. Assess server load to inform timing of follow-on attacks

## Instructions

### Step 1: Verify Endpoint Accessibility

**Context**: Confirm the /server-status/ page is exposed and returns data without errors.

**Command** ([[commands/curl-access-server-status]]):
```bash
curl -k -v https://target.example.com/server-status/
```

> This command sends a verbose GET request to the endpoint, ignoring SSL issues. Expected output includes HTTP 200 status and HTML content with sections like "Server Version," "Server Load," and a table of current connections. If successful, you'll see details like "Total Accesses: 12345" and recent requests (e.g., "GET /path HTTP/1.1 from 192.168.1.1").

### Step 2: Parse and Analyze Response

**Context**: Review the output for actionable intelligence, such as high-load indicators or leaked paths.

**Command** ([[commands/curl-access-server-status]]):
```bash
curl -k https://target.example.com/server-status/ | grep -E 'Total Accesses|Current Time|Request'
```

> Filters the response for key metrics. Successful output shows parsed lines like request logs, which can reveal internal paths or client details. Save to a file for further analysis: `curl ... > status.html`.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- [[Software]]

## Commands Used

- [[commands/curl-access-server-status]]

## Tools Used


## Tags

- information-disclosure
- apache
- reconnaissance
- server-status
