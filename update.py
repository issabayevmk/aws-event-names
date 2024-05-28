import requests
import json

def parse_policies_js(url):
    try:
        # Send a GET request to fetch the JavaScript file
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            # Extract JSON content
            js_content = response.text

            # Remove the callback function wrapper from JSON data
            json_data = js_content[js_content.find('{'):js_content.rfind('}') + 1]

            # Parse JSON data into Python dictionary
            parsed_json = json.loads(json_data)

            return parsed_json['serviceMap']

        else:
            print("Failed to retrieve data from the URL.")
            return None

    except Exception as e:
        print("An error occurred:", e)
        return None

# URL of the policies.js file
url = "https://awspolicygen.s3.amazonaws.com/js/policies.js"

# Call the function to parse the policies.js file
parsed_data = parse_policies_js(url)

security_services_list = [
    'access-analyzer',
    'account',
    'acm',                       # Certificate Manager
    'acm-pca',                   # Private Certificate Authority
    'artifact',
    'auditmanager',
    'cloudhsm',                  # Cloud HSM
    'cloudtrail',
    'config',
    'controltower',
    'cognito-identity',
    'cognito-idp',
    'cognito-sync',
    'detective',
    'ds',                        # Directory Service
    'fms',                       # Firewall Manager
    'guardduty',
    'iam',
    'inspector',
    'inspector2',
    'inspector-scan',
    'kms',                       # Key Management Service
    'macie2',
    'organizations',
    'payment-cryptography',
    'ram',                       # Resource Access Manager
    'route53',
    'secretsmanager',
    'securityhub',
    'securitylake',
    'shield',
    'sso',                       # Identity Center (successor to AWS Single Sign-On) directory
    'sso-directory',             # Identity Center (successor to AWS Single Sign-On)
    'sso-oauth',                 # IAM Identity Center OIDC service
    'verifiedpermissions',
    'verified-access',
    'waf',
    'waf2'                       # WAF V2
    'waf-regional',              # WAF Regional
]

all_services = open('all-services-events.txt', 'w')
all_services_reversed = open('all-services-events-reversed.txt', 'w')
security_services = open('security-services-events.txt', 'w')
security_services_reversed = open('security-services-events-reversed.txt', 'w')

#service = open('services.txt', 'w')
    
# Print the parsed data
for _, service_dict in parsed_data.items():
    #service_name = f"{service_dict['StringPrefix']}\n"
    #service.write(service_name)
    for action in service_dict['Actions']:
        service = service_dict['StringPrefix']
        line = f"{service}:{action}\n"
        reversed_line = f"{action}:{service}\n"
        all_services.write(line)
        all_services_reversed.write(reversed_line)

        if service in security_services_list:
            security_services.write(line)
            security_services_reversed.write(reversed_line)

all_services.close()
all_services_reversed.close()
security_services.close()
security_services_reversed.close()
        
