---
id: uuid-detect-dangling
tags:
  - subdomain-takeover
  - recon
  - piwik-cloud
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
updated_at: '2025-12-14T05:32:31.157Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Detect Dangling Piwik Subdomain

## Summary

This procedure identifies unmanaged or dangling subdomains on Piwik Cloud by accessing the subdomain URL and checking for availability indicators, which signals potential for takeover.

## Description

In scenarios where a service like Gratipay stops using Piwik analytics but leaves JavaScript embeds pointing to a Piwik subdomain, the subdomain becomes dangling if not properly deleted. This procedure involves directly visiting the subdomain to observe if Piwik Cloud displays it as available for registration, exploiting the misconfiguration for reconnaissance in a takeover attack. Expected outcomes include confirmation of availability, setting the stage for account creation and claiming.

## Requirements

1. Web browser with internet access
2. Knowledge of the target subdomain (e.g., derived from JavaScript embeds on the parent site)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Regularly audit and delete unused analytics subdomains on third-party services like Piwik Cloud
- Monitor DNS records for dangling CNAMEs pointing to unused providers
- Implement subdomain monitoring tools to alert on availability signals

## Objectives

1. Confirm subdomain availability for takeover
2. Gather evidence of misconfiguration
3. Prepare for subsequent claiming steps

## Instructions

### Step 1: Access Target Subdomain

**Context**: Visit the suspected dangling subdomain to check for Piwik Cloud's availability message.

No specific command required; use a web browser.

> Navigate to https://<subdomain>.piwik.pro/ (e.g., https://gratipay.piwik.pro/). Look for text indicating availability.

### Step 2: Validate Availability

**Context**: Confirm the message explicitly states the subdomain is free for use.

No command; manual inspection.

> Expected: Message like "THIS SUBDOMAIN IS AVAILABLE! <subdomain> is available! Use this subdomain for your Piwik Cloud service."

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[recon]]
