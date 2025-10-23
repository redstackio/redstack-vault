---
id: 84376964-db60-4d55-a45b-552b5e0b9b7a
name: dns2tcpc
type: tool
verified: false
created_at: '2019-08-28T21:17:21.227582+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# dns2tcpc

## Overview

Dns2tcp is a network tool designed to relay TCP connections through DNS traffic. Encapsulation is done on the TCP level, thus no specific driver is needed (i.e: TUN/TAP). Dns2tcp client doesn’t need to be run with specific privileges.Dns2tcp is composed of two parts : a server-side tool and a clien

## Description

Dns2tcp is a network tool designed to relay TCP connections through DNS traffic. Encapsulation is done on the TCP level, thus no specific driver is needed (i.e: TUN/TAP). Dns2tcp client doesn’t need to be run with specific privileges.Dns2tcp is composed of two parts : a server-side tool and a client-side tool. The server has a list of resources specified in a configuration file. Each resource is a local or remote service listening for TCP connections. The client listen on a predefined TCP port and relays each incoming connection through DNS to the final service.






