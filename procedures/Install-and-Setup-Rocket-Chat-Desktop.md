---
id: proc-install-rocket-chat
tags:
  - setup
  - electron
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.555Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Setup-Rocket-Chat-Desktop

## Summary

This procedure installs the vulnerable Rocket.Chat Desktop application on a Linux system (e.g., Xubuntu 20.04) and sets up authentication to a chat channel, preparing the environment for exploitation of the shell.openExternal() vulnerability.

## Description

The Rocket.Chat Desktop app, built on Electron, versions like 2.17.10 contain insufficient URL filtering in preload scripts (links.js), allowing protocols beyond file:// to execute external content. This step simulates the victim's setup, downloading from GitHub releases and logging in to enable chat-based delivery of malicious links. Expected outcome is a running app ready for link interaction, with no immediate exploitation.

## Requirements

1. Linux system (e.g., Xubuntu 20.04) with internet access
2. Valid Rocket.Chat server credentials for authentication
3. No special tools required beyond a web browser for download

## Defense

Defensive measures and detection strategies:

- Use app whitelisting and restrict downloads to official sources
- Monitor for unusual Electron app installations via endpoint detection tools
- Educate users on verifying app versions and avoiding untrusted chats

## Objectives

1. Establish a vulnerable Electron environment mimicking the victim
2. Gain access to a chat channel for payload delivery
3. Verify app functionality for link handling

## Instructions

### Step 1: Download and Install App

**Context**: Obtain the latest vulnerable release to replicate the target environment.

No command; use browser to navigate to GitHub releases page for Rocket.Chat Desktop (https://github.com/RocketChat/Rocket.Chat.Desktop/releases/tag/2.17.10), download the .deb package, and install via GUI or dpkg.

> Expected output: App installed and executable from applications menu.

### Step 2: Authenticate and Join Channel

**Context**: Log in to simulate victim access and prepare for message exchange.

Launch the app and enter server URL, username, and password to authenticate, then join or create a channel.

> Expected output: Successful login with channel visible and messaging enabled.

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
- electron
- rocket-chat
