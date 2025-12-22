---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - link-rendering
  - trusted-domains
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.357Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Default-Target-Blank-on-Trusted-Links

## Summary

This procedure examines how HackerOne renders default links to trusted domains, revealing the use of target='_blank' without rel='noopener' for UX improvements, creating an exploitable gap.

## Description

By embedding links to domains like YouTube in Markdown, observe the rendered attributes. HackerOne applies target='_blank' to bypass interstitial warnings for trusted sites, but omits rel='noopener', allowing potential window.opener access. This targets the web platform's Markdown parser; outcomes confirm the vulnerability for social engineering exploitation.

## Requirements

1. HackerOne account for embedding links
2. Example trusted URL (e.g., YouTube video)
3. Browser inspector for attribute verification

## Defense

Defensive measures and detection strategies:

- Add rel='noopener' to all target='_blank' links, even for trusted domains
- Implement client-side checks for window.opener usage
- Log link clicks and monitor for anomalous navigation

## Objectives

1. Confirm default target='_blank' application
2. Verify absence of rel='noopener'
3. Document UX-driven security trade-offs

## Instructions

### Step 1: Embed Trusted Link

**Context**: Insert a Markdown link to a trusted domain in a report or comment.

Input: [YouTube Video](https://www.youtube.com/watch?v=78Q2B_td-fs)

> The link renders with target='_blank' to enhance UX by avoiding interstitials.

### Step 2: Inspect Attributes

**Context**: Analyze the HTML to check for security attributes.

Inspect the <a> tag; look for target='_blank' and absence of rel='noopener' or noreferrer.

> Expected output: <a href="..." target="_blank"> without rel='noopener', confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[link-rendering]]
- [[trusted-domains]]
- [[xss]]
