---
tags:
  - packaging
  - gitlab
type: procedure
tools:
  - '[[tools/Nokogiri]]'
  - '[[tools/Faraday]]'
  - '[[tools/exp.rb]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1063322b-3894-4ba8-a896-d37e93013a67
created_at: '2025-12-11T03:47:39.832Z'
updated_at: '2025-12-11T03:47:39.832Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Package NuSpec into NuPkg

## Summary

This procedure compresses the malicious .nuspec XML into a .nupkg file, preparing it for upload to GitLab's NuGet registry.

## Description

Using a zip tool, the .nuspec is archived into a .nupkg format, which is essentially a zip file. This step is necessary to mimic a legitimate NuGet package upload, triggering the vulnerable metadata extraction upon submission.

## Requirements

1. Zip utility installed
2. Malicious dummy.nuspec file ready

## Defense

Defensive measures and detection strategies:

- Validate package contents before extraction
- Scan uploads for known traversal patterns

## Objectives

1. Create a valid .nupkg archive
2. Prepare for API upload

## Instructions

### Step 1: Zip the File

**Context**: Compress the .nuspec into .nupkg.

Execute:

```bash
zip dummy.nupkg dummy.nuspec
```

> This creates the package file for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- #zip

## Tags

- packaging
- gitlab
