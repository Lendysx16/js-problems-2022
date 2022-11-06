def num_is_prime(num):
    sq = int(num ** 0.5) + 1
    return not any(num % i == 0 for i in range(2, sq))


with open('files\\in.txt') as input_file:
    start = int(input_file.readline())
    end = int(input_file.readline())
    with open('files\\out.txt', 'w') as output_file:
        for i in range(start, end):
            if num_is_prime(i):
                output_file.write(str(i) + '\n')
