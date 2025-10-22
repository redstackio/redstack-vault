---
id: f90a07af-7dda-4430-af48-7edc68efc62d
name: hts
type: tool
verified: false
created_at: '2019-08-28T21:17:30.366693+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# hts

## Overview

HTTPTunnel is a tunneling software that can tunnel network connections through restrictive HTTP proxies over pure HTTP “GET” and “POST” requests. HTTPTunnel consists of two components: The client that resides behind the firewall and accepts network connections on ports that will either be mapped to

## Description

HTTPTunnel is a tunneling software that can tunnel network connections through restrictive HTTP proxies over pure HTTP “GET” and “POST” requests. HTTPTunnel consists of two components: 

The client that resides behind the firewall and accepts network connections on ports that will either be mapped to a specific remote target server/port (portmapping) or will act as a SOCKS (v4 and v5) proxy. The SOCKS authentication source can be a fixed user list, an LDAP or MySQL directory. The client is available as platform-independent Perl script or as Win32 binary.

The server that resides on the internet and accepts HTTP requests from the client which will be translated and forwarded to network connections to the remote servers.

Two different servers are available: 

The hosted server, which is basically a PHP script that must be put on a PHP enabled web server. Putting the PHP script on a webserver enables the webserver to act as your HTTP tunnel server.

The standalone server, which is available as platform-independent Perl script or as Win32 binary. This server can be used if you have a box on the internet where you can run your own programs (e.g. your box at home). Using the standalone server (as opposed to the hosted server) is recommended as it does not suffer from many restrictions that the webserver may impose on the PHP script, e.g. maximum script runtime (which will limit the duration of your connections), load-balanced server environments, provider policies etc.

Configuration of all components is done over a web-based GUI. SOCKS proxy cascading is supported.
