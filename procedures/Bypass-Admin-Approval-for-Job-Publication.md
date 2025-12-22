---
id: proc-001
tags:
  - auth-bypass
  - graphql
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.370Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Admin-Approval-for-Job-Publication

## Summary

This procedure exploits an incorrect authorization vulnerability in the inDrive Job platform by intercepting the GraphQL mutation request during job creation and modifying the status parameter from 'MODERATION' to 'ACTIVE', allowing immediate publication without admin review. It enables attackers to post arbitrary content, including scams, malware, or spam, disrupting the platform.

## Description

The inDrive Job platform requires admin approval for job offers, setting new vacancies to 'MODERATION' status via a GraphQL POST to /api/graphql. Due to missing server-side validation, attackers can use a proxy like Burp Suite to alter the 'status' variable in the UpdateVacancyStatus mutation. This bypasses the approval workflow, making the offer visible to all users. The target environment is the web application at https://injob.indriver.com/, requiring an employer account. Expected outcomes include successful publication of unauthorized jobs, potentially leading to phishing, malware distribution, or denial-of-service through flooding.

## Requirements

1. Valid employer account on inDrive Job platform with login credentials
2. Burp Suite installed and configured as a proxy for browser traffic
3. Direct network access to https://injob.indriver.com/ over HTTPS
4. Basic knowledge of HTTP request interception and JSON modification

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to validate status changes against user permissions
- Use input validation and sanitization for GraphQL parameters to prevent tampering
- Monitor for anomalous request patterns, such as frequent status updates from non-admin IPs
- Enable Web Application Firewall (WAF) rules to detect proxy-intercepted traffic signatures

## Objectives

1. Bypass the mandatory admin approval process for job offers
2. Publish malicious or unauthorized content on the platform
3. Disrupt legitimate platform usage through spam or flooding

## Instructions

### Step 1: Access Employer Mode and Initiate Job Creation

**Context**: Log in and start the job offer process to generate the target GraphQL request.

No specific command; use the web interface to navigate to https://injob.indriver.com/, log in as employer, and click to create a new job offer.

> This loads the form and establishes a session for subsequent requests.

### Step 2: Complete and Submit Job Form

**Context**: Fill details to trigger the initial submission request with 'MODERATION' status.

No specific command; enter job title, description, location, etc., in the form and submit. Intercept the POST to /api/graphql if needed for observation.

> The request payload includes the UpdateVacancyStatus mutation setting status to 'MODERATION'. Expected response: 200 OK with pending confirmation.

### Step 3: Intercept Request with Burp Proxy

**Context**: Capture the final GraphQL mutation during submission.

Configure browser proxy to 127.0.0.1:8080 (Burp listener). Submit the form again if needed to intercept the request in Burp Proxy.

> Forward to Repeater tab. The payload resembles: {"query": "mutation UpdateVacancyStatus($input: UpdateVacancyStatusInput!) { ... }", "variables": {"input": {"status": "MODERATION"}}}

### Step 4: Modify Status Parameter

**Context**: Alter the JSON to set status to 'ACTIVE' for bypass.

In Burp Repeater, edit the variables section: Change {"status": "MODERATION"} to {"status": "ACTIVE"}. Ensure the GraphQL query remains intact.

> Validate JSON syntax. No command; manual edit in Burp UI.

### Step 5: Resend Modified Request

**Context**: Execute the tampered request to publish the offer.

Click 'Send' in Burp Repeater to forward the POST to /api/graphql.

> Server responds with success, updating status to 'ACTIVE'. Verify in the platform UI: Offer now visible publicly without approval.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- auth-bypass
- graphql
- web-vulnerability
