---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - web
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-18T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:06.847Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Survey-and-Add-Media-in-Crowdsignal

## Summary

This procedure sets up the environment in Crowdsignal by creating a new survey, adding a multiple-choice question, and embedding media to prepare for intercepting the save request during XSS payload injection.

## Description

In the context of exploiting a stored XSS vulnerability, this initial setup involves navigating the Crowdsignal dashboard to create a survey and configure a question with embedded media. The media shortcode insertion creates the necessary HTTP request that can be intercepted and modified. This step requires an authenticated user account and assumes the browser is proxied through Burp Suite for traffic capture. Expected outcome is a ready-to-save question editor with a benign media embed.

## Requirements

1. Authenticated access to https://app.crowdsignal.com/dashboard
2. Browser configured to route traffic through Burp Suite proxy
3. Basic familiarity with web application interfaces

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit survey creation to trusted users
- Monitor for unusual survey creation patterns in application logs

## Objectives

1. Establish a survey context for payload injection
2. Position the application to generate a savable media-embedded question
3. Prepare for request interception without alerting the system

## Instructions

### Step 1: Access Dashboard and Create Survey

**Context**: Log in and initiate a new survey to access the question editor.

Navigate to https://app.crowdsignal.com/dashboard and click to create a new survey.

> This opens the survey builder interface.

### Step 2: Add Multiple Choice Question

**Context**: Select and configure a question type that supports media embedding.

In the survey editor, go to the question section and select "Multiple Choice" as the question type.

> Ensures compatibility with the media embed feature.

### Step 3: Embed Media Shortcode

**Context**: Insert a benign shortcode to trigger the media parameter in the save request.

Click "Add media", select "Embed Media", and paste [dailymotion id=x8oma9] into the embed field. Click to insert the media.

> Prepares the question for saving, generating the interceptable request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[web]]
