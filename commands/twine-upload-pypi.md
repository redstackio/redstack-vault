---
id: cmd-001
data: twine upload dist/*
tags:
  - upload
  - pypi
type: command
output: |-
  Uploading distributions to https://upload.pypi.org/legacy/
  Enter your username: __token__
  Enter your password: 
  Uploading yelp-cgeom-1.0.0.tar.gz
  100% |████████████████████| 1.2k/1.2k [00:01<00:00, 1.2kB/s]
  View at https://pypi.org/project/yelp-cgeom/1.0.0/
executor: bash
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:17.624Z'
verified: false
validated: true
submitted: true
---
---
# twine-upload-pypi

## Command

```bash
twine upload dist/*
```

## Description

Uploads built Python package distributions to PyPI using twine, enabling publication of malicious packages for dependency confusion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `dist/*` | Path to built distributions (sdist, wheel) | Yes |

## Examples

### Basic Usage

```bash
twine upload dist/*
```

### Advanced Usage

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

## Expected Output

Success message with upload progress and PyPI project URL.

## Related

- [[Related Procedure: Claim-and-Upload-Malicious-PyPI-Package]]
---
