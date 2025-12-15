---
id: cmd-curl-api-test
data: >-
  curl
  "https://api.planet.com/basemaps/v1/mosaics?api_key=KEY_HERE&_page_size=1000"
tags:
  - api-testing
  - credential-validation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.319Z'
verified: false
validated: true
submitted: true
---
# curl-api-key-test

## Command

```bash
curl "https://api.planet.com/basemaps/v1/mosaics?api_key=KEY_HERE&_page_size=1000"
```

## Description

Tests an API key by sending a GET request to the Planet Labs basemaps endpoint; used to validate if exposed keys grant access to resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` (implied) | Full API endpoint with api_key param | Yes |
| `_page_size` | Number of results to fetch | No |

## Examples

### Basic Usage

```bash
curl "https://api.planet.com/basemaps/v1/mosaics?api_key=afdb1e8a9c8142739553e3942283d6c8&_page_size=1000"
```

### Advanced Usage

For WMTS:

```bash
curl "https://api.planet.com/basemaps/v1/mosaics/wmts?service=wmts&request=GetCapabilities&format=text%2Fxml&api_key=8fe044edc78c46ba904bb62e550493a3"
```

## Expected Output

JSON array of mosaics for valid keys; error JSON like {"message": "Unauthorized"} for invalid.

## Related

- [[Related Procedure: Extract-and-Validate-Exposed-API-Keys]]
