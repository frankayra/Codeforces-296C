def BinSearch(num, begin, sign_factor, get, n):
            l, r = begin, n-1
            m, last_index_found = l+(r-l)//2, -1
            
            while(l < r):
                beg_to_m_gcd = get(begin, m)
                if beg_to_m_gcd == num:
                    last_index_found = m
                    
                if sign_factor == -1:
                    if beg_to_m_gcd <= num: 
                        r = m
                        m = l+(r-l)//2
                    else: 
                        l = m
                        m = l+(r-l+1)//2
                elif sign_factor == 1:
                    if beg_to_m_gcd >= num: 
                        l = m
                        m = l+(r-l+1)//2                    # Favorece el caso de acercar el limite izquierdo hacia la derecha
                    else: 
                        r = m
                        m = l+(r-l)//2                      # Viceversa


            print(f"last_index_found: {last_index_found}")
            return last_index_found

def main():
    array = [6, 5, 4, 4, 4, 4, 4, 4, 3, 2, 1]
    get = lambda a, b: array[b]
    print(BinSearch(4, 0, -1, get, len(array)))
    print(BinSearch(4, 0, 1, get, len(array)))

main()