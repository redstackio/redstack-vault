---
id: proc-uuid-5678
tags:
  - ssrf
  - bypass
  - redirect
  - cloud-metadata
  - uppy
  - node.js
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:45.938Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-SSRF-Blacklist-in-Uppy-Companion-Using-Redirects

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in Uppy Companion version 1.15.0 by providing a redirecting URL that bypasses the host IP blacklist check, allowing the server to follow redirects to internal endpoints like cloud metadata services and return sensitive data as a downloadable file.

## Description

The Uppy Companion server, part of the Uppy file uploader ecosystem, includes a URL fetching feature in @uppy/companion/src/server/helpers/request.js. A prior fix for SSRF (report #786956) implemented a blacklist on host IPs before initiating fetches, but it fails to validate or block subsequent redirects. Attackers can supply an external URL (e.g., a TinyURL) that redirects to blacklisted internal IPs, such as http://169.254.169.254/metadata/v1/ used in cloud environments like DigitalOcean or AWS. When the protocol changes from HTTPS to HTTP during redirect, the blacklist is not re-applied, enabling unauthorized access to internal services. The response is processed as file content and made available for download, leading to data exfiltration. This targets Node.js-based web applications using Uppy for file uploads.

## Requirements

1. Access to a Uppy Companion server v1.15.0 (e.g., via public demo or vulnerable deployment).
2. Ability to create or use a redirect service (e.g., TinyURL) pointing to internal endpoints.
3. Web browser for interacting with the Uppy interface.
4. Target server in a cloud environment with accessible metadata (e.g., DigitalOcean droplet).

## Defense

Defensive measures and detection strategies:

- Implement redirect validation in URL fetching libraries to re-check blacklisted hosts post-redirect.
- Use allowlists instead of blacklists for internal IPs and enforce strict URL parsing.
- Monitor server logs for unexpected redirects or requests to metadata endpoints (e.g., 169.254.169.254).
- Deploy web application firewalls (WAFs) to detect anomalous URL patterns in file upload features.

## Objectives

1. Bypass the SSRF blacklist to make unauthorized requests to internal hosts.
2. Retrieve sensitive cloud metadata, including instance details and potential credentials.
3. Exfiltrate data via the file upload/download mechanism without direct network access.

## Instructions

### Step 1: Set Up Access to Uppy Interface

**Context**: Prepare the environment by accessing the vulnerable Uppy Companion setup to reach the URL fetch feature.

Navigate to https://uppy.io/ or deploy a local Node.js instance with Uppy Companion v1.15.0.

> Ensure the Companion server is running and the file uploader interface is accessible.

### Step 2: Initiate URL Fetch Option

**Context**: Select the remote URL input to trigger the server-side fetching logic.

In the Uppy dashboard, choose to add a file from a URL.

> This invokes the request.js helper, which will parse and fetch the provided URL.

### Step 3: Input Bypass URL

**Context**: Provide a crafted URL that redirects to the internal target, evading the initial blacklist.

Enter https://tinyurl.com/gqdv39p (pre-configured to redirect to http://169.254.169.254/metadata/v1/).

> The external host passes the check; the redirect to the internal HTTP endpoint is not validated.

### Step 4: Execute Fetch and Process Response

**Context**: Trigger the request, allowing the server to follow the redirect and fetch metadata.

Click to fetch and upload the 'file'.

> The Companion server makes the SSRF request, retrieves JSON metadata, and stages it for upload.

### Step 5: Retrieve and Analyze Data

**Context**: Download the exfiltrated content to confirm successful access.

Download the uploaded file from Uppy storage.

> Open the file to view internal metadata, such as {"droplet_id": 12345, "region": "nyc1"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- uppy
- node.js
- cloud-metadata
