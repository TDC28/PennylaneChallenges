import json
import pennylane as qml
import pennylane.numpy as np


def compute_hessian(num_wires, w):
    """
    This function must create a circuit with num_wire qubits
    as per the challenge statement and return the Hessian of such
    circuit evaluated on w.

    Args:
        - num_wires = The number of wires in the circuit
        - w (np.ndarray): A list of length num_wires + 2 containing float parameters.
        The Hessian is evaluated at this point in parameter space.

    Returns:
        Union(tuple, np.ndarray): A matrix representing the Hessian calculated via
        qml.gradients.parameter_shift_hessian
    """

    # Define your device and QNode
    dev = qml.device('default.qubit', wires=num_wires)

    @qml.qnode(dev)
    def circuit(params):
        for i in range(num_wires):
            qml.RX(params[i], wires=i)

        for i in range(num_wires):
            qml.CNOT(wires=[i, (i + 1) % num_wires])

        qml.RY(params[num_wires], wires=1)

        for i in range(num_wires):
            qml.CNOT(wires=(i, (i + 1) % num_wires))

        qml.RX(params[num_wires+1], wires=num_wires-1)

        observable = qml.PauliZ(wires=0) @ qml.PauliZ(wires=num_wires-1)
        return qml.expval(observable)

    return qml.gradients.param_shift_hessian(circuit)(w)
