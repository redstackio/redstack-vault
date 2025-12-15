---
id: proc-001
tags:
  - reconnaissance
  - pypi
  - dependency-confusion
type: procedure
tools:
  - '[[tools/pip]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:17.680Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
---
# Identify-Unclaimed-Internal-Package-on-PyPI

## Summary

This procedure involves reconnaissance to identify internal package names that are unclaimed on the public PyPI registry, setting the stage for a dependency confusion attack by allowing hijacking of legitimate internal dependencies.

## Description

In a dependency confusion attack, attackers search for package names used internally by a target organization but not registered on public repositories like PyPI. By claiming these names, attackers can upload malicious versions that get installed when build systems or developers fallback to public sources due to misconfigurations. This targets environments like Yelp's where 'yelp-cgeom' was internal but unclaimed, leading to potential RCE during installation.

## Requirements

1. Access to public PyPI search (no authentication needed).
2. Knowledge of target company's internal naming conventions (e.g., 'yelp-*' for Yelp).
3. A tool or browser to query PyPI.

## Defense

Defensive measures and detection strategies:

- Explicitly claim all internal package names on public registries to prevent hijacking.
- Configure pip to use only internal indices with --index-url and --extra-index-url, avoiding public fallback.
- Implement package signing and integrity checks (e.g., via pip's --require-hashes).

## Objectives

1. Discover unclaimed internal packages to enable supply chain compromise.
2. Validate the package's internal usage without direct access.
3. Prepare for malicious upload.

## Instructions

### Step 1: Research Internal Package Names

**Context**: Gather potential internal package names from public leaks, job postings, or GitHub repos.

No specific command; manually search or use web scraping.

> For Yelp, identify 'yelp-cgeom' as an internal geometry package.

### Step 2: Check Availability on PyPI

**Context**: Query PyPI to confirm the package is unclaimed.

Use browser or [[commands/pip-search]]:

```bash
pip search yelp-cgeom
```

> If no results or 'No matching distribution found', the package is unclaimed. Expected output: Empty or error indicating absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Software

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pip]]

## Tags

- [[Reconnaissance]]
- [[pypi]]
---
