---
tags:
  - intercept
  - http-proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:12.871Z'
sub_techniques: []
id: aeefbe86-0df9-4c2b-8309-63a597d8cf8c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Phone-Number-Submission-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP request generated when submitting a phone number on the MTN web interface, revealing the vulnerable unauthenticated API endpoint for user data retrieval.

## Description

By proxying browser traffic through Burp Suite and submitting a test phone number, attackers can intercept the request to identify the exact API path and parameters. This targets MTN's web application on WildFly/10, where the endpoint lacks auth checks. Prerequisites include Burp Suite setup; outcomes include the full request details for replay.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp proxy (127.0.0.1:8080)
3. Access to the vulnerable web page from previous procedure

## Defense

Defensive measures and detection strategies:

- Encrypt internal API calls with TLS and monitor for proxy interception attempts
- Log all HTTP requests and alert on unusual User-Agent or proxy headers
- Deploy client-side certificate pinning to detect proxy usage

## Objectives

1. Capture the outgoing request during phone number submission
2. Identify the API endpoint structure
3. Prepare request for modification and replay

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up Burp to intercept traffic from the browser.

In Burp Suite, go to Proxy > Options and ensure Intercept is on. Install Burp's CA certificate in the browser if needed.

> Browser traffic now routes through Burp.

### Step 2: Submit Phone Number and Intercept

**Context**: Enter and submit a valid MTN phone number to trigger the request.

On the web page, input a number (e.g., 07012345678) and submit. In Burp Proxy > Intercept, capture the request.

> Expected: GET request to /vtu-service/api/pwa/pub/get-bio-data/{phone_number} with headers like Accept: application/json.

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

- [[intercept]]
- [[http-proxy]]
