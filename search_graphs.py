import math
import pandas as pd
import numpy as np


MAX_N = 1367
MIN_N = 2  


k_values = range(26, -1, -1)
t_values = range(37, 0, -1)


rows_count = MAX_N - MIN_N + 1
df = pd.DataFrame({
    "n": range(MIN_N, MAX_N + 1),
    "diff": [pd.NA] * rows_count,
    "k": [pd.NA] * rows_count,
    "t": [pd.NA] * rows_count,
    "a_full": [pd.NA] * rows_count, 
    "a_part": [pd.NA] * rows_count, 
    "b_full": [pd.NA] * rows_count, 
    "b_part": [pd.NA] * rows_count  
})
df.set_index("n", inplace=True)

def check_and_write(n, e, k, t, a_f, a_p, b_f, b_p):
    if MIN_N <= n <= MAX_N:
        harborth = math.floor(3 * n - math.sqrt(12 * n - 3))
        diff = e - harborth
        
        if diff >=0 and pd.isna(df.at[n, "diff"]):
            df.at[n, "diff"] = int(diff)
            df.at[n, "k"] = int(k)
            df.at[n, "t"] = int(t)
            df.at[n, "a_full"] = int(a_f)
            df.at[n, "a_part"] = int(a_p)
            df.at[n, "b_full"] = int(b_f)
            df.at[n, "b_part"] = int(b_p)

for k in k_values:
    for t in t_values:
       
        n_val = (k * k) - ((k - 1) * k / 2) + 3 + 2 * k + 3 * t + 2 * k * t + ((2 * k - (k + 1) + 3) * (k + 1) / 2)
        e_val = (3 * k * k) + ((-3 * k * k + k) / 2) + 3 + 4 * k + 6 * t + 6 * k * t + \
                (3 * (k + 1) * k) + ((-3 * (k + 1)**2 + 9 * (k + 1)) / 2) - (k + 1)

        
        saved_n = n_val
        saved_e = e_val

       
        for step_a in range(1, k + 2):
            a_rows_removed = step_a - 1
            
            
            curr_n = saved_n
            curr_e = saved_e
            
           
            check_and_write(curr_n, curr_e, k, t, a_rows_removed, 0, 0, 0)

           
            for step_b in range(1, k + 2):
                b_rows_removed = step_b - 1
                len_b = step_b 
                
                b_vertices_removed = 0
                
                
                for _ in range(len_b - 1):
                    curr_e -= 3
                    curr_n -= 1
                    b_vertices_removed += 1
                    check_and_write(curr_n, curr_e, k, t, a_rows_removed, 0, b_rows_removed, b_vertices_removed)
                
                
                curr_e -= 2
                curr_n -= 1
                b_vertices_removed += 1
                check_and_write(curr_n, curr_e, k, t, a_rows_removed, 0, b_rows_removed, b_vertices_removed)
            
            
            if step_a <= k:
                len_a = step_a
                a_vertices_removed = 0
                
                
                for _ in range(len_a - 1):
                    saved_e -= 3
                    saved_n -= 1
                    a_vertices_removed += 1
                    
                    check_and_write(saved_n, saved_e, k, t, a_rows_removed, a_vertices_removed, 0, 0)
                
                
                saved_e -= 2
                saved_n -= 1
                a_vertices_removed += 1
                check_and_write(saved_n, saved_e, k, t, a_rows_removed, a_vertices_removed, 0, 0)


cols_to_int = ["diff", "k", "t", "a_full", "a_part", "b_full", "b_part"]
df = df.astype({c: "Int64" for c in cols_to_int})


df.reset_index(inplace=True)
csv_str = df.to_csv(index=False, encoding="utf-8")
print(csv_str)
