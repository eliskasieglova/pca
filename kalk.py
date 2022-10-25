blue = 0.0888
green = 0.0813
red = 0.0604
nir = 0.3387
swir1 = 0.1532
swir2 = 0.0804


sum = blue + green + red + nir + swir1 + swir2
print(sum)

values = [blue, green, red, nir, swir1, swir2]
podily = []

for val in values:
    podily.append((val/sum)*100)



print(podily)

print(blue + green + nir + swir1)
