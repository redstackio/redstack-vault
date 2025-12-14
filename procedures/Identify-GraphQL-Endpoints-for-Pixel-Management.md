---
tags:
  - graphql
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/burp-intercept-traffic]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:00.063Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fde5c401-fba5-41f3-b5ea-96749e47601a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-GraphQL-Endpoints-for-Pixel-Management

## Summary

This procedure involves inspecting network traffic in the TikTok Ads portal to identify GraphQL queries responsible for managing Pixel events, revealing the structure and parameters used in event rule operations.

## Description

In the context of testing the TikTok Ads platform, this reconnaissance step uses a web proxy to capture API requests during normal Pixel event management tasks, such as creating or viewing campaigns. The goal is to locate the 'AddRulesToPixelEvents' mutation and understand its input parameters, including object IDs that reference Pixel events. This sets the stage for IDOR exploitation by providing the exact query format. Prerequisites include authenticated access to the portal and a tool for traffic interception. Expected outcomes include a captured payload ready for modification.

## Requirements

1. Authenticated session in TikTok Ads portal
2. Web proxy tool like Burp Suite configured to intercept HTTPS traffic
3. Browser with developer tools enabled for initial verification

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or repeated API probes in web application firewalls (WAF)
- Implement rate limiting on GraphQL endpoints to detect enumeration attempts

## Objectives

1. Capture legitimate GraphQL queries for Pixel management
2. Extract query structure and variable formats
3. Identify potential IDOR entry points in object references

## Instructions

### Step 1: Configure Proxy for Traffic Interception

**Context**: Set up Burp Suite to act as a proxy and capture requests from the TikTok Ads portal.

**Command** ([[commands/burp-intercept-traffic]]):
```bash
# No direct command; configure Burp Suite GUI: Proxy > Intercept > On, set browser proxy to 127.0.0.1:8080
```

> Launch Burp Suite, enable interception, and configure your browser to route traffic through it. Install the Burp CA certificate to handle HTTPS.

### Step 2: Trigger Pixel Management Actions

**Context**: Perform actions in the portal to generate relevant GraphQL requests.

**Instructions**: Log in to TikTok Ads, navigate to a campaign, and add or view Pixel events. Forward intercepted requests in Burp until you see POST requests to the GraphQL endpoint containing 'AddRulesToPixelEvents'.

**Expected Output**: Raw HTTP request with JSON payload, e.g., {"query": "mutation AddRulesToPixelEvents...", "variables": {"input": {"pixelEventId": "your_id"}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/burp-intercept-traffic]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- recon
- web
