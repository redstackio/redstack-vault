---
tags:
  - dos
  - impact-assessment
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7f69c191-6b35-418f-bdc6-706e915d3b03
created_at: '2025-12-13T09:00:34.725Z'
updated_at: '2025-12-13T09:00:34.725Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Observe Denial of Service Impact

## Summary

This procedure involves accessing the poisoned site to observe the Denial of Service effects, where resources fail to load due to invalid ports in cached links, rendering the site unusable.

## Description

Once the cache is poisoned, end users experience broken functionality as links to assets include closed ports (e.g., :1337), causing connection failures. This step validates the real-world impact without additional tools.

## Requirements

1. Confirmed cache poisoning
2. Web browser or HTTP client
3. Access to the target site

## Defense

Defensive measures and detection strategies:

- Implement port validation in URL generation
- Monitor for DoS patterns like failed resource loads

## Objectives

1. Validate DoS on users
2. Assess site breakage
3. Document impact

## Instructions

### Step 1: Access the Site

**Context**: Visit the homepage and inspect resource loading.

No specific command; use a browser to navigate to https://themes.shopify.com and check developer console for errors on URLs like https://themes.shopify.com:1337/.

> Expect failures on images, CSS, and other assets due to the closed port.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- dos
- impact-assessment
