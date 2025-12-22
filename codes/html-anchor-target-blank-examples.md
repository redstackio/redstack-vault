---
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:40Z'
updated_at: '2023-04-06T03:56:40Z'
platforms:
  - Web
tags:
  - phishing
  - tabnabbing
  - html
validated: true
---

# html-anchor-target-blank-examples

## Code

```html
<a href="..." target="_blank" rel="" />  
or
<a href="..." target="_blank" />
```

## Description

These HTML anchor tag examples demonstrate insecure link formats commonly associated with Tabnabbing phishing attacks. The first includes an empty `rel` attribute, and the second omits `rel` entirely. Both use `target="_blank"` without `noopener noreferrer`, allowing the linked page to access and potentially manipulate the originating window via `window.opener`. Use these as reference patterns when hunting for vulnerabilities in web content.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `...` | Placeholder for the target URL | `https://malicious-site.com` |

## Usage

Embed these in test HTML files to simulate and verify Tabnabbing behavior during security assessments. In hunting scenarios, search for matching patterns in source code or traffic to flag risky links. Always test in an isolated environment to avoid real exploitation.

## Detection

- Grep or regex searches in HTML/logs for `target="_blank"` without `rel="noopener noreferrer"`.
- Browser dev tools: Inspect elements and check for `window.opener` access.
- WAF logs: Alert on outbound content with these patterns.
- JavaScript monitoring: Detect blur/focus events combined with document writes.

## Related

- [[procedures/Hunt-for-Tabnabbing-Enabling-Links]]
