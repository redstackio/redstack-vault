---
id: tool-uuid-1
url: 'https://tinyurl.com'
tags:
  - url-shortener
  - redirection
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.640Z'
validated: true
submitted: true
---
# TinyURL

**Status**: Unverified

## Overview

TinyURL is a free URL shortening service that creates compact links and supports custom redirects, commonly used in SSRF attacks to proxy external URLs to internal endpoints.

## Description

TinyURL allows users to input any URL (including internal ones like http://0:6000/) and generates a short external alias (e.g., https://tinyurl.com/ybk7sqrg) that redirects to it. In offensive security, it's leveraged to bypass SSRF filters by providing an innocuous external URL that resolves internally on the server side.

## Features

- Feature 1: Instant URL shortening with custom aliases
- Feature 2: Permanent redirects (301/302) to any destination
- Feature 3: No authentication required for basic use

## Installation

### Requirements

- Web browser or API access

### Install Commands

No installation needed; access via web.

## Basic Usage

Visit https://tinyurl.com and enter the target URL to generate a short link.

### Common Options

| Option | Description |
|--------|-------------|
| Custom Alias | Specify a vanity URL |
| Preview | Enable/disable redirect preview |

## Examples

### Example 1: Basic Usage

Enter http://0:6000/ to get https://tinyurl.com/ybk7sqrg.

### Example 2: Advanced Usage

Use API: curl "http://tinyurl.com/create.php?url=http://0:6000/" to automate.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound requests to tinyurl.com from applications
- Flag API calls with shortener domains in URL parameters
- Analyze redirect chains in server logs

## Related Procedures

- [[procedures/Create-Redirect-URL-to-Internal-Endpoint-Using-TinyURL]]

## Related Tools

- [[Bitly]]
- [[Google URL Shortener]]

## References

- Official site: https://tinyurl.com
- IP encoding reference: http://www.pc-help.org/obscure.htm
