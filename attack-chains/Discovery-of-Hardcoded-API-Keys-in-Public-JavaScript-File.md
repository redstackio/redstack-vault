---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Discovery of Hardcoded API Keys in Public JavaScript File
type: attack_chain
description: >-
  Multi-stage reconnaissance chain to discover and extract sensitive API keys
  exposed in a publicly accessible minified JavaScript file on a staging web
  application.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.534Z'
procedures:
  - '[[procedures/Browse-Staging-Website-for-Sensitive-Resources]]'
  - '[[procedures/Identify-Sensitive-JavaScript-File-via-Network-Inspection]]'
  - '[[procedures/Extract-API-Keys-from-Minified-JavaScript]]'
techniques:
  - '[[Credentials In Files]]'
tactics:
  - '[[Credential Access]]'
tags:
  - information-disclosure
  - api-keys
  - javascript
  - reconnaissance
platforms:
  - Web
tools:
  - '[[tools/Browser-Network-Inspector]]'
  - '[[tools/JSONParserOnline]]'
complexity: low
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Discovery of Hardcoded API Keys in Public JavaScript File

Multi-stage attack chain demonstrating a complete reconnaissance workflow to identify and extract hardcoded sensitive API keys from a public web resource.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Browse Staging Site] --> B[Inspect Network Resources]
    B --> C[Parse JavaScript for Keys]
    C --> D[Extract Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Network-Inspector]]
- [[tools/JSONParserOnline]]

### Target Environment

- Web platform with publicly accessible staging site
- No specific services/ports required beyond HTTP/HTTPS
- Internet access to the target URL

### Initial Access Requirements

- No credentials needed
- Public network access to staging site
- No prior access required

## Detailed Attack Procedures

### Step 1: Browse Staging Website
procedure: [[procedures/Browse-Staging-Website-for-Sensitive-Resources]]

**Objective**: Access the target staging website and explore for potential sensitive resources using fuzzing or inspection techniques.

**Instructions**: Navigate to the staging site https://staging.empleio.stripo.email in a web browser. Perform JavaScript fuzzing by inspecting loaded resources or using browser developer tools to identify any minified files that may contain embedded data.

**Expected Output**: Identification of potential resource files loaded by the site.

**Success Indicators**:
- Site loads successfully
- Developer tools reveal network activity with JavaScript files

### Step 2: Identify Sensitive JavaScript File
procedure: [[procedures/Identify-Sensitive-JavaScript-File-via-Network-Inspection]]

**Objective**: Use browser tools to locate and access the specific JavaScript file containing sensitive data.

**Instructions**: Open the browser's network inspector while loading the site. Filter for JavaScript files and locate /main.c1965c58f39a0f4aadc3.js. Download or view its contents directly from the network tab.

**Expected Output**: Access to the minified JavaScript file contents.

**Success Indicators**:
- File identified in network requests
- File downloadable without authentication

### Step 3: Extract API Keys
procedure: [[procedures/Extract-API-Keys-from-Minified-JavaScript]]

**Objective**: Parse the JavaScript file to reveal and extract the hardcoded API keys.

**Instructions**: Use an online parser or text search to analyze the file. Search for patterns like 'aviaryApiKey' or 'youtubeApiKey' within the minified code to extract the cleartext credentials.

**Expected Output**: Exposed API keys such as aviaryApiKey and youtubeApiKey.

**Success Indicators**:
- Keys successfully parsed and readable
- Credentials in cleartext format

## Attack Chain Summary

### Key Achievements

1. Discovered publicly exposed JavaScript file on staging site
2. Identified hardcoded sensitive API keys for Aviary and YouTube services
3. Enabled potential unauthorized access to external APIs via disclosed credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]]

### MITRE ATT&CK Tactics

- [[Credential Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
