import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# read csv files
data = pd.read_csv("./data/Datasett_seertall_NRK_2019.csv")

# initiate list for each show
shows = []

# list with screens to loop over
screens = ['tablet', 'mobile', 'desktop']

# fill in all shows
for i in data.index:
    if data.seriesId[i] not in shows:
        shows.append(data.seriesId[i])

# initiate lists for each platform
shows_viewers_tablet = [0]*len(shows)
shows_viewers_mobile = [0]*len(shows)
shows_viewers_desktop = [0]*len(shows)
shows_viewers_total = [0]*len(shows)
print(shows_viewers_tablet)

# fill in all shows viewers on different plattforms
for i in data.index:
    for show in shows:
        if data.seriesId[i] == show and data.screen[i] == 'tablet':
            index = shows.index(show)
            shows_viewers_tablet[index]  = shows_viewers_tablet[index] + int(data.views[i])
            shows_viewers_total[index]  = shows_viewers_total[index] + int(data.views[i])
            
        elif data.seriesId[i] == show and data.screen[i] == 'mobile':
            index = shows.index(show)
            shows_viewers_mobile[index]  = shows_viewers_mobile[index] + int(data.views[i])
            shows_viewers_total[index]  = shows_viewers_total[index] + int(data.views[i])
        
        elif data.seriesId[i] == show and data.screen[i] == 'desktop':
            index = shows.index(show)
            shows_viewers_desktop[index]  = shows_viewers_desktop[index] + int(data.views[i])
            shows_viewers_total[index]  = shows_viewers_total[index] + int(data.views[i])



# plot data

# create 2 subplots
figures, axes = plt.subplots(2) 


# first plot (pie chart)
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" side om side 
plt.sca(axes[0])
plt.title("Most popular shows")
plt.pie(shows_viewers_total, explode=explode, rotatelabels=90, autopct='%1.1f%%',
        pctdistance=1.15, labeldistance=1.2, shadow=True, startangle=90) # draw pie chart
plt.legend(shows, loc=2) # shows as lavels to make visible, loc=2 is upper left
plt.axis('equal')  # ensure pie chart is drawn as circle
plt.xticks(rotation=90)



# second plot (bar chart)
x_axis = np.arange(len(shows))
plt.sca(axes[1])
plt.bar(x_axis - 0.2, shows_viewers_tablet, 0.1, label = 'Tablet')
plt.bar(x_axis - 0.1, shows_viewers_desktop, 0.1, label = 'Desktop')
plt.bar(x_axis, shows_viewers_mobile, 0.1, label = 'Mobile')
plt.bar(x_axis + 0.1, shows_viewers_total, 0.1, label = 'Total')


plt.xticks(x_axis, shows)
plt.xlabel("Shows")
plt.ylabel("Number of views")
plt.title("Number of views for different shows on different plattforms")
plt.legend()
plt.ticklabel_format(style='plain', axis='y') # remove scientific notation
plt.xticks(rotation=20) # make show-title visible
plt.show()
