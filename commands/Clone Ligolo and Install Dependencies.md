---
id: f81f0e2e-0579-4a88-9c22-e34332b58395
name: Clone Ligolo and Install Dependencies
type: command
executor: bash
data: 'cd `go env GOPATH`/src

  git clone https://github.com/sysdream/ligolo

  cd ligolo

  make dep

  '
output: null
created_at: '2023-04-06T03:56:22.792060+00:00'
updated_at: '2023-04-10T20:25:12.831311+00:00'
---

# Clone Ligolo and Install Dependencies

```bash
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep

```
