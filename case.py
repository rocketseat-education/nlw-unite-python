class AlgumaCoisa:
    def __enter__(self):
        print('Estou Entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou saindo')


with AlgumaCoisa() as ola:
    print('Estou no meio')
