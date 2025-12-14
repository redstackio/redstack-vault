---
tags:
  - graphql
  - introspection
  - schema-disclosure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:53.225Z'
sub_techniques: []
id: 4adca72d-4b33-49db-8201-8603d90cda04
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Observe-GraphQL-Schema-Dump

## Summary

This procedure captures and analyzes the response from the GraphQL introspection query sent via the WebSocket connection, revealing the complete API schema for reconnaissance.

## Description

The PoC automatically sends an introspection query in the WebSocket message payload, which queries the __schema field to extract all types, fields, queries, mutations, and directives. Due to the lack of authentication on 'start' type messages, the server responds with the full schema, enabling attackers to map the API for targeted exploits like query injection or data exfiltration.

## Requirements

1. Active WebSocket connection from previous step
2. PoC HTML loaded with introspection query scripted
3. Browser developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Disable GraphQL introspection in production
- Enforce auth on all query executions, including WebSocket
- Log introspection attempts and alert on schema queries

## Objectives

1. Receive and display the full GraphQL schema
2. Identify API methods and data types for further attacks
3. Validate the vulnerability exploitation

## Instructions

### Step 1: Trigger Query

**Context**: The PoC sends the query upon connection; observe the transmission.

The JavaScript in ws.html sends: {type: 'start', payload: {query: 'query IntrospectionQuery { __schema { ... } }'}} via WebSocket.

> No manual action needed; watch for the send event in console.

### Step 2: Capture and Review Response

**Context**: Parse the incoming WebSocket message containing the schema JSON.

The PoC displays the response on the page or in console. Copy and analyze the JSON for types like Query, Mutation, and custom objects.

> Expected: Detailed schema with all endpoints, e.g., {"data": {"__schema": {"types": [...]}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- graphql
- introspection
- schema-disclosure
