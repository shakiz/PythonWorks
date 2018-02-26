import matplotlib.pyplot as plt

fig=plt.figure()

x_axis=[1980,1985,1990,1995,2000,2005,2008,2015]
y_axis=[250,597,1054,1594,2453,3913,5003,17295]



plt.title('Bangladesh GDP in per year since 1980s')
plt.xlabel('Year')
plt.ylabel('GDP in million taka')
plt.plot(x_axis,y_axis)
plt.show()
plt.close()

#births per year sinc 2005-2014

year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
births=[2879,2901,2986,3022,2832,2868,2891,2933,0,0]



plt.title('birth rate of new born since 2005-2014')
plt.xlabel('Year')
plt.ylabel('Birth in million')
plt.bar(year,births)
plt.show()
plt.close()
