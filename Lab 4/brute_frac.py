def getStrings(n):
   return [list(bin(x)[2:].rjust(n, '0')) for x in range(2**n)]


def bruteforce_fractional(p,w,m):
    # For all weights, calculate the profit
    assert len(p) == len(w), "W and p not equal length"
    maxProfit = 0
    n = len(w)
    maxSeletion = ['0'] *n 
    
    solutions = getStrings(n)
    
    for s in solutions:
        
        item_rem = [i for i, x in enumerate(s) if x == '0']
        
        non_frac_profit=sum([int(s[i]) * p[i] for i in range(n)])
        weight = sum([int(s[i]) * w[i] for i in range(n)])
        
        fract_profit = 0
        temp_solution = s

        if weight<m:
            maxIndex = 0
            for i in item_rem:
                rem = m-weight if(m-weight < w[i]) else w[i]
                frac = (p[i]/w[i])*(rem)
                if frac > fract_profit:
                    fract_profit = frac
                    maxIndex = i
            temp_solution[maxIndex] = str(round(fract_profit/p[i],2)*100)+'%'
                

        totalProfit = fract_profit + non_frac_profit

        if weight<= m and totalProfit >= maxProfit:
            maxProfit = totalProfit
            maxSeletion = temp_solution


    return (int(maxProfit),('|'.join(maxSeletion)).split('|'))


wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
print(bruteforce_fractional(val, wt, capacity))