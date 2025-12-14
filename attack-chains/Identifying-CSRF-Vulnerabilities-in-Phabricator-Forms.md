---
id: ac-csrf-phabricator-identification
tags:
  - csrf
  - web
  - phabricator
  - vulnerability-scanning
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-Phabricator-Forms-for-CSRF-Tokens]]'
step_count: 1
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:27:29.657Z'
description: >-
  A reconnaissance-focused attack chain for identifying missing anti-CSRF tokens
  in Phabricator web application forms, enabling potential CSRF exploitation.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identifying CSRF Vulnerabilities in Phabricator Forms

Multi-stage attack chain demonstrating a reconnaissance workflow to identify potential CSRF vulnerabilities in the Phabricator web application by inspecting forms for missing anti-CSRF tokens.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Inspect Forms] --> B[Identify Missing Tokens]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Phabricator web application
- Access to authenticated user session
- No specific ports or services beyond standard HTTP/HTTPS (ports 80/443)

### Initial Access Requirements

- Valid user credentials for Phabricator
- Direct network access to the application
- No prior compromise needed

## Detailed Attack Procedures

### Step 1: Inspect Application Endpoints and Forms
procedure: [[procedures/Inspect-Phabricator-Forms-for-CSRF-Tokens]]

**Objective**: Review Phabricator URLs and forms to detect the absence of anti-CSRF tokens, which could allow unauthorized state-changing requests.

**Instructions**: Open the Phabricator application in a web browser and authenticate as a user. Use developer tools to examine the HTML source of various forms and endpoints. Look for the presence of CSRF tokens (typically hidden input fields with random values). Target multiple pages including dashboards, authentication flows, and manipulation interfaces. Document any forms lacking these tokens.

For example, navigate to the dashboard and inspect the form elements:

- Right-click on forms and select "Inspect Element".
- Search for input fields named like "csrf_token" or similar.
- Note URLs such as /dashboard/, /maniphest/, and others where tokens are absent.

Repeat for 15+ instances across the application.

**Expected Output**: A list of URLs and forms without anti-CSRF tokens, e.g., /Z1336, /applications/, /auth/start/.

**Success Indicators**:
- Identification of at least one form missing a CSRF token.
- Confirmation via HTML inspection that no random token value is present in the form.

## Attack Chain Summary

### Key Achievements

1. Systematic inspection of Phabricator endpoints revealing potential CSRF exposure.
2. Documentation of 15 vulnerable forms across authentication, dashboard, and task management areas.
3. Assessment of impact including possible account hijacking or data compromise for authenticated users.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
