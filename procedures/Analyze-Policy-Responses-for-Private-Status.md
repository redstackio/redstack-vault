---
tags:
  - policy-analysis
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:26:00.171Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 56673332-f02f-45b0-b4a2-8e04561cb51d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-Policy-Responses-for-Private-Status

## Summary

This procedure examines GraphQL query responses to differentiate between public, null, and private policies, inferring if programs operate invite-only internal configurations.

## Description

After querying multiple teams, responses are categorized: null indicates no policy, matching public content for open programs, and unique HTML for private ones. This reveals sensitive setups like invite-only rules. Target: HackerOne API responses. Prerequisites: Collected query outputs. Outcomes: Intelligence on private programs for targeted attacks.

## Requirements

1. Multiple query responses in JSON format
2. Text comparison tools (e.g., diff)
3. Knowledge of public HackerOne policy templates

## Defense

Defensive measures and detection strategies:

- Standardize policy outputs to mask differences
- Block or anonymize sensitive field responses
- Use WAF to detect pattern-based API abuse

## Objectives

1. Classify responses by condition
2. Infer private program status
3. Identify exploitable configurations

## Instructions

### Step 1: Categorize Responses

**Context**: Review JSON for policy_markdown_html values.

**Command** (Manual Analysis):
No specific command; parse JSON manually or with jq.

> Condition 1: null - no policy. Condition 2: Matches public markdown. Condition 3: Differs (e.g., invite-only mentions). Expected: Categorized list of teams.

### Step 2: Compare Against Public Policies

**Context**: Cross-reference with known public policies from HackerOne.

**Command** (Manual Diff):
Use text diff tools on extracted HTML.

> Expected: Highlights revealing private elements like internal guidelines.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Org Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[policy-analysis]]
- [[Reconnaissance]]
