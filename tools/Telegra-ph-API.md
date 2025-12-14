---
url: 'https://telegra.ph/Realtime-Updated-URL-to-Access-Flow-Connectors-09-23'
tags:
  - api
  - storage
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.766Z'
id: de484ffe-356c-44a0-8035-ebce0de289c2
validated: true
submitted: true
---
# Telegra-ph-API

**Status**: Unverified

## Overview

Telegra.ph API is a simple, anonymous publishing platform by Telegram for creating and editing public pages via HTTP requests, useful in security ops for exfiltrating or storing dynamic data like URLs without authentication beyond an access token.

## Description

The API allows GET/POST to endpoints like /createPage and /editPage, supporting HTML content with parameters for title, author, and content array. In attacks, it's leveraged to update a public page with sensitive info (e.g., fresh tokens) for remote access, as seen in automating persistent exploits.

## Features

- Feature 1: Anonymous page creation/editing
- Feature 2: JSON API for content updates
- Feature 3: Public read access without login

## Installation

### Requirements

- HTTP client (browser JS, curl, etc.)
- Access token from Telegra.ph account

### Install Commands

No installation; API-only:

```bash
# Example curl
curl "https://api.telegra.ph/createPage" -d '{"title":"Test","content":[]}' -H "Content-Type: application/json"
```

## Basic Usage

```bash
curl -X GET "https://api.telegra.ph/editPage/Page-Title?access_token=TOKEN&content=[{"tag":"p","children":["Text"]}]"
```

### Common Options

| Option | Description |
|--------|-------------|
| access_token | Token for edit access |
| title | Page title |
| content | Array of HTML elements |

## Examples

### Example 1: Basic Usage

Create page:
```bash
curl -d '{"title":"Test","author_name":"Anon","content":[{"tag":"p","children":["Hello"]}]}' https://api.telegra.ph/createPage
```

### Example 2: Advanced Usage

Edit with URL: As in iMacros EVAL for updating with encoded window.location.href.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Archive Collected Data]]
- [[Automated Exfiltration]]

### Tactics

- [[Exfiltration]]
- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- API calls from browser sessions to telegra.ph
- Public pages with encoded URLs/tokens
- Frequent edits to same page from suspicious IPs

## Related Procedures

- [[procedures/Automate-Persistent-Access-with-iMacros]]

## Related Tools

- [[Pastebin]]
- [[GitHub Gist]]

## References

- API docs: https://telegra.ph/api
- Example page: https://telegra.ph/
