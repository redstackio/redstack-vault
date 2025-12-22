---
tags:
  - xss
  - stored-xss
  - injection
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3fd9cebe-a774-473e-860c-17a1a7f3f65c
created_at: '2025-12-14T00:11:16.751Z'
updated_at: '2025-12-14T00:11:16.751Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Shopify Staff Name Field

## Summary

This procedure involves manually injecting a stored XSS payload into the staff name field of a Shopify test store using Burp Suite to intercept and modify POST requests, setting the stage for later execution in sensitive contexts.

## Description

The procedure targets insufficient sanitization in Shopify's staff management, allowing user-inputted data to be stored and potentially rendered without proper escaping. This was demonstrated on a test store like trstore-3.myshopify.com, where the payload persists and can execute in internal panels. Expected outcomes include successful storage and potential for arbitrary script execution leading to data compromise.

## Requirements

1. Access to a Shopify account for creating a test store
2. Burp Suite installed and configured for request interception
3. Basic knowledge of web requests and XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-controlled fields
- Monitor for unexpected script executions in admin panels using CSP and logging

## Objectives

1. Store malicious XSS payload in staff name field
2. Prepare for execution in internal contexts
3. Demonstrate vulnerability for reporting or exploitation

## Instructions

### Step 1: Set Up Test Store and Intercept Requests

**Context**: Create a test store and use Burp Suite to monitor traffic.

Configure Burp Suite to proxy requests to the Shopify staff management endpoint. Navigate to the staff creation page in the test store (e.g., trstore-3.myshopify.com).

> This step prepares the environment for injection.

### Step 2: Inject XSS Payload via POST Request

**Context**: Modify the intercepted POST request to include the XSS payload.

In Burp Suite, intercept the POST request to the staff name field and replace the name value with an XSS payload like '<script>alert(1)</script>'.

> The modified request stores the payload without immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[stored-xss]]
