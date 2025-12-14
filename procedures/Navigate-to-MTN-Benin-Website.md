---
tags:
  - recon
  - web-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:49.896Z'
sub_techniques: []
id: d62f688f-ef4d-4fd0-998b-01131fa909db
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
---
# Navigate to MTN Benin Website

## Summary

This procedure involves accessing the target MTN Benin website to establish initial contact with the attack surface, setting the stage for vulnerability exploration in the Messages section.

## Description

In a reflected XSS attack scenario, the first step is to navigate to the vulnerable website using a standard web browser. The target is https://www.mtn.bj/, a public-facing site without authentication barriers. This step confirms accessibility and loads the necessary pages for subsequent exploitation. Expected outcomes include successful page rendering, allowing progression to feature-specific navigation.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connectivity to reach public websites
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor access patterns
- Log and monitor unusual traffic to the homepage from reconnaissance tools

## Objectives

1. Confirm site accessibility for exploitation
2. Load the environment for further navigation
3. Identify any immediate access controls

## Instructions

### Step 1: Open Web Browser and Access URL

**Context**: Launch a browser and directly visit the target to verify public access.

No specific command required; manually enter the URL in the browser address bar.

> Manually navigate to `https://www.mtn.bj/`. The page should load without errors, displaying the MTN Benin homepage.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web-access]]
