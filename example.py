from random import randint;
from math import sqrt;
from math import ceil;

#This is intentionally horrible, albeit working, code. Alter it to make it
#more readable, styled, and documented. Also, why 500? Make this a more
#realistic and 'smart' number. How big should I primes be, should they really
#start at two?
primes = [2];
for interger in range(3, 100000): 
	root = ceil(sqrt(interger))
	for index, prime in enumerate(primes):
		if prime >= root: #checks if we are geting too big
			break
		elif interger % prime == 0:
			break
		else:
			primes.append(interger)
#This should also be changed.
sharedPrime = primes[randint(0, len(primes) - 1)];
while sharedPrime < 1000:
	sharedPrime = primes[randint(0, len(primes) - 1)];
sharedBase = randint(5, 1000000);

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

# next thing to do is a way to encrypt a message, and decrypt
