import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  /*
  states
    pokemonName: El nombre del Pokémon por el que queremos consultar en la API
    allPokemonNames: Los nombres de todos los Pokémon
    pokemonData: La información de Pokémon que recibimos de la API
  */
  const [pokemonName, setPokemonName] = useState(""); // Leer comentario al final del archivo
  const [allPokemonNames, setAllPokemonNames] = useState([]);
  const [pokemonData, setPokemonData] = useState(null);

  // COMPLETAR
  const getPokemonData = async () => {
    try {
      /*
      Consultar la API con,
        Endpoint: /pokemon/<pokemonName>
        Método: GET

      Y actualizar valor del state "pokemonData"
      */

      
    } catch (error) {
      console.log(error);
    }
  };

  // COMPLETAR
  const getPokemonNames = async (quantity) => {
    try {
      /*
      Consultar la API con,
        Endpoint: /pokemon?limit=<quantity>
        Método: GET

      Y actualizar valor del state "allPokemonNames"

      (Estos valores se reflejarán en las opciones del dropdown)
      */

      // Hint: usar <response>.data.results.map(pokemon => pokemon.name)


    } catch (error) {
      console.log(error);
    }
  }

  /*
  De aquí en adelante NO necesitan editar nada,
  pero los invitamos a explorar!
  */

  const handleFormSubmit = (event) => {
    event.preventDefault(); // Evitar que el formulario recargue la página
    getPokemonData();
  };

  useEffect(() => {
    getPokemonNames(100);
  }, [])

  return (
    <>
      <h1>Consulta PokeApi</h1>

      <div className='flex row'>
        <form onSubmit={handleFormSubmit} className='flex column'>
          <h3>Escribe el nombre de un Pokémon</h3>
          <input
            value={pokemonName}
            onChange={(event) => { setPokemonName(event.target.value) }} />
          <p><i>Debe ser completamente en minúscula</i></p>
          <button type="submit" disabled={pokemonName === ""}>Enviar</button>
        </form>

        <form onSubmit={handleFormSubmit} className='flex column'>
          <h3>Selecciona un Pokemón</h3>
          <select
            value={pokemonName}
            onChange={(event) => { setPokemonName(event.target.value) }}>
            <option value="">Selecciona un Pokémon</option>
            {allPokemonNames.map((name, index) => (
              <option key={index} value={name}>{name}</option>
            ))}
          </select>
          <button type="submit" disabled={pokemonName === ""}>Enviar</button>
        </form>
      </div>


      {pokemonData && (
        <div className='flex column'>
          <h2>{pokemonData.name}</h2>
          <img src={pokemonData.sprites.front_default} alt={pokemonData.name} />
          <p>Height: {pokemonData.height}</p>
          <p>Weight: {pokemonData.weight}</p>
        </div>
      )}
    </>
  )
}

export default App

/*
Por simplicidad de la actividad,
se usa el mismo state como value en ambos formularios.
Notarán que esto no es ideal,
y que genera comportamientos no deseados en los formularios.
*/
