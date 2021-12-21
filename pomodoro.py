from win10toast import ToastNotifier
from time import sleep, time

toaster = ToastNotifier()
toaster.show_toast("Sample Notification","Python is awesome!!!")

#il fattore di quanto è più lungo il periodo di studio rispetto a quello di pausa
FACTOR: int = 5
#variabile per memorizzare l'intervallo che passa tra la segnalazione e l'ack dell'utente
lag: float = 0.0
#il quantitativo di minuti che si vuole duri la pausa
break_min: int = 10


def ack_message() -> float:
    start: float = time()
    input()
    print("acked")
    return time() - start


def cycle(break_time: float):
    """
        Esegue un ciclo di studio di pomodoro. 
    """
    global lag
    #usata per memorizzare quanto tempo passa dalla segnalazione della pausa
    #all'effettivo inizio segnalato dall'utente
    start: float = 0.0

    sleep((FACTOR * break_time) + lag)
    toaster.show_toast("PAUSAAAAAAAAAAAA", "AO è ora de femmasse")
    lag = ack_message() / 5

    sleep(break_time + lag)
    toaster.show_toast("Torna a studiare", "se ricomincia")
    lag = ack_message() * 5



while True:
    cycle(break_min*60)