for i in range(20):
    print(f"indice {i}:   {(i | i+1)} == {(i + (i&-i))}")