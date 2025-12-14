---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - recon
  - url-injection
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
updated_at: '2025-12-14T17:26:06.110Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Vulnerable URL Path on smarthistory.khanacademy.org

## Summary

This procedure involves reconnaissance to identify the lack of input sanitization in the URL path suffix of the smarthistory.khanacademy.org subdomain, setting the stage for reflected XSS exploitation.

## Description

The smarthistory.khanacademy.org site fails to encode or validate URL path components, particularly suffixes after legitimate paths like '/Campin'. This allows attackers to inject HTML and JavaScript by appending payloads that break out of expected contexts. The procedure targets public-facing web pages to probe for reflection without authentication.

## Requirements

1. Web browser for manual testing
2. Public access to http://smarthistory.khanacademy.org/
3. Basic knowledge of HTML and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement strict URL path validation and encoding (e.g., using OWASP guidelines)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor access logs for anomalous URL patterns with script tags

## Objectives

1. Confirm unsanitized reflection of path suffixes
2. Identify injection points after legitimate resources
3. Validate potential for XSS without triggering alerts

## Instructions

### Step 1: Navigate to Legitimate Paths

**Context**: Access standard pages to understand the URL structure and response handling.

Visit http://smarthistory.khanacademy.org/Campin in a browser and inspect the page source (right-click > View Page Source).

> Look for how the URL path is reflected in HTML attributes or content.

### Step 2: Test for Sanitization Gaps

**Context**: Append test characters to probe for breakout opportunities.

Modify the URL to http://smarthistory.khanacademy.org/Campin"> and reload. Check if the closing quote appears unescaped in the HTML.

> Expected output: The page loads with the injected "> reflected, indicating poor encoding.

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
- [[web]]

