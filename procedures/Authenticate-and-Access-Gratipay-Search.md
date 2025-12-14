---
id: proc-gratipay-auth-search-001
name: Authenticate-and-Access-Gratipay-Search
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.439Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - authentication
  - web
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Authenticate-and-Access-Gratipay-Search

## Summary

This procedure outlines logging into the Gratipay web application and navigating to the search functionality, establishing an authenticated session necessary for exploiting the reflected XSS vulnerability via CSRF.

## Description

In the context of the Gratipay XSS/CSRF attack, authentication provides the session context required for the search feature to reflect user inputs without validation. The target environment is the web-based Gratipay platform at https://gratipay.com/. Expected outcomes include a valid session cookie that can be hijacked post-exploit. Prerequisites include valid user credentials and a browser configured for proxy interception if proceeding to subsequent steps.

## Requirements

1. Valid Gratipay user account credentials (username/email and password)
2. Web browser (e.g., Chrome or Firefox) with proxy support for tools like Burp Suite
3. Network access to https://gratipay.com/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to limit session hijacking impact
- Monitor login attempts for anomalies, such as unusual IP addresses or rapid successive logins

## Objectives

1. Establish an authenticated session on Gratipay
2. Access the vulnerable search endpoint at https://gratipay.com/search
3. Prepare the environment for request interception and payload injection

## Instructions

### Step 1: Log In to Gratipay

**Context**: Access the login page and authenticate to create a session.

Navigate to https://gratipay.com/ in your browser, click the login button, enter your credentials, and submit the form.

> Upon success, you will be redirected to the dashboard, and session cookies (e.g., _gratipay_session) will be set.

### Step 2: Navigate to Search Functionality

**Context**: Proceed to the search page to load the vulnerable interface.

From the dashboard, click the search icon or enter /search in the URL bar to reach https://gratipay.com/search.

> The search box should be visible and functional for benign queries, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web

