import pennylane as qml
import pennylane.numpy as np

dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def simple_circuit(angle):
    """
    In this function:
        * Rotate the qubit around the x-axis by angle.
        * Measure the probability the qubit is in the zero state.

    Args:
        angle (float): how much to rotate a state around the x-axis.

    Returns:
        np.array(float): the probability of of the state being in the 0
        ground state.
    """
    qml.RX(angle, wires=0)
    return qml.probs(wires=0)


print(simple_circuit(1)[0])