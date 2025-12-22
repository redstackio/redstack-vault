---
id: cmd-google-dork-mtn-001
data: 'google search: site:admyntec.co.za intitle:"MTN"'
tags:
  - recon
  - dorking
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.497Z'
verified: false
validated: true
submitted: true
---
# google-dork-mtn-site

## Command

```bash
google search: site:admyntec.co.za intitle:"MTN"
```

## Description

Google dork to find MTN-related pages on admyntec.co.za, used for initial recon to spot potential vulnerable endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| site:admyntec.co.za | Limits to domain | Yes |
| intitle:"MTN" | Pages with MTN in title | Yes |

## Examples

### Basic Usage

```bash
google search: site:admyntec.co.za intitle:"MTN"
```

### Advanced Usage

```bash
google search: site:admyntec.co.za intitle:"MTN" inurl:customer
```

## Expected Output

Search results listing URLs with MTN in title, e.g., admin pages with parameters.

## Related

- [[commands/sqlmap-exploit-url]]
