---
id: proc-access-registration
tags:
  - salesforce
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Cloud (Salesforce)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:43.143Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Salesforce-Registration-Page

## Summary

This procedure involves navigating to the Salesforce Experience Cloud registration page to load the necessary Aura framework components and trigger initial requests that can be intercepted for further exploitation.

## Description

In a Salesforce instance with misconfigured access controls, the public registration page allows unauthenticated users to access the Aura endpoint without checks. This step sets up the environment for intercepting and modifying requests to query sensitive ContentDocument objects, leading to BAC exploitation.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Proxy tool like Burp Suite configured for traffic interception
3. Direct internet access to the target Salesforce domain

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all public-facing pages via Salesforce sharing rules
- Monitor Aura endpoint logs for anomalous queries to ContentDocument
- Implement web application firewall (WAF) rules to block modified Aura payloads

## Objectives

1. Load the registration page without authentication
2. Trigger Aura requests for interception
3. Establish baseline for payload modification

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

No specific command; configure Burp as proxy (e.g., 127.0.0.1:8080) in browser settings.

> Ensure all HTTPS traffic is intercepted by installing Burp's CA certificate.

### Step 2: Navigate to Registration URL

**Context**: Access the target endpoint to load the page.

No command; enter URL https://[redacted].experience.[redacted]/s/registration in browser.

> Page should load without redirect to login; observe network tab for /aura POST requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[salesforce]]
- [[initial-access]]
