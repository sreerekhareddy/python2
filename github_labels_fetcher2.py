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
                        try:
                            key, value = description.split(':', 1)
                            label_dict[key.strip()] = value.strip()
                            print(f"{key.strip()} : {value.strip()}")
                        except ValueError:
                            print(f"Invalid label description format: {description}")
            else:
                print(f"No labels found for Pull Request #{pr_number}")
            return label_dict
        else:
            print(f"Failed to fetch labels. HTTP Status Code: {response.status_code}")
            print("Error:", response.json())
            return None
