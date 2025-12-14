---
tags:
  - web-proxy
  - traffic-interception
  - sqli-setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.250Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7a3d7ef5-c1d2-47bf-b4a9-eb4f82865c64
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-HTTP-Request-with-Burp-Suite

## Summary

This procedure sets up Burp Suite to intercept HTTP traffic from the target Revive Adserver admin panel, capturing the vulnerable GET request to admin-search.php for further analysis and exploitation.

## Description

In the context of exploiting SQL injection in Revive Adserver v6.0.0, intercepting requests allows identification of the 'keyword' parameter vulnerable due to lack of sanitization. This step uses Burp's proxy to monitor navigation and submission, preparing for payload injection. Prerequisites include a running Burp instance and authenticated access to the admin panel.

## Requirements

1. Burp Suite installed and launched
2. Target Revive Adserver accessible at http://localhost/www/admin/
3. Manager-level authentication credentials

## Defense

Defensive measures and detection strategies:

- Enable web application firewall (WAF) to block proxy traffic patterns
- Monitor for unusual HTTP proxy connections on port 8080
- Use application logging to detect repeated search queries

## Objectives

1. Capture the exact HTTP request structure for SQLMap input
2. Verify the presence of the injectable 'keyword' parameter
3. Prepare for automated exploitation without manual repetition

## Instructions

### Step 1: Launch and Configure Burp Suite

**Context**: Start Burp to enable proxy interception for the built-in browser.

**Instructions**: Open Burp Suite and ensure the proxy listener is active on 127.0.0.1:8080. Configure the browser to use this proxy.

### Step 2: Navigate to Endpoint and Capture

**Context**: Access the vulnerable page and intercept the request during search submission.

**Instructions**: In Burp's browser, go to http://localhost/www/admin/admin-search.php?keyword=test&compact=t. Submit the form to trigger interception in the Proxy > Intercept tab.

### Step 3: Inspect and Forward

**Context**: Review the captured request before forwarding to complete the flow.

**Instructions**: Examine the GET request for the 'keyword' parameter, then forward it to see the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-proxy
- traffic-interception
