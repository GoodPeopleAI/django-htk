# https://api.321forms.com/docs

DSS_321FORMS_API_BASE_RESOURCE_COMPANY = 'company/'
DSS_321FORMS_API_BASE_RESOURCE_DIVISION = 'division/'
DSS_321FORMS_API_BASE_RESOURCE_USERS = 'users/'

# users
DSS_321FORMS_API_RESOURCE_USER = DSS_321FORMS_API_BASE_RESOURCE_USERS + '%(user_id)s.json'
DSS_321FORMS_API_RESOURCE_USER_FORMS = DSS_321FORMS_API_BASE_RESOURCE_USERS + '%(user_id)s/forms.json'
DSS_321FORMS_API_RESOURCE_USER_FORM = DSS_321FORMS_API_BASE_RESOURCE_USERS + '%(user_id)s/form/%(form_id)s.json'
DSS_321FORMS_API_RESOURCE_USER_RESPONSES = DSS_321FORMS_API_BASE_RESOURCE_USERS + '%(user_id)s/responses.json'
DSS_321FORMS_API_RESOURCE_USER_EVERIFY = DSS_321FORMS_API_BASE_RESOURCE_USERS + '%(user_id)s/everify.json'

# user types
DSS_321FORMS_API_USER_TYPE_HR_STAFF = 'staff'
DSS_321FORMS_API_USER_TYPE_HR_ADMIN = 'hrAdmin'
DSS_321FORMS_API_USER_TYPE_EMPLOYEE = 'employee'
DSS_321FORMS_API_USER_TYPE_EMPLOYEE_COMPLETE = 'complete'

# companies
DSS_321FORMS_API_RESOURCE_COMPANY = 'company.json'
DSS_321FORMS_API_RESOURCE_COMPANY_USERS = DSS_321FORMS_API_BASE_RESOURCE_COMPANY + '%(company_id)s/%(user_type)s.json'
DSS_321FORMS_API_RESOURCE_COMPANY_DIVISIONS = DSS_321FORMS_API_BASE_RESOURCE_COMPANY + '%(company_id)s/divisions.json'
DSS_321FORMS_API_RESOURCE_COMPANY_FORMS = DSS_321FORMS_API_BASE_RESOURCE_COMPANY + '%(company_id)s/forms.json'
DSS_321FORMS_API_RESOURCE_COMPANY_FORM = DSS_321FORMS_API_BASE_RESOURCE_COMPANY + '%(company_id)s/form/%(form_id)s.json'

# divisions
DSS_321FORMS_API_RESOURCE_DIVISION_FORMS = DSS_321FORMS_API_BASE_RESOURCE_DIVISION + '%(division_id)s/forms.json'

# SSO
DSS_321FORMS_API_RESOURCE_SSO_GENERATE = 'SSO/generate.json'
DSS_321FORMS_API_RESOURCE_SSO_ENDPOINT = 'SSO/%(sso_key)s.json'
