---
tags:
  - source-review
  - path-traversal
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:27.928Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ebc231e3-a2fc-4dde-a7fe-44565a07ab0d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-Asset-Route-in-Lila-Source

## Summary

This procedure involves reviewing the Lila project's source code to identify the asset serving route vulnerable to path traversal due to missing path validation, setting the stage for exploitation.

## Description

In the context of auditing the Lila project (used by Lichess.org), examine the routes configuration to find handlers that serve assets without sanitizing user-supplied paths. The vulnerability at line 939 in conf/routes allows '../' sequences to traverse directories, potentially exposing server files. This is a reconnaissance step to confirm the root cause before testing.

## Requirements

1. Access to the Lila source code repository (e.g., GitHub)
2. Basic knowledge of Scala and Play Framework routing
3. Text editor or IDE for code review

## Defense

Defensive measures and detection strategies:

- Implement code review processes with static analysis tools like SonarQube to detect path traversal patterns
- Use web application firewalls (WAF) to monitor for '../' in requests
- Enforce least privilege on file system access for web servers

## Objectives

1. Confirm lack of path normalization in asset routes
2. Document the exact location of the vulnerability
3. Prepare for targeted endpoint testing

## Instructions

### Step 1: Clone and Examine Source Code

**Context**: Obtain the Lila source code and navigate to the routes file to inspect the asset serving logic.

Clone the repository and open conf/routes:

Review line 939, which defines the asset route without validation:

Expected: The route handler directly serves files based on user input without canonicalization.

### Step 2: Analyze Path Handling

**Context**: Check for absence of security controls like path normalization or whitelist validation.

Search for terms like 'assets' and '../' in the codebase. Confirm no use of libraries like java.nio.file.Paths for normalization.

Expected: Identification of the insecure route pattern, e.g., GET /assets/*file controllers.Assets.at(path="/public", file=file.raw)

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- source-review
- reconnaissance
- scala
