# corrected
# by Batagelj, V.; 11. December 2015
# Corrected network elements importance measures
# program expects as input data a Pajek file T with network with computed
# triangular weights and a file D with nodes degrees
wdir = 'c:/users/batagelj/work/python/graph/graph'
# gdir = 'C:/Users/batagelj/Documents/papers/2015/CRoNoS/london/nets/'
gdir = 'C:/Users/batagelj/Documents/manuscripts/corrected/corr/'
import sys, os
sys.path = [wdir]+sys.path
os.chdir(wdir)
import Graph
from copy import copy, deepcopy

T = "UsAirTri.net"
D = "deg.clu"
N = Graph.Graph.loadPajek(gdir+T)
N.loadPajekVec('deg',gdir+D)

P = deepcopy(N)
n = len(N)
d = [0]*n
for i in range(n): d[i] = N.getNode(i+1,'deg')-1
# --- Overlap weight
Tmed = 0
for e in N.links():
   (u,v,k) = e
   Te = N.getLink(e,'w')
   if Te > 0: Tmed = max(Tmed,min(d[u-1],d[v-1]))
   Td = d[u-1]+d[v-1]-Te
   if Td <= 0:
      over = 0; print(u,v,d[u-1],d[v-1],Te)
   else: over = Te/Td
   P.setLink(e,'over',over)

Tmax = 0
for e in N.links():
   (u,v,k) = e; Te = N.getLink(e,'w')
   if Te > Tmax: Tmax = Te
print('maxTe = ',Tmax)
# --- Corrected Overlap weight
for i in range(n): d[i] = N.getNode(i+1,'deg') - 1
for e in N.links():
   (u,v,k) = e
   Te = N.getLink(e,'w')
   over = 0
   if Te > 0:
      Td = Tmax + max(d[u-1],d[v-1]) - Te
      over = Te/Td
   P.setLink(e,'w',over)
P.savePajek(gdir+'CorrOverlapMax.net')
dat = open(gdir+'overlapMax.csv','w')
dat.write('"Te";"over";"cOver";"m";"M"\n')
for i in range(n): d[i] = N.getNode(i+1,'deg')
for e in P.links():
   (u,v,k) = e; Te = N.getLink(e,'w')
   over = P.getLink(e,'over'); cOver = P.getLink(e,'w')
   m = min(d[u-1],d[v-1]); M = max(d[u-1],d[v-1])
   dat.write(str(Te)+';'+str(over)+';'+str(cOver)+';'+str(m)+';'+str(M)+'\n')
dat.close()

# --- Clustering Coefficient --------------------------------------------------
E = [0]*n
for v in N.nodes():
   s = 0
   for e in N.edgeStar(v): s = s + N.getLink(e,'w')
   E[v-1] = s/2
for i in range(n): d[i] = N.getNode(i+1,'deg')
Cc = [0]*n
for i in range(n):
   if d[i] <= 1: Cc[i] = 0
   else: Cc[i] = 2*E[i]/d[i]/(d[i]-1)
   P.setNode(i+1,'Cc',Cc[i])
# --- Corrected Clustering Coefficient
cCc = [0]*n
for i in range(n):
   if d[i] <= 0: cCc[i] = 0
   else: cCc[i] = 2*E[i]/d[i]/Tmax
   P.setNode(i+1,'cCc',cCc[i])
P.savePajekVec('cCc',gdir+'CorrClusC.vec')
P.savePajekVec('Cc',gdir+'ClusC.vec')
csv = open(gdir+'ccMax.csv','w')
csv.write('"deg";"E";"Cc";"cCc"\n')
for i in range(n):
   csv.write(str(d[i])+';'+str(E[i])+';'+str(Cc[i])+';'+str(cCc[i])+'\n')
csv.close()

