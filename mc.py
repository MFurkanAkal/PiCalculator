import numpy as np

def monte_carlo_pi(number_of_samples = 100000000): # 100.000.000 adet nokta üretiyoruz.
    inside = 0 # İçerideki nokta sayısını 0'dan başlatıyoruz.

    for i in range(number_of_samples):
        x = np.random.rand() 
        y = np.random.rand() # x ve y eksenlerinde iki adet rastgele sayı üretiyoruz.
        
        if np.square(x) + np.square(y) < 1: # Çemberin içindeyse,
            inside+=1 # içerideki nokta sayısını bir artırıyoruz.

    return 4 * float(inside) / number_of_samples # 4 * çemberin içindekiler / hepsi
    
print(monte_carlo_pi())