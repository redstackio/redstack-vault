---
id: cmd-2552243-curl-poc
data: 'curl http://$SUBDOMAIN/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt'
tags:
  - web
  - verification
type: command
output: 'POC content: This subdomain is under attacker control via takeover.'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.661Z'
verified: false
validated: true
submitted: true
---
# curl-access-poc

## Command

```bash
curl http://$SUBDOMAIN/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
```

## Description

This command uses curl to fetch a proof-of-concept file from the taken-over subdomain, verifying attacker control and potential for hosting malicious content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://$SUBDOMAIN` | URL of the taken-over subdomain | Yes |
| `/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt` | Path to the POC file | Yes |

## Examples

### Basic Usage

```bash
curl http://█████.defense.gov/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
```

### Advanced Usage

```bash
curl -v http://█████.defense.gov/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
```

## Expected Output

Returns the content of the POC file served from the subdomain, indicating successful takeover.

## Related

- [[Related Procedure: Verify Subdomain Takeover with POC]]
