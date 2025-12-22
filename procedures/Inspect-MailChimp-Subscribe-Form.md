---
id: proc-inspect-mailchimp-form
tags:
  - csrf
  - recon
  - web-form
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:22.666Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-MailChimp-Subscribe-Form

## Summary

This procedure involves locating and analyzing the MailChimp subscribe form to identify its endpoint, parameters, and lack of CSRF protection, serving as the reconnaissance step for exploiting subscription vulnerabilities.

## Description

In the context of web application testing, inspect the subscribe form at endpoints like http://paragonie.us11.list-manage2.com/subscribe?u=260ff2c88e0a7e103f01ccd79&id=8ddb8569ca. The form accepts POST requests with fields for email (MERGE0), name (MERGE1, MERGE2), organization (MERGE3), and EMAILTYPE=html. No CSRF token is present, enabling forged requests. This step is crucial for replicating the submission in attacks, targeting environments with third-party mailing list integrations like MailChimp.

## Requirements

1. Browser or proxy tool (e.g., Burp Suite) for form inspection and request capture.
2. Access to the public subscribe form URL.
3. Basic knowledge of HTML forms and HTTP POST requests.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms.
- Monitor for anomalous subscription patterns from external IPs.

## Objectives

1. Document form structure and parameters.
2. Confirm absence of CSRF protection.
3. Prepare data for PoC development.

## Instructions

### Step 1: Locate the Form

**Context**: Navigate to the subscribe page to view the form HTML.

Inspect the form at http://paragonie.us11.list-manage2.com/subscribe?u=260ff2c88e0a7e103f01ccd79&id=8ddb8569ca and note fields for user details.

### Step 2: Capture Submission Request

**Context**: Submit the form to analyze the POST payload.

Use a proxy like Burp Suite to intercept the request to http://paragonie.us11.list-manage.com/subscribe/post, capturing parameters: u=260ff2c88e0a7e103f01ccd79, id=8ddb8569ca, MERGE0=email, MERGE1=first, MERGE2=last, MERGE3=org, EMAILTYPE=html, submit=Subscribe to list.

> Expected output: Full request details in proxy logs, confirming no anti-CSRF measures.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[recon]]
