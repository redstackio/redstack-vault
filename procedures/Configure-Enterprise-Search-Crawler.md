---
tags:
  - crawler-config
  - xxe
type: procedure
tools:
  - '[[tools/Enterprise-Search-UI]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 94717ad8-839e-4149-8f7f-36f261fa92ec
created_at: '2025-12-13T09:00:27.301Z'
updated_at: '2025-12-13T09:00:27.301Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Enterprise Search Crawler

## Summary

This procedure configures the Elastic Enterprise Search web crawler to target a malicious domain, triggering the parsing of vulnerable sitemap files.

## Description

By setting up a new engine in the Enterprise Search UI and enabling the web crawler with the attacker's domain, the crawler will fetch and parse the malicious sitemap.xml, leading to XXE exploitation. This requires administrative access to the UI.

## Requirements

1. Access to Enterprise Search UI
2. Valid credentials for engine creation
3. Attacker's domain URL

## Defense

Defensive measures and detection strategies:

- Validate and restrict domains for crawling
- Monitor crawler logs for errors or unusual activity

## Objectives

1. Initiate crawl on malicious domain
2. Trigger XXE via sitemap parsing
3. Enable data exfiltration

## Instructions

### Step 1: Create Engine and Enable Crawler

**Context**: Use the UI to set up crawling.

Log into Enterprise Search, create an engine, enable web crawler, enter the attacker's domain URL, and start the crawl.

> No specific command; UI-based configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Enterprise-Search-UI]]

## Tags

- [[crawler-config]]
- [[xxe]]
