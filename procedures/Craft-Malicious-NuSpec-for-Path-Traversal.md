---
tags:
  - path-traversal
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
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c4cc5067-fcc5-43bb-a180-04d4e219db8d
created_at: '2025-12-11T03:47:39.835Z'
updated_at: '2025-12-11T03:47:39.835Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Malicious NuSpec for Path Traversal

## Summary

This procedure crafts a malicious .nuspec XML file with path traversal sequences injected into the version field, exploiting the lack of validation in GitLab's metadata extraction service to enable arbitrary file paths.

## Description

The attack targets the ee/app/services/packages/nuget/metadata_extraction_service.rb in GitLab, which uses Nokogiri to parse the XML without sanitizing the version field. By including sequences like '../../../../../nyangawa', attackers can control filename construction for arbitrary file creation as the git user. This is part of a chain leading to file reads when combined with other vulnerabilities.

## Requirements

1. Text editor to create XML file
2. Knowledge of NuGet .nuspec format
3. Access to a GitLab project for testing

## Defense

Defensive measures and detection strategies:

- Implement input sanitization on XML fields in metadata extraction
- Monitor for anomalous file creations in GitLab logs

## Objectives

1. Create a traversable path in the version field
2. Prepare for packaging and upload
3. Enable arbitrary file placement

## Instructions

### Step 1: Create XML with Traversal

**Context**: Inject traversal sequences into the version tag of the .nuspec file.

Create a file named dummy.nuspec with content including <version>../../../../../nyangawa</version>.

> This allows the extraction service to construct filenames outside intended directories.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Nokogiri]]

## Tags

- path-traversal
- gitlab
