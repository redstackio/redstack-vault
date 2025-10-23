---
id: ff959f0b-52ce-493a-a4b6-d8b39b46e029
name: Download blobs
type: command
executor: bash
data: curl -s -k --user 'admin:admin' 'http://docker.registry.local/v2/wordpress-image/blobs/sha256:c314c5effb61c9e9c534c81a6970590ef4697b8439ec6bb4ab277833f7315058'
  > out.tar.gz
output: null
created_at: '2023-04-06T03:56:17.031230+00:00'
updated_at: '2023-04-10T20:33:50.751327+00:00'
---

# Download blobs

```bash
curl -s -k --user 'admin:admin' 'http://docker.registry.local/v2/wordpress-image/blobs/sha256:c314c5effb61c9e9c534c81a6970590ef4697b8439ec6bb4ab277833f7315058' > out.tar.gz
```


