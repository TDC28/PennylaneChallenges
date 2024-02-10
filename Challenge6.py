import json
import pennylane as qml
import pennylane.numpy as np

dev = qml.device('default.qubit', wires=2)


@qml.qnode(dev)
def trotterize(alpha, beta, time, depth):
    """This quantum circuit implements the Trotterization of a Hamiltonian given by a linear combination
    of tensor products of X and Z Pauli gates.

    Args:
        alpha (float): The coefficient of the XX term in the Hamiltonian, as in the statement of the problem.
        beta (float): The coefficient of the YY term in the Hamiltonian, as in the statement of the problem.
        time (float): Time interval during which the quantum state evolves under the interactions specified by the Hamiltonian.
        depth (int): The Trotterization depth.

    Returns:
        (numpy.array): The probabilities of measuring each computational basis state.
    """

    for i in range(depth):
        qml.IsingXX(2 * alpha * time / depth, (0,1))
        qml.IsingZZ(2 * beta * time / depth, (0, 1))

    return qml.probs()

print(trotterize(0.5,0.8,0.2,1))
