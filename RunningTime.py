import time
def timed_run(function,*args):
    "Calls the function with arguments *args and returns time and result"
    start = time.time()
    result = function(*args)
    end = time.time()
    return end - start, result
    
def timed_calls(n,fn,*args):
    """Calls a function n times if n is int or till n seconds if otherwise
    and returns min,max and average of running times"""
    if isinstance(n,int):
        times = [timed_run(fn,*args)[0] for _ in range(n)]
    else:
        time = 0.0
        times = []
        while (time < n):
            temp = timed_run(fn,*args)[0]
            times.append(temp)
            time += temp
#        times = []
#        while(sum(times) < n):
#            times.append(timed_run(fn,*args)[0])
            
    return min(times),average(times),max(times)
    
def average(numbers):
    return sum(numbers)/float(len(numbers))
