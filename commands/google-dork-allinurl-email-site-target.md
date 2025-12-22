---
data: 'allinurl:@<mailbox_domain> site:<target_domain>'
tags:
  - dorking
  - recon
  - leak-detection
type: command
output: Results showing leaked emails or sensitive info in URLs
executor: google
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.750Z'
id: 528e4b44-5cc3-4951-b677-21966a8a3ad3
verified: false
validated: true
submitted: true
---
# google-dork-allinurl-email-site-target

## Command

Search query:
```
allinurl:@<mailbox_domain> site:<target_domain>
```

## Description

This Google dork finds URLs on a target domain containing email addresses from a specific mailbox domain, useful for discovering leaked credentials or sensitive info embedded in URLs, as seen in reports of privileged information indexing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| allinurl:@<mailbox_domain> | Searches for URLs containing '@' followed by the mailbox domain (e.g., @example.com) | Yes |
| site:<target_domain> | Limits search to the target domain (e.g., site:grabtaxi.com) | Yes |

## Examples

### Basic Usage

```
allinurl:@gmail.com site:example.com
```

### Advanced Usage

Combine with other operators: `allinurl:@gmail.com site:example.com intext:token`

## Expected Output

List of search results with URLs embedding emails, potentially revealing sensitive leaks like auth tokens or private data.

## Related

- [[commands/google-dork-passenger-site-grab]]
- [[procedures/Verify-Search-Engine-Indexing-with-Google-Dorks]]
