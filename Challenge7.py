import json
import pennylane as qml
import pennylane.numpy as np


WIRES = 2
LAYERS = 5
NUM_PARAMETERS = LAYERS * WIRES * 3

initial_params = np.random.random(NUM_PARAMETERS)


def variational_circuit(params, hamiltonian):
    """
    This is a template variational quantum circuit containing a fixed layout of gates with variable
    parameters. To be used as a QNode, it must either be wrapped with the @qml.qnode decorator or
    converted using the qml.QNode function.

    The output of this circuit is the expectation value of a Hamiltonian, somehow encoded in
    the hamiltonian argument

    Args:
        - params (np.ndarray): An array of optimizable parameters of shape (30,)
        - hamiltonian (np.ndarray): An array of real parameters encoding the Hamiltonian
        whose expectation value is returned.

    Returns:
        (float): The expectation value of the Hamiltonian
    """
    parameters = params.reshape((LAYERS, WIRES, 3))
    qml.templates.StronglyEntanglingLayers(parameters, wires=range(WIRES))
    return qml.expval(qml.Hermitian(hamiltonian, wires=[0, 1]))


def optimize_circuit(params, hamiltonian):
    """Minimize the variational circuit and return its minimum value.
    You should create a device and convert the variational_circuit function
    into an executable QNode.
    Next, you should minimize the variational circuit using gradient-based
    optimization to update the input params.
    Return the optimized value of the QNode as a single floating-point number.

    Args:
        - params (np.ndarray): Input parameters to be optimized, of dimension 30
        - hamiltonian (np.ndarray): An array of real parameters encoding the Hamiltonian
        whose expectation value you should minimize.
    Returns:
        float: the value of the optimized QNode
    """

    dev = qml.device(name='default.qubit', wires=WIRES)
    opt = qml.GradientDescentOptimizer()

    @qml.qnode(dev)
    def wrapper(p):
        return variational_circuit(params=p, hamiltonian=hamiltonian)

    for i in range(5000):
        params, last = opt.step_and_cost(wrapper, params)

    return last
