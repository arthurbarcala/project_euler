#Probably correct but i'm not sure
def collatz_seq(term: int) -> int:
    terms_num = 1
    
    while term > 1:
        
        if term%2 == 0:
            term/=2
        else:
            term = (3*term)+1
        terms_num+=1
    return terms_num

def main() -> None:
    num = 0
    biggest_num = 0
    biggest_seq = 0
    while num < 1000000:
        term = collatz_seq(num)
        if term > biggest_seq:
            biggest_num = num
            biggest_seq = term
        num+=1
    print("Number: {}, Sequence terms: {}".format(biggest_num, biggest_seq))

if __name__ == "__main__":
    main()