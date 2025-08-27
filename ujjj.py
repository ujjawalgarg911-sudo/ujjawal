# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate all prime numbers till n (inclusive)
def primes_up_to_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Function to generate the first n prime numbers
def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Main function to tie everything together
def main():
    try:
        n = int(input("Enter a number: "))

        # a. Check if 'n' is prime
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

        # b. Generate all prime numbers till 'n'
        primes_till_n = primes_up_to_n(n)
        print(f"All prime numbers up to {n}: {primes_till_n}")

        # c. Generate first 'n' prime numbers
        first_n = first_n_primes(n)
        print(f"First {n} prime numbers: {first_n}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the main function
if __name__ == "__main__":
    main()
