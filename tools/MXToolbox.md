---
url: 'http://mxtoolbox.com/SuperTool.aspx'
tags:
  - dns
  - recon
type: tool
platforms:
  - Web
description: Online DNS lookup and analysis tool for verifying records like CNAMEs.
id: e8126b56-54dd-4c82-a890-7ca29dbd313c
created_at: '2025-12-14T04:51:10.524Z'
updated_at: '2025-12-14T04:51:10.524Z'
verified: false
validated: true
submitted: true
---
# MXToolbox

**Status**: Unverified

## Overview

MXToolbox is a web-based suite for DNS diagnostics, blacklists, and domain analysis, commonly used in security testing to quickly verify CNAME records and propagation.

## Description

It provides tools for CNAME lookups, MX records, and more, helping identify misconfigurations like dangling pointers to AWS S3 in subdomain takeover scenarios.

## Features

- Feature 1: CNAME record verification
- Feature 2: DNS propagation checks
- Feature 3: Integration with other DNS tools

## Installation

### Requirements

- Web browser

### Install Commands

No installation; web-based.

## Basic Usage

Visit http://mxtoolbox.com/SuperTool.aspx?action=cname%3aassets.goubiquiti.com&run=toolpage

### Common Options

| Option | Description |
|--------|-------------|
| action=cname | Query CNAME type |
| run=toolpage | Execute lookup |

## Examples

### Example 1: Basic Usage

Input: assets.goubiquiti.com in CNAME tool.

### Example 2: Advanced Usage

Combine with WHOIS for full domain intel.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to mxtoolbox.com from security scanners
- DNS query spikes from tool IPs

## Related Procedures

- [[Identify Dangling CNAME Records]]

## Related Tools

- [[DNSdumpster]]
- [[Dig]]

## References

- Official site: https://mxtoolbox.com
