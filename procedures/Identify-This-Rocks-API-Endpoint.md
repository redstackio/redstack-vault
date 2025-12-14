---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify-This-Rocks-API-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.939Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Active Scanning]]'
tags:
  - recon
  - api
  - web
platforms:
  - Web
tools: []
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify-This-Rocks-API-Endpoint

## Summary

This procedure involves inspecting network traffic on Rockstar Games' Social Club site to identify the API endpoint responsible for the 'This Rocks' button functionality, revealing its intended one-time invocation per user per item.

## Description

In the context of exploiting a race condition, the first step is to understand the backend API. The 'This Rocks' button sends a POST request to an endpoint like `/api/v1/rocks/create`, including authentication tokens and item IDs. Lack of proper synchronization allows concurrent calls to succeed multiple times. Prerequisites include an authenticated session on the site and browser developer tools or a proxy.

## Requirements

1. Authenticated access to Social Club site
2. Browser with developer tools (e.g., Chrome DevTools)
3. Target post or item to interact with

## Defense

Defensive measures and detection strategies:

- Implement API rate limiting per user and endpoint
- Log all API invocations with timestamps for anomaly detection
- Use mutex locks or database transactions to enforce single invocation

## Objectives

1. Locate the exact API endpoint and request format
2. Confirm the one-time limit mechanism (e.g., via response or database check)
3. Prepare for replay testing

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Open the browser's developer tools to monitor network requests while interacting with the button.

No specific command; use browser UI:

1. Log in to Social Club.
2. Navigate to a post and open DevTools (F12) > Network tab.
3. Click 'This Rocks' and filter for XHR/Fetch requests.

> Identify the POST request to the API endpoint, note headers (e.g., Authorization Bearer token) and payload (e.g., {"item_id": "123"}). Expected output: Endpoint URL and sample request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[api]]
- [[web]]
