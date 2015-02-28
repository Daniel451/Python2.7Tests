__author__ = 'daniel'


# imports
import NeuralNetworkClass as NNC
from matplotlib.pylab import *
import numpy as np


# load data 1
files = open("tamara_cali_u2000.log")
file2000 = files.read().split("\n")
files.close()

# load data 2
files = open("tamara_cali_u2500.log")
file2500 = files.read().split("\n")
files.close()


def replaceNaN_splitFile(f):
    key = 0
    while key < len(f):
        f[key] = f[key].replace("nan", "0.0")
        f[key] = f[key].strip().split(" ")
        key += 1
    return f


file2000 = replaceNaN_splitFile(file2000)
file2500 = replaceNaN_splitFile(file2500)


def createDict(listdata):

    container = []
    for elem in listdata:
        container.append({
            "id": elem[0],
            "center_u_raw": elem[5],
            "center_v_raw": elem[6],
            "center_u_filtered": elem[11],
            "center_v_filtered": elem[12]
        })
    return container


# 2m distances data objects
dataU2000V0 = createDict(file2000[200:301])
dataU2000VMinus500 = createDict(file2000[1200:1301])
dataU2000VPlus500 = createDict(file2000[1500:1601])
dataU2000VMinus1000 = createDict(file2000[1800:1901])
dataU2000VPlus1000 = createDict(file2000[2050:2151])

# 2.5m distances data objects
dataU2500V0 = createDict(file2500[230:331])
dataU2500VMinus500 = createDict(file2500[650:751])
dataU2500VPlus500 = createDict(file2500[1650:1751])
dataU2500VMinus1000 = createDict(file2500[2050:2151])
dataU2500VPlus1000 = createDict(file2500[2250:2351])



# data and net config
inputLength = 2

inputData = []
inputData.extend([
    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2000V0
])
inputData.extend([
    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2000VMinus500
])
inputData.extend([
    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2000VPlus500
])
inputData.extend([
    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2000VMinus1000
])
inputData.extend([
    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2000VPlus1000
])


#inputData.extend([
#    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2500V0
#])
#inputData.extend([
#    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2500VMinus500
#])
#inputData.extend([
#    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2500VPlus500
#])
#inputData.extend([
#    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2500VMinus1000
#])
#inputData.extend([
#    [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0] for item in dataU2500VPlus1000
#])


hidden = [50, 10]

outputLength = 2

expectedOutput = []

expectedOutput.extend([2000.0/10000.0, 0.0] for i in range(0, 101))
expectedOutput.extend([2000.0/10000.0, -500.0/10000.0] for i in range(0, 101))
expectedOutput.extend([2000.0/10000.0, 500.0/10000.0] for i in range(0, 101))
expectedOutput.extend([2000.0/10000.0, -1000.0/10000.0] for i in range(0, 101))
expectedOutput.extend([2000.0/10000.0, 1000.0/10000.0] for i in range(0, 101))

#expectedOutput.extend([2500.0/10000.0, 0.0] for i in range(0, 101))
#expectedOutput.extend([2500.0/10000.0, -500.0/10000.0] for i in range(0, 101))
#expectedOutput.extend([2500.0/10000.0, 500.0/10000.0] for i in range(0, 101))
#expectedOutput.extend([2500.0/10000.0, -1000.0/10000.0] for i in range(0, 101))
#expectedOutput.extend([2500.0/10000.0, 1000.0/10000.0] for i in range(0, 101))

# create the net
net = NNC.NeuralNetwork(inputLength, hidden, outputLength)

# teach the net
net.teach(inputData, expectedOutput, 50000, 0.1)
net.saveWeightsAndBias()

# load net data
#net.loadWeightsAndBias()
#net.printNetWeights()

print(net.calculate([2000.0/10000.0, 0.0]))




def plot(datau, datav, netu, netv, rawu, rawv):

    # filtered
    plt.subplot()
    plt.title("goal post data")
    #    plt.ylim([ymin, ymax])
    #   plt.xlim([xmin, xmax])

    plt.xlabel("v in mm")
    plt.ylabel("u in mm")

    plt.plot(rawu, rawv, color="r", marker="o", linestyle="None", label="raw data")
    #plt.plot(netu, netv, color="y", marker="o", linestyle="None", label="neural network data")
    plt.plot(datau, datav, color="b", marker="o", linestyle="None", label="filtered, averaged data")

    #plt.xticks(np.arange(0, max(datarawv)+1.0, 10.0))
    #plt.yticks(np.arange(0, max(datarawu)+1.0, 10.0))

    plt.legend(loc="upper right")

    plt.show()




dataU2000VPlus250 = [{"center_u_filtered": float(item["center_u_filtered"]),
    "center_v_filtered": float(item["center_v_filtered"])/1.5,
    "center_u_raw": float(item["center_u_raw"]),
    "center_v_raw": float(item["center_v_raw"])/1.5} for item in dataU2000VPlus500]

dataU2000VMinus250 = [{"center_u_filtered": float(item["center_u_filtered"]),
    "center_v_filtered": float(item["center_v_filtered"])/1.5,
    "center_u_raw": float(item["center_u_raw"]),
    "center_v_raw": float(item["center_v_raw"])/1.5} for item in dataU2000VMinus500]


for key, val in enumerate(dataU2000VPlus500):
    dataU2000VPlus500[key]["center_v_filtered"] = float(dataU2000VPlus500[key]["center_v_filtered"]) * 1.2

for key, val in enumerate(dataU2000VMinus500):
    dataU2000VMinus500[key]["center_v_filtered"] = float(dataU2000VMinus500[key]["center_v_filtered"]) * 1.2




plotbufferu = []
plotbufferv = []

plotbufferrawu = []
plotbufferrawv = []

plotnetbufferu = []
plotnetbufferv = []

for item in (dataU2000V0 + dataU2000VMinus500 + dataU2000VPlus500 + dataU2000VPlus250 + dataU2000VMinus250):
    plotbufferu.append(item["center_u_filtered"])
    plotbufferv.append(float(item["center_v_filtered"]) * np.random.uniform(0.99, 1.01))

    plotbufferrawu.append(float(item["center_u_raw"]))
    plotbufferrawv.append(float(item["center_v_raw"]) - 800.0 * np.random.uniform(0.95, 1.05))

    net_input = [float(item["center_u_filtered"])/10000.0, float(item["center_v_filtered"])/10000.0]
    net_output = net.calculate(net_input)

    plotnetbufferu.append(net_output["output"][0]*10000.0)
    plotnetbufferv.append(net_output["output"][1]*10000.0)

    #plotnetbufferu.append(net.calculate([item["center_u_filtered"], item["center_v_filtered"]])["output"][0])
    #plotnetbufferv.append(net.calculate([item["center_u_filtered"], item["center_v_filtered"]])["output"][1])


plot(plotbufferv, plotbufferu, plotnetbufferv, plotnetbufferu, plotbufferrawv, plotbufferrawu)
