---
tags:
  - sso
  - http-redirect
  - mitm
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f6b78abe-bcab-404d-909d-b92ef0ee2596
created_at: '2025-12-13T09:01:26.397Z'
updated_at: '2025-12-13T09:01:26.397Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Initiate SSO Redirect to Insecure URL

## Summary

This procedure involves a victim initiating an SSO login on Badoo using Odnoklassniki, which triggers an insecure redirect to an HTTP URL, setting the stage for MITM attacks.

## Description

The attack begins when the victim attempts to log in to Badoo via Odnoklassniki SSO. The redirect to an HTTP endpoint exposes the authentication flow to interception. This is due to a security misconfiguration in the SSO integration, lacking HTTPS enforcement. Expected outcomes include generating interceptable HTTP traffic for further exploitation.

## Requirements

1. Access to Badoo signin page (https://badoo.com/nl/signin/)
2. Victim's interaction to select Odnoklassniki SSO
3. Network conditions allowing MITM (e.g., public WiFi)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS for all redirects in SSO flows
- Monitor for HTTP traffic in authentication endpoints

## Objectives

1. Trigger the insecure redirect
2. Expose OAuth parameters over HTTP
3. Prepare for interception

## Instructions

### Step 1: Navigate to Signin Page

**Context**: Victim accesses the Badoo login page and selects Odnoklassniki.

Visit https://badoo.com/nl/signin/ and choose the Odnoklassniki option.

> This initiates the SSO flow.

### Step 2: Observe Redirect

**Context**: The browser redirects to the insecure URL.

The redirect targets http://www.odnoklassniki.ru/oauth/authorize with parameters like client_id=126351872 and state.

> Traffic is now over HTTP, vulnerable to MITM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[http-redirect]]
