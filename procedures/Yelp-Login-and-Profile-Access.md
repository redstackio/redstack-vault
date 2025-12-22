---
id: proc-yelp-login-001
tags:
  - authentication
  - web
  - yelp
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:23.174Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Yelp-Login-and-Profile-Access

## Summary

This procedure establishes an authenticated session on the Yelp website and navigates to the profile locations page, serving as the initial access point for exploiting the IDOR vulnerability in location editing.

## Description

The procedure involves logging into Yelp using valid credentials and accessing the profile locations endpoint. This sets up the necessary session cookies and context for intercepting subsequent requests. It targets the web-based Yelp platform and requires no special privileges beyond a standard user account. Expected outcomes include a valid session and visibility of personal saved locations, which can then be used to identify edit requests for manipulation.

## Requirements

1. Valid Yelp account credentials (username and password)
2. Web browser with proxy support (e.g., configured for Burp Suite)
3. Internet access to https://www.yelp.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for logins to prevent credential compromise
- Monitor for unusual login patterns or session anomalies using web application firewalls (WAF)
- Rate-limit login attempts to detect brute-force or automated access

## Objectives

1. Establish authenticated access to Yelp profile features
2. Load the profile locations page to prepare for request interception
3. Confirm session validity for subsequent exploitation steps

## Instructions

### Step 1: Access Login Page

**Context**: Begin the authentication process by navigating to the Yelp login endpoint.

No specific command; use a web browser to visit https://www.yelp.com/login and enter credentials.

> Upon successful login, the browser redirects to the user dashboard, confirming authentication.

### Step 2: Navigate to Profile Locations

**Context**: Access the saved locations page to view personal data and enable edit interactions.

No specific command; from the dashboard, go to https://www.yelp.com/profile_location.

> The page loads with a list of saved locations, indicating successful profile access.

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
- yelp
