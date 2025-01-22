import os
from github_labels_fetcher2 import GitHubPRLabelsFetcher

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

    # Check if the labels were returned as key-value pairs
    if labels:
        for key, value in labels.items():
            if key.lower() == "pmbd-prod":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='PMBD-Prod' value='{value}']")
            if key.lower() == "asw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='ASW' value='{value}']")
            if key.lower() == "bsw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='BSW' value='{value}']")

if __name__ == "__main__":
    main()
