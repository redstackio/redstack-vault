---
id: proc-gitlab-dashboard-redirect
name: Trigger Open Redirect in GitLab Dashboard Todos
tags:
  - open-redirect
  - phishing
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-gitlab-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.472Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Trigger Open Redirect in GitLab Dashboard Todos

## Summary

This procedure exploits an open redirect vulnerability in GitLab's Dashboard::TodosController by manipulating the 'host' parameter in the redirect_to call, allowing authenticated users to be redirected to arbitrary external sites for phishing purposes.

## Description

The vulnerability stems from the use of redirect_to params.merge(...) at line 10 of Dashboard::TodosController without validating the 'host' parameter. An attacker can craft a URL like /dashboard/todos?page=99999999&host=www.evil.com to trigger a redirect to the malicious site. This requires authentication but can trick logged-in users into visiting phishing pages, potentially leading to credential theft or malware distribution. The attack is low-effort and relies on social engineering to lure victims to the malicious URL.

## Requirements

1. Access to a vulnerable GitLab instance (pre-8.11.0 versions affected)
2. Valid authentication session (username/password or token)
3. Network connectivity to the GitLab server and target external site
4. Browser or curl for testing redirects

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect hosts in all redirect_to calls (e.g., only allow internal domains)
- Implement Content Security Policy (CSP) to restrict navigations
- Monitor access logs for anomalous 'host' parameters or high page numbers like 99999999
- Use web application firewall (WAF) rules to block unvalidated redirects

## Objectives

1. Redirect authenticated GitLab users to a controlled external phishing site
2. Bypass built-in redirect protections in Ruby on Rails
3. Demonstrate potential for social engineering attacks on GitLab users

## Instructions

### Step 1: Authenticate to GitLab

**Context**: Obtain a valid session to access the dashboard endpoint.

Log in via the GitLab web interface or use curl with session cookies. No specific command needed beyond standard login.

### Step 2: Craft and Trigger Malicious URL

**Context**: Manipulate the 'host' parameter to point to an external site, using a high page number to avoid normal pagination.

**Command** ([[commands/curl-test-gitlab-redirect]]):
```bash
curl -L -v "https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com" --cookie "session=your_session_cookie"
```

> This command follows the redirect (-L) and shows verbose output (-v) to confirm the 302 status and Location header pointing to the evil site. Replace gitlab.example.com with the target instance and session cookie with your authenticated value.

### Step 3: Verify Redirect in Browser

**Context**: Test in a real browser to simulate user interaction for phishing.

Visit the URL directly: https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com while logged in. The browser should redirect to the external site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-gitlab-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- gitlab
