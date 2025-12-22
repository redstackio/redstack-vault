---
id: 561d5b22-fc50-48dd-ab8a-b95f1de4177a
name: dig-dns-lookup-for-rebinding-domain
type: command
executor: bash
data: dig $_REBIND_DOMAIN +noall +answer
output: null
created_at: '2023-04-06T03:55:57.655647+00:00'
updated_at: '2024-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - dns
  - rebinding
verified: true
validated: true
---

# Dig-DNS-Lookup-for-Rebinding-Domain

## Command

```bash
dig $_REBIND_DOMAIN +noall +answer
```

## Description

This command uses the dig utility to perform a targeted DNS lookup on the rebinding domain, retrieving only the answer section to verify resolution records like A or CNAME pointing to localhost. It is essential for testing the dynamic DNS behavior in a rebinding setup, ensuring the domain resolves correctly for the initial and rebinding phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REBIND_DOMAIN | The domain name configured for the rebinding attack (e.g., www.example.com) | Yes |
| +noall | Suppresses all output except the answer section for concise results | Built-in |
| +answer | Displays only the answer section of the DNS response | Built-in |

## Examples

### Basic Usage

```bash
dig www.example.com +noall +answer
```

This queries the domain and shows the resolution record.

### Advanced Usage

```bash
dig @$_DNS_SERVER www.example.com +noall +answer +short
```

Specifies a custom DNS server and uses +short for even more minimal output.

## Expected Output

The command produces a streamlined DNS answer, indicating successful resolution. For a rebinding test showing a CNAME to localhost:

```
localhost.example.com.            381     IN      CNAME   localhost.
```

If the setup is working, repeated executions should show varying records (e.g., initial A to attacker IP, subsequent to localhost). Errors like NXDOMAIN indicate misconfiguration.

## Related

- [[procedures/DNS-Rebinding-to-Localhost]]
