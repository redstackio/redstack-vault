---
tags:
  - hardcoded-credentials
  - source-code-review
  - android
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:41.677Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b9dac0c7-f30e-4747-ae95-035c9a14db13
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Identify-Hardcoded-Credentials-in-Coinbase-Source-Code

## Summary

This procedure involves reviewing the public GitHub repository of the Coinbase Android app to identify and extract hardcoded consumer ID and secret credentials in plaintext, enabling attackers to impersonate the app in OAuth2 flows and gain unauthorized API access without user credentials.

## Description

The Coinbase Android app's source code is hosted publicly on GitHub, where sensitive credentials like the consumer ID and secret are embedded directly in files such as LoginManager.java without obfuscation. This flaw allows any attacker to download the code, locate the credentials at specific lines (e.g., line 49), and use them to register malicious apps or directly call the API, bypassing app-specific restrictions and potentially leading to rate limit abuse or exploitation of app features. The target environment is the app's public repository, requiring no special access beyond internet connectivity. Expected outcomes include obtaining the exact credential values for further exploitation in MITM or impersonation attacks.

## Requirements

1. Internet access to browse GitHub
2. Basic knowledge of Java and Android app structure
3. Text editor or browser to view source files

## Defense

Defensive measures and detection strategies:

- Remove sensitive data from public repositories and use secure secret management (e.g., environment variables or vaults)
- Implement code obfuscation with tools like ProGuard to hide strings and make reverse engineering difficult
- Monitor GitHub for leaked secrets using tools like GitHub's secret scanning or TruffleHog

## Objectives

1. Extract hardcoded consumer ID and secret from public source code
2. Verify credentials appear in API requests for validation
3. Enable impersonation of the app for unauthorized API usage

## Instructions

### Step 1: Access the GitHub Repository

**Context**: Navigate to the Coinbase Android app's public GitHub repository to locate the relevant source file containing credentials.

No specific command; use a web browser to visit https://github.com/coinbase/coinbase-android.

> Browse to the commit bc6a03229416736acc2ea6bc2fb13f55f7029751 and open coinbase-android/src/com/coinbase/api/LoginManager.java.

### Step 2: Locate and Extract Credentials

**Context**: Inspect the LoginManager.java file to find the hardcoded consumer ID and secret in plaintext.

No specific command; scroll to line 49 in the file viewer.

> The credentials will be visible as string literals, e.g., consumer ID: "example_id" and secret: "example_secret". Copy these for use in API calls or further testing.

### Step 3: Validate Credential Usage

**Context**: Confirm the credentials are used in app communications by preparing for API interception (links to next procedure).

No specific command; note the values for integration with tools like Charles Proxy.

> Successful extraction allows direct API authentication as the app, testable via curl or Postman with the extracted ID/secret.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- hardcoded-credentials
- source-code-review
