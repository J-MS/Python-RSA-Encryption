from math import ceil, sqrt
from random import shuffle, randint

#IMPROVE
primes = [2, 3, 5];
for num in range(7, 500000, 2):
	root = int(sqrt(num) + 1);
	p = True;

	for prime in primes:
		if (prime >= root):
			break
		elif (num % prime == 0):
			p = False;
			break

	if p:
		primes.append(num);

#IMPROVE
bigPrimes = primes[int(len(primes) / 2):]
shuffle(bigPrimes);


sharedPrime = bigPrimes[0];

sharedBase = randint(500000, 1000000);

#Alice and Bob's secret Keys.
aliceSK = 72
bobSK = 12

#Start Exchange
print("Publicly Shared Prime: " + str(sharedPrime));
print("Publicly Shared Base: " + str(sharedBase));

#Alice -> Bob base^sk mod p
A = ((sharedBase**aliceSK) % sharedPrime);
print("Alice sends " + str(A) + " over sniff-able protocol. (HTTP)");

#Bob -> Alice base^sk mod p
B = ((sharedBase**bobSK) % sharedPrime);
print("Bob sends " + str(B) + " over sniff-able protocol. (HTTP)");

print("\n\n\n");

print("Calculated Shared Secret Key:");

#For Alice
aliceSharedSK = ((B ** aliceSK) % sharedPrime);
print("Alice Shared Secret Key: " + str(aliceSharedSK));

#For Bob
bobSharedSK = ((A ** bobSK) % sharedPrime);
print("Bob Shared Secret Key: " + str(bobSharedSK));
