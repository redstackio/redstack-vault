---
tags:
  - auth-bypass
  - impresscms
type: procedure
tools:
  - '[[tools/sqli-php]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-sqli-poc]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:20.612Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ff04327e-d65c-47d3-bdb0-1873b258f2a2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Retrieve-Security-Token-via-Auth-Bypass

## Summary

This procedure exploits a related authentication bypass vulnerability in ImpressCMS (report #1081137) to obtain a security token, allowing unauthenticated access to endpoints like /include/findusers.php for subsequent SQL injection.

## Description

In ImpressCMS 1.4.2, an authentication flaw enables attackers to retrieve a valid security token without logging in. This token is then used in requests to bypass checks. The procedure uses a custom PHP PoC script to automate token retrieval by sending crafted requests to the vulnerable endpoint. Prerequisites include network access to the ImpressCMS installation. Expected outcomes include a usable token for chaining with SQLi attacks, leading to data extraction or modification.

## Requirements

1. Access to ImpressCMS 1.4.2 installation URL
2. Custom PoC script [[tools/sqli-php]]
3. PHP runtime for script execution

## Defense

Defensive measures and detection strategies:

- Implement proper session validation and token generation with CSRF protection
- Monitor for anomalous token requests without prior authentication
- Use web application firewalls (WAF) to detect bypass patterns

## Objectives

1. Gain unauthenticated access to protected API endpoints
2. Enable chaining with SQL injection for data exfiltration
3. Facilitate account takeover via extracted credentials

## Instructions

### Step 1: Execute PoC Script for Token Retrieval

**Context**: Run the script to exploit the auth bypass and capture the security token.

**Command** ([[commands/php-sqli-poc]]):
```bash
php sqli.php http://localhost/impresscms/
```

> This command targets the ImpressCMS URL, exploits the bypass in report #1081137, and outputs the retrieved security token. Expected output includes "[-] Retrieving security token..." followed by the token value.

### Step 2: Verify Token Usage

**Context**: Use the token in a test request to confirm access to /include/findusers.php.

**Command** ([[commands/php-sqli-poc]]):
```bash
# Manually test with curl using the token (integrate into script if needed)
curl -X POST http://localhost/impresscms/include/findusers.php -d "token=$TOKEN"
```

> Replace $TOKEN with the retrieved value. Successful response indicates no auth error, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/php-sqli-poc]]

## Tools Used

- [[tools/sqli-php]]

## Tags

- auth-bypass
- token-retrieval
