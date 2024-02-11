import json
import pennylane as qml
import pennylane.numpy as np


def hamiltonian(num_wires):
    """
    A function for creating the Hamiltonian in question for a general
    number of qubits.

    Args:
        num_wires (int): The number of qubits.

    Returns:
        (qml.Hamiltonian): A PennyLane Hamiltonian.
    """
    coefs, obs = [], []

    for j in range(num_wires):
        for i in range(0, j):
            coefs.append(1/3)
            obs.append(qml.PauliX(wires=i) @ qml.PauliX(wires=j))

    for k in range(num_wires):
        coefs.append(-1)
        obs.append(qml.PauliZ(wires=k))

    return qml.Hamiltonian(coefs, obs)


def expectation_value(num_wires):
    """
    Simulates the circuit in question and returns the expectation value of the
    Hamiltonian in question.

    Args:
        num_wires (int): The number of qubits.

    Returns:
        (float): The expectation value of the Hamiltonian.
    """

    # Put your solution here #

    # Define a device using qml.device
    dev = qml.device('default.qubit', wires=num_wires)

    @qml.qnode(dev)
    def circuit(num_wires):
        """
        A quantum circuit with Hadamard gates on every qubit and that measures
        the expectation value of the Hamiltonian in question.

        Args:
        	num_wires (int): The number of qubits.

		Returns:
			(float): The expectation value of the Hamiltonian.
        """

        # Put Hadamard gates here #
        for i in range(num_wires):
            qml.Hadamard(wires=i)

        # Then return the expectation value of the Hamiltonian using qml.expval
        return qml.expval(hamiltonian(num_wires))

    return circuit(num_wires)
