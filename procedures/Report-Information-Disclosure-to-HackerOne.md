---
id: 123e4567-e89b-12d3-a456-426614174004
name: Report-Information-Disclosure-to-HackerOne
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.512Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - responsible-disclosure
  - bug-bounty-reporting
  - platform-vulnerability
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Report-Information-Disclosure-to-HackerOne

## Summary

This procedure covers submitting the discovered information disclosure to HackerOne's platform, providing evidence to trigger internal review, content removal, and resolution with a bounty.

## Description

Using HackerOne's disclosure form, detail the video leak in report #1842822, attach evidence, and reference Code of Conduct violations. This leads to video deletion, platform audit, and a low-severity bounty, demonstrating responsible vulnerability handling in bug bounty ecosystems.

## Requirements

1. HackerOne account (free to create)
2. Compiled evidence from prior steps
3. Clear description of impact

## Defense

Defensive measures and detection strategies:

- Streamline internal triage for disclosure reports
- Implement feedback loops for bounty hunters
- Regularly train staff on privacy compliance

## Objectives

1. Notify HackerOne of the vulnerability
2. Ensure remediation and content removal
3. Receive acknowledgment and potential reward

## Instructions

### Step 1: Prepare Report

**Context**: Compile findings into a structured submission.

Draft details including URL, video ID, extracted data, and impact.

> Include screenshots or video clips as attachments.

### Step 2: Submit via Platform

**Context**: Use HackerOne's interface to file the report.

Log in and create a new disclosure report with all evidence.

> Submission confirmed; await triage and resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[responsible-disclosure]]
- [[bug-bounty-reporting]]
- [[platform-vulnerability]]
