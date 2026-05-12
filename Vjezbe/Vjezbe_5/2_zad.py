def racun(N):
    broj = 5

    for i in range(N):
        broj += 1/3

    for i in range(N):
        broj -= 1/3

    return broj

print("Za 200 iteracija: ", racun(200))
print("Za 2000 iteracija: ", racun(2000))
print("Za 20000 iteracija: ", racun(20000))