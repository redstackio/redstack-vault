---
type: command
executor: bash
data: |-
  mkdir ADFSpoofTools
  cd $_
  git clone https://github.com/dmb2168/cryptography.git
  git clone https://github.com/mandiant/ADFSpoof.git
platforms:
  - Linux
  - macOS
tags:
  - setup
  - git
verified: true
validated: true
---

# create-adfsspoof-tools-directory-and-clone-repositories

## Command

```bash
mkdir ADFSpoofTools
cd $_
git clone https://github.com/dmb2168/cryptography.git
git clone https://github.com/mandiant/ADFSpoof.git
```

## Description

Creates a dedicated directory for ADFSpoof tools and clones the modified cryptography library and ADFSpoof repository. Use this to set up the environment for Golden SAML token forging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_` | Refers to the newly created directory (automatic in bash) | Yes |

## Examples

### Basic Usage

```bash
mkdir ADFSpoofTools
cd $_
git clone https://github.com/dmb2168/cryptography.git
git clone https://github.com/mandiant/ADFSpoof.git
```

### Advanced Usage

If behind a proxy, add `git config --global http.proxy http://proxy:port` before cloning.

## Expected Output

Cloning into 'cryptography'...
remote: Enumerating objects: ..., done.
...
Cloning into 'ADFSpoof'...
...

Directories created and repositories cloned successfully.

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
