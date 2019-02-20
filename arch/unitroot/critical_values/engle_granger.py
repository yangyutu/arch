import numpy as np

eg_num_variables = np.arange(1, 13)
eg_cv = {
    "nc": {
        1: [
            [-2.56531, -3.96106, -36.61383, 0.0],
            [-3.34181, -10.42545, -9.89654, 0.0],
            [-3.86055, -13.81019, -15.88983, 0.0],
            [-4.27499, -17.40159, -22.54924, 0.0],
            [-4.63274, -20.87518, -40.25451, 0.0],
            [-4.95011, -24.81521, -51.9951, 0.0],
            [-5.23981, -28.95035, -49.47057, 0.0],
            [-5.50786, -32.91211, -60.41852, 0.0],
            [-5.76028, -36.30407, -108.3346, 292.20709],
            [-5.99595, -40.48187, -122.59292, 416.19765],
            [-6.21882, -44.93531, -124.30269, 344.85885],
            [-6.4327, -48.98175, -150.14852, 576.24021],
        ],
        5: [
            [-1.94129, -1.43667, -27.53483, 293.17833],
            [-2.76041, -6.71455, 9.21194, 0.0],
            [-3.29591, -8.88265, 11.16637, -154.05609],
            [-3.72154, -11.17293, 0.36772, 0.0],
            [-4.0852, -13.8498, -3.89309, -146.83769],
            [-4.40729, -16.7519, -9.71602, 0.0],
            [-4.70128, -19.71107, -15.26736, 0.0],
            [-4.97257, -22.8001, -20.63603, 0.0],
            [-5.22619, -25.83941, -31.37162, 0.0],
            [-5.46474, -29.09774, -36.69423, 0.0],
            [-5.69007, -32.66104, -27.82805, 0.0],
            [-5.90562, -35.81454, -52.66435, 313.77598],
        ],
        10: [
            [-1.61694, -0.84612, -3.45254, 0.0],
            [-2.45775, -5.3941, 17.48759, 0.0],
            [-3.002, -6.94074, 18.41839, -176.33032],
            [-3.43229, -8.73653, 11.6623, -178.64494],
            [-3.79937, -10.76673, -1.50258, 0.0],
            [-4.1237, -13.3115, 2.64903, -129.22759],
            [-4.41937, -15.81393, -1.52055, 0.0],
            [-4.69236, -18.42511, -6.21173, 0.0],
            [-4.947, -21.03479, -16.17567, 0.0],
            [-5.18636, -23.94811, -15.24812, 0.0],
            [-5.41309, -26.97555, -9.86284, 0.0],
            [-5.62919, -29.93246, -15.12123, 0.0],
        ],
    },
    "c": {
        1: [
            [-3.42939, -9.04951, -38.65063, 299.81138],
            [-3.89556, -12.88828, -36.28867, 0.0],
            [-4.29352, -16.4212, -54.12133, 245.12776],
            [-4.6427, -20.67068, -40.29239, 0.0],
            [-4.95745, -24.56677, -52.01652, 0.0],
            [-5.24499, -28.38688, -74.16502, 0.0],
            [-5.51121, -32.47825, -80.32785, 0.0],
            [-5.7604, -36.482, -103.37305, 0.0],
            [-5.99672, -40.51347, -120.58055, 412.42354],
            [-6.21951, -44.9197, -130.32127, 448.27299],
            [-6.43239, -49.28968, -141.31781, 511.4834],
            [-6.63668, -53.73437, -148.52868, 502.06667],
        ],
        5: [
            [-2.86129, -5.14873, -12.36841, 0.0],
            [-3.33587, -7.70271, -17.56084, 0.0],
            [-3.74014, -10.46995, -15.72601, 0.0],
            [-4.096, -13.29884, -19.56612, 0.0],
            [-4.41497, -16.29297, -23.51184, 0.0],
            [-4.70648, -19.31537, -31.77114, 0.0],
            [-4.97607, -22.52395, -30.08049, 0.0],
            [-5.22834, -25.69162, -39.01927, 144.25937],
            [-5.46645, -28.92464, -46.24198, 240.00926],
            [-5.69132, -32.49325, -41.86912, 171.78667],
            [-5.90647, -35.92924, -45.25811, 192.39371],
            [-6.11228, -39.39257, -53.83574, 333.65708],
        ],
        10: [
            [-2.56689, -3.61099, -9.58876, 0.0],
            [-3.04418, -5.76651, -5.14164, 0.0],
            [-3.4516, -7.98489, -7.0056, 0.0],
            [-3.80993, -10.36094, -8.01828, 0.0],
            [-4.13141, -12.92287, -6.29653, 0.0],
            [-4.42465, -15.46161, -13.26664, 0.0],
            [-4.69583, -18.22484, -11.22417, 0.0],
            [-4.94952, -21.00033, -14.61216, 0.0],
            [-5.18809, -23.94365, -12.18484, 0.0],
            [-5.41452, -26.89062, -13.92959, 0.0],
            [-5.63022, -29.93633, -14.57785, 0.0],
            [-5.83674, -32.98558, -19.30149, 190.4883],
        ],
    },
    "ct": {
        1: [
            [-3.95786, -14.46375, -23.67354, 0.0],
            [-4.32697, -17.89175, -32.28232, 0.0],
            [-4.66186, -21.47627, -41.47255, 0.0],
            [-4.97012, -25.20916, -45.98208, -271.06981],
            [-5.25385, -28.9107, -66.05407, 0.0],
            [-5.51806, -32.73328, -84.56796, 0.0],
            [-5.76621, -36.71672, -100.94389, 0.0],
            [-5.99954, -41.33218, -85.72141, 0.0],
            [-6.22235, -45.1738, -121.57906, 0.0],
            [-6.43515, -49.51636, -124.47142, 0.0],
            [-6.63928, -53.63334, -150.47817, 377.13865],
            [-6.83525, -57.83089, -178.22376, 706.80095],
        ],
        5: [
            [-3.4096, -9.12963, -8.62301, 0.0],
            [-3.77985, -11.51841, -14.04813, 0.0],
            [-4.11857, -14.06634, -21.87804, 0.0],
            [-4.4289, -16.84731, -25.83539, 0.0],
            [-4.7153, -19.94362, -19.9281, 0.0],
            [-4.98226, -22.96222, -26.57049, 0.0],
            [-5.233, -26.08357, -32.19074, 0.0],
            [-5.46973, -29.39927, -32.15236, 0.0],
            [-5.69469, -32.73386, -35.9542, 0.0],
            [-5.90917, -36.09209, -42.17154, 0.0],
            [-6.11407, -39.64588, -43.27053, 0.0],
            [-6.31106, -43.19348, -48.57149, 179.27424],
        ],
        10: [
            [-3.1265, -7.05005, -3.76714, 0.0],
            [-3.49568, -8.97572, -7.30778, 0.0],
            [-3.83483, -11.04662, -13.3054, 0.0],
            [-4.14613, -13.42439, -14.14323, 0.0],
            [-4.43367, -16.03385, -8.28769, 0.0],
            [-4.702, -18.69615, -7.32545, 0.0],
            [-4.95399, -21.34162, -12.6362, 0.0],
            [-5.19196, -24.148, -15.67516, 0.0],
            [-5.41771, -27.05414, -16.97723, 0.0],
            [-5.63287, -30.07677, -15.97841, 0.0],
            [-5.83886, -33.16908, -13.55009, 0.0],
            [-6.0363, -36.34216, -14.49967, 0.0],
        ],
    },
    "ctt": {
        1: [
            [-4.37085, -19.2718, -60.57539, 0.0],
            [-4.69229, -22.62539, -68.60664, 0.0],
            [-4.99062, -26.1695, -81.79922, 0.0],
            [-5.26834, -29.65749, -109.43084, 309.84983],
            [-5.52863, -33.71417, -105.74663, 0.0],
            [-5.7732, -37.76276, -115.02537, 0.0],
            [-6.00513, -41.92026, -119.82444, 0.0],
            [-6.22695, -45.70058, -152.56997, 489.05912],
            [-6.43876, -49.91375, -165.64724, 563.68363],
            [-6.6424, -54.0976, -187.68375, 823.63052],
            [-6.83744, -58.69286, -186.12393, 760.12199],
            [-7.02532, -63.19904, -188.58481, 709.82954],
        ],
        5: [
            [-3.83175, -13.10296, -25.06855, 0.0],
            [-4.15343, -15.48598, -30.86302, 0.0],
            [-4.45274, -18.13948, -33.93607, 0.0],
            [-4.73239, -20.94686, -36.71804, 0.0],
            [-4.99465, -23.85826, -44.38294, 0.0],
            [-5.24179, -27.0185, -43.44657, 0.0],
            [-5.47625, -30.13244, -53.53391, 225.91872],
            [-5.69906, -33.46406, -54.24084, 229.44631],
            [-5.91267, -36.82509, -56.01442, 229.65848],
            [-6.11735, -40.24378, -63.16465, 358.58686],
            [-6.31409, -43.69119, -70.62886, 460.8922],
            [-6.50369, -47.27836, -74.2144, 544.98443],
        ],
        10: [
            [-3.55284, -10.54834, -15.4041, 0.0],
            [-3.87319, -12.45731, -21.36845, 0.0],
            [-4.17265, -14.59896, -24.5818, 0.0],
            [-4.45266, -17.02585, -22.41412, 0.0],
            [-4.71572, -19.52035, -26.05204, 0.0],
            [-4.96369, -22.17878, -27.54217, 146.90796],
            [-5.19886, -24.96449, -26.12144, 133.48601],
            [-5.42262, -27.85023, -26.99377, 179.51091],
            [-5.63702, -30.70411, -32.52006, 278.34195],
            [-5.84211, -33.79982, -28.4263, 252.22458],
            [-6.03949, -36.92024, -26.86134, 248.30608],
            [-6.22959, -40.12848, -28.28935, 348.97583],
        ],
    },
}


class EngleGrangerCV(object):
    def __getitem__(self, item):
        # item ['nc',10,3]
        if (
            len(item) != 3
            or item[0] not in eg_cv.keys()
            or item[1] not in (10, 5, 1)
            or item[2] not in eg_num_variables
        ):
            raise KeyError("Item not found: {0}".format(item))
        return np.array(eg_cv[item[0]][item[1]][item[2] - 1])


engle_granger_cv = EngleGrangerCV()
