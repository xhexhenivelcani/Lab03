import csv
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome_deposito, responsabile=""):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome_deposito = nome_deposito
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self._contatore_prestiti = 1

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 5:
                        id_strum, tipo, marca, anno, val = row
                        nuovo_strumento = Strumento(id_strum.strip(), tipo.strip(), marca.strip(), anno, val)
                        self.strumenti.append(nuovo_strumento)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        # Calcolo del nuovo ID progressivo (es. S1, S2, S10...)
        max_num = 0
        for s in self.strumenti:
            if s.id_strumento.startswith('S'):
                try:
                    num = int(s.id_strumento[1:])
                    if num > max_num:
                        max_num = num
                except ValueError:
                    pass

        nuovo_id = f"S{max_num + 1}"
        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        def nuovo_prestito(self, data, id_strumento, cognome_allievo):
            # Verifica se lo strumento esiste
            strumento_esiste = any(s.id_strumento == id_strumento for s in self.strumenti)
            if not strumento_esiste:
                raise Exception(f"Errore: lo strumento con ID {id_strumento} non è presente nel sistema.")

            # Verifica se lo strumento è già in prestito
            strumento_in_prestito = any(p.id_strumento == id_strumento for p in self.prestiti)
            if strumento_in_prestito:
                raise Exception(f"Errore: lo strumento {id_strumento} è già in prestito.")

            # Crea il prestito
            nuovo_id_prestito = f"P{self._contatore_prestiti}"
            self._contatore_prestiti += 1

            nuovo_prestito_obj = Prestito(nuovo_id_prestito, data, id_strumento, cognome_allievo)
            self.prestiti.append(nuovo_prestito_obj)
            return nuovo_prestito_obj

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for prestito in self.prestiti:
            if prestito.id_prestito == id_prestito:
                self.prestiti.remove(prestito)
                return True
            # Se esce dal ciclo senza aver trovato il prestito
        raise Exception(f"Errore: prestito {id_prestito} non trovato.")