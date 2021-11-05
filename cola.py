class Cola:
    """Representa a una, con operaciones de primero, acolar y
    desacolar. El primero en ser acolado es también el primero
    en ser desacolado"""
    
    def __init__(self):
        """Inicializar cola. Crea una cola vacía."""
        self.items = []
        
    def acolar(self, x):
        """Agrega el elemento x como último de la cola."""
        self.items.append(x)
        
    def desacolar(self):
        """Desacola el primer elemento. No devuelve su
        valor. Si la cola está vacía, levanta ValueError."""
        
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        self.items.pop(0)
    
    def primero(self):
        """Devuelve el valor del primer elemento. No desacola el elemento.
        Si la cola está vacía, levanta ValueError."""
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items[0]
    
    def esta_vacia(self):
        """Devuelve True si la cola esta vacía, False si no."""
        return len(self.items) == 0