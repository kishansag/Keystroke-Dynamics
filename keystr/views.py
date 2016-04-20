from django.shortcuts import render
from .forms import StrokeForm
from django.shortcuts import redirect
from .models import stroke
import numpy as np
import math
# Create your views here.
def formpage(request):
	def filter(ts):
		t = ts.timecsv.split(",")
		k = ts.keycsv.split(",")
		s = ts.spincsv.split(",")
		ta = []
		ka = []
		sa = []
		for i in range(0,len(t)-1):
			ta.append(int(t[i]))
		for i in range(0,len(k)-1):
			ka.append(int(k[i]))	
		for i in range(0,len(s)-1):
			sa.append(int(s[i]))

		#x = np.array((ta,ka,sa), dtype = long)
		dt = []
		dk = []
		for i in range(0, len(sa)):
			if (sa[i] == 0):
				for k in range(i+1, len(sa)):
					if(ka[k] == ka[i]):
						if(sa[k] == 1):
							dt.append(ta[k]-ta[i])
							dk.append(ka[i])
							break

		ft = []
		fk1 = []
		fk2 = []
		for i in range(0, len(sa)):
			if (sa[i] == 1):
				for k in range(i+1, len(sa)):
					if(sa[k] == 0):
						ft.append(ta[k]-ta[i])
						fk1.append(ka[i])
						fk2.append(ka[k])
						break
		dta = []
		dku = []
		for i in range(0, len(dk)):
			if (dk[i] not in dku):
				dku.append(dk[i]) 
				temp = dt[i]
				l = 1
				for k in range(i, len(dk)):
					if(dk[i] == dk[k]):
						temp = temp + dt[k]
						l = l + 1
				dta.append(temp/l)

		fta = []
		fku1 = []
		fku2 = []	
		for i in range(0, len(ft)):
			if ((fk1[i] not in fku1) and (fk2[i] not in fku2)):
				fku1.append(fk1[i]) 
				fku2.append(fk2[i]) 
				temp = ft[i]
				l = 1
				for k in range(i, len(ft)):
					if(fk1[i] == fk1[k]):
						if(fk2[i] == fk2[k]):
							temp = temp + ft[k]
							l = l + 1
				fta.append(temp/l)
		return dta, dku, fta, fku1, fku2

	if request.method == "POST":
		form = StrokeForm(request.POST)
		if form.is_valid():
			stroke1 = form.save()
			jack3 = filter(stroke1)
			return render(request, 'formpage.html', {'form': form, 'dwell' : jack3[0], 'flight' : jack3[2]})
	else:
		form = StrokeForm()
	return render(request, 'formpage.html', {'form': form})

def loginpage(request):
	def filter(ts):
		t = ts.timecsv.split(",")
		k = ts.keycsv.split(",")
		s = ts.spincsv.split(",")
		ta = []
		ka = []
		sa = []
		for i in range(0,len(t)-1):
			ta.append(int(t[i]))
		for i in range(0,len(k)-1):
			ka.append(int(k[i]))	
		for i in range(0,len(s)-1):
			sa.append(int(s[i]))

		#x = np.array((ta,ka,sa), dtype = long)
		dt = []
		dk = []
		for i in range(0, len(sa)):
			if (sa[i] == 0):
				for k in range(i+1, len(sa)):
					if(ka[k] == ka[i]):
						if(sa[k] == 1):
							dt.append(ta[k]-ta[i])
							dk.append(ka[i])
							break

		ft = []
		fk1 = []
		fk2 = []
		for i in range(0, len(sa)):
			if (sa[i] == 1):
				for k in range(i+1, len(sa)):
					if(sa[k] == 0):
						ft.append(ta[k]-ta[i])
						fk1.append(ka[i])
						fk2.append(ka[k])
						break
		dta = []
		dku = []
		for i in range(0, len(dk)):
			if (dk[i] not in dku):
				dku.append(dk[i]) 
				temp = dt[i]
				l = 1
				for k in range(i, len(dk)):
					if(dk[i] == dk[k]):
						temp = temp + dt[k]
						l = l + 1
				dta.append(temp/l)

		fta = []
		fku1 = []
		fku2 = []	
		for i in range(0, len(ft)):
			if ((fk1[i] not in fku1) and (fk2[i] not in fku2)):
				fku1.append(fk1[i]) 
				fku2.append(fk2[i]) 
				temp = ft[i]
				l = 1
				for k in range(i, len(ft)):
					if(fk1[i] == fk1[k]):
						if(fk2[i] == fk2[k]):
							temp = temp + ft[k]
							l = l + 1
				fta.append(temp/l)
		return dta, dku, fta, fku1, fku2

	if request.method == "POST":
		form = StrokeForm(request.POST)
		if form.is_valid():
			stroke1 = form.save(commit=False)
			train = stroke.objects.all()
			length = len(train)
			for i in range(0 , length):
				if (train[i].email == stroke1.email):
					jack1 = filter(train[i]) 
					jack2 = filter(stroke1)
					dtf = []
					dkf =[]
					dtu = 0
					for i in range(0, len(jack1[1])):
						if jack1[0][i] not in dkf:
							dkf.append(jack1[0][i])
							for k in range(0, len(jack2[1])):
								if (jack2[1][k] == jack1[1][i]):
									dtf.append(jack2[0][k]-jack1[0][i])
									dtu = dtu + (jack2[0][k]-jack1[0][i])*(jack2[0][k]-jack1[0][i])
					dtu = math.sqrt(dtu)

					ftf = []
					fkf1 = []
					fkf2 = []
					ftu = 0
					for i in range(0, len(jack1[2])):
#						f=0
#						for j in range(0, len(fkf1)):
#							if(fkf1[j]==jack1[3][i]):
#								if(fkf2[j]==jack1[4][i]):
#									f=1
#									break
#						if f==0:
#							fkf1.append(jack1[3][i])
#							fkf2.append(jack1[4][i])
#						if ((jack1[3][i] not in fkf1) and (jack1[4][i] not in fkf2)):
#							fkf1.append(jack1[3][i])
#							fkf2.append(jack1[4][i])							
							for k in range(0, len(jack2[2])):
								if ((jack2[3][k] == jack1[3][i]) and (jack2[4][k] == jack1[4][i])):
									fkf1.append(jack1[3][i])
									fkf2.append(jack1[4][i])
									ftf.append(jack2[2][k]-jack1[2][i])
									ftu = ftu + (jack2[2][k]-jack1[2][i])*(jack2[2][k]-jack1[2][i])
					ftu = math.sqrt(ftu)
				#else
					#print "account not created"
			return render(request, 'loginpage.html', {'form': form, 'dwell' : jack2[0], 'flight' :jack2[2], 'ddiff': dtf, 'fdiff' : ftf, 'ddist' : dtu, 'fdist':ftu})
	else:
		form = StrokeForm()
	return render(request, 'loginpage.html', {'form': form})
