---
tags:
  - open-redirect
  - oauth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: fe88c3ca-a85b-44e7-a09a-3fc5408dc0cb
created_at: '2025-12-14T17:24:23.361Z'
updated_at: '2025-12-14T17:24:23.361Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Access-Facebook-Auth-Endpoint-with-Manipulated-Origin

## Summary

This procedure initiates the exploitation of an open redirect vulnerability by accessing Urban Dictionary's Facebook authentication endpoint with a manipulated 'origin' parameter set to an arbitrary external URL, setting the stage for post-authentication redirection.

## Description

The Urban Dictionary Facebook OAuth endpoint at `/auth/facebook` accepts an 'origin' query parameter without proper validation, allowing attackers to specify any URL. This step constructs and accesses the malicious URL to begin the OAuth flow, which can later redirect authenticated users to phishing sites. The target environment is the public-facing web application, requiring only browser access. Expected outcome is redirection to Facebook login without rejection of the origin.

## Requirements

1. Web browser with JavaScript enabled
2. Public access to http://www.urbandictionary.com
3. Knowledge of a target external domain for redirection (e.g., for testing: google.com; for attack: attacker-controlled phishing site)

## Defense

Defensive measures and detection strategies:

- Implement URL validation on the origin parameter, whitelisting only trusted domains (e.g., urbandictionary.com subdomains)
- Use HTTP response headers like Content-Security-Policy to restrict redirects
- Monitor access logs for unusual origin parameters containing external domains
- Employ Web Application Firewall (WAF) rules to block arbitrary redirects in OAuth flows

## Objectives

1. Initiate OAuth flow with unvalidated redirect target
2. Prepare for authentication that will trigger the redirect
3. Expose the vulnerability for phishing link crafting

## Instructions

### Step 1: Construct and Navigate to Manipulated URL

**Context**: Build the endpoint URL with the origin parameter to test or exploit the lack of validation.

No specific command required; use browser navigation.

Navigate to:

```url
http://www.urbandictionary.com/auth/facebook?origin=http://google.com
```

> This URL starts the Facebook login process. The origin parameter is passed through without sanitization, allowing any scheme and domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[oauth]]
