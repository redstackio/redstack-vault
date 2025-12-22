---
id: ac-uuid-863221
tags:
  - ssrf
  - bypass
  - concrete-cms
  - localhost
  - decimal-ip
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Bypass-Localhost-SSRF-Restrictions-with-Decimal-IP-Notation]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.288Z'
description: >-
  A multi-stage attack exploiting an SSRF vulnerability in Concrete CMS 8.5.2 by
  bypassing localhost restrictions using decimal IP notation, allowing
  unauthorized access to internal services.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF Bypass in Concrete CMS Using Decimal IP Notation

Multi-stage attack chain demonstrating exploitation of an SSRF vulnerability in Concrete CMS version 8.5.2, building on a prior SSRF discovery to bypass localhost access restrictions via decimal IP notation (0177.0.0.1 for 127.0.0.1). This enables interaction with internal services, potentially leading to information disclosure, service enumeration, or further exploitation based on exposed local endpoints.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Prior SSRF] --> B[Bypass Localhost Restrictions]
    B --> C[Interact with Internal Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[tools/curl]] for sending requests

### Target Environment

- Concrete CMS version 8.5.2 running on PHP
- Access to a URL fetching feature (e.g., file import or image proxy endpoint)
- Network access to the public-facing Concrete CMS instance

### Initial Access Requirements

- Valid user session or public access to the vulnerable endpoint
- Knowledge of the prior SSRF vulnerability (HackerOne #243865)
- No special credentials required beyond basic site access

## Detailed Attack Procedures

### Step 1: Review Prior SSRF Vulnerability
procedure: [[procedures/Bypass-Localhost-SSRF-Restrictions-with-Decimal-IP-Notation]]

**Objective**: Identify the existing SSRF in Concrete CMS that restricts localhost access, setting the stage for bypass testing.

**Instructions**: Refer to the previous report (HackerOne #243865) detailing the SSRF in the URL fetching feature. Confirm the endpoint allows external URL requests but blocks 127.0.0.1 or localhost. Test a standard localhost request to verify the block:

Use a browser or curl to submit a URL like `http://127.0.0.1:8080` to the vulnerable feature (e.g., via a file upload or import form in Concrete CMS).

```bash
curl -X POST 'https://target.com/concrete/path/to/fetch' --data 'url=http://127.0.0.1:8080' -b 'session_cookie=value'
```

**Expected Output**: Request fails or returns an error due to localhost restriction.

**Success Indicators**:
- Confirmation of SSRF existence with localhost block
- Endpoint identified for further testing

### Step 2: Bypass Localhost Restrictions
procedure: [[procedures/Bypass-Localhost-SSRF-Restrictions-with-Decimal-IP-Notation]]

**Objective**: Circumvent the localhost filter by encoding the IP address in decimal notation, enabling access to internal services.

**Instructions**: Modify the URL to use decimal notation for 127.0.0.1, which is 0177.0.0.1 (octal-decimal encoding bypasses string-based validation). Submit this to the same URL fetching endpoint, targeting an internal service port (e.g., port 8080 for a local metadata service).

Use curl to send the bypassed request:

```bash
curl -X POST 'https://target.com/concrete/path/to/fetch' --data 'url=http://0177.0.0.1:8080/internal-endpoint' -b 'session_cookie=value'
```

Monitor the response for signs of internal service interaction, such as leaked data or error messages from the local service.

**Expected Output**: Successful fetch from internal service, potentially returning data like service banners or metadata.

**Success Indicators**:
- Response contains internal service content
- No localhost block error; evidence of SSRF success

## Attack Chain Summary

### Key Achievements

1. Identified and confirmed existing SSRF limitations from prior report
2. Bypassed localhost restrictions using decimal IP notation
3. Enabled unauthorized interaction with local services for potential exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
