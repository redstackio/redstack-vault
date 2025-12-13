---
data: 'curl -s https://target-ghes.example.com/saml/metadata -o metadata.xml'
tags:
  - recon
  - saml
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c8c4895e-932e-4b3c-98df-84436a62d257
created_at: '2025-12-13T09:01:26.749Z'
updated_at: '2025-12-13T09:01:26.749Z'
verified: false
validated: true
submitted: true
---
# Fetch SAML Metadata

## Command

```bash
curl -s https://target-ghes.example.com/saml/metadata -o metadata.xml
```

## Description

This command downloads the SAML metadata XML from a GitHub Enterprise Server instance for analysis in vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | No |
| `https://target-ghes.example.com/saml/metadata` | URL of metadata endpoint | Yes |
| `-o metadata.xml` | Output file | Yes |

## Examples

### Basic Usage

```bash
curl -s https://target-ghes.example.com/saml/metadata -o metadata.xml
```

### Advanced Usage

```bash
curl -s -H 'User-Agent: Custom' https://target-ghes.example.com/saml/metadata -o metadata.xml
```

## Expected Output

A downloaded metadata.xml file containing SAML configuration details.

## Related
- [[procedures/Identify-Vulnerable-GHES-Instance]]
- [[commands/submit-saml-response]]
