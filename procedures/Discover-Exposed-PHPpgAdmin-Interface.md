---
tags:
  - information-disclosure
  - phppgadmin
  - web-scanning
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-phppgadmin]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Vulnerability Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0494b619-90b7-41c2-b99a-f389747116d0
created_at: '2025-12-14T17:24:55.757Z'
updated_at: '2025-12-14T17:24:55.757Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover-Exposed-PHPpgAdmin-Interface

## Summary

This procedure identifies unrestricted access to the PHPpgAdmin web interface, a PHP-based tool for PostgreSQL management, by probing for its presence and confirming lack of access controls, leading to potential information disclosure.

## Description

In scenarios where PHPpgAdmin is deployed without proper firewall rules or authentication gateways, attackers can discover the interface via direct HTTP requests. This exposure allows enumeration of the tool's availability and version, facilitating further attacks like brute-forcing. The target environment typically involves a web server hosting PHP applications alongside a PostgreSQL backend. Prerequisites include network reachability to the target IP on standard web ports.

## Requirements

1. Network access to the target web server (ports 80/443)
2. Basic HTTP probing tool like curl
3. Knowledge of common PHPpgAdmin paths (e.g., /phppgadmin/)

## Defense

Defensive measures and detection strategies:

- Implement IP whitelisting or reverse proxy with authentication for admin tools
- Use web application firewalls (WAF) to block unauthorized access to /phppgadmin/
- Monitor access logs for anomalous HTTP requests to admin paths

## Objectives

1. Confirm exposure of PHPpgAdmin without access restrictions
2. Gather interface details for subsequent exploitation
3. Enable escalation to brute-force or direct database access

## Instructions

### Step 1: Probe for PHPpgAdmin Presence

**Context**: Send an HTTP request to the suspected path to check for the interface's response, identifying banners or forms that indicate unrestricted access.

**Command** ([[commands/curl-access-phppgadmin]]):
```bash
curl -s http://target-ip/phppgadmin/ | grep -i "phpPgAdmin"
```

> This command fetches the page silently and searches for PHPpgAdmin-specific strings. A match confirms the tool is exposed and accessible without prior authentication.

### Step 2: Verify Lack of Access Controls

**Context**: Attempt to load the login page or server status to ensure no redirects or blocks occur, validating the information disclosure.

**Command** ([[commands/curl-access-phppgadmin]]):
```bash
curl -s http://target-ip/phppgadmin/servers.php | head -20
```

> Expected output includes partial database server info or login prompts without errors, indicating vulnerability to unauthorized discovery.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-phppgadmin]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[phppgadmin]]
- [[web-scanning]]
