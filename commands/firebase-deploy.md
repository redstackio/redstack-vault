---
data: firebase deploy
tags:
  - firebase
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.341Z'
id: c31c1d4e-f8bc-4f46-9fdc-30170dc1ee56
verified: false
validated: true
submitted: true
---
# firebase-deploy

## Command

```bash
firebase deploy
```

## Description

Deploys the configured hosting content to Firebase, making it live on a *.firebaseapp.com subdomain. Essential for pushing malicious static files in this attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Deploys all services; use --only hosting for specific | No |

## Examples

### Basic Usage

```bash
firebase deploy
```

### Hosting Only

```bash
firebase deploy --only hosting
```

## Expected Output

Progress bars, then URLs: ✔ Deploy complete! Hosting URL: https://hackerone-jm.firebaseapp.com

## Related

- [[commands/firebase-init]]
- [[procedures/Deploy-Malicious-Page-to-Firebase-Hosting]]
