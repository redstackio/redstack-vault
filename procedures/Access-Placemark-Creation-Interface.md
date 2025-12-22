---
tags:
  - wordpress
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:47.201Z'
sub_techniques: []
id: ee42ab60-a360-4809-82dc-ab6536bec7ff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access-Placemark-Creation-Interface

## Summary

This procedure outlines navigating to the Basic Google Maps Placemarks plugin interface in WordPress to access the placemark creation or editing form, serving as the entry point for exploiting the self-XSS vulnerability.

## Description

In a WordPress environment with the Basic Google Maps Placemarks Settings plugin installed, authenticated users can access the admin dashboard to manage placemarks. This step involves logging in and locating the specific settings page where the vulnerable title field is exposed. No technical exploits are involved here; it's standard navigation. Prerequisites include valid credentials and plugin activation. Expected outcome is the form ready for input manipulation.

## Requirements

1. Authenticated session in WordPress admin
2. Basic Google Maps Placemarks plugin installed and enabled
3. Web browser with cookies enabled for session persistence

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control to limit placemark editing to trusted users
- Monitor admin login attempts for anomalies

## Objectives

1. Gain access to the vulnerable input interface
2. Prepare for payload injection
3. Ensure session validity for subsequent steps

## Instructions

### Step 1: Log In to WordPress Admin

**Context**: Establish an authenticated session to access plugin settings.

Navigate to `/wp-admin/` and log in with valid credentials.

> Upon successful login, the dashboard loads.

### Step 2: Navigate to Plugin Settings

**Context**: Locate the placemark management section.

Go to Settings > Basic Google Maps Placemarks or the plugin's dedicated menu, then select Create New Placemark or Edit Existing.

> The form appears with fields including the title.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques



### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[admin-access]]
