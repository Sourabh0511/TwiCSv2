import csv
gap_dict={0: 0.5526509135902821, 1: 0.24007743596367245, 2: 0.10005930235073097, 3: 0.050899866391797034, 4: 0.025772485160149166, 5: 0.012743259604281883, 6: 0.006921813814821709, 7: 0.003782260831823902, 8: 0.0025179944171375454, 9: 0.0013858015415885731, 10: 0.0009767965383466976, 11: 0.0005578842679857202, 12: 0.00040798944691892693, 13: 0.0002452876695346507, 14: 0.00016157009004035805, 15: 0.00011596175529226758, 16: 0.00010405215500371109, 17: 8.120153344768683e-05, 18: 6.366105174451738e-05, 19: 4.214207449366168e-05, 20: 6.994411538254441e-05, 21: 4.1953757539315304e-05, 22: 4.369942067773079e-05, 23: 2.345900364548555e-05, 24: 2.3179991772365096e-05, 25: 2.242760476990983e-05, 26: 1.6492788459643106e-05, 27: 1.1119828361547062e-05, 28: 1.230437310285321e-05, 29: 1.4508593023529762e-05, 30: 1.1231387929262885e-05, 31: 1.154593979852995e-05, 32: 7.619135224317868e-06, 33: 8.856621052313268e-06, 34: 6.12571600808198e-06, 35: 2.6896876537473523e-06, 36: 7.334077049329426e-06, 37: 3.850785002642871e-06, 38: 5.320019011406792e-06, 39: 4.9941123534650825e-06, 40: 3.82129130836425e-06, 41: 4.603172005098138e-06, 42: 2.3221946977910374e-06, 43: 2.654147657600739e-06, 44: 2.7014113499526673e-06, 45: 2.292701003512416e-06, 46: 1.919530653218778e-06, 47: 2.2809773073071013e-06, 48: 3.79784391595362e-06, 49: 1.5403140010571484e-06, 50: 1.8900369589401567e-06, 51: 2.3104710015857223e-06, 52: 2.25148361302848e-06, 53: 1.919530653218778e-06, 54: 2.6896876537473523e-06, 55: 3.792166521616297e-07, 56: 1.5285903048518336e-06, 57: 7.523870024552677e-07, 58: 1.931254349424093e-06, 59: 1.5520376972624629e-06, 60: 7.701570005285742e-07, 61: 1.5285903048518336e-06, 62: 7.701570005285742e-07, 63: 1.913484351350786e-06, 64: 1.931254349424093e-06, 65: 1.9429780456294075e-06, 66: 1.5637613934677777e-06, 67: 1.1610973488955187e-06, 68: 7.701570005285742e-07, 69: 3.045456913498353e-06, 70: 7.818806967338889e-07, 71: 3.9094034836694444e-07, 72: 1.5520376972624629e-06, 73: 3.9094034836694444e-07, 74: 3.068904305908982e-06, 75: 1.1610973488955187e-06, 77: 1.1610973488955187e-06, 78: 1.5520376972624629e-06, 79: 1.5342676991891563e-06, 80: 1.883990657072165e-06, 83: 7.701570005285742e-07, 84: 1.9429780456294075e-06, 85: 7.818806967338889e-07, 86: 3.9094034836694444e-07, 87: 3.792166521616297e-07, 88: 1.1493736526902038e-06, 89: 3.9094034836694444e-07, 90: 3.9094034836694444e-07, 91: 1.5520376972624629e-06, 92: 7.701570005285742e-07, 93: 1.1316036546168975e-06}

with open('distr_values.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in gap_dict.items():
       writer.writerow([key, value])