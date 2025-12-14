---
tags:
  - reconnaissance
  - web
  - headers
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-headers]]'
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5aaf0566-3fdb-4d8c-8153-6e707e70e9a4
created_at: '2025-12-14T03:16:20.584Z'
updated_at: '2025-12-14T03:16:20.584Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-HTTP-Response-Headers-Manually

## Summary

This procedure involves manually fetching and inspecting HTTP response headers from a target website using command-line tools to identify security-related misconfigurations, such as improper X-XSS-Protection values that fail to enable browser XSS protections.

## Description

In web security assessments, examining HTTP response headers is a fundamental reconnaissance step to uncover misconfigurations in security policies. For the target https://www.sfl-tap.army.mil/, this procedure reveals the X-XSS-Protection header set to 'DENY', an invalid value that does not activate the browser's XSS Auditor and may confuse it with X-Frame-Options settings. The correct configuration '1; mode=block' enables detection and blocking of potential XSS payloads. This low-impact issue reduces built-in mitigations against reflected XSS attacks but requires no exploitation to detect. Prerequisites include basic command-line access and internet connectivity; no authentication is needed for public sites.

## Requirements

1. curl installed on the attacker's system (standard on most Linux/macOS distributions)
2. Network access to the target website over HTTPS
3. Basic understanding of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAFs) to monitor and alert on anomalous header inspection requests
- Regularly audit server configurations using tools like securityheaders.com to ensure proper header settings
- Enable logging of HTTP requests to detect repeated header probes from suspicious IPs

## Objectives

1. Retrieve and parse HTTP response headers from the target endpoint
2. Identify misconfigured security headers like X-XSS-Protection
3. Document potential risks to XSS mitigations for reporting

## Instructions

### Step 1: Fetch Response Headers

**Context**: Use curl to send a HEAD request to the target URL, retrieving only headers without the body to quickly inspect security configurations.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://www.sfl-tap.army.mil/
```

> This command outputs all response headers. Look for X-XSS-Protection: DENY, indicating the misconfiguration. Successful execution shows HTTP/1.1 200 OK or similar, followed by headers.

### Step 2: Analyze Header Values

**Context**: Manually review the output for security headers, noting invalid values and cross-referencing with standards (e.g., OWASP recommendations).

**Command** (No specific command; manual review):

> Compare against expected values: X-XSS-Protection should be '1; mode=block'. If 'DENY' appears, flag as a misconfiguration potentially weakening XSS defenses.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Reconnaissance]]
- [[web]]
- [[headers]]
