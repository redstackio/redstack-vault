---
id: 123e4567-e89b-12d3-a456-426614174005
name: Verify-Workflow-Creation-and-Activation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.802Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - verification
  - graphql-query
  - shopify
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Verify-Workflow-Creation-and-Activation

## Summary

Queries the GraphQL endpoint to confirm workflow installation and activation, validating the exploit's success and noting invisibility in standard UI.

## Description

After activation, workflows created via the internal endpoint do not appear in the Shopify Flow app, allowing hidden automations. This step retrieves details to verify impact.

## Requirements

1. workflowId from installation
2. Active session in Burp
3. Knowledge of expected automation (e.g., tagging)

## Defense

Defensive measures and detection strategies:

- Sync internal workflows to UI for visibility
- Alert on query patterns for hidden workflows
- Periodic audits of GraphQL query logs

## Objectives

1. Retrieve workflow state post-activation
2. Confirm unauthorized modifications possible
3. Highlight persistence of hidden automations

## Instructions

### Step 1: Craft Verification Query

**Context**: Use GraphQL query to fetch workflow by ID.

**Instructions**: Set body to {"query": "query { workflow(id: \"gid://shopify/FlowWorkflow/240ed0ee-d099-4066-8eac-7ce777ef4fe4\") { id name activationState steps { ... } } "} (include fragments as needed).

> Send via Repeater.

### Step 2: Analyze Output

**Context**: Check for active state and details.

**Instructions**: Parse response for activationState: ACTIVE and any errors.

> Expected: Details confirming creation; test by registering a customer to see tagging.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[verification]]
- [[graphql-query]]
- [[shopify]]
