# Resolución de una EDO de Variables Separables: Método de Euler

Proyecto en Python que resuelve analíticamente y de forma numérica (método de Euler) la ecuación diferencial ordinaria de primer orden

$$
\frac{dy}{dt} = -y, \qquad y(0) = 1,
$$

en el intervalo \( t \in [0, 1] \) con tamaño de paso \( h = 0.2 \).

---

## 1. Planteamiento del problema

Se considera el **problema de valor inicial (PVI)**:

$$
\begin{cases}
\dfrac{dy}{dt} = -y, & t \in [0, 1], \\[6pt]
y(0) = 1.
\end{cases}
$$

La EDO es de **variables separables**: se puede escribir como

$$
g(y)\, y' = h(t)
\quad\text{con}\quad
g(y) = -\frac{1}{y}\ (y \neq 0),\quad
h(t) = 1,
$$

o, de forma equivalente,

$$
\frac{1}{y}\, dy = -\, dt.
$$

---

## 2. Deducción analítica (solución exacta)

Partiendo de

$$
\frac{dy}{dt} = -y,
$$

y asumiendo \( y \neq 0 \), separamos variables:

$$
\frac{1}{y}\, dy = -\, dt.
$$

Integramos ambos miembros:

$$
\int \frac{1}{y}\, dy = -\int dt
\quad\Rightarrow\quad
\ln|y| = -t + C,
$$

donde \( C \) es la constante de integración. Exponenciando:

$$
|y| = e^{C}\, e^{-t} = K\, e^{-t},
\quad K = e^{C} > 0.
$$

Eliminando el valor absoluto (y permitiendo \( K \in \mathbb{R}\setminus\{0\} \)):

$$
y(t) = K\, e^{-t}.
$$

Aplicamos la condición inicial \( y(0) = 1 \):

$$
y(0) = K\, e^{0} = K = 1.
$$

Por tanto, la **solución exacta** es

$$
\boxed{y(t) = e^{-t}.}
$$

Verificación: \( y'(t) = -e^{-t} = -y(t) \) y \( y(0) = 1 \).

---

## 3. Método de Euler (método de las tangentes)

El método de Euler aproxima la solución de \( y' = f(t, y) \) avanzando a lo largo de la recta tangente en cada nodo.

Dado un tamaño de paso \( h > 0 \) y una condición inicial \( y_0 = y(t_0) \), la fórmula iterativa es

$$
y_{n+1} = y_n + h\, f(t_n, y_n),
\qquad
t_{n+1} = t_n + h.
$$

En este problema, \( f(t, y) = -y \), \( t_0 = 0 \), \( y_0 = 1 \) y \( h = 0.2 \), de modo que

$$
y_{n+1} = y_n + h(-y_n) = (1 - h)\, y_n = 0.8\, y_n.
$$

La malla temporal es

$$
t_n = 0,\ 0.2,\ 0.4,\ 0.6,\ 0.8,\ 1.0
\quad (n = 0, \ldots, 5).
$$

El error local es de orden \( O(h^2) \) y el error global de orden \( O(h) \); por eso, con \( h = 0.2 \) la aproximación se aparta visiblemente de \( e^{-t} \).

---

## 4. Estructura del repositorio

```
ecuacionesDifPy/
├── solver.py           # Implementación del método de Euler + gráfica
├── requirements.txt    # Dependencias (numpy, matplotlib)
├── README.md           # Esta documentación
├── LICENSE
└── .gitignore
```

---

## 5. Requisitos e instalación

- Python 3.10 o superior (recomendado)
- `numpy` y `matplotlib`

```bash
# (Opcional) crear un entorno virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 6. Ejecución

Desde la raíz del repositorio:

```bash
python solver.py
```

El script:

1. Aproxima \( y(t) \) con Euler en \( [0, 1] \) con \( h = 0.2 \).
2. Imprime una tabla con \( t_n \), \( y_{\text{Euler}} \), \( y_{\text{exacta}} \) y el error absoluto.
3. Genera y muestra una gráfica comparativa, guardada como `euler_vs_exact.png`.

---

## 7. Ejemplo de valores esperados

| \( n \) | \( t_n \) | \( y_{\text{Euler}} \) | \( y_{\text{exacta}} = e^{-t_n} \) |
|--------:|----------:|-----------------------:|-----------------------------------:|
| 0 | 0.0 | 1.00000000 | 1.00000000 |
| 1 | 0.2 | 0.80000000 | 0.81873075 |
| 2 | 0.4 | 0.64000000 | 0.67032005 |
| 3 | 0.6 | 0.51200000 | 0.54881164 |
| 4 | 0.8 | 0.40960000 | 0.44932896 |
| 5 | 1.0 | 0.32768000 | 0.36787944 |

---

## Licencia

Consulta el archivo [LICENSE](LICENSE) del repositorio.
