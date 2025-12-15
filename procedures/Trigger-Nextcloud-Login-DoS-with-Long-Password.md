---
tags:
  - dos
  - nextcloud
  - web
  - hashing-exhaustion
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.604Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8b015db5-e82c-48e6-9d0c-22212a716dca
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Trigger-Nextcloud-Login-DoS-with-Long-Password

## Summary

This procedure exploits a denial-of-service vulnerability in the Nextcloud demo login page by submitting an excessively long password, which triggers unbounded hashing computations leading to CPU and memory exhaustion. It demonstrates a simple resource exhaustion attack applicable to web applications with poor input validation on password fields.

## Description

The vulnerability stems from a password hashing implementation in the Nextcloud demo environment that does not restrict the maximum length of passwords accepted during login. By entering a password of up to 1,000,000 characters, the hashing process (likely using a computationally intensive algorithm like bcrypt without length caps) consumes excessive server resources, causing the login service to become unresponsive. This affects only the demo site at https://demo2.nextcloud.com and does not impact core Nextcloud products. The attack requires no authentication and can be performed manually via a browser, making it accessible to low-skill attackers. Expected outcomes include site unavailability for several minutes, with potential for repeated attacks to prolong downtime.

## Requirements

1. Web browser with developer tools for generating long strings (e.g., Chrome or Firefox).
2. Public access to the Nextcloud demo URL: https://demo2.nextcloud.com/index.php/login.
3. No special privileges or tools needed; manual input suffices.

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation to enforce maximum password lengths (e.g., 256 characters).
- Use rate limiting on login attempts to prevent repeated submissions.
- Monitor server CPU and memory usage for spikes during login operations; alert on anomalies.
- Deploy web application firewalls (WAF) to block oversized POST requests to login endpoints.

## Objectives

1. Exhaust server resources to deny service to legitimate users.
2. Demonstrate the impact of missing input sanitization in authentication flows.
3. Validate vulnerability in demo environments before production deployment.

## Instructions

### Step 1: Access the Login Page

**Context**: Begin by navigating to the vulnerable login endpoint to load the form.

No command required; use a web browser to visit https://demo2.nextcloud.com/index.php/login.

> The page should load the standard Nextcloud login interface with username and password fields.

### Step 2: Input Username

**Context**: Provide a username to advance to the password submission, simulating a legitimate login.

Enter any username, such as "demo" or "admin", into the username field.

> The field accepts the input, focusing attention on the password field without validation errors.

### Step 3: Generate and Submit Long Password

**Context**: Create and submit an excessively long password to trigger the hashing exhaustion.

Use browser developer tools (e.g., Console) to generate a long string: Open DevTools (F12), go to Console, and run JavaScript like:

```javascript
document.querySelector('input[name="password"]').value = '123456789'.repeat(111112); // Approx 1M chars
```

Then, submit the form by clicking the login button or pressing Enter.

> The submission initiates hashing, leading to high CPU/memory usage. The page will hang, and server logs may show resource spikes. Monitor via browser task manager for client-side effects or server tools for backend exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- nextcloud
- web
- hashing-exhaustion
