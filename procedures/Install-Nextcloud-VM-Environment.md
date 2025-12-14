---
tags:
  - setup
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.517Z'
sub_techniques: []
id: a7d9aa94-5b83-4997-83a6-8455dcefe28c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Nextcloud-VM-Environment

## Summary

This procedure sets up a vulnerable Nextcloud instance using the official VM image to test the Extract app path traversal vulnerability.

## Description

The official Nextcloud VM image provides a pre-configured Linux environment with Nextcloud, PHP, and enabled apps like Extract. It uses default settings including extra security options, simulating a production-like setup. This step ensures the target environment is ready for exploitation without custom installations.

## Requirements

1. VirtualBox or VMware for running the VM
2. Download access to the official Nextcloud VM image from Hansson IT
3. Basic virtualization knowledge

## Defense

Defensive measures and detection strategies:

- Use official images only from trusted sources
- Monitor VM deployments for unauthorized setups
- Enable VM integrity checks

## Objectives

1. Deploy a functional Nextcloud instance
2. Verify Extract app availability
3. Prepare for user creation and exploitation

## Instructions

### Step 1: Download and Import VM

**Context**: Obtain the official image and import it into your hypervisor.

Download the VM image from the Nextcloud website (provided by Hansson IT). Import into VirtualBox or VMware and boot the VM.

### Step 2: Access Web Interface

**Context**: Confirm the instance is running and accessible.

After boot, access https://[VM-IP]/ via browser. Complete any initial setup if prompted, using default credentials.

**Expected Output**: Nextcloud dashboard loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- nextcloud
