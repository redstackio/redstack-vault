---
id: proc-csrf-identify-zomato-2024
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.415Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify CSRF-Vulnerable Username Endpoint

## Summary

This procedure involves reconnaissance to identify web endpoints susceptible to CSRF attacks, specifically targeting Zomato's username selection feature by analyzing network traffic for unprotected POST requests.

## Description

In a CSRF attack scenario, the first step is to map the target's state-changing endpoints. For Zomato, the username_selector.php handles POST requests to update user handles via the 'uname' parameter. Without CSRF tokens, SameSite cookies, or origin checks, cross-site requests can forge actions. This procedure uses browser tools to observe legitimate requests and test for protections, confirming the endpoint's vulnerability in a web environment.

## Requirements

1. Access to a Zomato account for testing legitimate flows
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP requests and web security

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce SameSite=Strict on session cookies
- Validate Origin/Referer headers on sensitive endpoints
- Monitor for anomalous username changes in logs

## Objectives

1. Confirm the exact endpoint and parameters for username updates
2. Verify absence of CSRF protections
3. Establish foundation for payload crafting

## Instructions

### Step 1: Perform Legitimate Username Change

**Context**: Trigger a username change in Zomato to capture the request details.

Navigate to Zomato's profile settings, attempt to change your handle, and monitor the Network tab in browser DevTools. Look for the POST request to /php/username_selector.php.

**Expected Output**: Request details showing action="https://www.zomato.com/php/username_selector.php" method="POST" with form data uname=desiredhandle.

### Step 2: Test for CSRF Protection

**Context**: Attempt a cross-origin request to check if protections block it.

Create a simple HTML test page on a different domain (e.g., local file) with a form posting to the endpoint. Submit and observe if the request succeeds without authentication prompts or errors.

**Expected Output**: Successful username update without token validation, indicating CSRF vulnerability.

**Success Indicators**:
- Request completes with 200 OK or successful update
- No CSRF token observed in legitimate request

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
