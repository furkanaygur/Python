import matplotlib.pyplot as plt

# **************************************************

# year = [2011, 2012, 2013, 2014, 2015]

# player1 = [18, 29, 10, 21, 42]
# player2 = [11, 19, 51, 25, 73]
# player3 = [58, 29, 31, 51, 22]

# # Stack Plot

# plt.plot([], [], color="y", label="player1")
# plt.plot([], [], color="b", label="player2")
# plt.plot([], [], color="r", label="player3")

# plt.stackplot(year, player1, player2, player3, colors=["y","b","r"])
# plt.legend()
# plt.title("Goals by years")
# plt.xlabel("Years")
# plt.ylabel("Goals")

# plt.show()

# **************************************************

# Pie

# goals_types = 'Penalty', 'Shoot', 'Freekick'

# goals = [12,35,12]
# colors = ['y','b','r']

# plt.pie(goals, labels=goals_types, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05), autopct="%1.1f%%")

# plt.show()

# **************************************************

# Bar

# plt.bar([0.25, 1.25, 2.25, 3.25, 4.25],[50,40,70,80,20], label="BMW", width=.5 ,color = "blue")
# plt.bar([0.75, 1.75, 2.75, 3.75, 4.75],[80,20,20,50,60], label="MERCEDES", width=.5, color="silver")

# plt.legend()
# plt.xlabel("Day")
# plt.ylabel("Kilometres")
# plt.title("Infos")

# plt.show()

# **************************************************

# Histogram

Ages = [22,15,31,51,63,16,85,52,63,74,12,41,52,15,71]

ages_groups = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(Ages, ages_groups, histtype="bar", rwidth=0.8)
plt.xlabel("Ages Groups")
plt.ylabel("Person Count")
plt.title("Histogram Graphic")

plt.show()