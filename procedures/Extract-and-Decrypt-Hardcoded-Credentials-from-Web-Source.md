---
tags:
  - hardcoded-credentials
  - javascript
  - md5-decrypt
  - web-discovery
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
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:30:18.058Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: fb59c259-a448-493b-b1d6-43319e76639b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-and-Decrypt-Hardcoded-Credentials-from-Web-Source

## Summary

This procedure outlines the steps to discover and extract hardcoded admin credentials embedded in client-side JavaScript code on a web subdomain, including decrypting an MD5-hashed password to reveal plaintext sensitive information that could lead to unauthorized access.

## Description

In this attack scenario, admin credentials are insecurely stored directly in JavaScript source code accessible via the browser's developer tools or page source view. The vulnerability occurs on a public-facing subdomain where the code calls an API like `mobucksApi.placeAd` with embedded `uid` and `passwd` parameters. The username is in plaintext, while the password is MD5-hashed but easily reversible. This exposes credentials for potential abuse in accessing admin panels or client data. Prerequisites include only a standard web browser and public access to the target URL. Expected outcomes are the full set of admin credentials, enabling further exploitation like login attempts on backend systems.

## Requirements

1. Web browser with developer tools (e.g., Chrome, Firefox)
2. Public internet access to the target subdomain
3. Basic knowledge of HTML/JS inspection and MD5 cracking tools (online decoders suffice)

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding credentials in client-side code; use server-side authentication and environment variables
- Obfuscate or encrypt sensitive data if client-side storage is unavoidable, though server-side is preferred
- Implement Content Security Policy (CSP) to restrict script execution and monitor for source code access anomalies
- Regularly scan source code repositories and deployed assets for credential leaks using tools like TruffleHog
- Monitor for unusual login attempts or API calls from exposed credentials

## Objectives

1. Identify and extract hardcoded username and hashed password from public JavaScript
2. Decrypt the MD5 hash to obtain plaintext password
3. Assess potential for unauthorized access to admin functions and client information

## Instructions

### Step 1: Access and Inspect the Subdomain

**Context**: Begin by navigating to the vulnerable subdomain to load the page containing the exposed JavaScript.

No specific command required; use browser navigation.

> Enter the subdomain URL (e.g., redacted as ███) in the browser address bar. The page may redirect, but the source remains accessible.

### Step 2: View Page Source Code

**Context**: Retrieve the full HTML source to access embedded scripts where credentials are hardcoded.

No specific command required; use browser features.

> Press CTRL+U to open the source viewer or prepend `view-source:` to the URL. This displays the raw HTML including inline or linked JavaScript.

### Step 3: Search for Credentials in JavaScript

**Context**: Locate the specific parameters containing the credentials within the script code.

No specific command required; use search functionality.

> Use CTRL+F to search for 'uid' or 'passwd'. In the relevant script, identify `uid: 'mtnng'` and `passwd: 'bd31568138edbfc0552a1ecc6886ea'` in the `window.mobucksApi.placeAd` function call.

### Step 4: Crack the MD5 Hash

**Context**: Convert the exposed MD5 hash to its plaintext equivalent to complete credential recovery.

No specific command required; use an MD5 cracking service.

> Paste the hash 'bd31568138edbfc0552a1ecc6886ea' into an online MD5 decoder (e.g., md5decrypt.net). The tool reveals the original password (redacted as ███ for security).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- hardcoded-credentials
- javascript-exposure
- md5-crack
- web-vuln
