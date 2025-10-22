---
id: 1e8dfbbe-bca8-4c0a-bd82-d31d87798853
name: GraphQL Edge/Node Data Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.821292+00:00'
updated_at: '2023-04-10T20:22:23.622904+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Exploit]]'
- '[[Extract data using edges/nodes]]'
- '[[GraphQL Injection]]'
commands:
- '[[Send GraphQL query]]'
---

# GraphQL Edge/Node Data Extraction

## Summary

GraphQL is a query language for APIs that allows clients to request only the data they need, making it more efficient than traditional REST APIs. However, it can also be vulnerable to injection attacks, allowing an attacker to extract sensitive data. This procedure demonstrates how to exploit a Gra

## Description

# Description

GraphQL is a query language for APIs that allows clients to request only the data they need, making it more efficient than traditional REST APIs. However, it can also be vulnerable to injection attacks, allowing an attacker to extract sensitive data. This procedure demonstrates how to exploit a GraphQL injection vulnerability to extract data using edges/nodes. By injecting malicious code into the 'query' parameter, an attacker can extract data from the GraphQL API using edges/nodes, which are used to traverse the data graph. This technique can be used to extract data from a variety of sources, including databases, file systems, and APIs.

## Requirements

1. Access to a vulnerable GraphQL API

## Defense

1. Implement input validation and sanitization to prevent injection attacks.

1. Limit the scope of the GraphQL API to only expose necessary data.

1. Monitor GraphQL API access logs for suspicious activity.

## Objectives

1. Extract sensitive data from a GraphQL API using edges/nodes

# Instructions

1. To extract data using edges/nodes, follow these steps:
1. Identify a vulnerable GraphQL API.
2. Use a tool like GraphiQL to explore the API and identify the data graph.
3. Craft a malicious query that injects code into the 'query' parameter.
4. Use edges/nodes to traverse the data graph and extract sensitive data.

**Code**: [[{
  "query": "query {
    teams{
      total_count]]

> The 'query' parameter is used to specify the GraphQL query. By injecting malicious code into this parameter, an attacker can modify the query to extract sensitive data using edges/nodes. In the provided example, the 'teams' query is used to extract data from the GraphQL API. The 'total_count' field returns the total number of teams, while the 'edges' field returns an array of team objects. The 'node' field is used to extract specific fields from each team object, including the 'id', '_id', 'about', 'handle', and 'state' fields. By using edges/nodes, an attacker can traverse the data graph and extract sensitive data from the GraphQL API.

**Command** ([[Send GraphQL query]]):

```bash
{
  "query": "query {
    teams{
      total_count,edges{
        node{
          id,_id,about,handle,state
        }
      }
    }
  }"
}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Send GraphQL query]]

## Tags

- [[Exploit]]
- [[Extract data using edges/nodes]]
- [[GraphQL Injection]]
