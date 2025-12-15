---
id: tool-1
url: 'https://github.com/cloudflare/cfssl'
tags:
  - cert
  - pki
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.476Z'
validated: true
submitted: true
---
# cfssl

**Status**: Unverified

## Overview

CFSSL is a PKI toolkit for generating TLS certificates and CAs, commonly used in Kubernetes for forging or managing certs in security testing.

## Description

CFSSL provides commands like gencert for signing CSRs with custom profiles, enabling creation of trusted certificates for auth bypass in x509-based systems like Kubernetes API servers.

## Features

- Feature 1: CSR generation and signing with profiles (e.g., kubernetes for O=system:masters)
- Feature 2: JSON config for custom extensions and SANs
- Feature 3: Integration with cfssljson for PEM output

## Installation

### Requirements

- Go 1.16+

### Install Commands

```bash
# From GitHub
go install github.com/cloudflare/cfssl/cmd/cfssl@latest
go install github.com/cloudflare/cfssl/cmd/cfssljson@latest
```

## Basic Usage

```bash
cfssl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-version` | Show version |
| `--config` | Config file |

## Examples

### Example 1: Basic Usage

```bash
cfssl gencert -initca ca-csr.json | cfssljson -bare ca
```

### Example 2: Advanced Usage

```bash
cfssl gencert -ca=ca.pem -ca-key=ca.key -profile=kubernetes client-csr.json | cfssljson -bare client
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Certificate

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

- Monitor for cfssl binaries or processes in container images
- Detect unusual certificate generation in logs
- Scan for cfssl in pentest toolkits

## Related Procedures

- [[procedures/Forge-System-Masters-Certificate]]

## Related Tools

- [[tools/openssl]]
- [[tools/easy-rsa]]

## References

- Official documentation: https://cfssl.org/
- Related resources: Kubernetes PKI docs
