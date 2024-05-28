with open('aws-iam-actions-list/all-actions.txt') as actions_file:
    actions = actions_file.readlines()

print(actions[0])