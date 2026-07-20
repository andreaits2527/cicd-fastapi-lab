from fastapi import FastAPI

app = FastAPI(
    title="Laboratorio CI/CD",
    description="Semplice API FastAPI utilizzata per il laboratorio CI/CD",
    version="1.0.0",
)


def somma(a: float, b: float) -> float:
    """Restituisce la somma di due numeri."""
    return a + b


@app.get("/")
def stato():
    """Endpoint utilizzato per controllare lo stato del servizio."""
    return {"status": "ok"}


@app.get("/somma")
def calcola_somma(a: float, b: float):
    """Espone la funzione somma tramite API."""
    return {
        "a": a,
        "b": b,
        "risultato": somma(a, b),
    }