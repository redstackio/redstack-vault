---
id: cmd-003
data: npx degit "sveltejs/sapper-template#webpack" my-app
tags:
  - clone
  - shallow
type: command
output: ✔ cloned sveltejs/sapper-template#webpack to /path/my-app
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.540Z'
verified: false
validated: true
submitted: true
---
---

# npx-degit-webpack-example

## Command

```bash
npx degit "sveltejs/sapper-template#webpack" my-app
```

## Description

Executes degit via npx to shallow clone the Webpack branch of Sapper template into 'my-app' directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `degit` | Shallow clone tool | Yes |
| `"sveltejs/sapper-template#webpack"` | Repo and branch | Yes |
| `my-app` | Target directory | Yes |

## Examples

### Basic Usage

```bash
npx degit "sveltejs/sapper-template#webpack" my-app
```

### Advanced Usage

```bash
npx degit sveltejs/sapper-template#webpack ./app --force
```

## Expected Output

Confirmation of cloned directory with files.

## Related

- [[Related Procedure: Obtain-Webpack-Sapper-Example]]

---
