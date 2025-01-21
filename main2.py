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
    # token = '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'  # Replace with your GitHub token

    # Create an instance of the GitHubPRLabelsFetcher class
    fetcher = GitHubPRLabelsFetcher(owner, repo, GITHUB_TOKEN)

        
    # Fetch and print label descriptions
    labels = fetcher.fetch_and_print_labels(pr_number)

     # Print the fetched labels
    print(f"Fetched labels: {labels}")
    
    # Check if the labels were returned as key-value pairs
    if labels:
        key, value = labels
        # Set the TeamCity parameters for each key-value pair
        print(f"##teamcity[setParameter name='{key}' value='{value}']")

if __name__ == "__main__":
    main()
