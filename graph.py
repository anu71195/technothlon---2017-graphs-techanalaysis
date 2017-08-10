import matplotlib.pyplot as plt
import numpy as np
import csv
all_file=['TechnoKVJNVResults2017-04PM.csv']
for file in all_file:
	fr=open(file,'r');
	text=csv.reader(fr);
	a=[int(i) for i in input().split()]#5,25
	question_number=0
	for i in range(a[0],a[1]+1):
		xy={}
		question_number+=1;
		fr.seek(0)
		for score in text:
			if score[i] in xy:
				xy[score[i]]+=1;
			else:
				xy[score[i]]=1;
		x=[]
		y=[]
		flag=True;
		for i in xy:
			try:
				int(i)
			except:
				flag=False
				break;
		if flag ==True:
			temp_xy={}
			for i in xy:
				temp_xy[int(i)]=xy[i]
			xy=temp_xy;
		x=sorted(xy)
		for i in x:
			y.append(xy[i])
		temp_x=np.arange(len(x))
		my_xticks=x;
		ylab="frequency"
		xlab="question"+" "+str(question_number)
		axis_range=[min(x),max(x),min(y),max(y)]
		plt.xticks(temp_x,my_xticks)
		plt.xlabel(xlab)
		plt.ylabel(ylab)
		plt.tight_layout()
		plt.plot(temp_x,y,'r*')
		plt.show();
		




