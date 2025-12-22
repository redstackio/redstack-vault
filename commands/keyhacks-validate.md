---
id: uuid-for-keyhacks-command
data: python keyhacks.py --google-maps AIzaSyD_example_key
tags:
  - validation
  - api-keys
type: command
output: >-
  Key is valid. Project: Example App. Quota: High. Permissions: Maps SDK,
  Geocoding.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.115Z'
verified: false
validated: true
submitted: true
---
# keyhacks-validate

## Command

```bash
python keyhacks.py --google-maps AIzaSyD_example_key
```

## Description

Validates a suspected Google Maps API key by querying Google's endpoints to check validity, associated project, quotas, and permissions, helping assess exploitability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--google-maps` | Flag for Google Maps key validation | Yes |
| `AIzaSyD_example_key` | The API key to test | Yes |

## Examples

### Basic Usage

```bash
python keyhacks.py --google-maps AIzaSy...
```

### Advanced Usage

```bash
python keyhacks.py --mapbox pk.eyJ1...  # For MapBox keys
```

## Expected Output

JSON or text output detailing key status, e.g., 'Valid: True, Permissive: Yes'.

## Related

- [[Related Procedure: Search-for-Hardcoded-API-Keys-in-Decompiled-Files]]
