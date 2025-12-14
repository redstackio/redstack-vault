---
tags:
  - burp-suite
  - extension-install
type: procedure
tools:
  - '[[tools/Copy-as-Node-Request]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Java
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:53.865Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7804836d-a22c-47be-8a2f-b1c37fdc7f90
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Copy-as-Node-Request-Extension

## Summary

This procedure installs the vulnerable 'Copy as Node Request' Burp Suite extension, which enables copying HTTP requests as executable Node.js code but suffers from improper cookie sanitization leading to code injection.

## Description

The 'Copy as Node Request' extension is a BApp that generates Node.js code from intercepted Burp requests. Due to a flaw in its escapeQuotes function (lines 165-167 in BurpExtender.java), single quotes in cookie values are not escaped, allowing injection when the code is executed. This procedure sets up the environment for exploitation by installing the extension from the official BApp Store.

## Requirements

1. Burp Suite installed (Professional or Community)
2. Internet access to download from PortSwigger BApp Store
3. Java runtime for Burp Suite

## Defense

Defensive measures and detection strategies:

- Review and audit Burp extensions before installation
- Use updated versions of extensions or disable untrusted ones
- Monitor for anomalous Node.js executions post-Burp usage

## Objectives

1. Install the extension to access the vulnerable functionality
2. Verify extension loads without errors
3. Prepare for request interception and code generation

## Instructions

### Step 1: Access BApp Store

**Context**: Navigate to the extension's download page in Burp Suite.

**Instructions**: In Burp Suite, go to the Extender tab > BApp Store, search for 'Copy as Node Request', and click Install.

> Alternatively, download manually from https://portswigger.net/bappstore/e170472f83ef4da1bca5897203b6b33d and load via Extender > Extensions > Add.

### Step 2: Verify Installation

**Context**: Confirm the extension is active and functional.

**Instructions**: Check the Extensions tab for 'Copy as Node Request' listed as loaded.

> Test by intercepting a simple request and attempting to copy as Node.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Software

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Copy-as-Node-Request]]
- [[tools/Burp-Suite]]

## Tags

- burp-suite
- extension-install
