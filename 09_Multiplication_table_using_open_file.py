for i in range(2,31):
    with open(f"tables/Multiplication_tables_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")
            if j!=10:
                print('\n')