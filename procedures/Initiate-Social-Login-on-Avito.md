---
tags:
  - social-login
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.750Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e5ce5a38-93cf-4e91-9887-8683a1a719fc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate-Social-Login-on-Avito

## Summary

This procedure simulates or induces a victim to authenticate via social networks (OK or VK) on Avito.ru using the crafted malicious URL, triggering the redirect that reflects the XSS payload.

## Description

Avito.ru supports social logins from providers like OK.ru and VK.com, which redirect back after authentication without sanitizing the 'next' parameter. In an attack scenario, the victim clicks a phishing link to the malicious URL, selects social login, and completes auth on the provider site. This leads to a redirect to the injected javascript: URI. The procedure assumes web access and social accounts; outcomes include successful session establishment on Avito, priming the XSS.

## Requirements

1. Valid social media account (OK or VK)
2. Crafted malicious URL from prior procedure
3. Victim's browser with no strict security extensions

## Defense

Defensive measures and detection strategies:

- Enforce OAuth redirect URI validation on social providers
- Log and alert on anomalous redirect parameters in auth flows
- Educate users on phishing links leading to login pages

## Objectives

1. Complete authentication without errors
2. Trigger the post-login redirect
3. Maintain the unsanitized 'next' parameter

## Instructions

### Step 1: Visit Malicious URL

**Context**: Direct the victim to the crafted URL to load the login page.

**Instructions**: Open https://www.avito.ru/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert(document.cookie);/ in browser.

> Login prompt should appear with social options.

### Step 2: Select Social Provider

**Context**: Choose a provider to initiate OAuth flow.

**Instructions**: Click 'Login with OK' or 'Login with VK' button.

> Redirects to provider's auth page.

### Step 3: Complete Authentication

**Context**: Authorize on social site to return to Avito.

**Instructions**: Enter credentials and approve access on OK/VK site.

> Browser redirects back to Avito, executing the 'next' parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-auth]]
- [[oauth-redirect]]
