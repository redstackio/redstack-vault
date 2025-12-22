---
tags:
  - csrf
  - web
  - access
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.216Z'
sub_techniques: []
id: 1117a739-e5e5-40ee-b97d-f88961ee01e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Omise-Dashboard-and-Prepare-Form

## Summary

This procedure logs into the Omise dashboard and navigates to the subscriptions form to prepare for CSRF token capture, setting up the environment for exploitation.

## Description

In the context of exploiting the Omise CSRF vulnerability, initial access to the dashboard is required to interact with the email relay addition form. The Ruby on Rails application generates a per-session authenticity token that does not expire, enabling subsequent reuse. This step ensures the attacker has a valid session to capture legitimate requests.

## Requirements

1. Valid Omise account credentials
2. Browser with proxy support for Burp Suite
3. Network access to https://dashboard.omise.co

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for dashboard login
- Monitor for unusual login patterns or session anomalies

## Objectives

1. Establish authenticated session in Omise dashboard
2. Load the email relay addition form
3. Prepare for request interception

## Instructions

### Step 1: Login to Dashboard

**Context**: Authenticate to gain a session cookie for form interactions.

No specific command; use browser to log in at https://dashboard.omise.co and enter credentials.

> Successful login redirects to the dashboard home.

### Step 2: Navigate to Form

**Context**: Access the specific endpoint for adding email relays.

Navigate to https://dashboard.omise.co/test/subscriptions/new in the browser.

> Form loads with fields for email address and event groups.

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

- [[csrf]]
- [[web]]
