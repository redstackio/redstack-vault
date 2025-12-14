---
data: 'curl -u ''434762629765715:█████'' https://api.cloudinary.com/v1_1/reverb/usage'
tags:
  - api
  - cloudinary
  - usage
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cbcadf64-a819-429f-ba97-e65e7cf1b1ec
created_at: '2025-12-14T17:32:48.322Z'
updated_at: '2025-12-14T17:32:48.322Z'
verified: false
validated: true
submitted: true
---
# cloudinary-usage-api-call

## Command

```bash
curl -u '434762629765715:█████' https://api.cloudinary.com/v1_1/reverb/usage
```

## Description

This command performs a GET request to the Cloudinary usage endpoint using basic authentication to retrieve account statistics, demonstrating access after credential extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Basic auth credentials (api_key:api_secret) | Yes |
| URL | Endpoint with cloud_name (e.g., /v1_1/reverb/usage) | Yes |

## Examples

### Basic Usage

```bash
curl -u 'api_key:api_secret' https://api.cloudinary.com/v1_1/cloud_name/usage
```

### Advanced Usage

```bash
curl -u 'api_key:api_secret' -H "Accept: application/json" https://api.cloudinary.com/v1_1/reverb/usage
```

## Expected Output

JSON object with usage metrics: {"requests":1894689201,"resources":36029794,"derived_resources":256178843}. Errors include 401 for invalid auth.

## Related

- [[Related Procedure]]
