---
id: tool-uuid-001
name: Awesome-Autocomplete-Extension
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.064Z'
platforms:
  - Web
  - Browser Extension
tags:
  - autocomplete
  - github
  - xss-vector
url: >-
  https://chrome.google.com/webstore/detail/awesome-autocomplete-for/iagbdiplfdhkabedhbakigbhdcofejfn
validated: true
submitted: true
---

# Awesome-Autocomplete-Extension

**Status**: Unverified

## Overview

Awesome Autocomplete is a browser extension that enhances GitHub's search with advanced autocomplete suggestions powered by Algolia, but it vulnerably renders unsanitized HTML from repo names and issues, enabling XSS attacks.

## Description

The extension intercepts GitHub search queries, fetches indexed content via Algolia, and inserts it into the DOM using innerHTML without escaping, allowing malicious JS execution in the site's context. Commonly used for productivity, it's a vector for client-side attacks on authenticated users.

## Features

- Feature 1: Real-time autocomplete for repositories, issues, and users
- Feature 2: Integration with Algolia for fast indexing of GitHub data
- Feature 3: Customizable dropdown rendering (vulnerable to injection)

## Installation

### Requirements

- Chrome 57+ or Safari 10.1+
- macOS Sierra 10.12.4+ or Windows 7 x64+

### Install Commands

No CLI install; use browser store:

```bash
# Open Chrome and navigate to store URL, click 'Add to Chrome'
```

## Basic Usage

Enable on GitHub.com; search queries auto-trigger enhanced results.

### Common Options

| Option | Description |
|--------|-------------|
| Extension Toggle | Enable/disable via browser menu |
| Permissions | Grants access to github.com tabs |

## Examples

### Example 1: Basic Usage

Search "repo name" on GitHub; dropdown shows suggestions with repo details.

### Example 2: Advanced Usage

Enter payloads like `'><script>alert(1)</script>` to exploit rendering.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor browser extensions list for 'Awesome Autocomplete'
- Detection method 2: Inspect network requests to Algolia from GitHub tabs

## Related Procedures


## Related Tools

- [[tools/Browser-Developer-Tools]]
- [[tools/GitHub]]

## References

- Official documentation: Chrome Web Store page
- Related resources: HackerOne report #220494
