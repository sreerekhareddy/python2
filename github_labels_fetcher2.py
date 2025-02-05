import requests

class GitHubPRLabelsFetcher:
    def __init__(self, owner, repo, GITHUB_TOKEN):
        self.owner = owner
        self.repo = repo
        self.token = GITHUB_TOKEN
        self.url = f'https://api.github.com/repos/{self.owner}/{self.repo}/issues/labels'

    def fetch_labels(self, pr_number):
        # Set headers for authentication
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json',  # Ensure correct API version
        }

        # GitHub API URL for PR labels
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/issues/{pr_number}/labels'

        # Send GET request to fetch the labels for the specified PR
        response = requests.get(url, headers=headers)
        return response

    def fetch_and_print_labels(self, pr_number):
        response = self.fetch_labels(pr_number)

        if response.status_code == 200:
            # Parse the JSON response containing labels
            labels = response.json()
            label_dict = {}
            if labels:
                print(f"Labels for Pull Request #{pr_number}:")
                for label in labels:
                    description = label.get('description', '')
                    if description:
                        # Split the description by comma to separate multiple labels
                        descriptions = description.split(',')
                        for desc in descriptions:
                            try:
                                # splitting the description into key and value pair
                                key, value = desc.split(':', 1)
 
                                # checking that can we split value further on the basis of : present or not
                                # if yes then we will split it further and assign the key and value accordingly
                                if(value.find(":") != -1):
                                    key1, value1 = value.split(':', 1)
                                    key_repo = key.strip() + "_repo"
                                    label_dict[key_repo] = key1.strip()
                                    key_release = key.strip() + "_release"
                                    label_dict[key_release] = value1.strip()
 
                                else:
                                    key_release = key.strip() + "_release"
                                    label_dict[key_release] = value.strip()
                            except ValueError:
                                print(f"Invalid label description format: {desc}")
            else:
                print(f"No labels found for Pull Request #{pr_number}")
            return label_dict
        else:
            print(f"Failed to fetch labels. HTTP Status Code: {response.status_code}")
            print("Error:", response.json())
            return None
