---
data: rdoc
tags:
  - execution
  - rce
type: command
executor: bash
platforms:
  - Ruby
id: 93b403cd-4012-415d-9f48-f86457f70daa
created_at: '2025-12-14T17:23:42.414Z'
updated_at: '2025-12-14T17:23:42.414Z'
verified: false
validated: true
submitted: true
---
# rdoc-execute

## Command

```bash
rdoc
```

## Description

Runs RDoc to generate Ruby documentation, parsing `.rdoc_options` and cache files, which can trigger deserialization vulnerabilities leading to RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default execution in current directory | No |

## Examples

### Basic Usage

```bash
rdoc
```

### Advanced Usage

```bash
rdoc --op /output/dir
```

## Expected Output

Documentation generation output, potentially with command execution (e.g., date output) and errors like "no implicit conversion of nil into String" if exploited.

## Related

- [[commands/rdoc-version-check]]
