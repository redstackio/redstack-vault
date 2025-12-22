---
tags:
  - xxe
  - semrush
  - configuration
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ac18bf47-e651-425e-a3b3-608983112b9d
created_at: '2025-12-13T09:00:33.776Z'
updated_at: '2025-12-13T09:00:33.776Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Site Audit with Malicious Sitemap

## Summary

This procedure configures the Site Audit settings in Semrush to use a malicious sitemap URL, setting the stage for XXE exploitation by providing crafted XML that includes external entities.

## Description

Changing the crawl source to a custom sitemap URL allows the submission of malicious XML. The sitemap is hosted on an attacker-controlled server and designed to coerce the Java XML processor into resolving external entities, such as fetching local files or listing directories. This targets the Semrush web service on Linux. Expected outcomes include acceptance of the URL and preparation for audit triggering.

## Requirements

1. Existing Semrush project with attacker domain
2. Malicious sitemap.xml hosted (e.g., http://static.webhooks.pw/files/semrush_sitemap.xml)
3. Web browser for UI interaction

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Validate and sanitize user-provided sitemap URLs

## Objectives

1. Set crawl source to malicious URL
2. Prepare for XML processing
3. Enable entity resolution exploitation

## Instructions

### Step 1: Access Site Audit Settings

**Context**: Navigate to the audit configuration.

In the Semrush project, go to Site Audit and select to edit settings using [[tools/Firefox]] or [[tools/Google-Chrome]].

> Open the crawl source options.

### Step 2: Enter Malicious Sitemap URL

**Context**: Input the URL of the crafted sitemap.

Select 'Enter sitemap URL' and provide http://static.webhooks.pw/files/semrush_sitemap.xml.

> Save the changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- [[xxe]]
- [[semrush]]
- [[configuration]]
