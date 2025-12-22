---
tags:
  - reconnaissance
  - wordpress
  - version-identification
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
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:14.124Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b755418c-7f18-48aa-8180-132b2f25df6a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Outdated-WordPress-Version

## Summary

This procedure involves inspecting a target WordPress site to determine its version, identifying if it's outdated and potentially vulnerable to known exploits like XSS in MediaElement.js.

## Description

In an attack scenario targeting web applications, the first step is reconnaissance to gather information on the software stack. For WordPress sites, version details are often exposed in page source, meta tags, or HTTP headers. This procedure uses browser developer tools to extract this data without any specialized tools, confirming versions below 4.5.2 as vulnerable to reflected XSS via MediaElement.js. Expected outcomes include version confirmation, enabling further vulnerability research.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome, Firefox)
2. Direct HTTP/HTTPS access to the target site
3. Basic knowledge of HTML inspection

## Defense

Defensive measures and detection strategies:

- Remove or obscure WordPress version from meta generators and headers using plugins like Remove WP Version
- Implement Web Application Firewall (WAF) to block reconnaissance probes
- Regularly audit and update WordPress core and plugins

## Objectives

1. Confirm the target runs WordPress and identify its exact version
2. Determine if the version is outdated (e.g., < 4.5.2)
3. Gather evidence for subsequent vulnerability targeting

## Instructions

### Step 1: Access the Target Site

**Context**: Navigate to the suspected WordPress site to begin inspection.

Open the site in your browser and load the homepage or any public page.

### Step 2: Inspect Page Source

**Context**: Examine the HTML source for version indicators.

Right-click on the page and select "View Page Source" or use Ctrl+U. Search for keywords like "generator", "wp-content", or "wp-includes".

Look for:

```html
<meta name="generator" content="WordPress 4.2.4" />
<!-- or -->
<script src="/wp-includes/js/mediaelement/mediaelement.js?ver=4.2.4"></script>
```

> This reveals the version directly. If not found, proceed to network inspection.

### Step 3: Check Network Requests

**Context**: Use developer tools to inspect loaded resources for version info.

Open Developer Tools (F12), go to the Network tab, and reload the page. Filter for JS or CSS files from /wp-includes/ and check the URL parameters for "ver=".

**Expected Output**: Version string like "4.2.4" in resource URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[wordpress]]
- [[version-identification]]
