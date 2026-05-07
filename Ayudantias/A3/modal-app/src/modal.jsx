import React from 'react';
import { createPortal } from 'react-dom';
import './Modal.css'; // Importamos los estilos del modal

const Modal = ({ isOpen, onClose, children }) => {
  // Si el modal no está abierto, no renderizamos nada
  if (!isOpen) return null;
  // Obtenemos el elemento del DOM donde se montará el modal que esta en el archivo index.html
  const modalRoot = document.getElementById('modal-root');
  // Usamos createPortal, que es un método de React para renderizar un componente en un nodo del DOM que está fuera de la jerarquía del componente padre
  return createPortal(
    // Este div es el fondo del modal, que cubre toda la pantalla y tiene un efecto de opacidad. Al hacer clic en él, se cierra el modal.
    <div className="modal-overlay" onClick={onClose}>
      // Este div es el contenido del modal.
      // En el desarrollo web existe algo llamado Bubbling que básicamente es que si hay un click en un elemento
      // el padre, el padre del padre, el padre del padre, etc... también reciben ese click. 
      // Para evitar que el click en el contenido del modal cierre el modal, usamos e.stopPropagation() para detener la propagación del evento de clic.
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        // Este es el botón para cerrar "X"
        <button className="modal-close-btn" onClick={onClose}>
          &times;
        </button>
        // Aquí se renderiza el contenido que se le pase al modal, como el título, el párrafo y el botón de aceptar.
        {children}
      </div>
    </div>,
    // El segundo argumento de createPortal es el nodo del DOM donde se montará el modal, que en este caso es modalRoot.
    modalRoot
  );
};

export default Modal;