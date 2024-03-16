import numpy as np

PATH = "upload_Action_List.npy" # Can be modified into the name or path you want
action_list = np.load(PATH,allow_pickle=True) # The action list you upload
#action_list = [[0,1,2],[1,2,1,1],[2,2,2,2,2,2,2,2,1],[1,0,0,0,0,0,2,1,2,3], [1,2,3,1,2]]

print("Action list looks like ", action_list)
print("Action list's shape looks like ", np.shape(action_list))
for actions in action_list:
    print("Action shape looks like ", np.shape(actions))


new_action_list = []
distribution = {}
for actions in action_list:
    new_actions = []
    for action in actions:
        if action not in distribution.keys():
            distribution[action] = 1
        else:
            distribution[action] += 1
        new_actions.append(action)
    new_action_list.append(new_actions)
print(distribution)

#print(new_action_list)

NEWPATH="new"+PATH
np.save(NEWPATH ,np.array(action_list))

