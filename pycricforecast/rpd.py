def rpd(n_runs,n_balls):
    n_remain = 120 - n_balls
    rpd = n_runs/n_balls
    return n_runs+ (rpd*n_remain) 
