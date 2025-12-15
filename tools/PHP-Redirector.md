---
id: t-php-redirector
url: null
tags:
  - php
  - proxy
  - redirect
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.806Z'
validated: true
submitted: true
---
# PHP Redirector

**Status**: Unverified

## Overview

A simple PHP script acting as a proxy to perform 307 redirects while preserving forged headers like Content-Type for CSRF exploits.

## Description

In the attack, Flash POSTs to this script, which redirects to the target API (e.g., Federalist /v0/build/), maintaining application/json and bypassing CORS by chaining origins.

## Features

- 307 Temporary Redirect with header preservation
- Handles JSON payload forwarding
- Minimal code for quick deployment

## Installation

### Requirements

- PHP-enabled web server

### Install Commands

Upload script to server.

## Basic Usage

proxy.php?endpoint=https://target.com/api

### Common Options

| Option | Description |
|--------|-------------|
| endpoint | Target URL via GET |
| Content-Type | Set to application/json |

## Examples

### Example 1: Basic Script

<?php header('Location: ' . $_GET['endpoint'], true, 307); header('Content-Type: application/json'); ?>

### Example 2: With Payload Echo

<?php echo $_POST['data']; // Forward payload

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious 307 redirects in logs
- Forged Content-Type from external hosts
- PHP execution traces

## Related Procedures


## Related Tools

- [[tools/Flash-SWF-File]]

## References

- PHP header documentation
