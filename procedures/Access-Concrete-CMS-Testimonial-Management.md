---
tags:
  - access
  - cms
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:35.364Z'
sub_techniques: []
id: db87aaf0-bfd8-499e-825f-fb36b1dd00d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Concrete-CMS-Testimonial-Management

## Summary

This procedure outlines logging into Concrete CMS and navigating to the testimonial management interface to enable editing or creation of testimonials, setting the stage for vulnerability exploitation.

## Description

In Concrete CMS, testimonials are managed through the admin or content dashboard. This step requires authenticated access to reach the form where user input can be provided. The target environment is a standard Concrete CMS installation on PHP, accessible via web browser. Expected outcome is visibility of the editable Bio/Quote field without restrictions.

## Requirements

1. Valid user credentials with permissions to create or edit testimonials (e.g., editor role)
2. Web browser with internet access to the CMS URL
3. No special network configuration beyond standard HTTP/HTTPS

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit testimonial editing to trusted users
- Monitor login attempts and dashboard access logs for anomalous activity

## Objectives

1. Establish authenticated session in the CMS
2. Reach the testimonial input form
3. Prepare for payload injection

## Instructions

### Step 1: Authenticate to CMS

**Context**: Log in to gain access to administrative features.

Open a web browser and navigate to the Concrete CMS login page (e.g., /login). Enter credentials and submit the form.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Testimonials

**Context**: Locate the management interface for testimonials.

From the dashboard, go to Content > Testimonials (or equivalent path in the CMS theme). Select 'Add New' or edit an existing entry to load the form.

> The form loads with fields including Bio/Quote.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access
- cms
