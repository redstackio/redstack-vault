---
id: 123e4567-e89b-12d3-a456-426614174001
name: Review-SSH-CA-Authentication-Support
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.899Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - ssh-certificate
  - github
  - reconnaissance
commands: []
platforms:
  - Web
  - Cloud (GitHub Enterprise)
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Review-SSH-CA-Authentication-Support

## Summary

This procedure involves reviewing GitHub Enterprise documentation and features to identify support for SSH certificate authority (CA) authentication, particularly how certificates can include extensions for user impersonation, setting the stage for exploiting authentication weaknesses in services like gists.

## Description

In the context of GitHub Enterprise Server and Cloud, SSH CA authentication allows organizations to use signed SSH certificates instead of individual keys. These certificates can include extensions such as `login@github.com=username`, which specifies the authenticating user. This procedure focuses on understanding this mechanism to identify potential misuse in less-secured endpoints like gist.github.com. The target environment is GitHub Enterprise versions prior to 3.9, where such features are enabled but not uniformly validated across all services.

## Requirements

1. Access to GitHub Enterprise documentation or instance
2. Basic knowledge of SSH and certificate signing
3. Network access to review public or internal docs

## Defense

Defensive measures and detection strategies:

- Regularly audit SSH CA configurations and restrict extension usage
- Monitor for unusual certificate-based authentications in logs
- Implement endpoint-specific validation for all GitHub services

## Objectives

1. Confirm SSH CA support and extension capabilities in GitHub
2. Identify potential for username impersonation via extensions
3. Gather prerequisites for crafting exploitable certificates

## Instructions

### Step 1: Access GitHub Documentation

**Context**: Locate and read official documentation on SSH CA authentication to understand supported extensions.

Search for "SSH certificate authorities" in GitHub Enterprise docs and note the section on certificate extensions, confirming that `login@github.com=username` allows authentication as the specified user.

### Step 2: Verify Extension Usage

**Context**: Test or simulate extension inclusion in a controlled environment to confirm functionality.

In a test setup, generate a sample certificate with the extension and attempt authentication to a non-gist endpoint to validate the mechanism works as documented.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssh-certificate]]
- [[github]]
- [[Reconnaissance]]
