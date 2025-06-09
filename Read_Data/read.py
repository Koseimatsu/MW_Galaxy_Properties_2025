# 列名を定義
import pandas as pd
import numpy as np

def load_Global_data(filename = "../Global_Galaxy_Properties/Global_Evolution.dat"):
    columns = [
        "Time_Gyr", "M_star_Msun", "Mdust_Msun", "Mdust_a<2nm_Msun", "Mdust_a<50nm_Msun", "Mdust_a<500nm_Msun", 
        "Age_Gyr", "SFR_Msun_per_yr", "Avg_Dust_Size_um", "Gas_Metallicity", "Young_Star_Mass_Msun",
        "Dust_HalfMassRadius_kpc", "YoungStar_HalfMassRadius_kpc", "OldStar_HalfMassRadius_kpc",
        "Star_HalfMassRadius_kpc"
    ]

    df = pd.read_csv(filename, delim_whitespace=True, comment='#', names=columns)
    return df

def load_attenuation_curve(filename):
    columns = [
        "Time_Gyr", "Av", "A_B", "A_NUV", "A_FUV", "AFUV_Av", 
        "Bump", "C1", "C2", "C3", "C4"
    ]

    df = pd.read_csv(filename, delim_whitespace=True, comment='#', names=columns)
    return df

if __name__ == "__main__":
    # Load global galaxy properties
    global_data = load_Global_data(filename="../Global_Galaxy_Properties/Global_Evolution.dat")
    print(global_data.head())

    # Load attenuation curve data
    Models = ["Static", "Dynamic"]
    Attenuation_Models = ["NoScattering",  "WithScattering"]
    Inclinations = np.arange(0,91,10)
    for imodel, model in enumerate(Models):
        for iatten, atten_model in enumerate(Attenuation_Models):
            for itheta in range(len(Inclinations)):
                # Load the attenuation curve for each inclination
                filename = f"../Matsumoto2025_Attenuation/{model}/{atten_model}/" + "MW_Attenuation_Curves_i{:02}".format(Inclinations[itheta]) + ".dat"
                attenuation_curve = load_attenuation_curve(filename)
                print(f"Model: {model}, Attenuation: {atten_model}"
                      f", Inclination: {Inclinations[itheta]} degrees")
                print(attenuation_curve.head())