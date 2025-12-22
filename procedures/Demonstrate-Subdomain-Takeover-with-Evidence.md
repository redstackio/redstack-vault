---
tags:
  - subdomain-takeover
  - poc
  - evidence
type: procedure
tools: []
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
id: 1bfd0a7f-772a-4c62-b682-e0eea961cf33
created_at: '2025-12-14T04:51:10.891Z'
updated_at: '2025-12-14T04:51:10.891Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Subdomain Takeover with Evidence

## Summary

This procedure captures and documents proof of the subdomain takeover, including screenshots and videos, to validate the vulnerability for disclosure or reporting.

## Description

To demonstrate impact, the attacker records the controlled subdomain's state. This involves accessing the URL post-configuration, capturing visuals of the PoC content, and optionally showing the transition from unclaimed to claimed. Evidence is shared via URLs, images, and videos in vulnerability reports, emphasizing risks like phishing under trusted domains.

## Requirements

1. Configured PoC on the claimed subdomain
2. Screen capture tools (built-in browser or OS tools)
3. Video recording capability for dynamic proof

## Defense

Defensive measures and detection strategies:

- Establish a bug bounty or disclosure program to encourage responsible reporting
- Monitor HackerOne or similar platforms for reports on your domains
- Conduct periodic red-team exercises to simulate and detect takeovers

## Objectives

1. Provide verifiable proof of subdomain control
2. Highlight potential attack impacts
3. Facilitate responsible disclosure

## Instructions

### Step 1: Capture Screenshots

**Context**: Document the current state of the subdomain.

Visit https://de-headless.staging.gymshark.com/ and take screenshots of the PoC page showing custom content.

> Screenshots clearly display the takeover text and assets.

### Step 2: Record Demonstration Video

**Context**: Show the before-and-after for completeness.

Record a video accessing the unclaimed state (if recreatable) and then the claimed PoC, narrating the process.

> Video file demonstrates full control and resolution changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[poc]]
- [[evidence]]
