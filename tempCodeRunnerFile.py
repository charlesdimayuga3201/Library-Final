 d_var = 'SELECT returndate FROM BookBorrow where borrowkey = %s'
                    d_val = (e2.get())
                    cur.execute(d_var, d_val)
                    d_result = cur.fetchone()