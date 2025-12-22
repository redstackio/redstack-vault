---
id: tool-burp-repeater-001
url: 'https://portswigger.net/burp/documentation/desktop/testing-workflow/repeater'
tags:
  - request-modification
  - repeater
type: tool
verified: false
platforms:
  - Desktop Application
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.378Z'
validated: true
submitted: true
---
# Burp-Suite-Repeater

**Status**: Unverified

## Overview

Burp Suite Repeater is a module for manually sending, modifying, and reissuing HTTP requests, ideal for testing specific endpoints and observing responses without full proxy involvement.

## Description

Repeater allows copying requests from Proxy or other tabs, editing them, and sending repeatedly. Features include following redirections, updating request methods, and inspecting raw traffic. In security testing, it's used for precise exploitation, such as chaining requests or testing auth behaviors. The vulnerability here occurs when following cross-domain redirects, as it forwards sensitive headers like Authorization without domain checks.

## Features

- Feature 1: Manual request editing and resending
- Feature 2: Automatic following of redirections with header preservation
- Feature 3: Side-by-side request/response viewing

## Installation

### Requirements

- Burp Suite installed (included in core)

### Install Commands

No separate install; launch via Burp Suite GUI.

## Basic Usage

In Burp, right-click a request in Proxy > Send to Repeater, then click Send.

### Common Options

| Option | Description |
|--------|-------------|
| Follow redirection | Automatically send follow-up to Location |
| Update | Refresh request based on changes |

## Examples

### Example 1: Basic Usage

Send a GET /test to view response.

### Example 2: Advanced Usage

Follow a 302: Click Follow redirection after receiving redirect response.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Repeated requests from same IP with modified headers
- Logs showing Authorization headers on unexpected domains

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Postman]]

## References

- Official documentation: https://portswigger.net/burp/documentation/desktop/testing-workflow/repeater
- Related resources: PortSwigger Web Security Academy
