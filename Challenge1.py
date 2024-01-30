import pennylane as qml
import pennylane.numpy as np
dev = qml.device('default.qubit', wires=1)


test_input = [3.79894785, 0.71678115]


@qml.qnode(dev)
def circuit1(angles):
    """
    A Qnode implementing the circuit shown in the top part of the image

    Args:
        angles (np.ndarray(float)): A list [theta_1, theta_2] of angle
        parameters for the RX and RY gates respectively

    Returns:
        (np.tensor): The expectation value of the PauliX observable
    """
    qml.RX(angles[0], wires=0)
    qml.RY(angles[1], wires=0)
    return qml.expval(qml.PauliX(wires=0))


@qml.qnode(dev)
def circuit2(angles):
    """
    A Qnode implementing the circuit shown in the bottom part of the image

    Args:
        angles (np.ndarray(float)): A list [theta_1, theta_2] of angle
        parameters for the RX and RY gates respectively

    Returns: 
        (np.tensor): The expectation value of the PauliX observable
    """
    qml.RY(angles[1], wires=0)
    qml.RX(angles[0], wires=0)
    return qml.expval(qml.PauliX(wires=0))


def compare_circuits(angles):
    """
    Given two angles, compare two circuit outputs that have their order of
    operations flipped: RX then RY VERSUS RY then RX.

    Args:
        angles (np.ndarray(float)): An array of two angles [theta_1, theta_2]

    Returns:
        (float): The absolute value of the difference between the expectation
        values of the circuits.
    """
    return abs(circuit1(angles) - circuit2(angles))


print(compare_circuits(test_input))