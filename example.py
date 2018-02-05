from random import randint;

#This is intentionally horrible, albeit working, code. Alter it to make it
#more readable, styled, and documented. Also, why 500? Make this a more
#realistic and 'smart' number. How big should I primes be, should they really
#start at two?
primes = [p for p in range(2, 500) if 0 not in [p % c for c in range(2, p)]];

#This should also be changed.
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
