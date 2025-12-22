---
id: proc-uuid-001
tags:
  - open-redirect
  - phishing
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.063Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Manipulate-Redirect-URL-in-Fabric-io-Login

## Summary

This procedure involves crafting a malicious URL for the Fabric.io login endpoint by manipulating the 'redirect_url' parameter with an '@' prefix followed by an arbitrary external domain, exploiting insufficient validation to set up a phishing redirect.

## Description

In the context of testing or attacking the Fabric.io login page, the 'redirect_url' parameter is vulnerable to open redirects because it allows arbitrary URLs prefixed with '@' without whitelisting or domain checks. An attacker creates a phishing link like https://www.fabric.io/login?redirect_url=@evil-site.com, which loads the legitimate login form but redirects the user to the evil site after authentication. This enables credential theft on a fake login page or malware delivery. Prerequisites include basic web knowledge and a controlled domain for the redirect target.

## Requirements

1. Access to a web browser for URL construction and testing
2. A malicious domain or site under attacker control for the redirect
3. No credentials needed for this step; victim provides them later

## Defense

Defensive measures and detection strategies:

- Implement strict whitelisting for redirect URLs, allowing only internal or trusted domains
- Validate and sanitize the 'redirect_url' parameter to strip or reject '@' prefixes and external hosts
- Monitor login endpoint access logs for unusual redirect parameters and block suspicious patterns

## Objectives

1. Create a functional phishing link that evades redirect validation
2. Direct victims to the legitimate login while preparing malicious post-login navigation
3. Set the stage for credential harvesting or exploitation after authentication

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the login URL with the exploited parameter to test or deploy the redirect.

No specific command is required; manually construct the URL in the browser address bar or via a link generator.

Example URL construction:

```url
https://www.fabric.io/login?redirect_url=@evil-site.com
```

> This URL loads the Fabric.io login page. The '@' prefix tricks the server into interpreting 'evil-site.com' as the redirect target without validation. Expected output: The page renders normally, accepting the parameter.

### Step 2: Test URL Loading

**Context**: Verify the URL loads the login form without errors, confirming parameter acceptance.

Navigate to the constructed URL in a browser.

> Upon loading, the login form appears intact. Success is indicated by no error messages and the presence of the manipulated parameter in the address bar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[open-redirect]]
- [[Phishing]]
