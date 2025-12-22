---
id: tool-firebase-hosting
url: 'https://firebase.google.com/docs/hosting/quickstart'
tags:
  - hosting
  - static-site
  - cloud
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:33.480Z'
validated: true
submitted: true
---
# Firebase-Hosting

**Status**: Unverified

## Overview

Firebase Hosting is a free static content hosting service by Google, ideal for rapidly deploying malicious pages in web attack simulations due to its wildcard domain (*.firebaseapp.com) and ease of use.

## Description

Used in red teaming to host JavaScript payloads for iframe exploitation, Firebase provides global CDN delivery and free tiers up to 10GB storage. It integrates with CLI for Node.js-based deployments, making it suitable for quick PoC setups in vulnerability chaining like CSP bypasses.

## Features

- Feature 1: Automatic HTTPS and global edge caching
- Feature 2: CLI deployment via firebase-tools
- Feature 3: Free tier with custom domain support

## Installation

### Requirements

- Node.js and npm
- Google account for Firebase console

### Install Commands

```bash
npm install -g firebase-tools
firebase login
```

## Basic Usage

```bash
firebase init hosting
firebase deploy
```

### Common Options

| Option | Description |
|--------|-------------|
| `--only hosting` | Deploy only hosting config |
| `--project project-id` | Specify project |

## Examples

### Example 1: Basic Usage

```bash
firebase init hosting
# Follow prompts, then
firebase deploy
```

### Example 2: Advanced Usage

```bash
firebase deploy --only hosting --project my-malicious-project
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Firebase CLI processes (firebase binary)
- API calls to firebase.googleapis.com
- Suspicious static sites on *.firebaseapp.com with JS payloads

## Related Procedures


## Related Tools

- [[tools/Node.js]]

## References

- Official documentation: https://firebase.google.com/docs/hosting
- Related resources: Quickstart guide
