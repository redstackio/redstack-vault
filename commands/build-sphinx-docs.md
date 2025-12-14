---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: cd docs && make html
tags:
  - build
  - documentation
type: command
output: null
executor: bash
platforms:
  - Python
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:31.338Z'
verified: false
validated: true
submitted: true
---
# build-sphinx-docs

## Command

```bash
cd docs && make html
```

## Description

Navigates to the documentation directory and builds HTML output using Sphinx, triggering the vulnerable jQuery processing in fabric-sdk-py.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cd docs` | Changes to docs directory | Yes |
| `make html` | Invokes Makefile to generate HTML | Yes |

## Examples

### Basic Usage

```bash
cd docs && make html
```

### Advanced Usage

```bash
cd docs && make clean html  # Clean previous build first
```

## Expected Output

Build logs showing reST file processing, ending with 'build succeeded, output in _build/html'. No errors if payload is valid.

## Related

- [[Related Procedure: Demonstrate-XSS-in-fabric-sdk-py-Doc-Generation]]
