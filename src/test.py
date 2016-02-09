"""----------------
----Ibrahima Diao--
----Test Bilberry--
----------------"""
import shapefile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
#------lecture shapefile--------
r=shapefile.Reader("applitest")
#-------geometrie--------------
shapes=r.shapes();
a=len(shapes);
#------type-------------------
b=shapes[1].shapeType;
#print b
#------champ---------
champs = r.fields;
#print champs;
#-----record------
records=r.records();
#print records
c = len(records);
rec =r.record(3);
cns = []
for nshp in xrange(a):
       cns.append(records[nshp][0])
cns = np. array(cns)

#-------draw polygon and plot------
fig  = plt.figure()
ax   = fig.add_subplot(111)

for sha,recr in zip( shapes,cns) :

         ptchs   =[];
         pts     = np.array(sha.points);
         prt     = sha.parts;
         par     = list(prt) + [pts.shape[0]]
         
         if recr==1 :
             for pij in xrange(len(prt)): 
                 poly1 = Polygon(pts[par[pij]:par[pij+1]], facecolor='aqua', alpha=0.1);
                 plt.gca().add_patch(poly1);
                 
         else :
             for ij in xrange(len(prt)): 
                poly = Polygon(pts[par[ij]:par[ij+1]], facecolor='red', alpha=0.1);
                plt.gca().add_patch(poly);

plt.legend([poly,poly1], ["ouvert","ferme"])                       
ax.set_xlim(2.00512,2.00566)
ax.set_ylim(48.4142,48.4147)
plt.legend()
fig.savefig('touba.png')
plt.show();
 
      



