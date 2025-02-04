import os
from github_labels_fetcher2 import GitHubPRLabelsFetcher
from teamcity_api import get_teamcity_parameters  # Import from the new file

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

    # Fetch existing parameters from TeamCity
    teamcity_params = get_teamcity_parameters()

    if labels:
        print("##teamcity[setParameter name='HAS_LABELS' value='true']")
        
        for key, value in labels.items():
            param_name = key.strip()  # Standardizing the key name
            
            if param_name in teamcity_params:
                # If parameter exists, update it
                print(f"##teamcity[setParameter name='{param_name}' value='{value}']")
            else:
                # If parameter does not exist, create it only for the current build
                print(f"##teamcity[setParameter name='{param_name}' value='{value}'] (Temporary for this build)")

    else:
        print("##teamcity[setParameter name='HAS_LABELS' value='false']")

if __name__ == "__main__":
    main()
