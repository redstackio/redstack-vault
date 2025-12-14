---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Identify-GraphQL-Endpoint-in-Content-Outline-Builder
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.686Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - graphql
  - recon
  - web
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify-GraphQL-Endpoint-in-Content-Outline-Builder

## Summary

This procedure involves inspecting network traffic in Semrush's Content Outline Builder to identify the GraphQL endpoint responsible for handling user data requests, setting the stage for vulnerability exploitation.

## Description

In the context of testing Semrush's web application, this procedure uses browser tools or proxies to observe GraphQL requests triggered by user interactions. The target environment is the Content Outline Builder product, where GraphQL is used for querying user information. Expected outcomes include capturing the endpoint URL and query structure, revealing parameters like `userId` that can be manipulated later. Prerequisites include a valid authenticated session.

## Requirements

1. Authenticated access to Semrush Content Outline Builder
2. Browser with developer tools or a proxy like Burp Suite
3. Network connectivity to Semrush's domain

## Defense

Defensive measures and detection strategies:

- Implement request logging at the API gateway to monitor GraphQL query patterns
- Use web application firewalls (WAF) to detect anomalous endpoint probing
- Enforce rate limiting on GraphQL endpoints to hinder reconnaissance

## Objectives

1. Locate the GraphQL API endpoint for user data
2. Document the query structure and variables
3. Confirm the presence of manipulable parameters like userId

## Instructions

### Step 1: Authenticate and Interact

**Context**: Establish a session and trigger user data requests to capture traffic.

Log in to the Content Outline Builder and navigate to a feature that loads user profile or content data, such as viewing your outlines.

Open browser developer tools (Network tab) or configure Burp Suite as a proxy.

**Expected Output**: Network requests filtered to show POST to GraphQL endpoint.

### Step 2: Analyze Request Structure

**Context**: Examine the captured GraphQL query to understand its components.

Inspect the request payload for the query/mutation, variables (e.g., {"userId": "your_id"}), and headers like Authorization.

Note the endpoint, typically `/api/graphql` or similar.

**Expected Output**: JSON payload with user data fields in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql]]
- [[recon]]
- [[web]]
