export default function App() {

  const user = {
    id: 1,
    first_name: 'Melon',
    last_name: 'Chunk'
  }

  const destinations = [{id:1, location:'London'}, {id:2, location:'New York'}, {id:3, location:'Berlin'}];

  return (
    <>
    <h1>Key Bento</h1>
    <p>Hello {user.first_name} {user.last_name}, good to see you back!</p>
    <p>The following destinations are available: </p>
      {destinations.length === 0 ?
          <p> Unfortunately, no destinations are currently available </p>
        :
        <ul>
          {destinations.map(x => {return (
              <p key={x.id}>
              <li>{x.location}</li>
              </p>
            )})}
        </ul>
      }
    </>
  );
}
