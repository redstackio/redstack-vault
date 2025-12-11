---
data: >-
  await
  fetch("/import/bulk_imports.json",{method:"POST",headers:{"X-CSRF-Token":
  document.querySelector("[name=csrf-token]").content,"Content-Type":"application/json"},body:`{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"vakzz","destination_slug":"some_project_z_${Math.floor(Math.random()*10000)"}]};`});
tags:
  - fetch
  - api
  - gitlab
type: command
executor: javascript
platforms:
  - Web
id: 2872d5d3-3d3f-4d44-abdf-cc9095ffeafd
created_at: '2025-12-11T03:47:59.480Z'
updated_at: '2025-12-11T03:47:59.480Z'
verified: false
validated: true
submitted: true
---
# browser-fetch-bulk-import

## Command

```javascript
await fetch("/import/bulk_imports.json",{method:"POST",headers:{"X-CSRF-Token": document.querySelector("[name=csrf-token]").content,"Content-Type":"application/json"},body:`{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"vakzz","destination_slug":"some_project_z_${Math.floor(Math.random()*10000)"}]};`});
```

## Description

Sends a POST request to GitLab's bulk import endpoint to trigger repository import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `body` | JSON payload for import | Yes |
| `headers` | CSRF token and content type | Yes |

## Examples

### Basic Usage

Execute in browser console after navigating to import page.

### Advanced Usage

Modify payload for different sources/destinations.

## Expected Output

Response object indicating success (e.g., 201 Created), followed by project creation.

## Related

- [[procedures/Initiate-Bulk-Import-via-Browser-Console-to-Clone-Repository]]
- [[commands/flask-run-fake-server]]
