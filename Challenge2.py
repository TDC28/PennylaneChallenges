import pennylane as qml
import pennylane.numpy as np

dev = qml.device('default.qubit', wires=1)
test_input = 1.23456


@qml.qnode(dev)
def simple_circuit(angle):
    """
    In this function:
        * Rotate the qubit around the y-axis by angle
        * Measure the expectation value of the Pauli X observable

    Args:
        angle (float): how much to rotate a state around the y-axis

    Returns:
        Union[tensor, float]: The expectation value of the Pauli X observable
    """
    qml.RY(angle, wires=0)
    return qml.expval(qml.PauliX(wires=0))


print(simple_circuit(test_input))
