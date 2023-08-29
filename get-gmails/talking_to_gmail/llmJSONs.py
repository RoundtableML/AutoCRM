import json


# These are some sample json responses I got from feeding the prompt + email body into chatgpt

one_response = [{
"isRelatedToJob": True,
"companyName": "Vanlo",
"applicationStatus": "submitted",
"roleName": "unknown"
}]

responses = [{
    "isRelatedToJob": True,
    "companyName": "Medpace, Inc.",
    "applicationStatus": "in review",
    "roleName": "Junior Software Engineer"
}, {
    "isRelatedToJob": True,
    "companyName": "Unknown",
    "applicationStatus": "submitted",
    "roleName": "Python Engineer"
}, {
    "isRelatedToJob": False
}, {
    "isRelatedToJob": True,
    "companyName": "Rialtic, Inc.",
    "applicationStatus": "in review",
    "roleName": "Unknown"
}, {
    "isRelatedToJob": True,
    "companyName": "Microsoft",
    "applicationStatus": "in review",
    "roleName": "Software Engineer"
}, ]

json_responses = json.dumps(responses)
