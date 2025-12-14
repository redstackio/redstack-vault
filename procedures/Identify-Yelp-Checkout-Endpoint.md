---
id: proc-yelp-identify-endpoint-001
tags:
  - recon
  - web
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:48.208Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Yelp-Checkout-Endpoint

## Summary

This procedure outlines how to locate the /checkout/transaction_platform endpoint in Yelp's web platform used for processing food orders via Grubhub integration, serving as the initial reconnaissance step for identifying potential vulnerabilities in the checkout flow.

## Description

In the context of testing Yelp's food ordering system, this procedure involves simulating a user checkout to capture and analyze network traffic. The target environment is Yelp's web application, which lacks specific protections against endpoint enumeration in this case. Expected outcomes include confirming the endpoint URL and its key parameters, such as credit_card_id, enabling further vulnerability assessment.

## Requirements

1. Valid Yelp user account with access to food ordering features
2. Web browser with developer tools enabled (e.g., Chrome Network tab)
3. Optional: Intercepting proxy like Burp Suite for detailed request logging

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on checkout endpoints to detect enumeration attempts
- Use web application firewalls (WAF) to monitor unusual network inspection patterns
- Log and alert on repeated checkout initiations from the same IP

## Objectives

1. Locate the transaction processing endpoint
2. Document request parameters for subsequent testing
3. Establish baseline for IDOR assessment

## Instructions

### Step 1: Initiate Checkout Flow

**Context**: Start the food ordering process to trigger the relevant endpoint.

Log in to Yelp and select a Grubhub-integrated restaurant. Add items to cart and proceed to checkout. Open browser developer tools (F12) and navigate to the Network tab to monitor requests.

### Step 2: Capture Endpoint Request

**Context**: Identify the specific API call for transaction processing.

Complete the initial checkout steps until the payment selection. Filter network logs for POST requests to paths containing '/checkout'. Locate the /checkout/transaction_platform request and inspect its payload for parameters like credit_card_id.

**Expected Output**: Full request details, including URL, method (POST), and form data with your credit_card_id.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[endpoint-discovery]]
