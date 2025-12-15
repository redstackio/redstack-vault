---
id: proc-undici-review-001
name: Review-Undici-Security-Advisory
tags:
  - reconnaissance
  - advisory-review
  - undici
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:56.639Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-Undici-Security-Advisory

## Summary

This procedure involves analyzing an existing security advisory for the undici Node.js library to identify gaps in cross-origin redirect header handling, specifically the omission of Proxy-Authorization clearing, which hints at a potential information disclosure vulnerability.

## Description

In the context of auditing Node.js HTTP clients, review the GitHub Security Advisory GHSA-wqq4-5wpv-mx2g, which documents undici's behavior of clearing Authorization and Cookie headers during cross-domain redirects to prevent leakage. The advisory's focus on only these headers, without mentioning Proxy-Authorization, suggests a violation of the Fetch specification's forbidden header rules. This procedure sets the stage for PoC development by forming a hypothesis on credential leakage to third-party sites via redirects in applications using undici.

## Requirements

1. Access to GitHub Security Advisories (internet connection).
2. Basic knowledge of HTTP headers and the Fetch API specification.
3. Node.js development environment for context.

## Defense

Defensive measures and detection strategies:

- Regularly audit library advisories using tools like Dependabot or Snyk.
- Implement custom header stripping in applications using undici for redirects.

## Objectives

1. Identify undocumented header handling behaviors in undici.
2. Hypothesize on Proxy-Authorization persistence during redirects.
3. Prepare for PoC testing to confirm leakage.

## Instructions

### Step 1: Access the Advisory

**Context**: Locate and read the specific GHSA advisory to understand documented behaviors.

Browse to https://github.com/nodejs/undici/advisories/GHSA-wqq4-5wpv-mx2g and review the content.

> The advisory confirms clearing of Authorization and Cookie but omits Proxy-Authorization, indicating a potential gap.

### Step 2: Analyze Header Handling

**Context**: Compare against Fetch spec to spot omissions.

Note that per Fetch, Proxy-Authorization should be treated as a forbidden header and cleared on cross-origin requests/redirects.

> Expected outcome: Recognition that undici's implementation is incomplete, risking proxy credential exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[advisory-review]]
