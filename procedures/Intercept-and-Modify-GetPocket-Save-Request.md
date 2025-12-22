---
tags:
  - ssrf
  - intercept
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:09.040Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b955e8e8-776b-4ddd-8ac4-46a74a504904
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Intercept and Modify GetPocket Save Request

## Summary

This procedure details intercepting and modifying HTTP requests in the GetPocket save feature using Burp Suite to facilitate SSRF exploitation by altering localhost URLs for port probing.

## Description

As part of the SSRF attack, requests to save URLs are intercepted via a proxy tool like Burp Suite. The URL parameter is modified to target internal localhost ports, allowing replay and observation of server responses that differ based on port status. This enables blind scanning without direct network access.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Authenticated session in GetPocket
3. Basic understanding of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Enable HTTPS and certificate pinning to hinder proxy interception
- Log and alert on modified requests in application logs
- Use client-side validation for URLs before submission

## Objectives

1. Capture save requests for SSRF payload injection
2. Enable port-specific modifications for scanning
3. Validate SSRF trigger through response analysis

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for GetPocket traffic.

In Burp Suite, configure the proxy listener on port 8080 and set your browser to use it (e.g., via FoxyProxy extension).

### Step 2: Intercept Save Request

**Context**: Capture the submission of a localhost URL.

Submit `https://127.0.0.1:1/` via the save plus icon. Intercept in Burp Proxy and forward to Repeater.

### Step 3: Modify and Replay

**Context**: Change port and observe responses.

Edit the URL to `https://127.0.0.1:22/` in Repeater and send. Repeat for other ports, comparing lengths.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- modify-request
- burp
- ssrf
