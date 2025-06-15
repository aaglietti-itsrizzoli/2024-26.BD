import threading
import time

# Utilizzo un file di testo come dataset
# potrebbe essere una qualsiasi fonte big data
with open('map-reduce-dataset.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Rimuove il carattere di newline (\n) da ogni riga
# crea i data chunks da usare come input di ogni map function
data_chunks = [line.strip() for line in lines]

# Lista che conterrà i risultati dei thread
# che eseguono le singole map function
partial_results = []
lock = threading.Lock()

# Funzione MAP: conta parole in un chunk di testo
def map_function(chunk):
    # time.sleep(5)
    name = threading.current_thread().name
    tid = threading.get_native_id()
    print(f"Sono nel thread: {name} ({tid})")
    word_count = {}
    for word in chunk.split():
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    with lock:
        partial_results.append(word_count)

# Avvia un thread per ogni chunk
threads = []
for chunk_index, chunk in enumerate(data_chunks):
    t = threading.Thread(target=map_function, args=(chunk,), name=f"Thread-{chunk_index}")
    threads.append(t)
    t.start()

# Attende la fine di tutti i thread
for t in threads:
    t.join()

# Funzione REDUCE: combina i risultati parziali
final_result = {}
for partial in partial_results:
    for word, count in partial.items():
        final_result[word] = final_result.get(word, 0) + count

# Stampa il risultato finale
print("Conteggio finale delle parole:")
for word, count in final_result.items():
    print(f"{word}: {count}")
