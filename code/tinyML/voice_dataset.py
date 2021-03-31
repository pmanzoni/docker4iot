import numpy as np

NUMBER_OF_LABELS   = 2
DATA_SIZE_OF_LABEL = 50  # number of instances for each label

data = np.array([
# === SI Voice data start ===
[269.11, 138.41, 179.49, 179.10, 173.85, 195.99, 224.01, 226.95, 173.76, 138.45, 150.45, 144.95, 161.79, 138.88, 164.50, 140.70, 140.41, 114.84, 105.93, 146.18, 143.70, 133.96, 100.89, 49.91, 46.08, 70.17, 59.26, 50.56, 11.79, 7.07, 3.96, 16.15, ],
[108.66, 217.67, 240.60, 242.96, 221.42, 248.11, 126.18, 35.71, 35.02, 25.72, 34.15, 43.58, 31.48, 33.50, 46.63, 19.49, 33.47, 49.63, 31.43, 26.28, 44.18, 36.03, 35.19, 35.78, 31.86, 20.59, 13.11, 10.86, 7.03, 4.64, 6.53, 15.53, ],
[107.44, 114.28, 121.54, 124.74, 136.29, 137.33, 146.91, 136.71, 149.88, 148.63, 144.70, 137.02, 114.88, 110.01, 113.06, 113.60, 120.75, 133.82, 114.04, 87.26, 59.13, 42.81, 46.59, 46.78, 78.30, 68.58, 74.80, 77.93, 67.86, 51.60, 59.95, 61.85, ],
[101.79, 140.44, 175.48, 201.24, 217.48, 238.90, 254.83, 268.81, 274.76, 273.97, 268.80, 260.20, 239.36, 192.66, 160.24, 117.35, 90.14, 71.57, 61.93, 85.55, 86.53, 136.81, 184.92, 161.01, 572.84, 465.50, 485.03, 410.12, 277.66, 235.66, 263.88, 314.80, ],
[115.76, 117.89, 110.66, 102.48, 98.71, 91.12, 80.28, 80.61, 75.09, 117.07, 176.04, 241.91, 105.43, 449.81, 532.79, 491.36, 419.96, 400.83, 311.66, 380.33, 186.82, 144.76, 218.44, 150.22, 46.40, 123.86, 17.56, 121.35, 192.37, 163.69, 166.54, 172.74, ],
[451.71, 419.09, 431.77, 377.91, 432.35, 367.82, 358.43, 337.41, 335.52, 337.73, 322.15, 258.96, 209.27, 134.76, 89.09, 23.27, 72.08, 180.32, 192.55, 159.31, 139.66, 137.89, 142.08, 144.59, 144.66, 135.25, 126.02, 110.47, 97.71, 76.93, 55.77, 12.12, ],
[118.80, 346.84, 354.63, 442.96, 253.71, 331.17, 288.20, 368.47, 372.92, 409.70, 397.51, 411.28, 423.55, 400.97, 377.05, 309.08, 260.41, 207.59, 247.04, 272.12, 261.13, 221.85, 173.38, 102.67, 56.84, 10.95, 6.78, 19.17, 24.97, 33.29, 40.42, 52.42, ],
[243.95, 266.46, 302.31, 310.98, 270.67, 234.55, 179.99, 143.49, 104.53, 79.99, 55.78, 41.09, 32.15, 28.03, 25.08, 25.90, 26.28, 15.06, 8.84, 2.67, 5.70, 6.34, 11.49, 5.04, 2.08, 2.51, 7.09, 2.68, 9.39, 7.05, 4.87, 3.59, ],
[107.03, 121.90, 134.70, 135.95, 130.21, 120.74, 99.97, 77.88, 56.90, 30.35, 13.77, 4.74, 18.55, 34.05, 34.62, 47.28, 49.51, 49.69, 53.45, 50.64, 46.64, 35.00, 33.18, 50.84, 42.14, 71.13, 77.95, 86.04, 88.87, 113.57, 114.56, 335.81, ],
[160.93, 151.87, 136.67, 128.34, 120.89, 108.46, 101.63, 90.75, 79.73, 71.44, 52.95, 48.72, 58.43, 79.60, 92.20, 98.04, 128.07, 118.36, 155.86, 304.37, 391.90, 326.96, 285.48, 283.99, 281.13, 320.29, 297.21, 258.77, 293.46, 232.72, 197.78, 187.36, ],
[116.61, 208.91, 115.85, 84.86, 283.95, 326.23, 308.91, 282.89, 304.48, 323.75, 320.04, 278.39, 191.79, 168.88, 112.39, 93.28, 141.69, 170.73, 200.27, 216.95, 211.02, 215.75, 217.27, 207.74, 203.49, 197.59, 184.54, 175.02, 163.83, 147.56, 131.05, 119.64, ],
[271.13, 266.25, 241.40, 225.52, 212.42, 210.03, 207.82, 188.12, 143.16, 123.59, 83.53, 71.63, 40.82, 28.90, 12.00, 4.51, 4.54, 19.73, 33.23, 43.50, 61.37, 56.76, 49.27, 42.58, 24.10, 13.73, 13.19, 22.22, 40.06, 58.49, 68.09, 73.43, ],
[103.62, 249.68, 264.93, 260.60, 271.03, 241.48, 188.04, 166.23, 182.54, 196.37, 230.55, 200.92, 186.01, 157.35, 105.98, 82.32, 42.59, 22.03, 44.95, 67.19, 92.31, 91.83, 84.49, 73.87, 61.10, 50.51, 35.26, 25.75, 9.90, 2.24, 6.52, 5.06, ],
[105.17, 100.57, 92.31, 59.75, 25.47, 33.20, 36.21, 29.26, 22.84, 16.18, 11.22, 9.16, 2.60, 7.04, 10.64, 11.87, 19.57, 17.32, 14.11, 22.11, 17.92, 21.23, 15.01, 13.82, 17.57, 9.43, 12.86, 12.97, 1.96, 1.72, 9.70, 17.32, ],
[131.63, 127.79, 123.71, 118.69, 121.60, 110.97, 109.74, 98.66, 96.55, 95.54, 92.73, 88.86, 77.70, 62.81, 48.72, 23.62, 13.27, 10.06, 9.10, 21.43, 26.89, 33.61, 40.69, 43.20, 40.52, 32.22, 22.97, 11.59, 3.31, 20.08, 29.74, 47.31, ],
[101.22, 130.29, 164.42, 184.81, 209.45, 218.02, 215.98, 213.98, 201.24, 190.01, 168.53, 159.00, 132.63, 115.06, 92.92, 74.81, 51.78, 37.60, 13.58, 2.65, 21.54, 36.73, 51.57, 59.00, 65.93, 61.66, 58.52, 54.88, 49.91, 49.06, 39.17, 29.57, ],
[107.29, 102.40, 124.38, 112.63, 275.14, 259.94, 312.88, 249.04, 243.90, 230.33, 213.45, 178.54, 129.46, 132.12, 127.69, 105.03, 99.32, 121.99, 162.63, 179.41, 196.65, 207.46, 222.64, 237.26, 238.04, 216.71, 187.80, 162.70, 128.61, 103.33, 72.31, 61.18, ],
[245.45, 194.65, 161.84, 209.14, 209.83, 170.34, 158.94, 182.03, 163.97, 141.15, 129.15, 120.76, 110.91, 102.99, 104.55, 107.39, 99.81, 88.55, 59.93, 49.07, 61.32, 67.85, 54.99, 35.69, 8.31, 5.71, 26.58, 30.85, 36.52, 46.46, 52.03, 60.93, ],
[172.11, 199.40, 211.22, 191.16, 181.99, 175.32, 167.24, 162.61, 110.36, 23.13, 22.76, 36.66, 39.37, 16.89, 10.21, 3.72, 9.92, 44.62, 64.91, 94.27, 112.17, 136.18, 158.37, 170.98, 167.94, 168.10, 156.05, 135.10, 119.37, 99.91, 91.79, 65.87, ],
[165.55, 100.25, 61.80, 14.43, 5.71, 15.50, 18.71, 19.98, 11.76, 13.50, 26.30, 53.37, 67.26, 69.51, 53.38, 28.06, 4.90, 33.19, 53.39, 77.09, 87.51, 94.19, 95.67, 95.11, 92.27, 89.64, 83.13, 72.13, 66.07, 49.69, 36.55, 16.26, ],
[128.30, 213.02, 212.67, 191.07, 187.18, 216.36, 136.79, 133.73, 153.59, 136.01, 108.51, 90.23, 119.00, 177.89, 242.22, 274.84, 307.15, 311.55, 313.08, 308.47, 301.28, 281.76, 249.11, 223.63, 176.13, 147.90, 102.91, 76.02, 56.35, 55.51, 40.81, 29.14, ],
[158.57, 188.30, 184.87, 123.90, 134.86, 156.66, 122.90, 131.44, 131.93, 150.34, 151.60, 145.20, 150.12, 137.28, 86.46, 80.66, 82.94, 77.53, 63.06, 51.52, 31.07, 20.17, 1.68, 10.82, 19.06, 24.99, 19.59, 24.51, 26.01, 22.60, 22.48, 23.50, ],
[217.21, 119.29, 67.29, 15.67, 7.66, 32.53, 45.33, 67.06, 77.27, 91.71, 91.89, 98.05, 102.26, 103.62, 119.06, 134.13, 147.63, 174.12, 178.04, 182.42, 175.15, 165.57, 159.69, 152.29, 154.00, 150.47, 143.71, 133.96, 127.52, 105.06, 99.37, 81.90, ],
[228.68, 204.36, 186.29, 161.62, 150.46, 138.17, 133.89, 125.98, 110.98, 95.13, 78.68, 53.93, 40.64, 17.28, 4.32, 12.55, 17.32, 28.50, 29.73, 24.29, 23.75, 26.05, 24.93, 30.98, 34.76, 40.50, 49.05, 54.12, 62.91, 73.88, 78.51, 83.65, ],
[166.68, 167.18, 177.33, 185.83, 200.83, 211.56, 213.86, 223.61, 220.28, 222.86, 212.79, 196.75, 167.69, 143.23, 121.03, 115.53, 117.32, 122.84, 115.26, 104.16, 88.91, 83.00, 74.12, 72.31, 64.29, 60.33, 64.53, 65.59, 69.57, 72.48, 72.13, 73.24, ],
[101.82, 105.62, 105.27, 100.57, 84.86, 70.87, 45.33, 25.02, 19.65, 43.38, 85.14, 109.53, 135.70, 155.69, 172.88, 183.01, 192.25, 197.23, 202.66, 200.08, 188.44, 188.70, 173.76, 167.06, 153.60, 125.18, 113.04, 79.34, 282.18, 282.50, 268.91, 329.50, ],
[101.41, 89.84, 167.62, 255.78, 234.64, 217.01, 218.07, 175.26, 162.13, 128.09, 102.84, 112.23, 161.61, 123.56, 81.55, 46.26, 82.02, 117.71, 152.88, 166.76, 173.20, 171.96, 157.48, 148.56, 147.61, 134.10, 122.99, 108.19, 92.18, 86.78, 75.55, 78.14, ],
[111.50, 109.25, 150.03, 236.48, 239.89, 232.38, 241.36, 244.72, 262.67, 263.16, 241.01, 208.79, 154.52, 111.46, 67.08, 45.90, 9.70, 39.74, 76.13, 94.15, 112.42, 128.38, 137.33, 137.74, 137.57, 140.57, 148.91, 161.35, 190.07, 199.27, 214.98, 212.24, ],
[133.43, 73.91, 39.35, 8.37, 28.33, 44.69, 47.52, 45.83, 45.21, 43.86, 42.20, 39.12, 33.68, 35.55, 35.37, 25.66, 19.16, 3.42, 4.95, 7.38, 14.29, 39.84, 46.06, 48.88, 9.95, 43.03, 45.03, 44.03, 49.56, 52.42, 60.79, 58.13, ],
[107.25, 117.64, 133.94, 131.61, 115.34, 81.07, 34.52, 5.94, 22.40, 30.59, 33.20, 29.98, 20.13, 4.96, 11.41, 7.94, 40.19, 66.29, 81.87, 113.07, 129.17, 142.39, 135.24, 132.67, 122.20, 106.05, 99.54, 88.94, 96.07, 101.09, 116.93, 141.74, ],
[188.92, 200.76, 208.21, 217.24, 220.10, 218.17, 211.47, 196.44, 178.50, 160.34, 135.61, 109.25, 65.65, 45.66, 42.69, 84.34, 126.44, 126.34, 165.59, 172.60, 88.26, 58.65, 255.10, 254.78, 338.92, 321.23, 410.97, 390.13, 306.13, 279.67, 229.09, 231.29, ],
[150.90, 236.25, 226.20, 208.57, 238.18, 145.93, 177.82, 203.47, 201.37, 283.84, 282.64, 253.58, 211.25, 203.68, 212.39, 238.34, 279.81, 272.88, 224.15, 95.17, 14.34, 71.50, 107.67, 142.65, 153.76, 152.35, 143.22, 107.68, 80.90, 55.69, 45.15, 37.81, ],
[239.27, 178.84, 184.05, 199.68, 160.29, 169.71, 154.39, 156.71, 105.01, 105.19, 104.54, 83.25, 56.86, 40.95, 30.34, 18.35, 17.47, 31.76, 56.07, 68.44, 68.83, 69.89, 52.44, 39.61, 31.20, 29.47, 17.80, 5.77, 35.45, 58.55, 79.86, 83.77, ],
[227.12, 179.34, 178.58, 203.92, 220.25, 233.83, 228.88, 176.07, 118.81, 15.38, 49.20, 120.53, 158.16, 207.86, 223.93, 247.99, 254.79, 253.79, 257.57, 242.84, 236.85, 220.92, 202.84, 182.77, 161.11, 139.29, 127.65, 110.31, 99.43, 94.44, 88.71, 85.73, ],
[215.79, 217.52, 270.58, 386.37, 415.95, 409.28, 422.67, 280.00, 247.83, 192.87, 116.24, 145.44, 139.20, 156.77, 113.64, 82.06, 63.57, 46.00, 38.95, 31.97, 37.75, 40.28, 47.66, 49.31, 51.85, 57.70, 42.51, 30.63, 28.87, 25.81, 29.87, 25.58, ],
[243.25, 239.20, 162.98, 129.65, 96.61, 69.62, 52.52, 40.38, 31.86, 24.04, 16.58, 2.95, 7.67, 16.57, 41.59, 60.76, 84.22, 102.26, 129.50, 140.25, 157.01, 167.16, 175.86, 177.95, 192.50, 192.46, 197.17, 198.00, 199.31, 195.98, 199.19, 198.29, ],
[101.50, 109.92, 123.42, 137.76, 155.38, 176.43, 191.99, 215.08, 220.67, 236.21, 247.78, 249.81, 252.36, 253.72, 250.43, 249.44, 248.04, 242.79, 242.62, 233.41, 223.85, 210.52, 196.67, 175.82, 163.15, 135.06, 122.42, 102.14, 77.13, 51.78, 27.92, 4.65, ],
[102.48, 106.36, 105.13, 104.26, 155.57, 97.84, 97.57, 192.18, 292.87, 332.05, 368.28, 387.46, 400.59, 380.93, 306.13, 246.59, 166.87, 128.08, 76.81, 47.78, 16.71, 3.54, 19.85, 22.74, 22.27, 18.73, 8.52, 4.84, 23.37, 41.91, 75.81, 72.50, ],
[112.38, 83.77, 140.21, 314.67, 500.94, 552.90, 487.32, 451.47, 365.02, 272.58, 218.48, 163.10, 133.28, 120.06, 133.19, 124.17, 132.14, 100.31, 90.95, 88.23, 85.04, 78.85, 86.58, 90.60, 103.62, 110.94, 126.87, 135.69, 144.92, 152.94, 160.43, 165.36, ],
[352.53, 375.14, 320.37, 260.97, 312.92, 317.26, 274.97, 229.68, 222.71, 227.71, 148.53, 106.68, 21.31, 18.91, 48.90, 71.21, 94.33, 110.15, 120.59, 131.13, 145.97, 150.09, 157.97, 159.98, 162.50, 166.69, 164.45, 162.88, 161.04, 154.79, 152.93, 146.85, ],
[108.47, 131.59, 138.26, 191.99, 181.37, 184.85, 183.13, 200.96, 200.43, 198.30, 189.84, 188.50, 187.71, 142.73, 105.03, 61.82, 46.30, 37.32, 48.25, 61.44, 57.52, 57.81, 54.76, 54.00, 56.45, 66.12, 66.75, 68.38, 69.32, 64.01, 61.88, 55.38, ],
[186.42, 215.01, 219.72, 216.46, 210.87, 179.69, 160.73, 136.54, 114.45, 99.95, 85.31, 75.77, 72.91, 69.79, 74.16, 73.02, 68.15, 74.10, 70.32, 68.42, 70.35, 75.56, 82.37, 85.23, 96.80, 109.98, 114.48, 130.06, 134.42, 145.48, 153.89, 159.00, ],
[103.31, 99.94, 332.71, 666.72, 505.45, 636.55, 693.69, 705.46, 697.43, 638.52, 520.53, 386.28, 312.97, 280.87, 166.85, 113.44, 55.97, 66.03, 121.99, 144.83, 154.62, 128.48, 92.39, 86.37, 83.80, 88.35, 105.52, 111.57, 125.73, 129.21, 137.16, 132.83, ],
[150.61, 150.37, 140.22, 132.09, 121.05, 116.96, 102.89, 91.70, 88.90, 88.08, 83.00, 80.58, 103.63, 170.80, 181.51, 207.64, 152.11, 170.28, 114.86, 109.41, 120.60, 103.37, 90.86, 90.78, 82.84, 45.62, 44.11, 40.18, 48.09, 48.05, 45.08, 46.81, ],
[101.44, 105.97, 89.73, 65.18, 36.83, 16.59, 15.36, 15.47, 12.90, 14.50, 19.77, 20.91, 19.61, 27.19, 31.30, 30.45, 36.57, 37.39, 40.61, 42.12, 37.65, 38.32, 34.43, 34.32, 27.36, 20.21, 15.72, 5.17, 6.82, 2.93, 5.36, 5.48, ],
[101.18, 101.58, 110.70, 112.83, 107.11, 111.03, 105.09, 105.14, 98.19, 92.71, 91.42, 87.29, 80.07, 73.22, 66.56, 67.16, 61.10, 58.19, 55.90, 55.44, 49.96, 49.39, 45.49, 41.29, 38.81, 34.36, 38.30, 33.85, 31.01, 31.95, 22.79, 23.09, ],
[122.90, 177.02, 192.41, 193.55, 150.42, 145.75, 148.64, 131.29, 115.47, 99.30, 88.13, 88.00, 66.53, 50.40, 29.47, 26.74, 4.88, 7.48, 4.97, 3.61, 3.48, 3.02, 3.26, 3.12, 4.61, 3.13, 4.38, 6.69, 2.14, 1.49, 5.08, 2.43, ],
[115.27, 167.58, 182.37, 192.88, 171.41, 204.40, 183.22, 207.68, 237.40, 252.10, 242.89, 218.15, 188.16, 155.92, 113.20, 98.25, 55.81, 32.52, 9.98, 6.45, 18.89, 14.13, 21.84, 25.17, 23.53, 34.36, 46.10, 49.39, 60.74, 65.59, 68.70, 73.33, ],
[103.92, 158.89, 162.84, 185.69, 154.58, 172.00, 146.46, 102.08, 157.46, 169.74, 206.56, 232.22, 233.86, 239.01, 200.08, 167.88, 164.91, 167.89, 168.82, 170.07, 157.38, 140.89, 108.88, 91.29, 58.64, 35.92, 7.92, 12.03, 37.06, 47.38, 67.83, 76.22, ],
[100.86, 97.33, 95.98, 93.10, 91.00, 93.40, 88.47, 83.76, 87.46, 81.47, 83.15, 86.10, 87.77, 91.03, 87.49, 90.69, 84.59, 80.96, 69.55, 55.76, 45.07, 34.63, 13.90, 7.42, 9.76, 15.55, 26.59, 36.60, 43.38, 47.52, 57.22, 60.85, ],
# === SI Voice data end ===
# === NO Voice data start ===
[283.43, 280.10, 275.17, 274.44, 270.06, 268.93, 263.25, 259.63, 246.78, 243.34, 232.96, 226.73, 214.98, 208.69, 184.48, 172.21, 159.38, 149.75, 138.81, 135.91, 112.17, 104.95, 89.93, 87.08, 76.01, 73.15, 58.93, 58.61, 53.85, 46.18, 53.00, 39.47, ],
[102.53, 119.84, 164.40, 216.71, 175.22, 176.46, 203.15, 213.78, 234.16, 240.75, 245.50, 217.80, 241.23, 279.73, 329.74, 284.49, 321.11, 286.67, 269.42, 224.71, 204.30, 250.73, 221.78, 155.10, 216.44, 235.64, 74.81, 87.84, 84.55, 123.50, 48.71, 29.00, ],
[110.21, 113.51, 142.52, 153.87, 189.35, 205.89, 210.83, 205.22, 206.60, 206.14, 211.65, 223.24, 239.78, 247.29, 244.40, 237.98, 229.46, 222.88, 200.98, 192.75, 169.99, 157.08, 139.91, 124.28, 114.14, 98.88, 86.49, 77.63, 53.60, 49.04, 74.57, 97.58, ],
[105.15, 128.20, 175.12, 208.19, 258.03, 297.97, 348.42, 373.13, 444.12, 416.45, 492.12, 507.83, 485.85, 526.43, 561.19, 517.93, 535.98, 516.33, 512.81, 480.33, 468.75, 446.83, 411.07, 412.66, 369.94, 340.13, 341.29, 281.61, 279.19, 256.16, 232.81, 198.95, ],
[205.87, 248.35, 255.96, 250.05, 236.46, 246.05, 232.13, 215.89, 217.91, 231.45, 200.76, 189.36, 185.37, 146.87, 111.82, 115.78, 87.93, 90.51, 69.06, 76.26, 81.66, 93.81, 109.20, 112.80, 121.52, 124.25, 131.26, 143.91, 143.72, 143.25, 149.81, 142.67, ],
[151.66, 104.32, 116.93, 135.34, 138.78, 147.06, 133.77, 165.26, 145.09, 146.20, 133.62, 141.86, 142.88, 146.64, 148.52, 136.66, 132.54, 113.16, 108.83, 99.83, 86.62, 100.28, 99.94, 113.71, 125.67, 134.90, 142.29, 149.11, 158.08, 164.83, 168.51, 182.07, ],
[103.11, 82.77, 84.25, 74.92, 53.89, 41.78, 44.39, 49.60, 60.06, 67.38, 71.39, 71.96, 75.54, 76.39, 79.18, 81.58, 81.65, 80.78, 78.91, 79.93, 87.01, 75.01, 74.56, 76.85, 72.52, 75.15, 77.71, 77.89, 76.56, 75.50, 73.75, 76.52, ],
[147.03, 148.06, 154.31, 160.31, 164.09, 166.16, 165.41, 157.66, 152.38, 143.72, 135.42, 121.21, 99.90, 87.51, 58.89, 45.38, 14.91, 7.52, 32.33, 58.30, 88.01, 104.01, 132.43, 148.65, 164.46, 171.70, 191.48, 191.82, 197.58, 194.93, 188.66, 183.00, ],
[117.83, 57.49, 29.77, 14.18, 40.49, 69.39, 84.58, 109.49, 117.68, 128.46, 131.06, 129.15, 128.20, 125.34, 120.06, 126.48, 117.59, 127.66, 121.61, 112.35, 114.98, 104.14, 109.47, 94.69, 89.51, 78.39, 61.54, 54.84, 41.56, 22.90, 16.85, 2.61, ],
[107.72, 127.66, 144.90, 166.02, 182.32, 191.79, 192.43, 208.26, 211.17, 209.53, 211.93, 209.71, 206.21, 204.92, 195.39, 191.59, 189.01, 178.03, 174.67, 163.43, 156.80, 146.36, 134.16, 122.48, 112.60, 98.96, 92.48, 79.71, 67.15, 52.22, 35.79, 21.37, ],
[115.25, 115.47, 116.53, 126.49, 120.32, 121.13, 119.86, 115.27, 108.19, 105.03, 96.77, 89.52, 78.34, 75.52, 77.59, 67.42, 63.05, 60.36, 58.55, 54.44, 54.92, 60.57, 53.14, 56.77, 58.72, 58.24, 66.29, 60.55, 71.73, 67.48, 62.57, 63.94, ],
[105.40, 96.02, 101.76, 131.21, 103.96, 54.94, 33.16, 26.17, 25.38, 8.22, 18.45, 61.38, 114.43, 122.19, 72.68, 34.23, 12.22, 16.08, 4.00, 6.40, 35.30, 66.69, 79.73, 78.24, 85.95, 100.09, 108.57, 113.07, 112.66, 110.78, 110.45, 106.21, ],
[103.90, 118.26, 135.98, 158.54, 159.29, 168.86, 174.26, 161.34, 168.00, 167.37, 155.68, 152.39, 169.22, 182.54, 182.67, 200.83, 213.81, 206.43, 212.01, 246.45, 243.14, 228.52, 230.23, 222.01, 210.69, 190.98, 210.45, 172.67, 175.31, 184.68, 147.93, 124.80, ],
[168.54, 179.68, 213.85, 215.37, 236.10, 247.39, 247.06, 284.60, 278.99, 295.12, 297.55, 273.97, 300.21, 304.93, 274.65, 283.78, 285.99, 272.53, 238.66, 227.57, 203.72, 219.24, 167.46, 153.84, 136.91, 112.13, 115.81, 132.83, 150.45, 124.99, 114.46, 109.31, ],
[441.38, 450.39, 415.42, 397.22, 355.40, 323.31, 289.77, 313.79, 308.41, 296.02, 310.08, 268.86, 254.52, 238.29, 235.37, 229.07, 226.05, 214.50, 212.16, 218.33, 209.60, 216.09, 204.69, 193.30, 205.80, 187.64, 168.26, 169.41, 147.70, 131.94, 125.47, 115.77, ],
[213.06, 197.76, 179.79, 179.00, 190.42, 169.74, 169.26, 166.06, 153.53, 142.64, 147.70, 154.68, 180.79, 205.98, 221.29, 232.38, 264.16, 258.83, 304.18, 310.94, 278.73, 279.21, 301.26, 280.23, 273.19, 266.83, 275.43, 266.90, 269.24, 265.13, 259.22, 244.18, ],
[168.51, 162.36, 167.36, 160.11, 154.18, 145.38, 138.68, 135.63, 131.50, 118.45, 133.10, 116.39, 141.00, 149.10, 122.36, 125.21, 127.77, 110.84, 106.99, 97.04, 85.06, 82.52, 75.66, 61.50, 45.77, 43.58, 23.26, 17.38, 6.21, 6.52, 24.65, 31.36, ],
[114.28, 103.24, 93.05, 96.74, 97.25, 128.56, 107.69, 106.75, 121.15, 117.16, 125.98, 132.81, 137.96, 137.94, 132.90, 133.22, 119.27, 104.95, 83.01, 80.32, 83.85, 92.24, 119.66, 127.98, 133.81, 136.38, 127.83, 119.85, 114.22, 102.13, 92.16, 86.57, ],
[103.19, 121.93, 144.19, 155.69, 169.29, 177.44, 200.82, 151.40, 27.38, 34.87, 42.29, 22.32, 15.57, 42.92, 62.16, 77.10, 73.98, 60.60, 37.68, 20.11, 7.03, 23.79, 45.73, 61.57, 121.40, 101.42, 153.27, 155.53, 171.66, 193.24, 171.34, 180.65, ],
[117.10, 164.05, 204.15, 217.31, 241.02, 250.13, 190.29, 187.16, 147.14, 142.84, 115.14, 140.30, 129.00, 150.83, 204.46, 201.38, 231.00, 255.09, 254.49, 231.35, 225.39, 221.46, 192.13, 192.11, 171.12, 177.54, 178.74, 185.75, 185.55, 168.36, 168.23, 131.95, ],
[145.24, 151.76, 142.82, 164.74, 179.54, 194.52, 184.14, 187.39, 179.50, 159.94, 166.07, 173.84, 150.29, 151.89, 144.83, 139.79, 128.75, 123.99, 132.59, 117.11, 115.28, 123.02, 113.90, 124.76, 107.87, 106.53, 122.54, 91.87, 72.44, 61.61, 47.47, 36.97, ],
[266.85, 273.15, 269.21, 316.34, 283.74, 273.86, 308.56, 254.60, 243.56, 207.88, 171.56, 136.19, 100.38, 90.39, 73.60, 66.08, 48.20, 28.57, 28.24, 41.35, 38.78, 34.29, 33.67, 23.13, 22.01, 12.16, 10.72, 11.51, 15.22, 14.22, 20.55, 27.45, ],
[140.22, 148.30, 151.09, 146.50, 137.65, 116.37, 122.21, 93.24, 85.51, 68.58, 62.74, 62.69, 46.83, 51.86, 48.00, 45.72, 42.60, 32.70, 36.21, 30.18, 24.64, 14.33, 69.36, 53.75, 54.03, 111.84, 133.76, 242.71, 275.27, 313.95, 247.28, 306.80, ],
[199.05, 178.89, 156.99, 138.76, 116.44, 100.45, 65.45, 48.16, 14.06, 8.34, 41.71, 71.74, 103.12, 125.14, 144.84, 157.60, 164.51, 159.87, 157.84, 152.65, 138.00, 135.78, 124.95, 113.08, 105.33, 89.72, 79.39, 69.76, 56.94, 57.17, 48.62, 49.62, ],
[102.00, 118.13, 142.19, 148.59, 168.66, 174.03, 225.49, 178.71, 218.91, 298.45, 348.82, 500.50, 487.43, 490.64, 518.17, 428.17, 518.85, 426.80, 256.41, 164.00, 45.43, 2.92, 4.49, 6.91, 103.38, 143.82, 210.45, 242.64, 222.65, 220.17, 272.22, 280.19, ],
[111.34, 121.47, 149.20, 152.91, 144.42, 197.01, 193.31, 185.49, 190.50, 181.60, 185.27, 195.32, 214.67, 216.48, 220.70, 216.84, 229.94, 214.95, 196.65, 195.61, 173.83, 176.32, 152.15, 145.07, 138.62, 135.80, 122.98, 118.06, 121.20, 113.79, 106.00, 111.93, ],
[239.52, 240.80, 202.55, 198.72, 188.45, 179.55, 170.43, 167.83, 166.22, 150.59, 146.87, 152.75, 133.97, 128.31, 112.91, 116.48, 96.88, 84.62, 79.74, 82.66, 91.26, 81.88, 77.74, 75.55, 45.40, 21.47, 11.69, 17.21, 8.56, 5.62, 4.77, 16.87, ],
[181.60, 188.30, 185.10, 159.70, 151.55, 143.97, 125.97, 114.76, 104.99, 101.72, 86.78, 81.84, 88.35, 61.85, 39.10, 16.44, 8.58, 15.87, 26.46, 41.45, 58.28, 84.57, 96.12, 118.79, 131.28, 148.31, 157.67, 162.18, 169.43, 165.22, 167.51, 163.38, ],
[100.25, 94.76, 97.28, 96.33, 93.66, 100.50, 94.37, 56.78, 54.33, 49.09, 46.70, 44.41, 36.06, 32.48, 27.28, 29.68, 36.30, 46.54, 57.81, 66.58, 66.99, 82.00, 82.08, 98.18, 103.40, 104.92, 110.44, 113.16, 108.58, 97.95, 105.11, 88.94, ],
[105.78, 127.85, 167.91, 164.16, 170.00, 165.86, 155.36, 147.37, 162.56, 156.28, 163.90, 152.64, 161.54, 162.83, 180.44, 145.90, 136.63, 132.59, 139.57, 119.26, 112.65, 111.93, 114.07, 97.60, 97.88, 94.26, 91.06, 98.51, 97.59, 92.17, 85.18, 93.35, ],
[245.51, 277.97, 319.11, 356.48, 336.57, 324.77, 332.60, 325.27, 329.56, 311.38, 307.43, 327.29, 353.14, 347.17, 349.96, 341.58, 357.09, 368.33, 334.36, 338.91, 326.55, 331.99, 287.62, 264.85, 251.37, 236.18, 218.22, 208.34, 185.54, 177.44, 154.23, 148.17, ],
[170.48, 152.40, 154.72, 158.36, 143.59, 133.99, 130.20, 129.76, 131.32, 119.75, 131.35, 74.32, 49.40, 40.32, 40.24, 42.74, 39.38, 48.79, 41.80, 45.52, 65.85, 31.18, 63.47, 51.52, 154.95, 318.98, 488.73, 693.70, 785.27, 810.45, 796.12, 707.76, ],
[145.45, 143.75, 111.08, 101.86, 93.23, 95.76, 71.23, 75.59, 87.43, 99.48, 106.50, 107.38, 111.87, 109.61, 103.74, 104.35, 90.36, 90.20, 79.92, 73.00, 65.65, 51.95, 35.08, 28.02, 17.91, 15.74, 11.28, 15.65, 16.94, 19.44, 33.38, 34.25, ],
[107.80, 31.31, 265.11, 392.73, 515.33, 554.08, 545.84, 516.23, 466.66, 387.73, 364.59, 304.66, 303.18, 295.44, 225.58, 214.13, 196.50, 160.14, 128.99, 139.77, 152.19, 146.31, 150.97, 170.34, 204.11, 203.67, 216.52, 229.21, 214.23, 215.98, 240.83, 218.59, ],
[106.58, 91.50, 145.89, 177.56, 174.95, 168.34, 178.70, 167.41, 149.14, 155.55, 159.36, 147.29, 146.82, 147.58, 152.64, 148.05, 155.03, 157.42, 165.97, 158.12, 155.38, 157.16, 150.69, 152.60, 151.58, 150.24, 159.12, 157.12, 152.58, 140.43, 143.95, 119.58, ],
[166.98, 171.65, 145.85, 143.24, 152.00, 134.37, 132.53, 139.01, 128.00, 127.32, 114.64, 113.08, 111.82, 123.21, 111.08, 111.40, 118.96, 133.20, 170.84, 192.19, 203.89, 209.09, 221.90, 228.99, 224.37, 222.72, 226.90, 219.16, 198.77, 189.19, 170.45, 159.26, ],
[139.02, 128.11, 120.35, 122.33, 125.67, 119.62, 113.25, 124.88, 112.46, 112.90, 99.45, 93.06, 94.90, 92.46, 92.73, 89.87, 79.15, 28.51, 24.39, 20.25, 19.81, 22.00, 26.76, 23.17, 26.44, 19.25, 20.37, 30.18, 37.08, 46.82, 60.01, 86.30, ],
[266.37, 221.98, 197.54, 188.10, 170.13, 166.91, 159.21, 127.32, 119.67, 113.25, 112.50, 104.94, 81.77, 68.28, 60.36, 54.33, 44.44, 29.35, 22.93, 19.01, 20.62, 13.99, 16.02, 12.73, 7.75, 6.65, 2.41, 2.14, 2.98, 10.50, 12.49, 17.57, ],
[143.96, 144.40, 132.98, 134.98, 127.80, 129.89, 124.74, 137.14, 110.81, 113.69, 106.30, 104.98, 98.10, 57.59, 33.64, 32.56, 37.97, 38.05, 48.51, 55.81, 62.30, 57.88, 63.74, 69.85, 70.44, 70.84, 74.60, 83.30, 93.23, 109.03, 148.31, 167.06, ],
[136.28, 138.03, 136.66, 135.69, 132.47, 132.19, 133.06, 136.89, 159.02, 161.78, 171.25, 179.74, 183.44, 179.89, 182.51, 190.12, 188.08, 183.92, 176.90, 161.55, 149.83, 148.69, 144.38, 147.63, 147.32, 86.82, 77.06, 125.75, 287.65, 442.70, 436.03, 650.40, ],
[145.99, 122.89, 114.35, 103.90, 105.62, 103.40, 99.24, 112.25, 116.74, 132.79, 140.93, 140.50, 137.26, 126.75, 119.38, 105.70, 93.33, 81.38, 72.73, 56.03, 51.20, 27.65, 10.46, 9.17, 24.45, 29.56, 31.73, 31.66, 32.92, 26.69, 16.65, 18.65, ],
[191.38, 197.38, 211.25, 199.83, 184.74, 172.54, 155.64, 142.70, 112.71, 94.03, 69.91, 43.88, 33.60, 28.16, 34.78, 42.47, 37.14, 43.13, 38.55, 31.54, 25.89, 33.92, 30.35, 38.72, 68.30, 62.37, 101.53, 158.58, 10.99, 105.91, 270.82, 349.60, ],
[232.13, 216.01, 189.77, 169.68, 140.19, 133.83, 109.72, 102.49, 89.79, 86.31, 70.47, 53.43, 40.64, 26.02, 2.95, 4.06, 23.43, 34.15, 36.74, 35.51, 33.49, 27.39, 10.36, 7.16, 12.46, 19.74, 23.47, 31.54, 34.00, 36.85, 26.56, 23.20, ],
[141.88, 140.28, 136.19, 127.79, 114.79, 104.30, 100.09, 95.11, 94.49, 100.70, 74.17, 59.98, 60.78, 56.66, 57.84, 56.55, 49.33, 61.58, 62.91, 40.92, 43.47, 10.26, 6.84, 36.13, 51.35, 66.75, 64.44, 74.02, 71.29, 23.76, 37.48, 179.63, ],
[176.87, 162.52, 161.88, 143.77, 127.41, 112.92, 99.08, 83.17, 75.83, 48.20, 29.38, 29.60, 28.38, 32.09, 25.61, 21.76, 23.62, 10.86, 12.38, 9.37, 3.62, 9.44, 33.04, 55.82, 62.26, 77.21, 84.29, 83.66, 79.87, 63.79, 50.17, 25.08, ],
[137.48, 139.35, 141.75, 145.46, 139.03, 139.07, 131.87, 120.41, 102.86, 99.88, 66.04, 44.53, 20.01, 38.01, 51.02, 56.29, 62.85, 64.34, 63.25, 60.17, 50.88, 35.97, 24.04, 15.83, 2.86, 6.35, 5.52, 17.68, 45.14, 93.77, 134.70, 152.44, ],
[135.12, 140.52, 133.71, 131.72, 119.42, 109.58, 93.25, 83.97, 52.56, 40.50, 20.25, 15.97, 7.43, 7.54, 2.91, 2.66, 3.30, 3.72, 7.01, 5.27, 5.05, 3.67, 3.17, 4.22, 4.53, 3.49, 10.61, 3.68, 11.43, 13.71, 10.92, 17.22, ],
[113.19, 105.22, 93.96, 92.88, 90.33, 67.89, 49.42, 29.03, 30.41, 26.08, 27.03, 30.52, 31.28, 30.09, 27.94, 15.66, 3.22, 16.96, 27.29, 38.20, 36.23, 23.11, 8.46, 14.51, 35.08, 52.82, 60.29, 70.23, 69.23, 110.69, 135.32, 109.50, ],
[105.89, 111.74, 114.24, 110.59, 104.54, 101.47, 92.70, 85.66, 81.28, 75.02, 62.37, 75.84, 90.66, 101.22, 101.58, 101.08, 99.89, 93.44, 86.54, 82.95, 75.49, 67.23, 62.20, 60.65, 54.56, 47.56, 45.99, 39.72, 40.08, 41.15, 42.20, 40.23, ],
[104.59, 98.89, 100.34, 97.70, 98.24, 99.62, 98.49, 103.82, 122.77, 129.13, 135.01, 140.10, 124.18, 89.43, 85.16, 76.97, 70.11, 68.65, 63.54, 64.89, 59.14, 50.70, 35.86, 15.76, 14.97, 39.41, 30.57, 4.80, 67.54, 57.15, 83.17, 101.37, ],
# === NO Voice data end ===
])

target = np.array(
    [label for label in range(NUMBER_OF_LABELS) for _ in range(DATA_SIZE_OF_LABEL)]
    )
