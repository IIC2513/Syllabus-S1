import { useState, useEffect } from "react";

function Contador() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    if (count === 10) {
      alert("¡Has llegado a 10!");
    }
  }, [count]);

  const disminuir = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert("No puedes disminuir más, el contador ya está en 0!");
    }
  };
  

  return (
    <div className="container">
      <h1>Contador: {count}</h1>
      <div className="button-container">
        <button onClick={() => setCount(count + 1)}>➕ Aumentar</button>
        <button onClick={disminuir}>➖ Disminuir</button>
        <button onClick={() => setCount(0)}>🔄 Reset</button>
      </div>
    </div>
  );
}

export default function App() {
  return <Contador />;
}
