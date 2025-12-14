---
data: cat subdomains.txt | httpx -silent -o live-subdomains.txt
tags:
  - probe
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.209Z'
id: 28da66dd-ac92-406f-a00e-5ae85173d9bd
verified: false
validated: true
submitted: true
---
# httpx-probe

## Command

```bash
cat subdomains.txt | httpx -silent -o live-subdomains.txt
```

## Description

Probes a list of subdomains to check for live HTTP/HTTPS responses, filtering out dead hosts during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-silent` | Suppress extra output | No |
| `-o` | Output file | Yes |

## Examples

### Basic Usage

```bash
httpx -l subdomains.txt -o live.txt
```

### Advanced Usage

```bash
httpx -l subdomains.txt -status-code -title -o live.txt
```

## Expected Output

List of responding subdomains with status codes.

## Related

- [[Related Procedure: Enumerate Subdomains for Takeover]]
