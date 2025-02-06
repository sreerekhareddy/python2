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
    #teamcity_params = get_teamcity_parameters()

    if labels:
        print("##teamcity[setParameter name='HAS_LABELS' value='true']")
        for key, value in labels.items():
            if 'bsw' in key.lower():
                print(f"##teamcity[setParameter name='BSW_repo' value='{key}']")
                print(f"##teamcity[setParameter name='BSW_release' value='{value}']")
            else:
                print(f"##teamcity[setParameter name='{key}_release' value='{value}']")
    else:
        print("##teamcity[setParameter name='HAS_LABELS' value='false']")

if __name__ == "__main__":
    main()
