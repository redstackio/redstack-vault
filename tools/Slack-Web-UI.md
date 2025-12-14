---
id: tool-slack-web-ui
url: >-
  https://{YOUR-TEAM-HOSTNAME}.slack.com/files/{YOUR-MEMBER-ID}/{FILE-ID}/title/edit
tags:
  - slack
  - ui
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.089Z'
validated: true
submitted: true
---
# Slack-Web-UI

**Status**: Unverified

## Overview

Slack's web interface for editing file titles and JSON structures, exploited for direct HTML injection into Posts.

## Description

Provides access to editable JSON fields vulnerable to HTML insertion.

## Features

- Feature 1: File title editing
- Feature 2: JSON structure modification
- Feature 3: Preview rendering

## Installation

### Requirements

- Browser

### Install Commands

N/A; web-based.

## Basic Usage

Navigate to edit URL.

### Common Options


## Examples

### Example 1: Basic Usage

Edit title to inject <map> tags.

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

- Log UI edits for malicious patterns.

## Related Procedures


## Related Tools

- [[tools/Slack-API-files-info]]

## References

- Slack help
