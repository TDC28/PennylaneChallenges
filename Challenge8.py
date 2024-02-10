import json
import numpy as np


def initialize_state():
    """
    Prepare a qubit in state |0>.

    Returns:
        array[float]: the vector representation of state |0>.
    """

    return np.array([1, 0])


def apply_u(U, state):
    """
    Apply the quantum operation U on the state

    Args:
        U (np.array(array(complex))): A (2,2) numpy array with complex entries
        representing a unitary matrix.
        state (np.array(complex)): A (2,) numpy array with complex entries
        representing a quantum state.

    Returns:
        (np.array(complex)): The state vector after applying U to state.
    """

    return np.matmul(U, state)


def measure_state(state, num_meas: int):
    """
    Measure a quantum state num_meas times.

    Args:
        state (np.array(complex)): A (2,) numpy array with complex entries
        representing a quantum state.
        num_meas(float): The number of computational basis measurements on state.

    Returns:
        (np.array(int)) A (num_meas,) numpy array of zeros and ones, representing
        measurement outcomes on the state
    """

    measurements = []

    for i in range(num_meas):
        measurements.append(np.random.choice([0, 1], p=[state[0]**2, state[1]**2]))

    return np.array(measurements)


def quantum_algorithm(U):
    """
    Use the functions above to implement the quantum algorithm described above.

    Try and do so using three lines of code or less!

    Args:
        U (np.array(array(complex))): A (2,2) numpy array with complex entries
        representing a unitary matrix.

    Returns:
        np.array(int): the measurement results after running the algorithm 20 times
    """

    state = apply_u(U, initialize_state())
    measurements = measure_state(state, 20)
    return measurements


# if __name__ == "__main__":
#     U = np.array([[0.70710678, 0.70710678], [0.70710678, -0.70710678]])
#     print(quantum_algorithm(U))
