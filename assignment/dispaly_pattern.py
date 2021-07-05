def disp_pattern(num):
    for i in range(1,num+1):
        print(([j for j in range(1,i)]), end=" ")
        print("")

disp_pattern(5)