---
id: proc-inspect-phabricator-csrf
tags:
  - csrf
  - web
  - phabricator
  - inspection
  - vulnerability-scanning
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:27:29.653Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Inspect-Phabricator-Forms-for-CSRF-Tokens

## Summary

This procedure involves manually inspecting forms and endpoints in the Phabricator web application using browser developer tools to identify missing anti-CSRF tokens, which protect against Cross-Site Request Forgery attacks by ensuring requests originate from legitimate user actions.

## Description

Phabricator, a web-based code review and project management tool, may expose vulnerabilities if its forms lack anti-CSRF tokens—unique, session-specific values that validate request authenticity. This procedure simulates a security audit by navigating authenticated sessions and examining HTML for token absence. In a real attack scenario, this reconnaissance could precede crafting malicious requests to force unwanted actions like data modification or account takeover. The process targets various endpoints, revealing 15 instances of missing protections, though Phabricator maintainers deemed the findings invalid due to built-in mitigations like same-site cookies. Prerequisites include a running Phabricator instance and user access; outcomes include a vulnerability report highlighting risks to authenticated users, such as social-engineered actions leading to compromise.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome, Firefox).
2. Valid Phabricator user credentials for authenticated access.
3. Direct network connectivity to the Phabricator server (HTTP/HTTPS).

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens in all state-changing forms using frameworks like Phabricator's built-in protections.
- Enforce SameSite cookie attributes (Strict or Lax) to mitigate cross-site requests.
- Monitor application logs for anomalous form submissions without tokens.
- Use Web Application Firewalls (WAF) to detect and block CSRF patterns.

## Objectives

1. Identify forms vulnerable to CSRF by confirming token absence.
2. Document affected endpoints for remediation or exploitation planning.
3. Assess potential impact on user sessions and application integrity.

## Instructions

### Step 1: Authenticate and Navigate to Target Endpoints

**Context**: Gain access to the Phabricator interface to reach forms requiring inspection. This establishes a legitimate session for viewing protected elements.

Log in to Phabricator using provided credentials. Navigate to key areas such as the dashboard, authentication pages, and task maniphest.

**Expected Output**: Successful login and access to URLs like /dashboard/, /maniphest/, /auth/start/.

### Step 2: Inspect Form Elements for Tokens

**Context**: Use browser tools to examine the HTML structure of forms on each page, searching for anti-CSRF token fields.

Open developer tools (F12 or right-click > Inspect). For each target URL (e.g., /Z1336, /applications/, /diffusion/, /feed/query/all/):

- Locate <form> tags.
- Search the DOM for hidden inputs like <input type="hidden" name="csrf_token" value="random_value">.
- If absent, note the URL and form purpose (e.g., login, task creation).

Repeat across 15+ endpoints, including /book/phabricator/article/installation_guide/, /home/menu/view/245/, and /differential/.

**Expected Output**: Screenshots or notes listing URLs with missing tokens, e.g., "No CSRF token in /maniphest/ task form."

### Step 3: Validate and Document Findings

**Context**: Confirm the vulnerability by attempting a test request (non-exploitative) and compile results.

In the console, simulate a form submission without a token to observe behavior (do not execute maliciously). Document root cause (missing random tokens) and impact (potential unauthorized actions via social engineering).

**Expected Output**: A report summarizing 15 vulnerable instances and their locations.
