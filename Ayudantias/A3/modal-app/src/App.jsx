import React, { useState } from 'react';
import Modal from './modal';

export default function App() {
  // Este estado controla si el modal está abierto o cerrado
  // isModalOpen es el booleano que cambia de valor.
  // setIsModalOpen es la función que se encarga de cambiar el valor de isModalOpen.
  // Inicializamos el hook con false, porque el modal empieza cerrado.
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Ejemplo de Portales en React</h1>
      <p>El equivalente a Teleport para manejar modales sin problemas de z-index.</p>
      // Este botón abre el modal al hacer clic, cambiando el estado isModalOpen a true.
      <button onClick={() => setIsModalOpen(true)}>
        Abrir Modal
      </button>
      // El modal esta escuchando el estado isModalOpen, si es true se renderiza el modal, si es false no se renderiza nada.
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        <h2>¡Hola! Soy un Modal 🚀</h2>
        <p>
          Fíjate en el inspector de elementos de tu navegador. 
          Aunque mi código React está dentro del componente App, 
          en el DOM estoy dentro de <code>#modal-root</code>.
        </p>
        // Este botón es el que cierra el modal al hacer clic, cambiando el estado isModalOpen a false.
        // Es otro distinto al "X". El modal lo recibe como children.
        <button onClick={() => setIsModalOpen(false)}>Aceptar</button>
      </Modal>
    </div>
  );
}