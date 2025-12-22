---
tags:
  - shopify
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-ssti-rce-payload]]'
  - '[[commands/curl-http-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c7c654f3-7bdd-440e-b15d-566daa171f40
created_at: '2025-12-11T06:10:15.490Z'
updated_at: '2025-12-11T06:10:15.490Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Install and Access Return Magic App

## Summary

This procedure outlines the initial steps to install the Return Magic app on a Shopify store and access its admin features, setting the stage for vulnerability testing in the email templates.

## Description

The Return Magic app is installed via the Shopify admin interface, providing access to customizable email templates that use Handlebars.js. This procedure is necessary for reaching the vulnerable components without requiring special privileges beyond store access.

## Requirements

1. Access to a Shopify store admin
2. Internet connection for app installation
3. Browser for navigation

## Defense

Defensive measures and detection strategies:

- Monitor app installations and admin access logs
- Use app vetting processes before installation

## Objectives

1. Install the app successfully
2. Access the email workflow settings
3. Prepare for template editing

## Instructions

### Step 1: Install the App

**Context**: Install the app to enable its features.

Navigate to the Shopify app store and install Return Magic.

> No specific command; performed via UI.

### Step 2: Navigate to Admin Page

**Context**: Access the app's management interface.

Go to https://<shop>.myshopify.com/admin/apps/returnmagic.

> UI navigation.

### Step 3: Open Settings and Emails Workflow

**Context**: Reach the vulnerable email section.

From the top menu, open Settings, then Emails -> Workflow.

> Prepares for template editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- initial-access
