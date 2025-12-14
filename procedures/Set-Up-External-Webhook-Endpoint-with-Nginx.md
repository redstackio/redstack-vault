---
id: proc-nginx-webhook-001
tags:
  - webhook
  - nginx
  - tls
type: procedure
tools:
  - '[[tools/nginx]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:32:01.442Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Connection Proxy]]'
---
# Set-Up-External-Webhook-Endpoint-with-Nginx

## Summary

This procedure deploys an nginx-based TLS endpoint on a GCE VM to act as an external Validating Webhook receiver, logging incoming admission reviews and always allowing requests to facilitate the DoS test without blocking legitimate operations.

## Description

To exploit the webhook mechanism, an external server must be set up to handle HTTPS requests from the Kubernetes API Server. Nginx is configured with a custom nginx.conf to listen on ports 80 and 443, set client_max_body_size to 5M for large payloads, and proxy /validator requests to an /ok endpoint that returns a JSON response {'response': {'allowed': true}}. The VM needs a public IP for accessibility, and TLS certificates are assumed self-signed or provided. Logs are formatted to capture request details for verification.

## Requirements

1. GCE VM with public IP in the same region as GKE
2. Nginx installed on Ubuntu/Debian Linux
3. TLS certificate for the domain (e.g., docker.lonimbus.com)
4. Firewall rules allowing 80/443 inbound

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound connections from API Server to external IPs
- Use webhook failurePolicy: Fail instead of Ignore to block suspicious configs
- Implement rate limiting on webhook endpoints

## Objectives

1. Provide a responsive external endpoint for webhook calls
2. Log large payload transmissions for analysis
3. Ensure low-latency responses to avoid timeouts

## Instructions

### Step 1: Provision GCE VM

**Context**: Create a VM instance for hosting nginx.

**Command** ([[commands/gcloud-compute-instances-create]]):
```bash
gcloud compute instances create webhook-vm --zone=us-central1-c --machine-type=e2-medium --image-family=ubuntu-2004-lts --image-project=ubuntu-os-cloud --tags=webhook
```

> Creates VM; expected output: Instance created.

### Step 2: Install and Configure Nginx

**Context**: SSH to VM and set up nginx with custom config.

**Command** ([[commands/apt-install-nginx]]):
```bash
sudo apt update && sudo apt install -y nginx openssl
```

> Installs nginx; expected output: nginx installed.

Create nginx.conf with:

```nginx
server {
    listen 80;
    listen 443 ssl;
    server_name docker.lonimbus.com;
    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;
    client_max_body_size 5M;
    location /validator {
        proxy_pass http://localhost/ok;
        access_log /var/log/nginx/webhook.log custom;
    }
    location /ok {
        return 200 '{"response": {"allowed": true}}';
        default_type application/json;
    }
}
log_format custom '$remote_addr - $request_time - $body_bytes_sent';
```

Then:

**Command** ([[commands/nginx-reload]]):
```bash
sudo cp nginx.conf /etc/nginx/sites-available/default && sudo nginx -t && sudo systemctl reload nginx
```

> Reloads config; expected output: Test successful, reloaded.

### Step 3: Generate Self-Signed Cert

**Context**: For TLS, generate cert if needed.

**Command** ([[commands/openssl-gen-cert]]):
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt -subj "/CN=docker.lonimbus.com"
```

> Creates cert; expected output: Generating key and cert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Connection Proxy]] Proxy (Webhook as Proxy for Payloads)

### Sub-Techniques


## Commands Used

- [[commands/gcloud-compute-instances-create]]
- [[commands/apt-install-nginx]]
- [[commands/nginx-reload]]
- [[commands/openssl-gen-cert]]

## Tools Used

- [[tools/nginx]]

## Tags

- webhook
- nginx
- tls
