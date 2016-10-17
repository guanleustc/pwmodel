from context import pwmodel as pwm
from pwmodel import NGramPw, PcfgPw, HistPw, helper
import pytest
import os

# leak_file = os.path.expanduser('../leaked/test-withcount.txt.bz2')
leak_file = os.path.expanduser('../leaked/myspace-withcount.txt.bz2')
# leak_file = os.path.expanduser('../leaked/rockyou-withcount.txt.bz2')
# leak_file = "rockyou"

if __name__ == "__main__":
    pwm1 = NGramPw(pwfilename=leak_file, n=4)
    print (pwm1.prob('abc123'))
    result = pwm1.qth_pw(1)[1]
    print(result)


    hm = pwm.HistPw(leak_file)
    print (hm.prob('abc123'))
    result = hm.qth_pw(1)[1]
    print(result)


    L = [hm.qth_pw(q)
         for q in xrange(1, 20, 1)]
    print(L)
    print(zip(L, L[1:]))
    # assert all(x>y for x,y in zip(L, L[1:]))