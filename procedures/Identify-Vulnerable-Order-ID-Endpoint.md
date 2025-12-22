---
tags:
  - recon
  - web
  - endpoint-discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5d752584-e018-4cb2-ad77-8f3c2f1946cf
created_at: '2025-12-14T03:15:30.585Z'
updated_at: '2025-12-14T03:15:30.585Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Order-ID-Endpoint

## Summary

This procedure involves locating web endpoints on a target application, such as Zomato's order API, that accept the order_id parameter for querying database records, setting the stage for injection testing.

## Description

In a typical e-commerce or food delivery platform like Zomato, order details are fetched via API endpoints using parameters like order_id. This procedure uses traffic interception to map these endpoints and confirm parameter usage. The target environment is a public-facing web application with a SQL backend. Prerequisites include network access to the site and a proxy tool. Expected outcomes include the full URL and parameter context for further exploitation.

## Requirements

1. Proxy tool like Burp Suite for traffic interception
2. Valid order_id value from a legitimate request (e.g., from browsing orders)
3. Internet access to the target domain (www.zomato.com)

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to log unusual endpoint access patterns
- Use parameter whitelisting to restrict order_id to numeric values only

## Objectives

1. Discover the exact endpoint handling order_id queries
2. Verify parameter is user-controlled and reaches the database
3. Establish baseline response for anomaly detection

## Instructions

### Step 1: Intercept Legitimate Traffic

**Context**: Browse the target site to trigger order-related requests and capture them.

Use Burp Suite proxy to monitor HTTP traffic while navigating to an order page.

**Expected Output**: Captured GET or POST request with order_id parameter.

### Step 2: Analyze Parameter Usage

**Context**: Examine the request to confirm order_id is in the query string or body.

In Burp Repeater, resend the request and note the endpoint path (e.g., /api/v1/orders/{order_id}).

**Expected Output**: Valid order details in response JSON or HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[web]]
