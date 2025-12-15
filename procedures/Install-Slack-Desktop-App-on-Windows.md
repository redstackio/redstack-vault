---
tags:
  - slack
  - installation
  - windows
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Windows
techniques: []
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 26d1ce8e-f55f-42f6-abdb-9eb440551676
created_at: '2025-12-14T17:31:19.746Z'
updated_at: '2025-12-14T17:31:19.746Z'
verified: false
validated: true
submitted: true
---
# Install-Slack-Desktop-App-on-Windows

## Summary

This procedure outlines the standard installation of the Slack desktop application on a 64-bit Windows system, which is the first step in demonstrating session persistence vulnerabilities.

## Description

The Slack desktop app for Windows is downloaded from the official website and installed via a simple executable. This sets up the environment for authentication and subsequent testing of credential persistence. The process requires no special privileges beyond standard user rights and is identical to legitimate app deployment. In an attack scenario, this could be performed by a legitimate user whose session will later be exploited.

## Requirements

1. 64-bit Windows operating system (Windows 10 or later)
2. Internet access to download the installer from slack.com/downloads/windows
3. Standard user account with permission to install software

## Defense

Defensive measures and detection strategies:

- Enforce group policy to restrict app installations on shared devices
- Monitor for frequent installations of collaboration tools like Slack
- Use endpoint detection to log app installations and user activity

## Objectives

1. Deploy the Slack app to prepare for session creation
2. Ensure compatibility with 64-bit Windows for accurate vulnerability testing
3. Verify installation without errors to proceed to authentication

## Instructions

### Step 1: Download Installer

**Context**: Obtain the official 64-bit installer to ensure authenticity and compatibility.

Navigate to https://slack.com/downloads/windows in a web browser and select the 64-bit version for download.

### Step 2: Run Installation

**Context**: Execute the setup to install the app in the default location.

Double-click the downloaded .exe file (e.g., SlackSetup.exe), follow the prompts to accept terms, and complete the installation. No custom paths are needed for standard testing.

> The installer runs silently or with minimal prompts, placing files in %LOCALAPPDATA%\Slack.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[windows]]
- [[installation]]
