---
id: proc-uuid-1
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.414Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Search

## Summary

This procedure outlines how to inject a malicious JavaScript payload into the Moneybird web application's search functionality for 'Incoming (Manual Journal)', exploiting inadequate input sanitization in the JavaScript module to store the payload for later execution.

## Description

In the Moneybird application, the search feature for manual journals processes user inputs without proper escaping or validation, allowing stored XSS. An attacker with authenticated access can submit a payload that gets persisted in the application's data store or session. When another user (or the same user) views the search results, the payload is rendered into the DOM via the JavaScript module, executing in the browser context. This can steal cookies, keystrokes, or redirect users. The vulnerability was identified through manual testing of the search interface.

## Requirements

1. Valid authenticated session in Moneybird (user credentials required)
2. Web browser with developer console access
3. Knowledge of basic JavaScript payloads for testing

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript errors or unexpected DOM manipulations in browser logs

## Objectives

1. Store malicious payload in the search results data
2. Ensure payload persists without immediate detection
3. Set up for execution upon viewing affected content

## Instructions

### Step 1: Authenticate to Application

**Context**: Establish a valid session to access the vulnerable search functionality.

Log in to Moneybird at https://my.moneybird.com using provided credentials. Verify successful login by accessing the dashboard.

### Step 2: Navigate to Vulnerable Search

**Context**: Locate the search interface for Incoming Manual Journals where the JavaScript module handles inputs.

From the main menu, navigate to the 'Incoming' section and select 'Manual Journal'. Initiate a search query.

### Step 3: Submit Malicious Payload

**Context**: Inject the XSS payload into the search field to exploit the lack of sanitization.

Enter the following payload in the search box: `<script>alert('XSS Exploited')</script>`. Submit the search.

> The input is processed by the JavaScript module without encoding, storing the raw HTML/JS in the results data.

**Expected Output**: Search results load, potentially displaying the injected content unescaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
