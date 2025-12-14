---
tags:
  - base64
  - payload
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.095Z'
sub_techniques: []
id: ed1d4b4d-3d31-4961-8b8f-1baa736fa445
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Encode-Malicious-URL-in-Base64

## Summary

This procedure encodes a target malicious URL into Base64 format to prepare it for injection into the vulnerable ?feed-stats-url= parameter, bypassing superficial filters in the WordPress Feed Statistics plugin.

## Description

Attackers select a phishing site (e.g., http://www.sooevilsite.com/) and convert it to Base64 (e.g., aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v) using encoding tools. This step is crucial as the plugin decodes the parameter directly for redirects, allowing arbitrary external destinations without restrictions.

## Requirements

1. Target malicious URL (e.g., phishing page)
2. Base64 encoding capability (online tool or browser console)
3. Understanding of URL encoding to ensure compatibility

## Defense

Defensive measures and detection strategies:

- Decode and validate Base64 parameters server-side before redirecting
- Block redirects to non-whitelisted domains
- Log and alert on Base64-decoded URLs containing external hosts

## Objectives

1. Create a valid Base64 payload from malicious URL
2. Ensure payload decodes correctly for redirect
3. Avoid encoding errors that could break the exploit

## Instructions

### Step 1: Select Target URL

**Context**: Choose a malicious site for redirection, such as a phishing page mimicking the legitimate site.

Define the URL: http://www.sooevilsite.com/.

> This URL will host the phishing content to steal credentials or deliver malware.

### Step 2: Perform Base64 Encoding

**Context**: Convert the plain URL to Base64 using a reliable encoder.

Use a browser developer console or online tool: In Firefox console, execute btoa('http://www.sooevilsite.com/') to get aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v.

> Verify by decoding: atob('aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v') should return the original URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- base64
- phishing
