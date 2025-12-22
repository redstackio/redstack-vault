---
id: proc-navigate-intercept-001
tags:
  - web
  - recon
  - proxy-intercept
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:05.346Z'
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
# Navigate to Pages Section and Intercept Request

## Summary

This procedure involves navigating to the pages management section in the Acronis admin panel and intercepting the search API request to analyze its structure for potential vulnerabilities.

## Description

Once inside the admin panel, the pages section handles dashboard content indexing via a search feature. Intercepting the GET request to /api/admin/pages reveals the 'search' parameter, which interacts with the backend database. This step uses a proxy tool to capture traffic, enabling manual testing in a Laravel-based PHP application environment.

## Requirements

1. Active admin session
2. Proxy tool configured (e.g., Burp Suite) to intercept browser traffic
3. Network access to dev.acronis.host API

## Defense

Defensive measures and detection strategies:

- Encrypt API traffic with HTTPS and validate certificates
- Log all API requests and monitor for proxy-like User-Agents
- Rate-limit search queries to prevent abuse

## Objectives

1. Capture the exact API request format
2. Identify parameters for injection testing
3. Prepare for vulnerability confirmation

## Instructions

### Step 1: Access Pages Section

**Context**: Load the pages management interface to trigger search functionality.

Manually navigate to https://admin.acronis.host/#/pages and input a search term (e.g., '*') in the search bar.

> The interface indexes pages, sending a request to the backend.

### Step 2: Intercept the Request

**Context**: Use a proxy to capture the outgoing API call.

With proxy active, observe the GET request: /api/admin/pages?page=1&limit=100&sort=%2Btype&filter=%7B%7D&search=* to dev.acronis.host.

> Request details saved in proxy history for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- recon
