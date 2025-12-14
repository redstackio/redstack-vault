---
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-search-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
id: 2c43d162-3b27-488e-a274-1448896457fc
created_at: '2025-12-14T03:46:31.611Z'
updated_at: '2025-12-14T03:46:31.611Z'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Reflected XSS in siteBaseUrl Parameter

## Summary

This procedure involves probing the /searchasyoutype/v1/search endpoint on openapi.starbucks.com to identify reflection of the siteBaseUrl parameter in HTML without proper sanitization, setting the stage for XSS exploitation.

## Description

In a web vulnerability assessment, access the search endpoint with sample parameters to observe how user input in siteBaseUrl is handled. The parameter is reflected directly into an HTML href attribute without encoding, allowing potential context breakout via newline injection. This is a reconnaissance step to confirm the vulnerability before payload crafting. Expected outcomes include viewing the raw input in the page source, indicating insufficient output encoding.

## Requirements

1. Public access to https://openapi.starbucks.com
2. Basic knowledge of HTTP requests and HTML inspection
3. Optional API key for the x-api-key header (may be required for full access)

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Sanitize and encode all user inputs in URL contexts using HTML entity encoding
- Monitor for anomalous requests to search endpoints with unusual parameters

## Objectives

1. Confirm parameter reflection in response
2. Identify context (e.g., href attribute) for payload design
3. Establish baseline for exploitation testing

## Instructions

### Step 1: Send Test Request to Endpoint

**Context**: Craft a simple GET request to the endpoint with benign parameters to inspect the response.

**Command** ([[commands/curl-access-search-endpoint]]):
```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://example.com" --header "x-api-key: YOUR_API_KEY"
```

> This command sends a GET request (using -G for query params) and outputs the HTML response. Pipe to | grep siteBaseUrl to spot reflection. Expected output: HTML snippet like <a href="http://example.com">, showing direct insertion.

### Step 2: Inspect Response in Browser

**Context**: Load the URL in a browser to view rendered HTML and source.

**Command** (Manual Browser Access):

Open https://openapi.starbucks.com/searchasyoutype/v1/search?query=coffee&siteBaseUrl=http://example.com in browser, then view page source (Ctrl+U).

> Look for unsanitized siteBaseUrl in attributes. Success if no encoding (e.g., no &amp; for &).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/curl-access-search-endpoint]]

## Tools Used

-

## Tags

- [[xss]]
- [[recon]]
- [[web]]
