---
tags:
  - idor
  - enumeration
  - api
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:30.112Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a6bce82d-f4ee-4cc4-8000-ab6df1446034
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-User-IDs-and-Emails-via-Dashboard-API

## Summary

This procedure intercepts API responses from the dashboard endpoint in the MTN MoBad application to enumerate user IDs and emails, providing identifiers for subsequent IDOR exploitation.

## Description

In the MTN MoBad web application, the dashboard loads data via a POST request to /app/dashboardData, which inadvertently includes details of other users in the response JSON. By proxying traffic with Burp Suite, an authenticated attacker can capture this data to discover valid user IDs and emails without additional authentication. This step is foundational for targeting specific accounts in IDOR attacks, occurring in a web environment where the application lacks proper data filtering.

## Requirements

1. Authenticated session to mtnmobad.mtnbusiness.com.ng
2. Burp Suite installed and configured as an HTTP proxy (e.g., browser proxy set to 127.0.0.1:8080)
3. Network access to the target domain

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on API endpoints to filter responses based on the authenticated user's ID
- Use rate limiting and logging on dashboard endpoints to detect anomalous data access patterns
- Employ Web Application Firewalls (WAF) to inspect and block requests that proxy sensitive user data

## Objectives

1. Extract user IDs and emails from unprotected API responses
2. Identify potential targets for account manipulation
3. Enable escalation to profile modification without direct authentication

## Instructions

### Step 1: Configure Proxy and Access Dashboard

**Context**: Set up Burp Suite to intercept all traffic from the browser to capture API calls.

Intercept traffic by enabling Burp Proxy and navigating to the dashboard.

**Technical Details**: Access https://mtnmobad.mtnbusiness.com.ng/#/dashboard/home with Burp Proxy active.

### Step 2: Intercept and Analyze Dashboard Request

**Context**: Capture the POST request to the dashboard endpoint and review the response for user data.

In Burp's Proxy tab, intercept the POST to /app/dashboardData; examine the JSON response body for arrays containing user objects with 'id' and 'email' fields.

**Technical Details**: The response includes data like {"users": [{"id": "123", "email": "victim@example.com"}, ...]} without authorization checks.

**Expected Output**: List of user IDs and emails extracted for targeting.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[enumeration]]
- [[api]]
