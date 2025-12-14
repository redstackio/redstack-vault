---
tags:
  - information-disclosure
  - frontpage
  - sharepoint
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-FrontPage-Configuration-File]]'
step_count: 1
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:25:12.792Z'
description: >-
  A reconnaissance attack chain exploiting public access to a FrontPage
  configuration file on a U.S. Department of Defense SharePoint subdomain,
  revealing version details and internal scripting paths for further targeting.
skill_level: beginner
impact_level: medium
id: 8127a8a3-1ca2-4162-baab-4fa00bb24a92
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Information Disclosure of FrontPage Configuration on DoD SharePoint Server

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access Configuration File] --> B[Disclose Information]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]

### Target Environment

- Web platform
- SharePoint services
- No specific ports required (HTTPS/443 implied)

### Initial Access Requirements

- Public internet access to the target subdomain
- No credentials needed
- Direct URL knowledge or subdomain enumeration

## Detailed Attack Procedures

### Step 1: Access Configuration File
procedure: [[procedures/Access-FrontPage-Configuration-File]]

**Objective**: Retrieve sensitive FrontPage configuration details, including version and scripting paths, to aid in reconnaissance of the SharePoint server.

**Instructions**: Launch [[tools/Firefox]] and navigate directly to the vulnerable URL `https://███████/_vti_inf.html`. The page will load an HTML file containing embedded comments with configuration data. Inspect the source code to extract details such as the FrontPage version (e.g., 16.00.0.000) and scripting URLs like FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc".

**Expected Output**: An HTML page with comments revealing configuration information, viewable in the browser's developer tools or page source.

**Success Indicators**:
- Page loads without authentication prompt
- Configuration details visible in HTML comments
- Version and scripting paths extracted

## Attack Chain Summary

### Key Achievements

1. Successful unauthenticated access to _vti_inf.html
2. Disclosure of FrontPage version 16.00.0.000
3. Extraction of internal SharePoint scripting paths for potential follow-on attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---

*Last updated: 2023-10-01T00:00:00Z*
