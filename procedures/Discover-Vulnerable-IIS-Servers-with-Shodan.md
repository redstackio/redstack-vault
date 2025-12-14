---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - recon
  - shodan
  - iis
  - ms15-034
type: procedure
tools:
  - '[[tools/Shodan]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/shodan-search-vulnerable-iis]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:32.274Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Vulnerable-IIS-Servers-with-Shodan

## Summary

This procedure uses Shodan to search for internet-exposed Windows IIS servers vulnerable to MS15-034 (CVE-2015-1635), a remote code execution flaw in the HTTP.sys driver, enabling identification of high-value targets like government servers without direct interaction.

## Description

Shodan indexes public-facing devices and banners, allowing queries for specific vulnerabilities. In this scenario, attackers search for IIS servers with unpatched HTTP.sys components, focusing on organizations like the U.S. Department of Defense. The procedure reveals servers via port 80 exposure and vulnerability tags, setting up exploitation. Prerequisites include a Shodan API key for advanced queries; outcomes include IP lists for further testing, with risks of full compromise if exploited.

## Requirements

1. Shodan account with API key for authenticated searches
2. Internet access to query Shodan's database
3. Basic knowledge of search facets like ports, organizations, and CVE tags

## Defense

Defensive measures and detection strategies:

- Restrict server exposure: Use firewalls to limit public access to IIS ports
- Patch management: Apply MS15-034 updates promptly and monitor for unpatched systems
- Shodan monitoring: Set up alerts for your organization's IPs appearing in vulnerability searches
- Banner hiding: Configure IIS to obscure version details in HTTP responses

## Objectives

1. Identify exposed IIS servers associated with target organizations
2. Confirm vulnerability indicators without active scanning
3. Gather IPs for targeted exploitation attempts

## Instructions

### Step 1: Authenticate and Query Shodan

**Context**: Log in to Shodan CLI and perform a targeted search for IIS servers vulnerable to MS15-034.

**Command** ([[commands/shodan-search-vulnerable-iis]]):
```bash
shodan search --fields ip_str,port,org "port:80 iis 'Microsoft-IIS' vuln:CVE-2015-1635" --limit 10
```

> This command queries Shodan's database for HTTP servers on port 80 running IIS with the specific CVE tag, returning IPs, ports, and organizations. Expected output includes a list like: IP: 192.0.2.1, Port: 80, Org: U.S. Dept of Defense. Filter for relevant targets.

### Step 2: Refine and Export Results

**Context**: Narrow down results to high-value targets and save for exploitation.

**Command** ([[commands/shodan-download-results]]):
```bash
shodan download --limit 100 vulnerable_iis.json "port:80 iis vuln:CVE-2015-1635 org:'Department of Defense'"
```

> Exports matching results to JSON for offline analysis. Expected output: A file with detailed banners confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/shodan-search-vulnerable-iis]]
- [[commands/shodan-download-results]]

## Tools Used

- [[tools/Shodan]]

## Tags

- recon
- shodan
- iis
- ms15-034
