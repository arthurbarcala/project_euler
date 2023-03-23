def main() -> None:
    t1 = 1
    t2 = 2
    t3 = t1+t2
    n = 4000000
    sum = 0
        
    while t3 < n:
        t1 = t2
        t2 = t3
        t3 = t1+t2
        
        if t3%2 == 0:
            sum+=t3
    
    print(sum)

if __name__ == "__main__":
    main()