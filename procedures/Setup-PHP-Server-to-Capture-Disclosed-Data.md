---
tags:
  - data-capture
  - php-server
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 40607378-3591-41d3-9a6d-9cd500498b73
created_at: '2025-12-13T09:00:34.295Z'
updated_at: '2025-12-13T09:00:34.295Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Setup PHP Server to Capture Disclosed Data

## Summary

This procedure creates a PHP script on the attacker-controlled host to handle incoming OPTIONS and POST requests, capturing and logging the disclosed CSRF token and email in JSON format.

## Description

The script mimics the legitimate server response to avoid suspicion, while extracting sensitive data from the request payload. This is crucial for chaining to CSRF attacks. Requires PHP environment on the malicious host. Expected outcome is logged data ready for use in account takeover.

## Requirements

1. PHP server setup on malicious host (e.g., localhost)
2. Ability to handle HTTP requests at /user/check_email
3. Prior disclosure requests redirected to this host

## Defense

Defensive measures and detection strategies:

- Use secure token generation and validation
- Implement rate limiting on sensitive endpoints

## Objectives

1. Capture CSRF token and email
2. Return mimicking JSON response
3. Store data for further attacks

## Instructions

### Step 1: Create and Deploy PHP Script

**Context**: Write a PHP file to process OPTIONS for CORS and POST for data capture.

> The script should log the X-CSRF-Token and email from the POST body, then echo a JSON response like {"token": "captured_token", "email": "captured_email"}.

### Step 2: Run the Server

**Context**: Start the PHP server to listen for incoming requests.

> Use php -S localhost:80 to host the script and capture data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- data-capture
- php-server
