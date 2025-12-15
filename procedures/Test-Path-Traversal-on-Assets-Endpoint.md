---
tags:
  - path-traversal
  - vulnerability-testing
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.924Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 81615ce0-3e69-493f-a3d8-0964527b1134
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Path-Traversal-on-Assets-Endpoint

## Summary

This procedure tests the /assets/ endpoint for path traversal by appending '../' to supplied paths, verifying if arbitrary files can be read outside the assets directory, such as build.sbt.

## Description

Targeting the Lila project's public-facing asset endpoint (e.g., on Lichess.org), craft requests with traversal payloads to escape the intended directory. Successful tests confirm the lack of validation, allowing access to parent directories and files like build configurations, which can aid in reconnaissance.

## Requirements

1. Public access to the target web application (e.g., https://lichess.org)
2. Web browser or HTTP client for manual requests
3. Knowledge of the target URL structure

## Defense

Defensive measures and detection strategies:

- Apply path normalization in server-side code using canonical paths
- Log and alert on requests containing '../' or absolute paths
- Restrict file serving to a chrooted or whitelisted directory

## Objectives

1. Verify traversal capability on /assets/
2. Retrieve a non-sensitive file to confirm exploitability
3. Assess server response for error handling

## Instructions

### Step 1: Craft Traversal Request

**Context**: Use a simple traversal payload to target a known file outside assets.

Access https://lichess.org/assets/../build.sbt in a web browser or via HTTP GET request.

Expected: Server returns the contents of build.sbt, including Scala build details.

### Step 2: Validate Response

**Context**: Check if the response is the actual file content rather than an error or asset.

Inspect the HTTP response body for build.sbt syntax (e.g., libraryDependencies). If served, vulnerability is confirmed.

Expected: Raw file text without asset headers or 404 error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- testing
- exploit
