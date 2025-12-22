---
id: proc-craft-load-scripts-request
name: Craft Request to Load-Scripts Endpoint
tags:
  - dos
  - exploit
  - wordpress
type: procedure
tools:
  - '[[tools/Apache-JMeter]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:36.832Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft Request to Load-Scripts Endpoint

## Summary

This procedure constructs and sends a single HTTP GET request to WordPress's /wp-admin/load-scripts.php with an excessively long 'load' parameter, triggering CVE-2018-6389 to generate ~3MB of data and consume significant server resources.

## Description

The endpoint concatenates numerous JavaScript files specified in the 'load' parameter (comma-separated list) without checks, leading to high CPU and memory usage during file I/O and processing. This is the core exploitation step, demonstrated on sites like https://iandunn.name/, where no authentication is required.

## Requirements

1. Confirmed vulnerable endpoint from prior reconnaissance.
2. [[tools/Apache-JMeter]] installed for request crafting.
3. List of WordPress script names (e.g., from core files: eutil,common,wp-a11y, etc.).

## Defense

Defensive measures and detection strategies:

- Patch WordPress to version 5.0.1+ or apply security plugins like Wordfence.
- Restrict /wp-admin/ access via IP whitelisting or authentication middleware.
- Log and alert on requests with 'load' parameter exceeding 100 characters.

## Objectives

1. Generate large response to exhaust per-request resources.
2. Validate single-request impact.
3. Prepare for amplification.

## Instructions

### Step 1: Prepare Script List

**Context**: Compile a long comma-separated list of script names to maximize data generation.

Create a text file with entries like: eutil,common,wp-a11y,quicktags,svg-painter,jquery-ui-core,... (aim for 200+ names).

### Step 2: Configure and Send Request in JMeter

**Context**: Use JMeter to simulate the malicious GET request.

Launch JMeter, create a Thread Group (1 thread, 1 loop). Add HTTP Request sampler: Server Name = iandunn.name, Path = /wp-admin/load-scripts.php, Method = GET, Parameters: Name=load, Value=your-long-list.txt (use CSV Data Set if needed).

Run the test and monitor response size.

**Expected Output**: ~3MB response body with concatenated JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Apache-JMeter]]

## Tags

- [[dos]]
- [[cve-2018-6389]]
