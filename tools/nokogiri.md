---
id: tool-005
url: 'https://nokogiri.org/'
tags:
  - library
  - parsing
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.594Z'
validated: true
submitted: true
---
# nokogiri

**Status**: Unverified

## Overview

Nokogiri is a Ruby gem for parsing HTML and XML, dependency for Drupalgeddon2 to handle form data.

## Description

Enables secure parsing in exploits, extracting elements like form_build_id from Drupal responses.

## Features

- Feature 1: HTML/XML parsing
- Feature 2: XPath/CSS selectors
- Feature 3: Fast performance

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install nokogiri
```

## Basic Usage

```bash
# Via Ruby script
```

### Common Options

N/A; library usage.

## Examples

### Example 1: Basic Usage

In script: require 'nokogiri'; doc = Nokogiri::HTML(response)

## MITRE ATT&CK Mapping

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

- Gem installation logs

## Related Procedures

- [[procedures/Download-and-Setup-Drupalgeddon2-Exploit]]

## Related Tools

- [[Related Tool: BeautifulSoup]]

## References

- https://nokogiri.org/tutorials
