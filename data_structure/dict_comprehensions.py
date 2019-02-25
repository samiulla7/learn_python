state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 
output_dict = {} 
# Using loop for constructing output dictionary 
# zip(state, capital) = [('Gujarat', 'Gandhinagar'), ('Maharashtra', 'Mumbai'), ('Rajasthan', 'Jaipur')]
# unzip state,capital = zip(*zip(state, capital))
# state,capital = zip(*zip(state, capital))
#state === ('Gujarat', 'Maharashtra', 'Rajasthan')
#capital === ('Gandhinagar', 'Mumbai', 'Jaipur') 
for (key, value) in zip(state, capital): 
    output_dict[key] = value 
print("Output Dictionary using for loop:", 
                              output_dict) 
#output
# Output Dictionary using for loop: {'Gujarat': 'Gandhinagar',
#                                    'Maharashtra': 'Mumbai', 
#                                    'Rajasthan': 'Jaipur'}

# Now with  dict comprehension way:
dict_using_comp = {key:value for (key, value) in zip(state, capital)} 
print("Output Dictionary using for loop:", 
                              dict_using_comp) 
#output
# Output Dictionary using for loop: {'Gujarat': 'Gandhinagar',
#                                    'Maharashtra': 'Mumbai', 
#                                    'Rajasthan': 'Jaipur'}
