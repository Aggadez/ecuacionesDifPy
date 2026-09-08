"""
Resolución numérica de una EDO de variables separables mediante el método de Euler.

Problema:
    dy/dt = -y,  y(0) = 1,  t ∈ [0, 1],  h = 0.2

Solución exacta:
    y(t) = exp(-t)
"""

from __future__ import annotations

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


def f(t: float, y: float) -> float:
    """
    Lado derecho de la EDO: y' = f(t, y).

    Parameters
    ----------
    t : float
        Variable independiente (no se usa en este problema autónomo).
    y : float
        Variable dependiente.

    Returns
    -------
    float
        Valor de f(t, y) = -y.
    """
    return -y


def analytical_solution(t: NDArray[np.floating] | float) -> NDArray[np.floating] | float:
    """
    Solución exacta y(t) = exp(-t).

    Parameters
    ----------
    t : array_like o float
        Punto(s) donde evaluar la solución.

    Returns
    -------
    array_like o float
        Valor(es) de la solución analítica.
    """
    return np.exp(-t)


def euler_method(
    f_rhs: Callable[[float, float], float],
    t0: float,
    y0: float,
    t_end: float,
    h: float,
) -> tuple[NDArray[np.floating], NDArray[np.floating]]:
    """
    Aproxima la solución de y' = f(t, y) con el método de Euler.

    Fórmula iterativa:
        y_{n+1} = y_n + h * f(t_n, y_n)

    Parameters
    ----------
    f_rhs : Callable[[float, float], float]
        Función f(t, y) del problema de valor inicial.
    t0 : float
        Tiempo inicial.
    y0 : float
        Condición inicial y(t0).
    t_end : float
        Extremo derecho del intervalo de integración.
    h : float
        Tamaño de paso (debe ser positivo).

    Returns
    -------
    tuple[NDArray, NDArray]
        Vectores (t, y) con la malla temporal y la aproximación numérica.

    Raises
    ------
    ValueError
        Si h <= 0 o si t_end < t0.
    """
    if h <= 0:
        raise ValueError("El tamaño de paso h debe ser positivo.")
    if t_end < t0:
        raise ValueError("t_end debe ser mayor o igual que t0.")

    n_steps = int(np.round((t_end - t0) / h))
    t = np.linspace(t0, t0 + n_steps * h, n_steps + 1)
    y = np.empty(n_steps + 1, dtype=float)
    y[0] = y0

    for n in range(n_steps):
        y[n + 1] = y[n] + h * f_rhs(float(t[n]), float(y[n]))

    return t, y


def plot_comparison(
    t_num: NDArray[np.floating],
    y_num: NDArray[np.floating],
    t_exact: NDArray[np.floating],
    y_exact: NDArray[np.floating],
    output_path: str = "euler_vs_exact.png",
) -> None:
    """
    Grafica la solución de Euler frente a la solución analítica.

    Parameters
    ----------
    t_num : NDArray
        Nodos temporales del método de Euler.
    y_num : NDArray
        Aproximación numérica en t_num.
    t_exact : NDArray
        Malla fina para la curva exacta.
    y_exact : NDArray
        Solución analítica en t_exact.
    output_path : str, optional
        Ruta del archivo PNG de salida.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(t_exact, y_exact, "b-", linewidth=2, label=r"Exacta: $y(t)=e^{-t}$")
    plt.plot(
        t_num,
        y_num,
        "ro--",
        markersize=8,
        linewidth=1.5,
        label="Euler ($h=0.2$)",
    )
    plt.xlabel(r"$t$", fontsize=12)
    plt.ylabel(r"$y(t)$", fontsize=12)
    plt.title(r"EDO $y'=-y$, $y(0)=1$: Euler vs. solución exacta")
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    # Solo abre ventana interactiva si el backend lo permite.
    if "agg" not in plt.get_backend().lower():
        plt.show()
    print(f"Gráfica guardada en: {output_path}")


def print_table(
    t: NDArray[np.floating],
    y_num: NDArray[np.floating],
    y_exact: NDArray[np.floating],
) -> None:
    """
    Imprime una tabla comparativa de valores numéricos y exactos.

    Parameters
    ----------
    t : NDArray
        Nodos temporales.
    y_num : NDArray
        Aproximación de Euler.
    y_exact : NDArray
        Solución exacta en los mismos nodos.
    """
    error = np.abs(y_exact - y_num)
    print(f"{'n':>3}  {'t_n':>6}  {'y_Euler':>12}  {'y_exacta':>12}  {'|error|':>12}")
    print("-" * 52)
    for n, (ti, yn, ye, err) in enumerate(zip(t, y_num, y_exact, error)):
        print(f"{n:3d}  {ti:6.2f}  {yn:12.8f}  {ye:12.8f}  {err:12.8f}")


def main() -> None:
    """Punto de entrada: resuelve, tabula y grafica el PVI."""
    t0 = 0.0
    y0 = 1.0
    t_end = 1.0
    h = 0.2

    t_num, y_num = euler_method(f, t0, y0, t_end, h)
    y_exact_nodes = analytical_solution(t_num)

    print("Método de Euler — dy/dt = -y, y(0) = 1, h = 0.2\n")
    print_table(t_num, y_num, y_exact_nodes)

    t_fine = np.linspace(t0, t_end, 200)
    y_fine = analytical_solution(t_fine)
    plot_comparison(t_num, y_num, t_fine, y_fine)


if __name__ == "__main__":
    main()
