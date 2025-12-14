---
id: proc-uuid-1
tags:
  - mapbox
  - setup
  - tool-installation
type: procedure
tools:
  - '[[tools/Mapbox-Studio-Classic]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Third-party Software]]'
updated_at: '2025-12-14T03:16:30.279Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Third-party Software]]'
---
---

# Setup-Mapbox-Studio-Classic

## Summary

This procedure installs and initializes the Mapbox Studio Classic desktop application, enabling the creation of custom map styles necessary for injecting XSS payloads in subsequent steps.

## Description

Mapbox Studio Classic is a legacy desktop tool for designing and uploading custom map styles to Mapbox.com. In this attack scenario, it is used to prepare a style project where an XSS payload can be embedded in the attribution field. The target environment is any desktop OS with internet access, and the outcome is a ready-to-edit style project. Prerequisites include a Mapbox account and basic familiarity with map design tools.

## Requirements

1. Internet access to download from https://www.mapbox.com/mapbox-studio/
2. Mapbox account for later upload
3. Desktop OS (Windows, macOS, or Linux)

## Defense

Defensive measures and detection strategies:

- Monitor downloads of legacy Mapbox tools like Studio Classic, which is deprecated
- Enforce use of modern Mapbox tools (e.g., Mapbox Studio web app) with built-in sanitization
- Network logs for unusual uploads to Mapbox API endpoints

## Objectives

1. Install Mapbox Studio Classic securely
2. Launch and create a new style project
3. Prepare for payload injection without triggering local alerts

## Instructions

### Step 1: Download and Install

**Context**: Obtain the official Mapbox Studio Classic application to avoid tampered versions.

No command required; use browser to visit https://www.mapbox.com/mapbox-studio/ and download the installer for your OS. Run the installer and follow on-screen prompts to complete setup.

> Expected output: Application icon appears in your applications menu or desktop.

### Step 2: Launch and Create New Style

**Context**: Initialize a new project to begin style editing.

Launch Mapbox Studio Classic from your applications. Select 'New Style' from the welcome screen, enter a random name (e.g., 'TestStyle') and description (e.g., 'Custom map for demo'), then click 'Create'.

> Expected output: The style editor opens with a blank canvas and default layers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Third-party Software]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mapbox-Studio-Classic]]

## Tags

- [[mapbox]]
- [[setup]]

