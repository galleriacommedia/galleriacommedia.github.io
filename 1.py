=(287,5-(INDEX(J:J; MAX(FILTER(ROW(J10:J21);NOT(ISBLANK(J10:J21));J10:J21>0)); 0)) + INDEX(K:K; MAX(FILTER(ROW(K10:K21);NOT(ISBLANK(K10:K21));K10:K21>0)); 0))/(EOMONTH(TODAY();0) - TODAY())*7