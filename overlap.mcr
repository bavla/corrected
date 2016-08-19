NETBEGIN 2
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 1

Msg Overlap weights
Msg by Vladimir Batagelj, August 2015
Msg ---------------------------
Msg network N
N 2 SETLINEVAL1 1 1 (332)
N 2 DLOOPS 2 (332)
N 2 ATOE 2 (332)
N 2 SIMPLSINGLE 2 (332)
V 1 DEGV 2 [2] (332)
N 3 RINGS3 2 [5,1] (332)
N 4 NETVECT 2 1 1 1 1 (332)
Msg const = -2; Click OK
N 5 ADDLINVAL 4 -2.0000 1 (332)
N 4 DN  (332)
N 6 CROSSINTERSECT 5 3 2 (332)
N 5 DN  (332)
N 7 CROSSINTERSECT 3 6 4 (332)
N 3 DN  (332)
N 6 DN  (332)
N 7 NETNAME Overlap weights
Msg Finished
Msg ---------------------------
