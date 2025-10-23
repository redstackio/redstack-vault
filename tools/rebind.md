---
id: 5188e0d0-3400-44f1-84d6-d37655037e65
name: rebind
type: tool
verified: false
created_at: '2019-08-28T21:17:30.797003+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# rebind

## Overview

Rebind is a tool that implements the multiple A record DNS rebinding attack. Although this tool was originally written to target home routers, it can be used to target any public (non RFC1918) IP address. Rebind provides an external attacker access to a target router’s internal Web interface. This 

## Description

Rebind is a tool that implements the multiple A record DNS rebinding attack. Although this tool was originally written to target home routers, it can be used to target any public (non RFC1918) IP address. Rebind provides an external attacker access to a target router’s internal Web interface. This tool works on routers that implement the weak end system model in their IP stack, have specifically configured firewall rules, and who bind their Web service to the router’s WAN interface. Note that remote administration does not need to be enabled for this attack to work. All that is required is that a user inside the target network surf to a Web site that is controlled, or has been compromised, by the attacker.






