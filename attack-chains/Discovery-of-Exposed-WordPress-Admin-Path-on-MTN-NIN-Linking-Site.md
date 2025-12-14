---
tags:
  - improper-access-control
  - wordpress-exposure
  - web-recon
  - admin-path-leak
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Navigate-to-Target-Website]]'
  - '[[procedures/Access-NIN-Link-Status-Page]]'
  - '[[procedures/Inspect-HTML-Source-for-Exposed-Paths]]'
step_count: 3
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.689Z'
description: >-
  A reconnaissance attack chain that uncovers improper access controls by
  exposing the WordPress admin path in the HTML source code of the MTN NIN
  linking website, enabling potential unauthorized administrative access.
skill_level: beginner
impact_level: high
id: b0200d14-6285-4f66-bbfe-0c33a63778e5
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Discovery of Exposed WordPress Admin Path on MTN NIN Linking Site

Multi-stage attack chain demonstrating reconnaissance to identify misconfigurations in a public-facing web application, specifically exposing WordPress administrative endpoints on the MTN NIN linking site.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Site] --> B[Access Status Page]
    B --> C[Inspect Source Code]
    C --> D[Identify Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Publicly accessible web application
- WordPress-based site
- No special ports or services required beyond standard HTTPS (port 443)

### Initial Access Requirements

- Internet access
- No credentials or prior access needed
- Target URL: https://nin.mtn.ng/

## Detailed Attack Procedures

### Step 1: Navigate to Target Website
procedure: [[procedures/Navigate-to-Target-Website]]

**Objective**: Gain initial access to the public-facing MTN NIN linking website to begin reconnaissance.

**Instructions**: Open a web browser and directly access the target URL to load the homepage.

**Expected Output**: The homepage of https://nin.mtn.ng/ loads successfully, displaying the main interface for NIN linking services.

**Success Indicators**:
- Page loads without errors
- Site is responsive and accessible

### Step 2: Access NIN Link Status Page
procedure: [[procedures/Access-NIN-Link-Status-Page]]

**Objective**: Interact with the site to load the specific page containing the vulnerable HTML source.

**Instructions**: On the homepage, locate and click the 'Check your NIN Link Status' button to navigate to the status checking interface.

**Expected Output**: The NIN link status page loads, presenting a form or interface for entering details.

**Success Indicators**:
- Button click triggers page transition
- New page content related to NIN status is displayed

### Step 3: Inspect HTML Source for Exposed Paths
procedure: [[procedures/Inspect-HTML-Source-for-Exposed-Paths]]

**Objective**: Examine the page source code to identify misconfigurations, such as exposed administrative paths.

**Instructions**: Right-click on the MTN yellow bar at the top of the page and select 'Inspect' (or use Ctrl+Shift+I) to open developer tools. Navigate to the Elements tab and search the HTML for paths like '../wp-admin/admin-ajax.html'.

**Expected Output**: The HTML source reveals the exposed WordPress admin path '../wp-admin/admin-ajax.html' in the code.

**Success Indicators**:
- Developer tools open and display HTML
- Exposed admin path is visible in the source, indicating improper access controls

## Attack Chain Summary

### Key Achievements

1. Successful navigation and interaction with the target site without authentication
2. Identification of WordPress-based technology stack through source inspection
3. Discovery of high-severity vulnerability allowing potential unauthorized admin access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
