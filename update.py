import requests
import json

from security_events import security_events


def parse_policies_js(url):
    try:
        # Send a GET request to fetch the JavaScript file
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            # Extract JSON content
            js_content = response.text

            # Remove the callback function wrapper from JSON data
            json_data = js_content[js_content.find("{") : js_content.rfind("}") + 1]

            # Parse JSON data into Python dictionary
            parsed_json = json.loads(json_data)

            return parsed_json["serviceMap"]

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

aws_events = []

for _, service_dict in parsed_data.items():
    for action in service_dict["Actions"]:
        service = service_dict["StringPrefix"]
        aws_events.append(f"{service}:{action}")


aws_events.sort()

with open("all-aws-event-names.txt", "w") as all_aws_events_file, open(
    "all-aws-event-names-reversed.txt", "w"
) as all_aws_events_reversed_file, open(
    "aws-security-events.txt", "w"
) as aws_security_events_file, open(
    "aws-security-events-reversed.txt", "w"
) as aws_security_events_file_reversed:
    for line in aws_events:
        all_aws_events_file.write(f"{line}\n")

        service_name, event_name = line.split(":", 1)
        all_aws_events_reversed_file.write(f"{event_name}:{service_name}\n")

        if (
            service_name in security_events
            and event_name in security_events[service_name]
        ):
            aws_security_events_file.write(f"{line}\n")
            aws_security_events_file_reversed.write(f"{event_name}:{service_name}\n")
