import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import style
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import axes3d

kota=[] ; th2015=[] ; th2016=[]
plt.figure('3D Plotting',figsize=(10,5))
custom=plt.subplot(111,projection='3d')
def print3D():
    data=open("./Matplotlib Training/Persentase Perokok RI.csv").read()
    baris=data.split('\n')
    for isidata in baris:
        x,y,z=isidata.split(',')
        kota.append(x)
        th2015.append(float(y))
        th2016.append(float(z))
    kota.remove(kota[0]);th2015.remove(th2015[0]);th2016.remove(th2016[0])
    xalas = np.arange(0,len(kota))
    yalas = np.repeat(0.5,len(kota))
    zalas = np.zeros(len(kota))
    xdinding = np.ones(len(kota))
    ydinding = np.ones(len(kota))
    zdinding = np.array(th2015)
    custom.bar3d(xalas,yalas,zalas,xdinding,ydinding,zdinding,color=['r','g','b','c','k','w','r','g','b','c','k','w','r','g','b','c','k','w','r','g','b','c','k','w','r','g','b','c','k','w','r','g','b','c']) #bisa beri color tiap bar, color=[]
    # custom.set_xlabel('Nilai X')
    plt.xticks(xalas,kota,rotation=90)
    custom.set_ylabel('Nilai Y')
    custom.set_ylim(0,10)
    custom.set_zlabel('Nilai Z')
    plt.show()

print3D()