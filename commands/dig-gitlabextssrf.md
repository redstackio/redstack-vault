---
data: dig +noall +answer gitlabextssrf.webhooks.pw
tags:
  - dns
  - rebinding
type: command
executor: bash
platforms:
  - Linux
id: 65ec9d5b-7f61-4673-9fbc-b3c83e234878
created_at: '2025-12-14T03:46:09.469Z'
updated_at: '2025-12-14T03:46:09.469Z'
verified: false
validated: true
submitted: true
---
# dig-gitlabextssrf

## Command

```bash
dig +noall +answer gitlabextssrf.webhooks.pw
```

## Description

Queries DNS for the custom domain used in ToCToU exploitation, demonstrating alternating IP resolutions for rebinding attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +noall | Suppress non-answer sections | Yes |
| +answer | Show only answer section | Yes |
| gitlabextssrf.webhooks.pw | Domain to resolve | Yes |

## Examples

### Basic Usage

```bash
dig +noall +answer gitlabextssrf.webhooks.pw
```

### Advanced Usage

```bash
dig +short gitlabextssrf.webhooks.pw
```

## Expected Output

Alternating A records: e.g., 198.211.125.160 or 127.0.0.1 with 0 TTL.

## Related

- [[Related Procedure]]
