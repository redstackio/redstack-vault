---
tags:
  - shopify
  - setup
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a3f3d3c5-ae72-46ce-b0a2-0c79dac54c91
created_at: '2025-12-14T17:32:48.521Z'
updated_at: '2025-12-14T17:32:48.521Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Controlled-Store-and-Upload-File

## Summary

This procedure sets up an attacker-controlled Shopify store and uploads a file to it, extracting necessary details like absoluteKey, key, and path for use in subsequent cross-store copying attacks.

## Description

In the context of exploiting Shopify's undocumented fileCopy mutation, this initial setup allows the attacker to create a source store (storeB) independent of the target (storeA). The uploaded file serves as the payload for unauthorized copying, bypassing permission checks. This step requires Shopify partner access or trial store creation and focuses on obtaining CDN-hosted file metadata.

## Requirements

1. Shopify partner account or ability to create trial stores
2. Web browser for admin interface access
3. File to upload (e.g., innocuous image like 1.jpg)

## Defense

Defensive measures and detection strategies:

- Monitor for rapid creation of multiple trial stores from suspicious IPs
- Rate-limit file uploads on new stores
- Log and alert on file metadata extractions via API

## Objectives

1. Establish controlled source for malicious files
2. Extract file details for GraphQL exploitation
3. Prepare for permission bypass in target store

## Instructions

### Step 1: Create New Shopify Store

**Context**: Sign up for a new trial store to gain full control without affecting the target.

No command required; use Shopify's signup process to create storeB.myshopify.com.

> Expected: Admin access granted to new store.

### Step 2: Upload Test File

**Context**: Upload a file via the admin files section to generate CDN paths.

Navigate to Settings > Files in the admin dashboard and upload 1.jpg.

> Expected: File listed with details: absoluteKey='s/files/1/d/0864/0471/6006/6199/files/1.jpg', key='files/1.jpg', path='https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6'.

### Step 3: Extract File Details

**Context**: Copy the generated metadata for use in fileCopy mutation.

Inspect the file entry in the admin UI or API response.

> Expected: All three parameters (absoluteKey, key, path) noted accurately.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[setup]]
