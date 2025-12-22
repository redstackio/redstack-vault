---
id: proc-uuid-12345
tags:
  - recon
  - swagger-ui
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:33.675Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Swagger-UI-Endpoint-for-External-Configuration

## Summary

This procedure involves accessing and analyzing a Swagger UI instance to identify its support for external API specification loading via the ?configUrl= parameter, setting the stage for potential exploitation in outdated versions.

## Description

In this reconnaissance step, the attacker visits the target Swagger UI hosted on GitHub Pages, such as https://adobedocs.github.io/OAE_PartnerAPI/, and examines the interface. Swagger UI fetches and displays external YAML or JSON files using the ?configUrl= query parameter. In vulnerable outdated versions, this feature lacks proper sanitization, allowing subsequent XSS attacks. The procedure confirms the endpoint's behavior without executing exploits, focusing on understanding the attack surface for authenticated or unauthenticated users.

## Requirements

1. Web browser with developer tools enabled
2. Public access to the target URL
3. Basic knowledge of web applications and query parameters

## Defense

Defensive measures and detection strategies:

- Update Swagger UI to the latest version to patch known vulnerabilities
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor access logs for unusual ?configUrl= parameter usage

## Objectives

1. Confirm presence of Swagger UI and external loading capability
2. Identify version to assess vulnerability status
3. Gather details for crafting targeted payloads

## Instructions

### Step 1: Access the Target Endpoint

**Context**: Navigate to the Swagger UI page to observe its functionality.

Open a web browser and visit https://adobedocs.github.io/OAE_PartnerAPI/. Inspect the page using developer tools (F12) to verify Swagger UI elements and check for the ?configUrl= parameter in the documentation or URL examples.

> Expected output: Swagger UI interface loads, displaying API specs, with references to external config loading.

### Step 2: Test Basic External Loading

**Context**: Verify the parameter's ability to load arbitrary external files without exploitation.

Append a benign URL to the parameter, e.g., https://adobedocs.github.io/OAE_PartnerAPI/?configUrl=https://example.com/api.yaml. Observe if the UI attempts to fetch and render the file.

> Expected output: UI updates with the loaded spec if valid, confirming the feature is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- swagger-ui
- web
