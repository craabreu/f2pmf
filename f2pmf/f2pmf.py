"""
f2pmf.py
RBF Regression from Gradient Samples

Handles the primary functions
"""


class Variable:
    """
    One of the inputs of the Radial Basis Function network.

    Parameters
    ----------
        id : str
            A valid identifier string for this variable.
        min_value : float
            The minimum allowable value for this variable.
        max_value : float
            The maximum allowable value for this  variable.
        periodic : bool
            Whether the variable is periodic with period `L = max_value - min_value`.

    Example
    -------
        >>> import f2pmf
        >>> import numpy as np
        >>> f2pmf.Variable('psi', -np.pi, np.pi, True)
        <psi in [-3.141592653589793, 3.141592653589793], periodic>

    """
    def __init__(self, id, min_value, max_value, periodic):
        self.id = id
        self.min_value = min_value
        self.max_value = max_value
        self.periodic = periodic

    def __repr__(self):
        status = 'periodic' if self.periodic else 'non-periodic'
        return f'<{self.id} in [{self.min_value}, {self.max_value}], {status}>'

    def __getstate__(self):
        return dict(
            id=self.id,
            min_value=self.min_value,
            max_value=self.max_value,
            periodic=self.periodic,
        )

    def __setstate__(self, kw):
        self.__init__(**kw)
