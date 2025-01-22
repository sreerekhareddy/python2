import os
from github_labels_fetcher2 import GitHubPRLabelsFetcher

def find_matching_key(key, sources):
    """
    Finds a matching key in the sources, case-insensitively.
    Returns the matching key from the sources if found, else returns the original key.
    """
    lower_key = key.lower()
    for source in sources:
        for src_key in source:
            if src_key.lower() == lower_key:
                return src_key
    return key

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

    # Get current environment variables (TeamCity parameters)
    env_vars = os.environ

    # Example: Add any other configurations or parameters here
    config_params = {
        'Example-Config': 'value'
        # Add other configuration parameters as needed
    }

    # Combine all sources
    sources = [env_vars, config_params]

    # Check if the labels were returned as key-value pairs
    if labels:
        for key, value in labels.items():
            # Find matching key from all sources
            matching_key = find_matching_key(key, sources)
            # Print PRACTISE={matching_key}
            print(f"PRACTISE='{matching_key}'")
            # Set the TeamCity parameters for each value
            print(f"##teamcity[setParameter name='{matching_key}' value='{value}']")
            print(f"Parameter set: name='{matching_key}' value='{value}'")

if __name__ == "__main__":
    main()
