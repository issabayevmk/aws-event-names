# AWS Event Names

## Overview
The AWS Event Names Generator is a Python-based utility inspired by [TryTryAgain](https://github.com/TryTryAgain/aws-iam-actions-list) and designed to monitor changes in AWS Events, particularly focused on AWS IAM actions. When changes are detected, it automatically updates the repository with the latest all aws events list and security-important events list. This tool is particularly useful for maintaining up-to-date information on AWS event names and security-critical events. Security-critical events are listed in 'security-_events.py' file and based 

## Features
 - Automated Monitoring: Periodically checks 'https://awspolicygen.s3.amazonaws.com/policygen.html' for updates.
 - AWS Event Names Generation: Automatically generates a comprehensive list of AWS event names.
 - Security Important Events: Identifies and highlights AWS security-important events.
 - Automated Commits: Commits the processed results back to the repository.

 ## Usage
 - Get the latest full AWS event names list or security-important events list directly from the repo
 - Clone the repo locally and run 'update.py'

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push to the branch.
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to open an issue or contact the repository owner.
