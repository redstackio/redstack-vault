---
id: proc-extract-files-lfi
tags:
  - file-read
  - discovery
  - lfi
  - expressionengine
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.448Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1083.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Extract-Sensitive-Files-via-LFI

## Summary

This procedure uses an established LFI vulnerability to read and extract contents of sensitive local files on the server, such as configuration files or system logs, to gather information for further attacks.

## Description

Once LFI is confirmed in the XML processing, this procedure targets high-value files like /etc/passwd for user enumeration or application configs for credentials. It relies on iterative payload testing to traverse directories and avoid null-byte restrictions common in PHP. Expected outcomes include data exfiltration, potentially chaining to RCE if writable locations are found.

## Requirements

1. Confirmed LFI vulnerability in the target feature
2. Knowledge of server OS (e.g., Linux paths like /etc/)
3. Tools for capturing large responses if files are big

## Defense

Defensive measures and detection strategies:

- Restrict file system access for the web server user (e.g., chroot or AppArmor)
- Enable PHP's open_basedir directive to limit file inclusion paths
- Monitor server logs for unexpected file reads (e.g., via auditd on Linux)
- Implement content security policies to detect anomalous data in responses

## Objectives

1. Read and capture contents of target sensitive files
2. Identify useful information like credentials or paths
3. Validate data for chaining to other exploits

## Instructions

### Step 1: Test with Known File

**Context**: Verify LFI works by including a small, non-sensitive file to build confidence.

Submit XML payload targeting `file:///proc/version` or similar.

**Expected Output**: Kernel version or system info in the response.

### Step 2: Target Sensitive Files

**Context**: Escalate to high-impact files using traversal (e.g., ../../../../etc/passwd).

Modify payload: `<!ENTITY test SYSTEM "file://../../../../etc/passwd">`. Submit and capture output. Iterate for files like /var/log/apache2/access.log.

**Expected Output**: Full file contents displayed or embedded in XML output.

> Example output: Lists of users, hashes, or log entries confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- [[T1083.001]] Local System File Discovery

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- file-read
- discovery
- lfi
