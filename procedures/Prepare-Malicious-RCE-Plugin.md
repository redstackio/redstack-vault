---
tags:
  - rce
  - malicious-plugin
  - preparation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Upload Malware]]'
updated_at: '2025-12-14T17:23:24.859Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: af7dd805-de78-4380-a98c-d7438012a2b1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Upload Malware]]'
---
# Prepare-Malicious-RCE-Plugin

## Summary

This procedure prepares a malicious JAR plugin (rce.jar) from a provided zip file, setting up the payload for exploitation of the pdkinstall vulnerability in Atlassian Crowd to enable remote code execution.

## Description

In the context of CVE-2019-11580, the attacker reverse-engineers the pdkinstall plugin and creates a custom malicious JAR that, when installed, provides a servlet endpoint for command execution. This step involves downloading the exploit package, extracting it, and positioning the file for upload. It requires local access to the exploit files and basic file manipulation on a Linux system. Prerequisites include obtaining the rce-plugin.zip from a trusted exploit source like the HackerOne report.

## Requirements

1. Access to rce-plugin.zip containing the malicious rce.jar
2. Linux environment for extraction and navigation
3. Basic file permissions to read/write locally

## Defense

Defensive measures and detection strategies:

- Scan for and disable development plugins like pdkinstall in production builds
- Monitor file downloads and extractions of JAR/ZIP files in attack simulation environments
- Implement file integrity checks on exploit artifacts during red teaming

## Objectives

1. Extract the malicious rce.jar for upload
2. Position the file in the working directory
3. Ensure readiness for network-based exploitation

## Instructions

### Step 1: Download and Extract Plugin

**Context**: Obtain the exploit package and unzip it to access the malicious JAR, which contains the RCE payload.

No specific command; use browser or wget to download rce-plugin.zip, then:

```bash
unzip rce-plugin.zip
```

> This extracts rce.jar, a custom plugin that installs a servlet for command execution upon invocation.

### Step 2: Navigate to Plugin Directory

**Context**: Change into the extracted directory to locate rce.jar for the subsequent upload step.

```bash
cd path/to/extracted/folder
```

> Confirms rce.jar is present via `ls`, preparing for curl upload. Expected output: Listing including rce.jar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Upload Malware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- malicious-plugin
