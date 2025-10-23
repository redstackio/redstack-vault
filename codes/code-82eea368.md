---
id: 82eea368-9c15-4aa4-97c6-10f6498358d3
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:17.318299+00:00'
updated_at: '2023-04-06T03:56:17.333156+00:00'
---

# Code Snippet 82eea368

**Language**: ps1

```ps1
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv-and-hostpid/pod/priv-and-hostpid-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv/pod/priv-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpath/pod/hostpath-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpid/pod/hostpid-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostnetwork/pod/hostnetwork-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostipc/pod/hostipc-exec-pod.yaml
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/nothing-allowed/pod/nothing-allowed-exec-pod.yaml
```


