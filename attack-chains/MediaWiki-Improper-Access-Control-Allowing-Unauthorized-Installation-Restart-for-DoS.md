---
tags:
  - mediawiki
  - access-control
  - dos
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Access-MediaWiki-Config-Page-Without-Auth]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploiting a misconfigured MediaWiki installation where the configuration page
  is publicly accessible, enabling unauthorized users to restart the wiki and
  cause denial of service on a DoD asset.
skill_level: low
impact_level: high
id: ed425c6d-1f00-4929-8fa7-42abc8ee497a
created_at: '2025-12-14T17:28:58.924Z'
updated_at: '2025-12-14T17:28:58.924Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# MediaWiki Improper Access Control Allowing Unauthorized Installation Restart for DoS

Multi-stage attack chain demonstrating a complete attack workflow targeting a misconfigured MediaWiki instance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Configuration Page] --> B[Restart Installation]
    B --> C[Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser or basic HTTP client sufficient)

### Target Environment

- Web platform with MediaWiki installed
- Exposed HTTP/HTTPS service on standard ports (80/443)
- No authentication required for /mw-config/ endpoint

### Initial Access Requirements

- Network access to the target web server
- No credentials needed due to misconfiguration
- Direct URL knowledge of the MediaWiki instance

## Detailed Attack Procedures

### Step 1: Access Configuration Page and Restart
procedure: [[procedures/Access-MediaWiki-Config-Page-Without-Auth]]

**Objective**: Bypass access controls to reach the MediaWiki configuration page and trigger a restart, disrupting the service.

**Instructions**: Navigate to the target MediaWiki installation's configuration endpoint using a web browser or HTTP client. The page will load without prompting for authentication, displaying a 'restart installation' button. Interact with the button to reset the wiki setup.

First, access the endpoint using [[commands/curl-access-mediawiki-config]]:

```bash
curl -i https://target-domain.com/mw-config/index.php
```

This retrieves the page content, confirming public accessibility. Then, in a browser, visit the URL and click the 'restart installation' button to execute the reset.

**Expected Output**: HTTP response with 200 OK and HTML content showing the configuration interface, including the restart option. Upon clicking restart, the application will reinitialize, temporarily taking the wiki offline.

**Success Indicators**:
- Page loads without login prompt
- Restart button is visible and clickable
- Wiki becomes unresponsive post-restart, confirming DoS

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication on sensitive configuration endpoint
2. Triggered unauthorized restart of MediaWiki installation
3. Achieved denial of service on the target DoD asset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
