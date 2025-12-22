---
url: 'https://www.npmjs.com/package/uppy'
tags:
  - file-uploader
  - ssrf
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.551Z'
id: 04c62976-2c72-41cc-ad73-52c78060e605
validated: true
submitted: true
---
# Uppy

**Status**: Unverified

## Overview

Uppy is a JavaScript file uploader library with a modular plugin system, including a Companion server for handling remote URLs, which can be exploited for SSRF to access internal resources during security assessments.

## Description

Uppy supports drag-and-drop uploads, progress tracking, and integrations like URL fetching via Companion. Version 1.8.0's Companion has an SSRF flaw in the /get endpoint, allowing arbitrary internal fetches. In red teaming, it's used to simulate or exploit upload proxies in web apps, enabling metadata exfiltration or internal scanning.

## Features

- Feature 1: Plugin-based architecture (Dashboard, URL, Tus for uploads)
- Feature 2: Companion server for backend URL processing
- Feature 3: CDN delivery for quick client-side setup

## Installation

### Requirements

- Node.js for server; browser for client

### Install Commands

```bash
# Client via CDN (no install)
# Server
npm install @uppy/companion
```

## Basic Usage

```bash
# Server start (after install)
companion
```

### Common Options

| Option | Description |
|--------|-------------|
| `companionUrl` | URL to Companion server in URL plugin |
| `debug` | Enable verbose logging |

## Examples

### Example 1: Basic Usage

```javascript
new Uppy.Core().use(Uppy.Url, {companionUrl: 'http://localhost:3020'});
```

### Example 2: Advanced Usage

```javascript
new Uppy.Core({plugins: ['Url', 'Tus']}).use(Uppy.Url, {companionUrl: 'http://localhost:3020'}).use(Uppy.Tus, {endpoint: 'https://tus.io/files/'});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to uppy/transloadit CDNs
- Server processes running companion on non-standard ports
- Upload logs showing URL fetches to internal hosts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/npm]]
- [[tools/Tus]]

## References

- Official documentation: https://uppy.io/
- Related resources: HackerOne report #786956
