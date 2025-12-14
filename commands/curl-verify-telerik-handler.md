---
data: 'curl -sk https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau'
tags:
  - recon
  - web
type: command
output: >-
  {"message": "RadAsyncUpload handler is registered successfully, however, it
  may not be accessed directly."}
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.439Z'
id: a0f5b567-f4c9-4e5f-9d00-ce9b9fcc4112
verified: false
validated: true
submitted: true
---
# curl-verify-telerik-handler

## Command

```bash
curl -sk https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau
```

## Description

Sends a GET request to verify if the Telerik RadAsyncUpload handler is registered, essential for CVE-2019-18935 exploitation. Use when probing ASP.NET apps for vulnerable endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL certificate validation | Yes |
| `-s` | Silent mode, no progress output | Yes |
| URL | Target handler endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -sk https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau
```

### Advanced Usage

```bash
curl -sk -H "User-Agent: Mozilla/5.0" https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau
```

## Expected Output

JSON response confirming handler registration, indicating vulnerability potential.

## Related

- [[procedures/Verify-Telerik-Upload-Handler-Registration]]
