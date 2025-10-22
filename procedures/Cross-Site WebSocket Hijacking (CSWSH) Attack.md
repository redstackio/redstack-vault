---
id: 06bada19-edae-4f39-8ca5-9776185df6f9
name: Cross-Site WebSocket Hijacking (CSWSH) Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.354897+00:00'
updated_at: '2023-04-06T03:56:41.378830+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Cross-Site WebSocket Hijacking (CSWSH)]]'
- '[[Web Sockets]]'
commands:
- '[[Check Sec-WebSocket-Protocol header]]'
- '[[Creating a WebSocket server]]'
- '[[Handling WebSocket connection]]'
- '[[Installation of WebSocket package]]'
---

# Cross-Site WebSocket Hijacking (CSWSH) Attack

## Summary

The Cross-Site WebSocket Hijacking (CSWSH) attack is a type of attack that allows an attacker to hijack a WebSocket session between a client and a server. This attack can be used to gain access to sensitive information or to execute arbitrary code on the server. The attack works by tricking the cli

## Description

# Description

The Cross-Site WebSocket Hijacking (CSWSH) attack is a type of attack that allows an attacker to hijack a WebSocket session between a client and a server. This attack can be used to gain access to sensitive information or to execute arbitrary code on the server. The attack works by tricking the client into sending a WebSocket request to the server that includes a malicious payload. When the server receives the request, it processes the payload and executes the attacker's code. This attack can be particularly dangerous because it can be executed from a remote location, and the attacker can remain anonymous.

From a technical perspective, the CSWSH attack works by exploiting the fact that WebSocket requests are not bound to the same-origin policy. This means that a WebSocket request can be sent to a different domain than the one that served the original web page. The attacker can use this to their advantage by crafting a WebSocket request that appears to come from a legitimate source, but actually includes a malicious payload.

The business value of this attack is that it can be used to gain access to sensitive information or to execute arbitrary code on the server. This can result in a data breach, loss of intellectual property, or disruption of business operations.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of WebSocket protocol

1. Ability to craft a malicious WebSocket request

## Defense

1. Use strict Cross-Origin Resource Sharing (CORS) policies to limit which domains can access the WebSocket server

1. Implement proper input validation and sanitization to prevent injection attacks

1. Use encryption to protect the WebSocket traffic from interception and tampering

## Objectives

1. To gain access to sensitive information

1. To execute arbitrary code on the server

# Instructions

1. To prevent Cross-Site WebSocket Hijacking (CSWSH) attack, ensure that the WebSocket handshake is protected using a CSRF token or a nonce. Always validate the origin of the WebSocket request and ensure that the WebSocket connections are authenticated and authorized.

**Code**: [[<script>
  ws = new WebSocket('wss://vulnerable.ex]]

> The given code snippet demonstrates how an attacker can exploit a Cross-Site WebSocket Hijacking (CSWSH) vulnerability to steal sensitive information from a user's authenticated WebSocket connection. The attacker sets up a WebSocket connection to the vulnerable server and sends a message to the server. The server sends a reply which is intercepted by the attacker. The attacker then sends the intercepted data to their own server using the fetch API. As the cookies are automatically sent by the browser, the attacker can use the authenticated WebSocket connection of the user on their own controlled site. This attack can be prevented by using a CSRF token or a nonce to protect the WebSocket handshake and by validating the origin of the WebSocket request.

2. To configure the Sec-WebSocket-Protocol, follow the below instructions:

**Code**: [[Sec-WebSocket-Protocol]]

> 1. Identify the websocket protocol used by your web application.
2. Adjust the code accordingly to your exact situation.
3. Replace the 'Sec-WebSocket-Protocol' field with the identified protocol.
4. Save and test the configuration to ensure it's working as expected.

**Command** ([[Check Sec-WebSocket-Protocol header]]):

```bash
Sec-WebSocket-Protocol
```

3. To add a WebSocket header in the handshake request, use the following command:

**Code**: [[WebSocket]]

> The WebSocket header is used to send additional information in the handshake request. To add it, use the 'WebSocket' object and provide the header value as the second parameter in the 'new WebSocket(url, protocols)' constructor. The 'protocols' parameter is optional and can be used to specify the sub-protocols that the client and server can use to communicate.

**Command** ([[Installation of WebSocket package]]):

```bash
npm install --save ws
```

**Command** ([[Creating a WebSocket server]]):

```bash
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });
```

**Command** ([[Handling WebSocket connection]]):

```bash
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
  ws.send('something');
});
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Check Sec-WebSocket-Protocol header]]
- [[Creating a WebSocket server]]
- [[Handling WebSocket connection]]
- [[Installation of WebSocket package]]

## Tags

- [[Cross-Site WebSocket Hijacking (CSWSH)]]
- [[Web Sockets]]
