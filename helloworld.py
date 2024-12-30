import pandas as pd

states = ["Texas", "California", "Ohio"]
population = [5,6,7]

dict_states = {'States': states, 'Population': population}
df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_csv('states.csv')

# for state in states:
#     print(state)

#file handling:
# with open('filename.txt', 'mode') as file:
#     file.write("text to write")