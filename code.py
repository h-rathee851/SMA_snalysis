
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
import sys, traceback



# In[164]:

# Defining Variables and Arrays to store data
data_ = []
day_data_ = []
day_data_50_ = []
day_data_200_ = []
SMA_50_ = []
SMA_200_ = []
SMA_50_tot = 0
SMA_200_tot = 0
is_50_up = False
was_50_up = False
# Reading market data from file
f = open("HistoricalQuotes.csv",'r')
lines = f.readlines()


# In[165]:

# Defining the plot
fig, ax = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(10)
sc = ax.scatter(day_data_,data_,s=1, label = "Closing Value")
line_50, = ax.plot([], [], 'g',lw=2, label = "SMA 50")
line_200, = ax.plot([], [], 'r', lw=2, label = "SMA 200")
plt.xlim(0,len(lines))
plt.ylim(0,50)
plt.legend()
plt.xlabel("No. Of Days")
plt.ylabel("Closing Value")
plt.title("SMA Cross Over Analysis for NYSE: APAM over 3 years")
# plt.clf()

def animate(i):
    
    global SMA_50_tot , SMA_200_tot, is_50_up, was_50_up

    day = i-1
    
    if i > 1:
        
        # Reading and appending data
        data = lines[i].split(",")
        data[1] = data[1][1:-1]
        data_.append(float(data[1]))
        day_data_.append(day);
        sc.set_offsets(np.c_[day_data_,data_])
        SMA_50_tot +=  data_[-1]
        SMA_200_tot += data_[-1]
                
        
    if day >= 50:
        
        day_data_50_.append(day)
        #Calculate SMA 50 days and add to array
        SMA_50_.append(SMA_50_tot/50.0)
        line_50.set_data(day_data_50_,SMA_50_)
        SMA_50_tot -= data_[day-50]
        
    if day >= 200:
        
        day_data_200_.append(day)
        #Calculate SMA 50 days and add to array
        SMA_200_.append(SMA_200_tot/200.0)
        line_200.set_data(day_data_200_,SMA_200_)
        SMA_200_tot -= data_[day-200]
        
        if ((SMA_50_[-1] > SMA_200_[-1]) & (day == 200)):
            
            was_50_up = True
        
        if (day != 200):
            
            if ((SMA_50_[-1] > SMA_200_[-1])):
                
                is_50_up = True
            else:
                
                is_50_up = False
                
             # Check if SMA does a crossover   
            if(is_50_up != was_50_up):
                print("SMA 50 Crosses SMA 200 on day: ", day)
                was_50_up = is_50_up
        

# Show the graph
anim = FuncAnimation(fig, animate, 
                frames=len(lines), interval=100, repeat=False) 


plt.show()


ch = input("Do you want to Quit?[y/n]")

if( ch == "y"):

    sys.exit(0)
    




