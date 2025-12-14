---
tags:
  - csrf
  - request-capture
  - burp
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.998Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: ef12a1d4-01c4-400f-88c1-ed09b7def39e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-and-Analyze-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and analyze a legitimate POST request for changing demographic settings on Glassdoor, extracting key parameters like gdToken for CSRF PoC construction.

## Description

To assess the CSRF vulnerability, intercept the HTTP traffic during a demographic update in the attacker's session. The target endpoint is https://www.glassdoor.com/member/account/settings_changeUserInformation.htm (POST). Parameters include newGender, birthYear, highestEducation, and gdToken, which is tied to the gdId cookie. Analysis reveals token specificity, preventing cross-session reuse. Prerequisites: Burp Suite proxy configured in browser; attacker logged in.

## Requirements

1. Burp Suite Professional with Intercept enabled
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Active attacker session on Glassdoor

## Defense

Defensive measures and detection strategies:

- Enable HTTPS Everywhere and HSTS to complicate interception
- Log proxy-like traffic anomalies (e.g., repeated requests from localhost)
- Use client-side token validation beyond cookies

## Objectives

1. Extract gdToken and form structure
2. Identify CSRF protection mechanisms
3. Validate request parameters for PoC replication

## Instructions

### Step 1: Configure Interception

**Context**: Set up Burp Suite to capture outgoing requests.

Launch Burp Suite, turn on Intercept in the Proxy tab, and configure your browser to route traffic through Burp.

> Expected output: Intercept toggle active; browser traffic paused on requests.

### Step 2: Trigger and Capture Request

**Context**: Perform a settings change to generate the target POST.

In the attacker session, modify demographics (e.g., set gender to FEMALE, birth year to 1940, education to HIGH_SCHOOL) and submit. Intercept the POST request.

> Expected output: Raw request in Burp: POST /member/account/settings_changeUserInformation.htm with body parameters and headers including Cookie: gdId=...; gdToken=...

### Step 3: Analyze in Repeater

**Context**: Forward and inspect the request for token details.

Send the intercepted request to Repeater, examine parameters, and note the gdToken value.

> Expected output: Token appears as a unique string (e.g., eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...); confirm ~10-minute expiration via repeated tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[burp]]
