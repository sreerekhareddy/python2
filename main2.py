import os
from github_labels_fetcher2 import GitHubPRLabelsFetcher
from teamapi import get_teamcity_parameters  # Assuming you've imported this function

def main():
    # GitHub repository details
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN environment variable is not set")
    owner = 'sreerekhareddy'  # Replace with the repository owner's GitHub username
    repo = 'python2'  # Replace with the repository name
    pr_number = 1  # Replace with the pull request number

    # Create an instance of the GitHubPRLabelsFetcher class
    fetcher = GitHubPRLabelsFetcher(owner, repo, GITHUB_TOKEN)

    # Fetch and print label descriptions
    labels = fetcher.fetch_and_print_labels(pr_number)

    # Fetch existing TeamCity parameters
    teamcity_params = get_teamcity_parameters()

    if labels:
        print("##teamcity[setParameter name='HAS_LABELS' value='true']")
        for key, value in labels.items():
            # Convert the label key to lowercase for case-insensitive comparison
            key_lower = key.lower()

            # Check if the key exists in TeamCity parameters (case-insensitive)
            found = False
            for param_name in teamcity_params:
                if param_name.lower() == key_lower:  # Compare lowercase keys
                    # If parameter exists (case-insensitive match), update it
                    print(f"##teamcity[setParameter name='{param_name}' value='{value}']")
                    found = True
                    break

            # If no matching TeamCity parameter found, create it (temporary for build)
            if not found:
                print(f"##teamcity[setParameter name='{key}' value='{value}'] (Temporary for this build)")

    else:
        print("##teamcity[setParameter name='HAS_LABELS' value='false']")

if __name__ == "__main__":
    main()
