'''
Michael Barnard
Created for NPR Lab

Analysis of impedance data from the gen 3 TEENI device
'''

import os
import sys
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def Load_EIS_Data(data_folder, condition, setup):
    '''
    Load data and labels from one folder into a single datastructure
    Headers are Freq (Hz), Z' (Ω), -Z'' (Ω), Z (Ω), -Phase (°)
    '''

    # Empty list to temporatily hold all channel data before moving to array
    channel_data_list = []

    # Iterate through every channel csv file
    # 1A, 1B, ..., 4C, 4D
    for ch_num in "1234":
        for ch_letter in "ABCD":
            file_name = \
                f'cond{condition}_setup{setup}_ch{ch_num}{ch_letter}__FRA.csv'

            single_channel_data = \
                np.genfromtxt(data_folder + file_name, delimiter=",")
            channel_data_list.append(single_channel_data[1:, :])

    channel_data = np.asarray(channel_data_list)

    return channel_data

def Plot_Data():
    '''
    Plot data in pretty pictures so I can stare at it
    '''

    ff = 0


if __name__ == "__main__":
    # Update global font size to 22 because 4k screen
    mpl.rcParams.update({'font.size': 22})
    # Channel LUT to convert an index into a label
    channel_LUT = ["1A", "1B", "1C", "1D",
                   "2A", "2B", "2C", "2D",
                   "3A", "3B", "3C", "3D",
                   "4A", "4B", "4C", "4D",
                    ]

    data_folder = '/home/michael/Documents/OttoLab/TEENI/Data/2019_09_16__gen3_DUT1_impedance/'

    # Data output in format: channel, row, column
    EIS_channel_data = Load_EIS_Data(data_folder, 1, 1)

    # Iterate through all channels
    # TODO: There has to be a more effective way
    # for i in range(EIS_channel_data.shape[0]):
    for i in (8,9,10,11):
        plt.plot(EIS_channel_data[i, :, 0], EIS_channel_data[i, :, 3], label=channel_LUT[i])
    plt.xlabel('Freq (Hz)')
    plt.xscale("log")
    plt.ylabel('Z (Ohms))')
    plt.yscale("log")
    plt.grid(which="both", axis="both")
    plt.legend()

    plt.show()

    # fig, ax = plt.figure()
    # ax.plot(EIS_channel_data[0, ])

    ff = 0
