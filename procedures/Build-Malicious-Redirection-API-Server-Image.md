---
id: proc-build-redirect-image-001
tags:
  - ssrf
  - docker
  - go
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:46:08.952Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Build-Malicious-Redirection-API-Server-Image

## Summary

This procedure builds a Docker image containing a simple Go server that responds to HTTP requests with 30X redirects (e.g., 301 or 302) to an attacker-controlled endpoint, enabling SSRF exploitation in Kubernetes aggregated API servers.

## Description

In the context of Kubernetes SSRF, the malicious server mimics metrics-server responses but redirects clients (like control plane components) to external attacker servers. This leads to leakage of bearer tokens and sensitive data. The procedure uses a basic Go HTTP server from main.go, compiled and containerized for deployment as a pod. Prerequisites include Go installed and Docker access; the image is tagged as docker.io/weinong/go-redirect for pushing to a registry.

## Requirements

1. Go runtime (version 1.18+) for compiling main.go
2. Docker installed with push access to a registry (e.g., Docker Hub)
3. Source code: main.go implementing HTTP handler for redirects

## Defense

Defensive measures and detection strategies:

- Restrict pod deployments in kube-system namespace to trusted images
- Enable image scanning with tools like Trivy to detect malicious binaries
- Monitor API server logs for unexpected redirects or external connections

## Objectives

1. Create a functional redirection server image
2. Ensure compatibility with Kubernetes pod specs
3. Prepare for hijacking aggregated API endpoints

## Instructions

### Step 1: Compile the Go Server

**Context**: Build the Go binary from main.go, which sets up an HTTP server returning 301 redirects to http://attacker.com/redirect.

No specific command; use `go build -o redirect-server main.go` locally.

> Compiles the binary; verify by running `./redirect-server` and curling localhost:8080 to see redirect response.

### Step 2: Build Docker Image

**Context**: Containerize the binary using a Dockerfile that exposes port 8080 and sets the entrypoint.

Use [[tools/Docker]] to build:

```bash
docker build -t docker.io/weinong/go-redirect .
```

> Builds the image; test with `docker run -p 8080:8080 docker.io/weinong/go-redirect` and confirm redirects via curl.

### Step 3: Push Image to Registry

**Context**: Make the image available for Kubernetes deployment.

```bash
docker push docker.io/weinong/go-redirect
```

> Pushes to Docker Hub; success indicated by image ID in registry.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- ssrf
- docker
- go
