with open('monitored-repo/all-actions.txt') as actions_file:
    actions = actions_file.readlines()

print(actions[0])