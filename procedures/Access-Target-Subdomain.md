---
id: proc-uuid-001
tags:
  - recon
  - web-access
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:32.125Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Target-Subdomain

## Summary

This procedure involves navigating to a target web subdomain to establish initial access and confirm the presence of vulnerable software like Tableau on a U.S. Department of Defense site.

## Description

In the context of exploiting web vulnerabilities, the first step is to access the public-facing subdomain. For this attack on a DoD site using Tableau, simply loading the URL in a browser reveals the environment. No advanced tools are needed, but caution is advised due to the sensitive nature of government infrastructure. Prerequisites include internet access and knowledge of the subdomain URL (e.g., https://██████.dod.mil/).

## Requirements

1. Web browser with developer tools enabled
2. Public internet access to the target subdomain
3. Basic understanding of web navigation

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual access patterns
- Log all inbound requests to subdomains and alert on reconnaissance-like behavior

## Objectives

1. Confirm subdomain accessibility and load Tableau interfaces
2. Gather initial observations for further exploitation
3. Establish baseline for vulnerability probing

## Instructions

### Step 1: Navigate to Subdomain

**Context**: Directly access the target to verify it's online and hosting Tableau.

Open your web browser and enter the subdomain URL (e.g., https://██████.dod.mil/).

> Load the page and inspect for Tableau-specific elements like login prompts or dashboard previews. If the page loads without errors, the access is successful.

### Step 2: Observe Environment

**Context**: Scan for indicators of Tableau deployment.

Use browser developer tools (F12) to inspect network requests and page source for Tableau-related paths or scripts.

> Look for references to /en/ or authentication endpoints. Successful observation confirms the target environment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
