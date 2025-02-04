# teamcity_api.py
import requests

# TeamCity Configuration
TEAMCITY_URL = "https://practisework.teamcity.com"
USERNAME = "renusree"
PASSWORD = "123456789"
BUILD_ID = "Intilization_Intialstep"  # Use correct build type ID

def get_teamcity_parameters():
    """Fetches existing parameters from TeamCity."""
    api_url = f"{TEAMCITY_URL}/app/rest/latest/buildTypes/id:{BUILD_ID}"
    headers = {"Accept": "application/json"}

    response = requests.get(api_url, auth=(USERNAME, PASSWORD), headers=headers, verify=False)

    if response.status_code == 200:
        build_config = response.json()
        return {param['name']: param.get('value', 'N/A') for param in build_config.get("parameters", {}).get("property", [])}
    else:
        print(f"Failed to fetch TeamCity parameters. Status Code: {response.status_code}, Response: {response.text}")
        return {}
