---
id: proc-uuid-1
tags:
  - recon
  - endpoint-discovery
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-endpoint-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:47.297Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Zomato Instagram Tag Relay Endpoint

## Summary

This procedure identifies the vulnerable https://www.zomato.com/php/instagram_tag_relay endpoint by examining Zomato's web structure and testing parameter reflection, setting the stage for XSS exploitation.

## Description

In the context of penetration testing Zomato's web application, this step involves reconnaissance to locate endpoints related to Instagram integration. The 'callback' parameter in GET and POST requests to this PHP endpoint is directly reflected without sanitization, enabling subsequent XSS attacks. Prerequisites include public internet access; no authentication is needed initially.

## Requirements

1. Access to a web browser or curl for testing
2. Knowledge of Zomato's domain and Instagram features
3. Optional: Proxy tool like Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block suspicious parameter values
- Log and monitor requests to internal endpoints like /php/
- Enforce Content Security Policy (CSP) to restrict script execution

## Objectives

1. Locate the instagram_tag_relay endpoint
2. Confirm reflection of 'callback' parameter
3. Validate vulnerability for further exploitation

## Instructions

### Step 1: Examine Zomato Site for Endpoints

**Context**: Use browser dev tools or manual navigation to find Instagram-related URLs.

Search for links or API calls involving Instagram tags on Zomato pages.

**Expected Output**: Discovery of https://www.zomato.com/php/instagram_tag_relay.

### Step 2: Test Basic Reflection

**Context**: Send a simple request to check if 'callback' echoes back unsanitized.

Execute [[commands/curl-basic-endpoint-test]] to probe the endpoint:

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=test"
```

> This command sends a GET request; look for 'test' in the response body without escaping.

**Expected Output**: Response containing the raw 'test' value, indicating lack of sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-endpoint-test]]

## Tools Used


## Tags

- recon
- endpoint-discovery
